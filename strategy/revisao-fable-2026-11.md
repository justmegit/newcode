# Revisão externa — viabilidade, adequação e plano
**5 nov 2026 · leitura integral do branch `consultoria-b2b-fable` · documento de opinião, não de decisão**

Li tudo: `CLAUDE.md`, `KICKOFF.md`, brand book, `positioning.md` (v2), `market-analysis.md`, `go-to-market.md`, os 11 casos v4 com os juízes e os registos de provas, os dois ensaios, o one-pager do assessment, a proposta AI Act, a secção «AI Search Visibility», o bio kit, a cópia do site, o `report-engine` e o backlog/decisões. Corri o `check_v4.py`: passa em todos os casos e na secção 5 do site.

Respeito as secções `[DECIDIDO]`. Onde discordo, proponho e não altero.

---

## 0. Veredicto, em dez linhas

1. **O negócio é viável e a tese está certa.** O mercado não é a restrição; a análise bottom-up é honesta e a posição no «espaço vazio» entre Big4 e freelancers é real e defensável.
2. **O risco não está no mercado nem nos materiais. Está no tempo.** O plano é de julho; estamos em novembro. Os seis itens que bloqueiam tudo (nome, email, ano, foto, `[FILL]`, decisão de anonimato) continuam por fechar, e nenhuma ação pública aconteceu. O repositório tem quatro meses de produção e zero meses de venda.
3. **A oferta promete mais largura do que a prova sustenta.** Os 11 casos são excelentes, mas são quase todos sobre o motor comercial (media, leads, conteúdo, recrutamento, catálogo, clipping). O assessment vende «transformação da empresa» em seis dimensões. Um Country Manager industrial vai ler os casos e pensar «grande consultor de marketing digital». Recomendo estreitar a promessa até onde está a prova.
4. **O preço do assessment está baixo para a posição.** A 9.500€, a diária real nos primeiros assessments cai abaixo dos 560€ do freelancer sénior da Malt. A própria análise de mercado já o diz; eu subscrevo e proponho 12.000€, a decidir a frio.
5. **A camada Advise é 72% da receita prevista e não tem um único caso.** É a lacuna de prova mais cara do conjunto.
6. **A base de clientes atual é estreita e um pilar está a encolher.** Onze casos vêm de três relações (Conceptance, grupo ISQ, SOGEM). A Conceptance é B2C, internalizou o site e migrou o CRM sozinha. O SOGEM não decidiu. Resta o ISQ.
7. **A secção «AI Search Visibility» (1.500€ / 350€ por mês) não pertence à Bluewright.** É exatamente o Grupo 4. Ou fica na Blue Serenity, ou entra como medição dentro do assessment.
8. **A camada 0 «AI Use Review» a 2.500€ repete o padrão de subpreço.** O que vale ouro nessa proposta é o programa de literacia do Art. 4, não a review.
9. **O ativo mais valioso continua por inventariar:** a rede de trinta anos de ex-alunos. O GTM diz que é a prioridade absoluta desde julho.
10. **Próximos 30 dias: zero documentos novos, uma tarde de decisões, vinte conversas.** O resto deste documento serve para isso.

---

## 1. Estado real, numa tabela

