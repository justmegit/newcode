# Arquitetura técnica replicável — v1, 05/11/2026

Objetivo: servir 30 clientes com **um** núcleo em n8n, em que cada cliente novo é **dados, não nós**. Hoje a Vitória é um workflow de ~62 nós feito à medida; duplicá-lo por cliente dá 30 cópias para corrigir a cada bug. A arquitetura abaixo mantém o n8n e a infraestrutura atual (Coolify, Data Tables, Groq, Gemini) e muda a forma de os organizar.

Legenda: **[existe]** já está construído · **[novo]** a construir · **[?]** a confirmar na primeira execução.

> **Atualização 05/11/2026.** A Cloud API está ligada pela **YCloud** (WABA `1648511630107490`, número 926 `phone_number_id` `1436224236241306`, CONNECTED). A YCloud substitui a Chakra como plataforma nesta v1. As referências à Chakra abaixo leem-se "plataforma"; o adaptador concreto é o da YCloud (secção 3, [A]).

---

## 1. Princípios

1. **Um núcleo, N inquilinos.** Um conjunto de workflows partilhados; um registo de clientes (`clientes`) com tudo o que é específico: nome da secretária, tom, número do dono, tabelas, funcionalidades ligadas.
2. **Formato interno neutro.** Tudo o que entra (YCloud, Meta direta, Evolution enquanto durar) é convertido para uma mensagem interna única; tudo o que sai passa por um só "expedidor". Trocar de fornecedor é trocar um adaptador.
3. **O cérebro decide, as ferramentas fazem.** Um LLM com ferramentas (marcar, cancelar, consultar pagamento, escalar) em vez de árvores de nós por intenção. Menos nós, mais fácil de afinar com texto.
4. **Base de conhecimento inteira no contexto.** Com 50 a 300 entradas por cliente não há RAG vetorial: a base inteira vai no prompt. Mais barato, mais previsível, zero infraestrutura. Vetores só se um cliente passar de ~300 entradas.
5. **Nada de painel para o dono.** Toda a interface do dono é WhatsApp. O painel do Alexandre é o n8n e, mais tarde, uma vista simples sobre a tabela de eventos.
6. **Tudo o que é durável vive em tabelas, versionado em git.** Workflows exportados em JSON para o repositório; prompts e bases de conhecimento em ficheiros que se carregam para as tabelas.

---

## 2. Visão geral

```
 Cliente final (WhatsApp)          Dono (app WhatsApp Business, coexistência)
          │                                     │
          ▼                                     ▼
   ┌───────────────────── Meta Cloud API ──────────────────────┐
   │ WAAC + Messaging account: no portfólio Blue Serenity      │
   │ (Modelo 1) ou no do cliente, partilhadas como parceiro (2)│
   └───────────────┬────────────────────────────┬──────────────┘
                   │ webhooks                   ▲ envios
                   ▼                            │
           ┌──── YCloud ────┐           ┌──── YCloud API ────┐
           │ (Tech Provider)│           │ (nunca Graph direta│
           └───────┬────────┘           │ por fora da YCloud)│
                   │                    └─────────▲──────────┘
                   │                              │
 ══════════════════╪══════════ n8n (auto.blueserenity.pt) ═══════════════════
                   ▼                              │
   [A] Adaptadores de entrada ──► Mensagem interna ──► [B] Router de inquilino
   (YCloud | Meta direta | Evolution)                          │
                                                               ▼
                                              [C] Estado da conversa + coexistência
                                                               │
                                                               ▼
                                         [D] Cérebro (LLM + ferramentas + KB no prompt)
                                          │        │         │          │
                                          ▼        ▼         ▼          ▼
                                   [E] Agenda [F] Cobranças [G] Escalação [H] Resposta
                                          │        │         │          │
                                          └────────┴─────────┴──────────┘
                                                               ▼
                                              [I] Expedidor (janela 24 h, templates, fila)
                                                               │
   Workflows agendados: [J] Lembretes · [K] Resumos · [L] Monitor · [M] Relatório mensal
   Tabelas: clientes · kb_* · alunos · aulas · marcacoes · conversas · escalacoes · pagamentos · eventos
 ════════════════════════════════════════════════════════════════════════════
```

