# AI Act como porta de entrada — proposta de oferta
**Rascunho · julho 2026 · PROPOSTA, não decisão.** Altera a arquitetura de oferta de `strategy/positioning.md` §4 com uma camada nova. Aguarda decisão do Alexandre.

---

## 1. Veredicto sobre a ideia

A analogia com o RGPD está certa na estrutura e errada no calendário. Vale a pena, mas não pela razão óbvia — e a versão óbvia da oferta faria mal à marca.

**Onde a analogia se sustenta:** regulação horizontal, aplicação direta, quase toda a gente abrangida, coimas altas, e — o ponto decisivo — **obriga a um inventário que ninguém tem.** Foi isso que criou o mercado do RGPD em 2017–2018, não o texto legal.

**Onde a analogia parte, e é preciso saber antes de abrir a boca num cliente:**

1. **O prazo que criaria pânico acabou de se mover.** O Digital Omnibus é lei (Regulamento (UE) 2026/1744, em vigor em julho de 2026). As obrigações dos sistemas de alto risco passaram de 2 de agosto de 2026 para **2 de dezembro de 2027** (Anexo III) e **2 de agosto de 2028** (Anexo I). Quem estava a preparar-se acabou de receber mais dezasseis meses. **Vender urgência sobre alto risco em agosto de 2026 é vender um prazo que já não existe** — e qualquer diretor financeiro informado apanha isso. Custaria mais credibilidade do que traria reuniões.

2. **Quem compra "compliance" é o jurídico, não o CEO.** O mercado do RGPD foi ganho por sociedades de advogados e por DPO-as-a-service. A Bluewright não tem credencial jurídica e não deve fingir que tem. Entrar por aí é competir com a PwC Portugal, a Andersen e todos os escritórios de Lisboa e Madrid, num terreno onde a Bluewright perde.

3. **A conformidade comoditiza depressa.** As Big4 orçamentam entre 80.000 e 200.000 USD; dentro de um ano estará reduzida a checklist. Acaba em documento, não em processo instalado. É o contrário de *from problem to process*.

4. **A maioria das empresas ibéricas de média dimensão é *deployer*, não *provider*.** As obrigações reais que lhes caem em cima são estreitas. Inflacioná-las seria desonesto e detetável.

**Onde a ideia é genuinamente boa** — e é melhor do que a versão que o Alexandre tinha em mente:

O que entra em vigor **depois de amanhã** não é um problema jurídico. É um problema de inventário. E é o inventário que abre a porta.

---

## 2. O que está mesmo em vigor — o mapa, sem exageros

| Obrigação | Desde / a partir de | A quem se aplica | Estado |
|---|---|---|---|
| Art. 5 — práticas proibidas | 2 fev. 2025 | todos | em vigor, alargado |
| **Art. 4 — literacia em IA** | **2 fev. 2025** | **todo o provider e deployer, qualquer nível de risco** | **em vigor há 17 meses** |
| Obrigações GPAI, governação, coimas | 2 ago. 2025 | modelos de uso geral | em vigor |
| **Art. 50 — transparência** | **2 ago. 2026** | providers e deployers | **não foi adiado** |
| Supervisão nacional das obrigações em vigor | 3 ago. 2026 **[VERIFICAR]** | — | ANACOM (PT), AESIA (ES) |
| Proibição NCII / CSAM; fim do período de tolerância de marcação | 2 dez. 2026 | — | novo |
| Alto risco — Anexo III | **2 dez. 2027** | sistemas autónomos | **adiado** |
| Alto risco — Anexo I | **2 ago. 2028** | embebidos em produtos regulados | **adiado** |

**Três factos que valem a pena reter:**

**Art. 50 aplica-se a 2 de agosto de 2026 — daqui a dois dias — e não foi adiado.** Exige informar quem interage com um sistema de IA, marcar conteúdo sintético de forma legível por máquina, revelar reconhecimento de emoções e categorização biométrica às pessoas expostas, e identificar deepfakes e certos textos de interesse público. Para um *deployer* típico é estreito. Mas obriga a saber onde há chatbots, onde há conteúdo gerado, e sob que contrato.

