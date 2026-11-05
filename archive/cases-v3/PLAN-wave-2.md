# Plano da 2.ª vaga de casos (24 out 2026) — proposta do estratega, por validar

Objetivo: um diretor-geral cético de uma subsidiária ibérica marcar uma conversa sobre o Assessment. Método: ver HANDOFF.md.

**Limite do plano:** as 4 páginas antigas da Blue Serenity não foram lidas (WebFetch bloqueado para web.archive.org). Nada aqui afirma factos delas.

## Recomendação: 4 peças

1. **ISQ España** (um só caso, eixo «do clipping à inteligência de mercado»; recrutamento e conteúdo fundidos ou descartados). Substitui o caso 2. Dados brutos: execuções n8n.
2. **Caso 3, «long game»** (Advise). Bloqueia a Fase 0 (`positioning.md`). Cliente a escolher, de preferência outro que não a ISQ (dBwave.i se a relação for longa).
3. **ISQ Formação** (Transform, modelo replicável). Só com dados de antes e depois em produção.
4. **Escola de equitação**: micro-caso só para LinkedIn, fora do site (B2C, fora do alvo).

Lacunas: a camada 1 só tem o caso 4; a camada 3 está vazia; a Capacitação não tem caso (ou se encontra formação com dados de adoção, ou entra como secção do caso 1). Risco de concentração: no máximo 2 peças ISQ no site.

## Mapa

| Candidato | Camada | Prova esperada | Risco | Nome |
|---|---|---|---|---|
| ISQ ES: clipping -> inteligência | Transform | alta (execuções n8n) | ninguém usa os resultados; retenção | nomeável (autorização) |
| ISQ ES: recrutamento | Transform | desconhecida | RGPD | fundir |
| ISQ ES: conteúdo | Transform | fraca (vaidade) | sobrepõe-se aos casos 2 e 5 | fundir/descartar |
| ISQ Formação: radar | Transform | por confirmar | «faz disparar» sem número | nomeável |
| Equitação | Capacitação pequeno | média | B2C | anónima |
| ISQ/dBwave.i antigos | Advise | duração | desatualizado | nomeáveis |
| «Clientes, não reféns» | — | material p/ ensaio da camada 3 | não é caso | — |
| «Quanto custa um site» | — | descartar (posicionamento de agência) | — | — |

## Casos

1. **«The press clipping that became a sales input»**. Pergunta: *o que é que a sua equipa já recolhe e que ninguém transforma em decisão?* Fontes: execuções n8n da instância autoisq (só leitura), histórico de versões, ficheiros semanais no SharePoint, amostra reclassificada por alguém da ISQ. Rácios: execuções bem-sucedidas, semanas entregues no prazo, precisão da classificação, resumos abertos, publicações que originaram ação. Procurar o que falhou: execuções falhadas, bloqueios de scraping, classificações erradas, resultados não lidos.
2. **Long game**. Pergunta: *quem decide o digital na sua empresa sem ter interesse no que se compra?* Fontes: faturas, propostas, versões do site. Rácios: anos, compromissos, parte recorrente. Procurar: projetos abandonados.
3. **ISQ Formação**: «the shop was the wrong question». Pergunta: *a sua ferramenta serve o cliente ou o processo de outra pessoa?* Fontes: analytics da loja antiga e nova, back-office, CRM. Rácios: conversão antes/depois, encomendas ainda manuais, oportunidades do radar contactadas e inscritas. Procurar: falsos positivos do radar, problemas de migração, funções não usadas.
4. **Equitação**: registos das conversas. Rácios: perguntas resolvidas sem humano, parte fora de horas, encaminhamentos. Procurar: respostas erradas.

## Juízes e critério

Todos: `check_ledger.py` passa; memorando adversarial sem ponto grave por resolver; 3 de 5 leitores marcariam conversa. Falha imediata: número sem linha no registo, ou resultado só com métricas de vaidade. ISQ nomeada: juiz 3 substituído por aprovação escrita do cliente. Anónimos: juiz 3 numa sessão limpa. ISQ Formação: sem antes/depois não se publica.

## Perguntas ao Alexandre (desbloqueiam tudo)

1. Guarda as 4 páginas antigas localmente ou cola o texto?
2. ISQ España: quais dos três âmbitos estão em produção e desde quando? Houve decisões tomadas a partir do clipping?
3. Quem aprova por escrito a nomeação (ISQ España e ISQ Formação)?
4. Acesso só de leitura às execuções em autoisq? Qual a retenção?
5. ISQ Formação: em produção, em construção ou em proposta? O radar já existe?
6. Que número sustenta «faz disparar o valor»?
7. Qual o cliente do caso 3 e desde que ano? Estado da relação com a dBwave.i?
8. Equitação: qual foi a «vitória»? Os registos podem ser exportados?
9. Há formação executiva com dados de assiduidade/adoção?
10. A regra «só rácios» aplica-se também a clientes nomeados?
11. Quem são os 5 leitores (juiz 4)?
12. Recrutamento: quem é dono dos dados de RH, há dados pessoais?