---

## 3. Módulos

### [A] Adaptadores de entrada [existe parcialmente]
Um webhook por fornecedor, cada um a produzir a mesma **mensagem interna**:

```json
{ "tenant_phone_id": "1401196933066472", "from": "3519xxxxxxx", "msg_id": "wamid...",
  "ts": 1762300000, "type": "text|audio|image|button|reaction|echo",
  "text": "...", "media_url": "...", "reply_to": "wamid...", "raw": {} }
```
- **YCloud** [novo, prioritário]: webhook `whatsapp.inbound_message.received` em formato próprio da YCloud, com assinatura `YCloud-Signature` a verificar no n8n antes de processar; a média vem num `link` que se descarrega com a chave de API (header `X-API-Key`, lida da env var `YCLOUD_API_KEY`). Mapeamento de ~10 campos para o formato interno. Ecos do dono em coexistência: confirmar se a YCloud os reencaminha e com que evento [?].
- **Chakra** [reserva]: só se a plataforma mudar ao terceiro número.
- **Meta direta** [existe]: `GpJxyM42Psl8Zy7c`, mesma mudança de saída. Reserva: sem coexistência, só serviria números dedicados puros.
- **Evolution** [existe]: o 938 do Mike continua a entrar por aqui até migrar; mapeamento Evolution → interno. É a única razão para o formato Evolution continuar a existir; apaga-se com a migração do 938.
- **Eco do dono** (coexistência): as mensagens que o dono envia da app chegam como eventos de eco (campo `smb_message_echoes` no webhook da Meta [?]). O adaptador marca `type: "echo"`. É o sinal para o módulo [C].

### [B] Router de inquilino [novo]
Procura `tenant_phone_id` na tabela `clientes`; se não existe, regista em `eventos` e ignora (protege contra números desconhecidos). Anexa à mensagem o registo do cliente: nome da secretária, nome do dono, número do dono, tom, fuso, tabelas, funcionalidades (`cobrancas`, `presenca`), horário de silêncio, idioma.

### [C] Estado da conversa e coexistência [novo]
Tabela `conversas` (uma linha por `tenant` + `contacto`): último contacto, `janela_24h_ate`, `humano_ate`, `intencao_pendente`, `dados_parciais` (slots de uma marcação a meio), `escalacao_aberta`.
- Ao receber **eco do dono**: `humano_ate = agora + 4 h` nessa conversa. A secretária cala-se até lá. O dono pode devolver a conversa com uma palavra combinada ("Clara, continua") ou deixa passar as 4 h.
- Ao receber mensagem do cliente com `humano_ate` no futuro: não responde, só regista. Se o dono não responder em 2 h, a secretária manda ao dono um lembrete de escalação.
- Agrupamento: várias mensagens curtas em 8 s tratadas como uma (evita respostas em catadupa). [existe na Vitória? confirmar]

### [D] Cérebro [existe, a refazer]
- **Transcrição**: notas de voz → Gemini (atual). Imagens de comprovativos → Gemini com pedido de extrair valor, data e nome.
- **Prompt de sistema** montado a partir do registo do cliente + base de conhecimento inteira (`kb_<cliente>`, ordenada por tema) + estado da conversa + regras fixas (identificar-se como virtual na primeira mensagem, nunca inventar, escalar o que está na lista "escala sempre", tom).
- **Modelo**: Groq (atual) como principal pelo custo e latência; Gemini Flash como alternativa automática se o Groq falhar ou limitar. Escolha do modelo é um campo em `clientes` com valor por omissão global, para poder testar por cliente.
- **Ferramentas** (function calling): `consultar_horarios(dia)`, `vagas(aula_id)`, `marcar(contacto, aula_id, nome_aluno)`, `remarcar(marcacao_id, aula_id)`, `cancelar(marcacao_id)`, `estado_pagamento(contacto)`, `registar_pagamento(contacto, valor, meio)`, `escalar(resumo, pergunta_ao_dono)`, `responder(texto)`. Cada ferramenta é um sub-workflow de poucos nós sobre as tabelas.
- **Guarda-chuvas**: resposta máxima de 600 caracteres; se o modelo quiser responder a algo fora da base, a ferramenta `escalar` é obrigatória; resposta de recurso fixa se o LLM falhar ("Vou confirmar com o Ricardo e já lhe digo").