| Peça | Estado | O que falta |
|---|---|---|
| Tese e posicionamento | Sólidos, fechados | Nada. Não reabrir. |
| Marca (nome, identidade, tokens) | Pronta | Verificação de nome (domínio, LinkedIn, EUIPO/INPI) — **bloqueia tudo desde julho** |
| Análise de mercado e GTM | Muito bons | Quatro `[VERIFICAR]` em §7; Kit Consulting por confirmar |
| Assessment (camada 1) | Especificado, one-pager e PDF | Preço a rever a frio; kit de entrega (guião de entrevistas, modelo de scoring) inexistente |
| Casos (11, v4) | Prontos, verificados, honestos | 5 `[FILL]` (01, 06 resolvido, 09, 10, 11); caso Advise inexistente; teste com 5 leitores por fazer |
| Site | Construído, local | Foto, email, decisão sobre quantos casos mostrar, deploy |
| Bio kit e CV | Prontos | Alinhar ano de fundação e línguas |
| Transição de clientes atuais | Nem guião nem conversas | Tudo |
| Rede dormente | Nada | Inventário (300 → 120 nomes) |
| AI Act (camada 0 + literacia) | Proposta de julho, hoje desatualizada | Decisão; a janela do Art. 50 (2 ago) já passou |
| AI Search Visibility | Ficheiro solto na raiz | Decisão de **não** integrar na Bluewright |
| Report engine | Funcional, interno | Nada. É o que justifica a avença mensal. Manter. |

---

## 2. Viabilidade

### 2.1 A economia da unidade

O assessment é descrito como ~13 dias de esforço. Nos primeiros três ou quatro, enquanto o método se constrói (guião de entrevistas, modelo das seis dimensões, benchmark), a experiência diz 16 a 20 dias.

| Dias reais | Diária a 9.500€ | Diária a 12.000€ | Diária a 15.000€ |
|---|---|---|---|
| 13 | 731€ | 923€ | 1.154€ |
| 16 | 594€ | 750€ | 938€ |
| 18 | 528€ | 667€ | 833€ |
| 20 | 475€ | 600€ | 750€ |

Referência: freelancer de estratégia com 15+ anos, Espanha, 560€/dia (Malt 2026, citado em `market-analysis.md` §5). **A 18 dias reais, o assessment a 9.500€ paga menos do que o grupo de que a marca quer distinguir-se.** O argumento da decisão 7 («um diagnóstico barato diz freelancer») aponta, com os números na mão, para cima e não para baixo.

A avença, pelo contrário, está bem posicionada: 2.500€/mês por ~2 dias é 1.250€/dia. **A margem do negócio está na camada 3.** O assessment é o bilhete de entrada; pode ser pago abaixo da avença, mas não abaixo do freelancer.

### 2.2 O tecto e a rampa

O modelo de regime estável (5 avenças + 6 assessments ≈ 207k€, tecto 200–260k€) está certo para uma pessoa. O que o repositório não contém, e sem o qual não consigo fechar a viabilidade:

- receita atual da Blue Serenity por cliente e por mês;
- custos fixos e o custo do operador júnior que aparece nos casos 06 e 11;
- quantos meses de rampa a receita legada aguenta.

O ano 1 do GTM (4 assessments, 2 conversões, 3 avenças) dá, na melhor das hipóteses, 80–120k€ de receita nova, grande parte no segundo semestre. **A viabilidade da transição depende de a receita legada cobrir 6 a 9 meses.** É a única pergunta de viabilidade que o Alexandre tem de responder e que nenhum documento responde.

### 2.3 Concentração e dependência

- **Três relações sustentam toda a prova.** A Conceptance (quatro casos e o ensaio) dá sinais de saída: site e email internalizados em semanas, CRM migrado por decisão própria, caso 04 em que «nada mudou». O SOGEM está parado à espera da administração. O grupo ISQ é hoje a única relação com profundidade e a candidata natural à primeira avença.
- **Um modelo operacional escondido.** Os casos 06 e 11 funcionam com «um operador júnior do nosso lado» e um sénior a desenhar. Isso não é o «no pyramid of juniors» do site; é um serviço gerido, com receita recorrente (o caso 06 vale ~40% de um júnior, portanto ~12–14k€/ano). Não está em nenhuma camada da oferta. Ou se nomeia dentro da camada 3 («Advise, com operação») ou cria-se uma contradição que um cliente atento apanha.

### 2.4 Conclusão de viabilidade