**O Art. 4 é uma obrigação de formação, está em vigor há dezassete meses, e aplica-se a toda a gente.** O Omnibus suavizou a redação — de "assegurar um nível suficiente" para "tomar medidas para apoiar o desenvolvimento" da literacia em IA — mas continua vinculativa para todo o deployer, independentemente do nível de risco, e estende-se a contratados e prestadores de serviços. Quem não fez nada **já está em incumprimento**, e não tem prazo futuro atrás do qual se esconder.

**Espanha acrescenta uma camada nacional com dever explícito de inventariar.** O Projeto de Lei Orgânica para o bom uso e governação da IA foi aprovado em Conselho de Ministros a 26 de maio de 2026, ainda não em vigor **[VERIFICAR estado atual]**, com coimas até 35 M€ ou 7% do volume de negócios mundial para práticas proibidas, AESIA como autoridade central e o dever de inventariar e supervisionar o uso de IA a recair sobre as empresas. Portugal não aprova lei nacional — o regulamento aplica-se diretamente e a ANACOM coordena catorze autoridades setoriais.

---

## 3. O ângulo — porque isto é uma porta e não um produto

Ninguém consegue cumprir seja o que for antes de saber **que IA está a ser usada, por quem, para quê e ao abrigo de que contrato.** E praticamente nenhuma empresa média ibérica sabe:

- pessoas a usar ferramentas por conta própria, sem decisão de ninguém;
- funcionalidades de IA ligadas pelo fornecedor dentro de software que a empresa já tinha — CRM, RH, marketing, apoio ao cliente — sem que alguém as tenha escolhido;
- pilotos iniciados por uma equipa e nunca reportados;
- e, do lado do papel, confusão sobre se a empresa é *provider* ou *deployer* de cada um deles — usar um modelo de terceiros não faz de ninguém provider automaticamente.

A melhor formulação que encontrei na análise jurídica é esta: **é um inventário de casos de uso, não de sistemas.**

Ora, um inventário de casos de uso de IA, por função, com dono e contrato identificados, **é literalmente a semana 1 do assessment.** A obrigação legal força a conversa que a Bluewright já quer ter, com a pessoa com quem já quer falar, e paga-a.

E há um segundo encaixe, ainda melhor. O Art. 4 é uma obrigação de **formar pessoas para usarem IA corretamente**. É a camada de Capacitação, com uma obrigação legal a criar-lhe procura. Trinta anos de docência e o Título de Especialista não têm equivalente em nenhum dos quatro grupos concorrentes mapeados em `market-analysis.md` §4. **É o melhor encaixe produto-mercado de todo o reposicionamento.**

> A conformidade é a razão para abrir a porta. A adoção é o que se vende lá dentro. Nunca ao contrário.

---

## 4. A oferta proposta

### 4.1 O que NÃO fazer

Uma "Auditoria de Conformidade com o AI Act". Compete com advogados, entrega um documento, morre quando a checklist comoditizar, e transforma a Bluewright num fornecedor de conformidade. O próprio nome do produto — *AI Act Readiness Assessment* — é o termo mais saturado do mercado. Usá-lo é aceitar ser comparado com toda a gente.

### 4.2 Camada 0 — **AI Use Review**

*Uma semana. Preço fixo. Todo o AI em uso, mapeado contra o que a lei exige mesmo.*

| | |
|---|---|
| **Duração** | 5 dias úteis |
| **Preço proposto** | **2.500€, tudo incluído** |
| **Crédito** | 100% creditado no *Digital & AI Readiness Assessment* se avançar em 90 dias |
| **Decisor** | CEO / Country Manager, assinatura única, sem comité |