### [E] Agenda [novo]
Tabelas `aulas` (horários recorrentes: dia da semana, hora, duração, grupo, lotação, professor; exceções por data) e `marcacoes` (aluno, contacto, aula, data, estado: marcada/cancelada/falta/presente, criada por: secretária/dono). Regras do negócio (antecedência, prazo de cancelamento, lista de espera) são campos em `clientes`. Opcional [novo, depois]: espelho num Google Calendar por cliente só para o Alexandre ver; nunca fonte de verdade.

### [F] Cobranças [novo]
Fase 1: `alunos` (nome, contacto do encarregado, mensalidade, dia de vencimento) e `pagamentos` (mês, valor, estado, meio, comprovativo, confirmado por). Lembretes por [J]. O dono confirma por mensagem ("recebi da Inês") que o cérebro converte em `registar_pagamento`. Fase 2: webhook do processador (Ifthenpay/EuPago/Stripe, decisão adiada) → `pagamentos` → agradecimento automático.

### [G] Escalação [existe parcialmente]
Tabela `escalacoes` (tenant, contacto, resumo, pergunta, estado, resposta do dono, criada, fechada). Ao escalar: mensagem curta ao **número pessoal do dono** a partir do número do negócio (template `escalacao_aviso` [existe] se fora da janela; texto livre se dentro). O dono responde "sim"/"não"/texto/voz; o cérebro, ao receber mensagem do número do dono, procura a escalação aberta mais recente e fecha-a respondendo ao cliente final com o conteúdo. Se houver mais do que uma aberta, pergunta ao dono qual ("É sobre a Inês ou sobre o Tomás?").

### [H] Resposta e [I] Expedidor [existe como gateway `gwKc8toftwSRD7G8`]
Um único ponto de saída: recebe `{tenant, para, texto | template+parâmetros, media}`, verifica a janela de 24 h na tabela `conversas`, escolhe texto livre ou template (lógica do gateway atual, mantida), chama `POST https://api.ycloud.com/v2/whatsapp/messages` com `X-API-Key` (nunca a Graph API por fora da YCloud: a faturação Meta passa pela carteira YCloud e envios externos ficariam fora dela), regista em `eventos`, trata erros (131047 janela fechada → template; 130429 limite → fila e tentativa em 60 s). Fila simples: tabela `fila_envios` com tentativas, processada de minuto a minuto.

### [J] Lembretes [novo]
A cada 15 min: marcações nas próximas 20 a 28 h sem lembrete enviado → template `lembrete_aula`. Diariamente às 10h: mensalidades a vencer em 3 dias e vencidas há 1 dia → `lembrete_mensalidade` / `mensalidade_atraso`, só para clientes com `cobrancas` ligado, respeitando horário de silêncio e um máximo de 1 lembrete de pagamento por semana por aluno.

### [K] Resumos [novo]
Diário 20h (opcional por cliente) e semanal segunda 8h: consulta `marcacoes`, `pagamentos`, `escalacoes` e as respostas marcadas como "não soube" em `eventos`; o LLM redige em 10 linhas no tom fixo da secção 2 do guião de demonstração; envia ao dono.

### [L] Monitor [existe `O0Q9FqGuDEJQ8RTA`, a alargar]
A cada 15 min, por inquilino: (0) **saldo da carteira YCloud** (alarme abaixo de 5 $; carteira vazia bloqueia os canais); (1) `health_status` da conta na Graph API (corrigir já o `phone_number_id` antigo que o monitor ainda lê); (2) última mensagem recebida vs. esperado (um cliente que costuma ter 30 mensagens/dia e está a zero há 6 h é alarme); (3) erros do expedidor na última hora; (4) **ping sintético** de hora a hora: o número de teste da Blue Serenity envia "ping" a cada secretária e espera resposta em 60 s. Alerta por WhatsApp ao Alexandre e por e-mail; se o próprio n8n cair, um monitor externo gratuito (ex.: UptimeRobot ou Better Stack no plano grátis) bate no `/healthz` do n8n.