Viável, com três condições: (a) a receita legada cobre a rampa; (b) pelo menos duas avenças assinam até fevereiro, vindas da base atual; (c) o assessment é reposicionado em preço antes de ser público. Se (a) falhar, o plano passa a precisar de um ano de rendimento paralelo (docência) e o calendário do GTM estica para 18 meses, o que também é viável, mas é outro plano.

---

## 3. Adequação

### 3.1 O que encaixa bem

- **Tese ↔ dados.** MIT 95%, McKinsey 5,3×, 37% das PME portuguesas sem função digital. A tese deixou de ser opinião. O artigo de lançamento escreve-se sozinho.
- **Alexandre ↔ alvo.** Engenheiro, quatro línguas, telecom, docência, vendas técnicas. O perfil é raro no mercado ibérico e os quatro diferenciadores do §4 da análise de mercado são verificáveis.
- **Forma ↔ posicionamento.** Preço publicado, âmbito fechado, prazo fixo, «no follow-up sequence if the answer is no». A forma faz o trabalho de separação do Grupo 4.
- **Casos ↔ voz.** Fracassos assumidos, números com registo, «three questions to ask your team tomorrow». Não conheço consultoria ibérica a publicar casos com esta honestidade. É o ativo de marca mais distintivo que o repositório tem.
- **Report engine ↔ avença.** Relatório mensal com duas frases do consultor é a prova recorrente de valor. É o que faz uma avença durar anos.

### 3.2 O que não encaixa

**a) A promessa é mais larga do que a prova.** Dos 11 casos, 9 vivem no motor comercial e de comunicação (media, leads, afirmações, conteúdo, recrutamento como comunicação, catálogo online, clipping, cross-selling). O assessment promete seis dimensões ao nível da empresa, incluindo «processos e operações» e «dados e sistemas». Um diretor de operações industrial não encontra nos casos nada sobre produção, logística, ERP, manutenção ou serviço técnico.

A correção não é inventar prova; é estreitar a promessa. E há uma coerência feliz: **as filiais ibéricas de grupos estrangeiros são, na esmagadora maioria, operações comerciais e de serviço.** O mandato do Country Manager é vender e servir em Iberia o que a sede produz. O problema dele *é* o motor comercial. Proponho que o assessment se chame e se descreva como diagnóstico do motor comercial e dos processos que o rodeiam (marketing, vendas, serviço, comunicação, recrutamento comercial), mantendo as seis dimensões como lentes. É mais vendável, é verdadeiro, e nenhuma das onze provas fica de fora.

**b) Quatro casos são de um cliente B2C.** A Conceptance vende pérgolas a famílias. Os casos 02–05 são tecnicamente irrepreensíveis, mas um comprador B2B repara na primeira linha («households»). As lições transferem-se; a credencial não. Sugiro usar 02 e 04 (os mais fortes) com o contexto reenquadrado para a relação B2B que existe por baixo: um instalador dentro de uma **rede de revendedores de um fabricante europeu**. E isso abre um ICP (ver §5).

**c) A camada Advise não tem prova.** É 150k€ dos 207k€ do modelo. O «long game» saiu do site por não ter cliente. A relação ISQ é multi-anual e tem seis casos; um caso Advise escreve-se a partir dela sem violar a regra «um cliente, um desafio» se o desafio for o da gestão («não tenho ninguém que lidere o digital por dentro e não quero contratar um diretor»).

**d) AI Search Visibility.** Audit a 1.500€, monitor a 350€/mês, execução GEO. É um produto de agência de marketing, com preços de agência, numa página de consultoria sénior. Contraria o posicionamento, o brand book (tokens diferentes, inclusive) e a decisão 1. A medição de visibilidade em assistentes de IA é uma boa ferramenta: cabe dentro da dimensão «motor comercial» do assessment, como uma linha, e eventualmente na Blue Serenity como serviço legado. Não cabe na Bluewright como oferta.