**Dias 1–2 — Inventário.** Todo o uso de IA: comprado, embebido em ferramentas já existentes, e o que ninguém autorizou. Por função, com dono e contrato.

**Dia 3 — Classificação.** Cada caso de uso pelo papel da empresa (provider ou deployer) e pela obrigação que realmente aciona: Art. 5, Art. 50, Art. 4, alto risco em 2027–2028, ou nenhuma.

**Dia 4 — Lacunas.** O que é exigível agora, o que é exigível em dezembro de 2027, e — dito explicitamente — **o que não tem obrigação nenhuma.** Dizer a um cliente que 80% da lista dele não exige nada é a coisa mais credível que se pode fazer numa primeira semana, e é exatamente o que um escritório a faturar à hora não vai dizer.

**Dia 5 — Registo e sessão.** Um registo de uma página que a empresa passa a manter, o mapa de obrigações, o esboço do plano de literacia do Art. 4, e uma sessão de trabalho com a gestão.

**Porquê 2.500€.** É um produto de uma semana; é uma assinatura fácil, abaixo dos limiares de delegação de competências da maior parte das filiais, logo sem comité; e é a forma mais barata que existe de comprar uma primeira conversa com um CEO que nunca aceitaria uma reunião fria. O crédito integral no assessment mantém a disciplina de `positioning.md` §6: generosidade explícita e quantificada, nunca desconto.

### 4.3 Capacitação — **AI Literacy Programme (Art. 4)**

Vendável isoladamente e o item de maior margem da carteira.

- Sessão executiva para a gestão: o que a lei exige, o que a empresa está mesmo a usar, o que decidir.
- Sessões por equipa, adaptadas à função — quem usa IA em vendas não precisa do mesmo que quem a usa em operações.
- **Registo do que foi entregue, a quem, quando e com que conteúdo.** Este ponto é o produto: sendo o Art. 4 uma obrigação de meios, a prova das medidas tomadas *é* a conformidade. É o que a empresa mostra à autoridade.
- Repetível anualmente. Sem tecto de entrega — não consome dias de consultoria sénior na mesma proporção.

**Preço: a decidir.** Recomendo preço por sessão e por programa, nunca por participante — cobrar à cabeça converte formação em mercadoria e convida à comparação com plataformas de e-learning a 30€ por pessoa.

### 4.4 Como as camadas encaixam

```
AI Use Review (1 semana, 2.500€)
        └─ crédito 100% ──▶ Digital & AI Readiness Assessment (4 semanas, 9.500€)
                                    └─ crédito 50% ──▶ Transformação (camada 2)
                                                              └──▶ Advise (camada 3)
        └────────────────────────▶ AI Literacy Programme (Art. 4) — em qualquer ponto
```

A Camada 0 não canibaliza o assessment: qualifica-o. Quem faz a review e não avança não era cliente do assessment; quem avança, avança já convencido e com o inventário feito.

---

## 5. Regras de honestidade — inegociáveis

Estas não são cautelas de estilo. Quebrar qualquer uma delas destrói mais valor do que a oferta inteira gera.

1. **Nunca dizer "tornamo-lo conforme".** O que se produz é o inventário e o mapa do que se aplica. O parecer jurídico fica com os advogados do cliente. A Bluewright não é uma sociedade de advogados — e dizê-lo em voz alta é um diferenciador face a quem deixa a fronteira por esclarecer.
2. **Nunca usar o prazo de alto risco como urgência.** Foi adiado, publicamente, para dezembro de 2027. Quem o invocar em agosto de 2026 é apanhado.
3. **Nunca inflacionar as coimas.** Os 35 M€ / 7% aplicam-se a práticas proibidas. Não é o que acontece a quem se esqueceu de identificar um chatbot.
4. **Nunca vender a review como fim.** É uma porta. Se o cliente só precisar da review, entrega-se a review e vai-se embora — e diz-se isso à partida.

---

## 6. Momento