### [M] Relatório mensal [novo]
Dia 1 de cada mês, por inquilino, a partir de `eventos`: mensagens, conversas, % escalado, marcações, faltas, pagamentos lembrados, custo Meta estimado. Texto de 10 linhas ao dono; versão completa para o Alexandre (faturação e margem).

---

## 4. Modelo de dados (tabelas)

| Tabela | Chave | Campos principais | Partilhada? |
|---|---|---|---|
| `clientes` | `tenant_id` | nome negócio, `phone_number_id`, waac_id, messaging_account_id, nome secretária, tom, nome e número do dono, fuso, modelo LLM, funcionalidades, regras da agenda, horário de silêncio, estado (teste/ativo/pausado) | única |
| `kb_<tenant>` | id | tema, pergunta, resposta, ativo, atualizado em | uma por cliente |
| `alunos` | id | tenant, nome, contacto, grupo, mensalidade, vencimento, ativo | única, coluna tenant |
| `aulas` | id | tenant, dia semana, hora, duração, grupo, lotação, professor, exceções | única |
| `marcacoes` | id | tenant, aluno, contacto, aula, data, estado, origem, lembrete enviado | única |
| `conversas` | tenant+contacto | janela 24h até, humano até, intenção pendente, dados parciais, escalação aberta | única |
| `escalacoes` | id | tenant, contacto, resumo, pergunta, estado, resposta, datas | única |
| `pagamentos` | id | tenant, aluno, mês, valor, estado, meio, comprovativo, confirmado por | única |
| `fila_envios` | id | tenant, para, payload, tentativas, próximo envio, erro | única |
| `eventos` | id | tenant, ts, direção, contacto (pseudonimizado), tipo, intenção, ferramenta, latência, tokens, erro | única |

**Onde vivem**: n8n Data Tables agora (zero infraestrutura, já em uso). Migrar para **Postgres no Coolify** com o mesmo esquema quando houver mais de 5 clientes ou quando `eventos` passar de algumas centenas de milhar de linhas; os sub-workflows de ferramentas são o único sítio que muda. Backup diário do n8n e das tabelas para fora do servidor (o incidente de 14/09 a 28/10 mostrou que não havia quem reparasse; o backup tem de ser automático e verificado pelo monitor).

**RGPD**: conteúdo das conversas guardado 90 dias e depois apagado por workflow; `eventos` guarda o número pseudonimizado (hash com sal) e estatísticas sem limite; apagamento total de um cliente por um workflow "offboarding" que remove `kb_<tenant>` e todas as linhas com o seu `tenant`.

---

## 5. Segredos, acessos e ambientes

- **Um token para todos os clientes**: utilizador de sistema `n8n` do portfólio Blue Serenity com acesso aos ativos partilhados pelos clientes (acesso de parceiro). Token em `META_WABA_TOKEN` (já existe; precisa de `business_management` para ler `health_status` e gerir templates dos clientes [?]). Chave da YCloud em `YCLOUD_API_KEY`. Nunca tokens por cliente.
- **Env vars no Coolify**, nunca em nós do n8n. Rotação anual. Segredos nunca em git.
- **Ambientes**: um só n8n, com um **inquilino de teste** permanente ("Centro Hípico da Ribeira", a Clara da demonstração) em estado `teste`. Qualquer alteração ao núcleo testa-se primeiro com a Clara, com um guião fixo de 12 mensagens (as 20 perguntas, uma marcação, uma escalação, um eco do dono). Sem segundo servidor por agora.
- **Versões**: exportar os workflows em JSON para o repositório (`workflows/`), prompts em `prompts/`, bases de conhecimento em `kb/<tenant>.csv`, com uma etiqueta de versão por alteração ao núcleo. Um script carrega `kb/*.csv` para as tabelas. O repositório `newcode` serve para isto.

---

## 6. Custos e limites a respeitar

- Meta: 1 000 conversas de serviço grátis por número e mês; templates utility ~0,0142 €; limite de 250 contactos únicos/dia iniciados pelo negócio enquanto o negócio do cliente não estiver verificado [?]; os lembretes contam para esse limite, as respostas não.
- Groq: limites de pedidos por minuto no plano gratuito; a partir de 5 clientes, plano pago ou Gemini como alternativa automática.
- n8n: execuções por minuto no servidor atual; a agregação de mensagens (8 s) e a fila de envios protegem picos (a hora de ponta é o fim do dia, quando todos remarcam).
- Orçamento por cliente (do documento de oferta): 12 a 18 €/mês. O módulo [M] mede o real.