**e) AI Act, camada 0.** A análise jurídica é a melhor peça do repositório depois dos casos: o Omnibus, o Art. 4 em vigor desde fevereiro de 2025, a distinção provider/deployer, as regras de honestidade. Mas:
- O documento é de julho e fala do Art. 50 «daqui a dois dias». Estamos em novembro. A supervisão nacional e a lei orgânica espanhola estão em `[VERIFICAR]`. Precisa de atualização antes de qualquer uso.
- Uma review de uma semana a 2.500€ é a quarta tabela de preços e a mais baixa. Qualifica, sim, mas também ensina ao mercado que a Bluewright se compra por 2.500€. O inventário de casos de uso de IA é, por definição, a semana 1 do assessment; prefiro vendê-lo como entregável nomeado dessa semana do que como produto solto.
- O que tem procura legal, margem alta e encaixe único com trinta anos de docência é o **AI Literacy Programme (Art. 4)**, com registo do que foi entregue a quem. Esse sim, adoto como linha de Capacitação com preço por programa, não por participante, exatamente como a proposta recomenda.

**f) Onze casos de quatro compromissos.** O juiz avisou que pode ler-se como enchimento. Concordo. O site ganha em mostrar seis (02, 04, 06, 07, 09, 11) e guardar os restantes para propostas, com a frase «drawn from four engagements» a dizer a verdade com elegância.

**g) Pequenas incoerências que um comprador apanha.** Fundação 2007 (one-pager) vs 2008 (bio) vs 2009 (LinkedIn). Francês «fluent» no one-pager e na cópia do site vs «gets by» no bio kit. `positioning.md` §5 fala em «três casos» quando existem onze. O `README.md` aponta para `strategy/case-studies.md`, que já não existe. Nada disto é grave isoladamente; junto, sinaliza falta de acabamento numa marca cujo argumento é o acabamento.

---

## 4. Ajustes recomendados, por ordem

Marcados como **[PROPOSTA]** porque tocam em secções decididas ou em preço, e a regra da casa é propor e esperar.

1. **[PROPOSTA] Preço do assessment: 12.000€.** Coincide com o bono do segmento A do Kit Consulting, fica dentro da banda independente internacional (15–75k€, por baixo) e mantém a diária acima do freelancer até 20 dias reais. Mudar antes de publicar; depois de público, subir preço custa mais do que o dinheiro.
2. **[PROPOSTA] Estreitar a promessa do assessment ao motor comercial e processos adjacentes.** Mesmas seis dimensões como lentes; nome e primeiro parágrafo reescritos. Alinha prova, alvo e comprador.
3. **Retirar «AI Search Visibility» da Bluewright.** Guardar a medição como linha do assessment. Decidir se vive na Blue Serenity.
4. **Camada 0: não como produto a 2.500€.** Inventário de IA passa a entregável nomeado da semana 1. Adotar o **AI Literacy Programme (Art. 4)** como oferta de Capacitação, com one-pager próprio. Atualizar o documento AI Act para novembro antes de o usar.
5. **Escrever o caso Advise** a partir da relação ISQ, desafio da gestão, não da operação.
6. **Seis casos no site, não onze.** Os outros cinco ficam para propostas e LinkedIn.
7. **Nomear o modelo «sénior + operador» dentro da camada 3** ou retirar do site a frase «no pyramid of juniors» em favor de «no hours to sell. One senior partner accountable for the outcome».
8. **Alinhar ano de fundação, línguas e email em todos os documentos**, numa só passagem.
9. **Construir o kit de entrega do assessment antes do primeiro cliente**: guião de entrevistas por dimensão, grelha de scoring, modelo do roadmap. Está em «Someday» no backlog; devia estar em Fase 0. Sem ele, os 13 dias viram 20.
10. **Higiene do repositório** (§8).

---

## 5. Clientes

### 5.1 Clientes atuais: a receita de 2027 começa aqui