O Art. 50 aplica-se **a 2 de agosto de 2026**. A supervisão nacional arranca a seguir. É o melhor momento dos próximos dezoito meses para publicar o artigo de lançamento previsto na Fase 3 do `ops/backlog.md`.

E o artigo da tese e o artigo do AI Act são o mesmo artigo. A tese diz que a tecnologia não transforma nada sem processo e sem pessoas. O AI Act, na prática, obriga as empresas a fazer exatamente duas coisas: **saber o que estão a usar** (processo) e **preparar quem o usa** (pessoas). A lei europeia acabou de tornar obrigatório aquilo que a Bluewright já dizia ser o que faltava.

Ângulos para o artigo, por ordem de força:
1. *O prazo que se moveu, e os dois que não se moveram.* Serviço público puro — metade do mercado ainda pensa que 2 de agosto era o prazo do alto risco.
2. *A obrigação que está em vigor há dezassete meses e quase ninguém cumpriu.* Art. 4.
3. *Ninguém sabe que IA tem dentro de casa.* O argumento do inventário, que leva à Camada 0 sem a mencionar.

---

## 7. Decisões que precisam do Alexandre

- [ ] Avançar ou não com a Camada 0. Se sim, `strategy/positioning.md` §4 tem de ser atualizado — é o registo de decisões.
- [ ] Preço da AI Use Review: 2.500€ ou outro. **Atenção ao padrão já identificado em `CLAUDE.md`** — abaixo de 2.000€ deixa de ser um produto sénior e passa a ser um favor.
- [ ] Preço e formato do AI Literacy Programme.
- [ ] Nome final do produto. *AI Act Readiness* está saturado; *AI Use Review* é sóbrio e descritivo. Alternativa a considerar: *AI in Use*.
- [ ] Confirmar o estado do Projeto de Lei Orgânica espanhol e a data de arranque da supervisão nacional. **[VERIFICAR]**
- [ ] Decidir se o one-pager EN da Camada 0 se produz antes ou depois do artigo de lançamento.

---

## Fontes

Gibson Dunn — [EU AI Act Omnibus Agreement: postponed high-risk deadlines](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/) · Sidley — [EU lawmakers reach provisional agreement to delay key AI Act obligations](https://datamatters.sidley.com/2026/06/22/eu-lawmakers-reach-provisional-agreement-to-delay-key-eu-ai-act-obligations/) · Freshfields — [The final Digital Omnibus on AI](https://www.freshfields.com/en/our-thinking/blogs/technology-quotient/eu-ai-act-unpacked-34-the-final-digital-omnibus-on-ai-key-amendments-to-the-a-102nber) · [Article 50 transparency: the deadline that was not postponed](https://www.aiactblog.nl/en/posts/article-50-transparency-deadline-2-august-2026) · [Artigo 4.º — Literacia em IA](https://artificialintelligenceact.eu/article/4/) · Latham & Watkins — [Mandatory training and prohibited practices](https://www.lw.com/en/insights/upcoming-eu-ai-act-obligations-mandatory-training-and-prohibited-practices) · Andersen — [ANACOM assume supervisão em Portugal](https://pt.andersen.com/2025/10/03/ai-act-anacom-assume-supervisao-em-portugal/) · PwC Portugal — [AI Act: o que muda para as empresas em Portugal em 2026](https://www.pwc.pt/pt/sala-imprensa/artigos-opiniao/2026/ai-act-muda-empresas-portugal-2026.html) · Economist & Jurist — [Ley de gobernanza de la IA: deber de inventariar](https://www.economistjurist.es/zbloque-1/ley-de-gobernanza-de-la-ia-el-deber-de-inventariar-y-supervisar-el-uso-de-inteligencia-artificial-recae-sobre-las-empresas-con-sanciones-de-hasta-35-millones-de-euros/) · Groath — [AI governance consulting: where Big-4 frameworks fall short](https://groath.ai/strategy/ai-governance-consulting)