---

## 7. Plano de migração a partir do estado atual

Regra inalterada: **a Evolution e o 938 não se tocam até a Cloud API estar a funcionar e testada.**

| Fase | O que se faz | Serve quem |
|---|---|---|
| 0 (agora) | Vitória na Evolution, como está. Começar o registo `clientes` com uma linha (Lisbon Riding Club) e a tabela `eventos`. | Mike |
| 1 | **Em curso (05/11):** 926 ligado pela YCloud. Falta: templates recriados na WABA nova, `YCLOUD_API_KEY` no Coolify, adaptador YCloud → formato Evolution que a Vitória atual espera (atalho desta fase; o formato interno entra na fase 2), gateway a enviar pela YCloud, monitor com o `phone_number_id` novo, saldo na carteira. Teste com o número do Alexandre; corte pela env var `EVOLUTION_URL`. | Mike em teste, sem clientes finais |
| 2 | Construir o núcleo ([B] a [I]) a partir da Vitória, módulo a módulo, com a **Clara** (inquilino de teste) a correr em paralelo. A Vitória continua a servir o Mike. | Clara |
| 3 | Passar o Lisbon Riding Club para o núcleo: linha em `clientes`, `kb_escola` → `kb_lrc`, agenda e alunos carregados. Um dia de execução em sombra (o núcleo recebe tudo, responde só ao Alexandre) antes de ligar. | Mike |
| 4 | Lembretes [J], resumos [K], monitor alargado [L]. Desligar a Vitória antiga. | Mike |
| 5 | Migrar o 938 por coexistência (sessão de arranque do Mike, opção A, com o Alexandre a fazer tudo no telemóvel do Mike). Desligar a Evolution. | Mike |
| 6 | Segundo cliente: só dados. Medir as horas de arranque; se passarem de 8 h, o problema é no núcleo, não no cliente. | Cliente 2 |

Esforço estimado do núcleo (fases 2 a 4): 40 a 60 horas de trabalho do Alexandre com apoio desta sessão, a espaçar por 4 a 6 semanas, sem parar o piloto.

---

## 8. O que fica em aberto e como se fecha

1. Formato exato do webhook da YCloud: fechado com o primeiro payload real na fase 1 (já se sabe o nome do evento e a assinatura).
2. Eco do dono na coexistência via YCloud [?]: testar na fase 5 com o 938, ou antes com um número de teste em coexistência.
2b. Escala além de 2 canais: como a coexistência é a predefinição e só existe em Tech Providers aprovados, a Cloud API direta com app própria fica excluída. Ao terceiro número, Chakra (favorita) ou YCloud paga. Nessa altura o adaptador [A] e o expedidor [I] ganham uma segunda implementação; o resto do núcleo não muda. Manter o adaptador "Meta direta" só como reserva.
3. Permissão `business_management` no token do utilizador de sistema [?]: adicionar no Business Suite da Blue Serenity quando se gerar o próximo token; sem ela o monitor não lê `health_status` dos clientes.
4. Agregação de mensagens em 8 s: confirmar se a Vitória já o faz; se não, é a primeira coisa a acrescentar ao núcleo.
5. Postgres vs. Data Tables: decidir ao quinto cliente com os números de `eventos` à frente.

---

## 9. Ordem de trabalho sugerida para esta sessão

1. Escrever o esquema das tabelas em ficheiros CSV vazios com cabeçalhos e a linha do Lisbon Riding Club em `clientes` (sem segredos).
2. Escrever o prompt de sistema do cérebro com as regras fixas e os espaços para o registo do cliente e a base.
3. Definir as 9 ferramentas (nome, parâmetros, o que devolvem) em JSON, prontas a colar no nó do LLM.
4. Desenhar o adaptador YCloud → formato interno assim que houver um payload real do webhook da YCloud.
5. Preparar o guião de teste de 12 mensagens da Clara.