| Relação | Estado | Movimento |
|---|---|---|
| Grupo ISQ (España + Academy) | Seis casos, operação em curso, relação multi-anual | **Primeira avença.** Conversa de transição em dezembro; formalizar o que já existe (sénior + operador + report) como Advise. É a prova viva da camada 3. |
| Conceptance | Internalizou site e email, migrou CRM, caso 04 sem mudança | Conversa honesta de encerramento ou redução a report mensal. Não gastar energia de aquisição aqui. O ensaio só se publica depois. |
| SOGEM | Cenários entregues, administração sem decisão | Um follow-up com data. Se não decide até janeiro, o caso 01 fecha como está (perguntas ao leitor) e a relação entra em modo passivo. |

### 5.2 O ICP que a prova sustenta hoje

Dois padrões saem dos casos e são B2B puros:

**A. Fabricantes europeus que vendem em Iberia através de redes de instaladores ou revendedores.** É o que está por baixo da Conceptance (rede de um fabricante europeu) e da ISQ Academy (academia para a rede de revendedores de um fornecedor). O comprador é o fabricante ou a sua filial ibérica; o problema é «os meus parceiros locais não vendem nem comunicam como a marca precisa». É *channel enablement* com processo, e o Alexandre tem duas provas. Setores: produtos de construção, climatização, energia solar e armazenamento, equipamento técnico, outdoor living. Nomes via CCILA, CCLBL e CCI France (empresas alemãs, belgas e francesas com filial comercial em Portugal e Espanha).

**B. Filiais ibéricas de grupos de serviços técnicos e industriais, 50–500 pessoas.** É o ISQ España. O Country Manager vende serviços regulados, recruta técnicos, comunica sob regras do grupo. Casos 06, 07, 08, 11 falam-lhe diretamente. **Atenção ao conflito:** vender a concorrentes diretos do ISQ España em Espanha (inspeção e certificação) usando casos do ISQ é desconfortável, mesmo anonimizado, e a reidentificação já disse que quem conhece o setor reconhece. Preferir setores adjacentes: engenharia, manutenção industrial, serviços de energia, ambiente, segurança, formação técnica.

**C. Segundo anel, mais tarde:** PME técnicas ibéricas sem liderança digital. Só via Kit Consulting (se elegível) e ex-alunos. Não por outbound.

### 5.3 Canais, confirmando o GTM com três notas

- **Ex-alunos: é a lista que falta há quatro meses.** 300 nomes brutos, 120 priorizados, cargo e empresa atuais. Uma semana de trabalho de LinkedIn. Tudo o resto espera por isto.
- **Câmaras: sócio → orador → autor → referências.** CCILA e AmCham Portugal primeiro. A sessão fechada para membros com os dados da §3 da análise de mercado e o Art. 4 do AI Act («a obrigação em vigor há 21 meses que quase ninguém cumpriu») é o melhor título dos próximos seis meses.
- **Kit Consulting: a verificação mais valiosa do plano, ainda por fazer.** Se um consultor estabelecido em Portugal pode aderir ao catálogo de Asesores Digitales, Espanha passa a ter procura financiada a montante e o preço de 12.000€ coincide com o bono.

### 5.4 Quem não perseguir
Grandes empresas (processo de fornecedores, Big4), B2C, retalho, agências à procura de subcontratação, e qualquer marketplace de freelancers. Já está no GTM; repito porque a tentação regressa quando a agenda está vazia.

---

## 6. Plano de ação: 30 / 60 / 90 dias

### Dias 1–14: decidir e inventariar (nenhum documento novo)
- [ ] **Uma tarde de decisões**: nome (domínio, LinkedIn, EUIPO/INPI), email, ano de fundação, linha das línguas, foto. Seis decisões, uma tarde.
- [ ] **Três decisões de oferta, a frio**: preço (9.500 vs 12.000), promessa (empresa vs motor comercial), AI Search Visibility (fora). Registar em `decisions.md`.
- [ ] **Inventário da rede**: 300 nomes, 120 priorizados, em folha com cargo, empresa, dimensão, origem do capital.
- [ ] **Kit Consulting**: ler as bases de 2026, confirmar elegibilidade, ou pedir a resposta à Red.es.
- [ ] **Agendar a conversa com o ISQ** sobre a avença.

### Dias 15–45: casa arrumada e primeira receita
- [ ] Caso Advise escrito; seis casos escolhidos; `[FILL]` que dependem de tempo marcados com data.
- [ ] Site publicado com foto, email, seis casos, preço decidido.
- [ ] LinkedIn reposicionado (headline, About, banner).
- [ ] Guião de transição (EN + PT) e as três conversas: ISQ, Conceptance, SOGEM. **Meta: 1 avença assinada.**
- [ ] Adesão à CCILA e à AmCham Portugal.
- [ ] Kit de entrega do assessment: guião de entrevistas e grelha de scoring, versão 1.
- [ ] AI Act atualizado; one-pager do AI Literacy Programme.

### Dias 46–90: visível
- [ ] Artigo de lançamento: a tese com os dados e o Art. 4 como gancho de atualidade.
- [ ] Contacto pessoal com os 120, dez por semana, sem anexos, pedindo uma conversa.
- [ ] Primeira proposta de sessão a uma câmara.
- [ ] Cadência quinzenal de conteúdo iniciada; a grelha de auto-avaliação das seis dimensões como primeira peça.
- [ ] **Meta aos 90 dias: 2 avenças, 8 conversas de diagnóstico, 1 assessment contratado.**

### Indicadores (os cinco do GTM, mantidos)
Contactos pessoais (120/ano), conversas de diagnóstico (20), propostas (9), assessments (4), receita recorrente (7.500€/mês). Acrescento um sexto, para os primeiros 90 dias: **dias sem conversa comercial**. Se passar de cinco, o problema não é o plano.

---

## 7. Próximos passos para o Alexandre, esta semana

1. Marcar a tarde de decisões (§6, dias 1–14) e fazê-la.
2. Abrir a folha de ex-alunos e começar pelos 50 que já sabe de cor.
3. Enviar a mensagem ao ISQ a propor a conversa de dezembro.
4. Decidir o preço, a frio, com a tabela da §2.1 à frente.
5. Dizer-me qual das propostas da §4 aceita, e eu executo as alterações nos documentos.

---

## 8. Higiene do repositório

- A pasta `bluewright/` é uma cópia integral da raiz (sem `strategy/`, `site/` e `report engine/`). Duas fontes de verdade. Apagar.
- `strategy/cases/__pycache__/` está versionado. Adicionar `__pycache__/` e `*.pyc` ao `.gitignore`.
- `README.md` aponta para `strategy/case-studies.md`, que não existe; a tabela está desatualizada face à v4.
- `positioning.md` §5 e §8 descrevem três casos e tarefas já feitas. Atualizar sem tocar nas secções `[DECIDIDO]`.
- `report engine/` tem ficheiros com nome de cliente real e dados GA4. `CATALOGUE.md` tem o mapa cliente ↔ caso. Tudo bem num repositório privado; antes de partilhar o repositório com os cinco leitores de teste, ou com quem quer que seja, separar o que é interno.
- O ficheiro `bluewright-ai-visibility-section.html` na raiz usa tokens diferentes do brand book. Mover para `archive/` com a decisão.
- Todos os documentos de estratégia datam de julho. Uma linha «revisto em nov 2026» em cada um evita que um leitor futuro leia prazos do AI Act já passados como futuros.

---

## 9. O que não consegui avaliar

- Receita e custos atuais (§2.2). Sem isto, a viabilidade é condicional.
- A dimensão real da rede de ex-alunos. O GTM diz, e bem, que é o input que mais altera o plano.
- Se os cinco leitores do público-alvo marcariam conversa depois de ler os casos. O teste está desenhado e não foi feito.
- A elegibilidade no Kit Consulting.

Nenhum destes quatro depende de mim. Todos dependem de uma semana do Alexandre.
