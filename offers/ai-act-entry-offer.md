# AI Act como porta de entrada — análise e decisão
**Versão 2 · 5 nov 2026 · DECIDIDO em parte** (`ops/decisions.md` #16). Substitui o rascunho de julho de 2026. A análise jurídica (§1–§3) mantém-se, com as datas atualizadas; a oferta (§4) reflete o que foi decidido: **sem camada 0**, o inventário de IA passa a entregável da semana 1 do assessment, e o **AI Literacy Programme** (Art. 4) é adotado como produto de Capacitação.

**O que mudou de julho para novembro, em três linhas.** O Art. 50 (transparência) está em vigor desde 2 de agosto de 2026; a janela de «serviço público» sobre esse prazo fechou. O Art. 4 (literacia) está em vigor há **vinte e um meses** e continua, pela nossa leitura do mercado, largamente por cumprir. A proposta de uma review a 2.500€ foi recusada por repetir o padrão de subpreço identificado em `CLAUDE.md`.

---

## 1. Veredicto sobre a ideia

A analogia com o RGPD está certa na estrutura e errada no calendário. Vale a pena, mas não pela razão óbvia — e a versão óbvia da oferta faria mal à marca.

**Onde a analogia se sustenta:** regulação horizontal, aplicação direta, quase toda a gente abrangida, coimas altas, e — o ponto decisivo — **obriga a um inventário que ninguém tem.** Foi isso que criou o mercado do RGPD em 2017–2018, não o texto legal.

**Onde a analogia parte, e é preciso saber antes de abrir a boca num cliente:**

1. **O prazo que criaria pânico moveu-se.** O Digital Omnibus é lei (Regulamento (UE) 2026/1744, em vigor desde julho de 2026). As obrigações dos sistemas de alto risco passaram de 2 de agosto de 2026 para **2 de dezembro de 2027** (Anexo III) e **2 de agosto de 2028** (Anexo I). **Vender urgência sobre alto risco em 2026 é vender um prazo que não existe** — e qualquer diretor financeiro informado apanha isso. Custaria mais credibilidade do que traria reuniões.

2. **Quem compra "compliance" é o jurídico, não o CEO.** O mercado do RGPD foi ganho por sociedades de advogados e por DPO-as-a-service. A Bluewright não tem credencial jurídica e não deve fingir que tem. Entrar por aí é competir com a PwC Portugal, a Andersen e todos os escritórios de Lisboa e Madrid, num terreno onde a Bluewright perde.

3. **A conformidade comoditiza depressa.** As Big4 orçamentam entre 80.000 e 200.000 USD; dentro de um ano estará reduzida a checklist. Acaba em documento, não em processo instalado. É o contrário de *from problem to process*.

4. **A maioria das empresas ibéricas de média dimensão é *deployer*, não *provider*.** As obrigações reais que lhes caem em cima são estreitas. Inflacioná-las seria desonesto e detetável.

**Onde a ideia é genuinamente boa** — e é melhor do que a versão que o Alexandre tinha em mente:

O que está em vigor desde agosto de 2026 não é um problema jurídico. É um problema de inventário. E é o inventário que abre a porta.

---

## 2. O que está mesmo em vigor — o mapa, sem exageros

| Obrigação | Desde / a partir de | A quem se aplica | Estado |
|---|---|---|---|
| Art. 5 — práticas proibidas | 2 fev. 2025 | todos | em vigor, alargado |
| **Art. 4 — literacia em IA** | **2 fev. 2025** | **todo o provider e deployer, qualquer nível de risco** | **em vigor há 21 meses** |
| Obrigações GPAI, governação, coimas | 2 ago. 2025 | modelos de uso geral | em vigor |
| **Art. 50 — transparência** | **2 ago. 2026** | providers e deployers | **em vigor; não foi adiado** |
| Supervisão nacional das obrigações em vigor | 3 ago. 2026 **[VERIFICAR estado efetivo em nov 2026]** | — | ANACOM (PT), AESIA (ES) |
| Proibição NCII / CSAM; fim do período de tolerância de marcação | 2 dez. 2026 | — | novo |
| Alto risco — Anexo III | **2 dez. 2027** | sistemas autónomos | **adiado** |
| Alto risco — Anexo I | **2 ago. 2028** | embebidos em produtos regulados | **adiado** |

**Três factos que valem a pena reter:**

**Art. 50 aplica-se desde 2 de agosto de 2026 e não foi adiado.** Exige informar quem interage com um sistema de IA, marcar conteúdo sintético de forma legível por máquina, revelar reconhecimento de emoções e categorização biométrica às pessoas expostas, e identificar deepfakes e certos textos de interesse público. Para um *deployer* típico é estreito. Mas obriga a saber onde há chatbots, onde há conteúdo gerado, e sob que contrato.

**O Art. 4 é uma obrigação de formação, está em vigor há vinte e um meses, e aplica-se a toda a gente.** O Omnibus suavizou a redação — de "assegurar um nível suficiente" para "tomar medidas para apoiar o desenvolvimento" da literacia em IA — mas continua vinculativa para todo o deployer, independentemente do nível de risco, e estende-se a contratados e prestadores de serviços. Quem não fez nada **já está em incumprimento**, e não tem prazo futuro atrás do qual se esconder.

**Espanha acrescenta uma camada nacional com dever explícito de inventariar.** O Projeto de Lei Orgânica para o bom uso e governação da IA foi aprovado em Conselho de Ministros a 26 de maio de 2026; o seu estado em novembro de 2026 está por confirmar **[VERIFICAR antes de qualquer uso comercial]**, com coimas até 35 M€ ou 7% do volume de negócios mundial para práticas proibidas, AESIA como autoridade central e o dever de inventariar e supervisionar o uso de IA a recair sobre as empresas. Portugal não aprova lei nacional — o regulamento aplica-se diretamente e a ANACOM coordena catorze autoridades setoriais.

---

## 3. O ângulo — porque isto é uma porta e não um produto

Ninguém consegue cumprir seja o que for antes de saber **que IA está a ser usada, por quem, para quê e ao abrigo de que contrato.** E praticamente nenhuma empresa média ibérica sabe:

- pessoas a usar ferramentas por conta própria, sem decisão de ninguém;
- funcionalidades de IA ligadas pelo fornecedor dentro de software que a empresa já tinha — CRM, RH, marketing, apoio ao cliente — sem que alguém as tenha escolhido;
- pilotos iniciados por uma equipa e nunca reportados;
- e, do lado do papel, confusão sobre se a empresa é *provider* ou *deployer* de cada um deles — usar um modelo de terceiros não faz de ninguém provider automaticamente.

A melhor formulação que encontrei na análise jurídica é esta: **é um inventário de casos de uso, não de sistemas.**

Ora, um inventário de casos de uso de IA, por função, com dono e contrato identificados, **é literalmente a semana 1 do assessment** — e, desde 5 de novembro de 2026, é um entregável nomeado dela: o **registo de uso de IA**, entregue à sexta-feira da primeira semana. A obrigação legal força a conversa que a Bluewright já quer ter, com a pessoa com quem já quer falar.

E há um segundo encaixe, ainda melhor. O Art. 4 é uma obrigação de **formar pessoas para usarem IA corretamente**. É a camada de Capacitação, com uma obrigação legal a criar-lhe procura. Trinta anos de docência e o Título de Especialista não têm equivalente em nenhum dos quatro grupos concorrentes mapeados em `market-analysis.md` §4. **É o melhor encaixe produto-mercado de todo o reposicionamento.**

> A conformidade é a razão para abrir a porta. A adoção é o que se vende lá dentro. Nunca ao contrário.

---

## 4. A oferta — o que foi decidido

### 4.1 O que NÃO fazer (mantém-se)

Uma "Auditoria de Conformidade com o AI Act". Compete com advogados, entrega um documento, morre quando a checklist comoditizar, e transforma a Bluewright num fornecedor de conformidade. O próprio nome do produto — *AI Act Readiness Assessment* — é o termo mais saturado do mercado. Usá-lo é aceitar ser comparado com toda a gente.

### 4.2 Sem camada 0 — o inventário vive dentro do assessment

A proposta de julho era uma **AI Use Review** de uma semana a 2.500€, com crédito integral no assessment. Foi recusada a 5 de novembro de 2026 (`ops/decisions.md` #16) por três razões:

1. **Repete o padrão de subpreço.** Uma quarta tabela de preços, a mais baixa, ensina ao mercado que a Bluewright se compra por 2.500€. Abaixo de 2.000€ deixa de ser um produto sénior e passa a ser um favor; a 2.500€ está a um passo disso.
2. **É, por definição, a semana 1 do assessment.** Vendê-la à parte era vender duas vezes a mesma semana.
3. **A janela do Art. 50 fechou.** O argumento «daqui a dois dias» que justificava um produto de entrada rápido deixou de existir em agosto.

O que fica da ideia, e é o que valia: o **registo de uso de IA** é agora entregável nomeado da semana 1 do *Commercial Engine Assessment* — toda a IA em uso, comprada, embebida ou não autorizada, por função, dono e contrato, com a obrigação que cada caso aciona (Art. 5, Art. 50, Art. 4, alto risco em 2027–2028) ou nenhuma. Dizer ao cliente que 80% da lista não exige nada continua a ser a coisa mais credível que se pode fazer numa primeira semana. O parecer jurídico fica com os advogados do cliente; o inventário é dele.

### 4.3 Capacitação — **AI Literacy Programme (Art. 4)** — ADOTADO

Vendável isoladamente e o item de maior margem da carteira. One-pager em `offers/ai-literacy-programme.md`.

- Sessão executiva para a gestão: o que a lei exige, o que a empresa está mesmo a usar (o registo, se existir), o que decidir.
- Sessões por equipa, adaptadas à função — quem usa IA em vendas não precisa do mesmo que quem a usa em operações.
- **Registo do que foi entregue, a quem, quando e com que conteúdo.** Este ponto é o produto: sendo o Art. 4 uma obrigação de meios, a prova das medidas tomadas *é* a conformidade. É o que a empresa mostra à autoridade.
- Repetível anualmente. Não consome dias de consultoria sénior na mesma proporção.

**Preço: por decidir (Alexandre).** Por sessão e por programa, nunca por participante — cobrar à cabeça converte formação em mercadoria e convida à comparação com plataformas de e-learning a 30€ por pessoa. É a única decisão que bloqueia o PDF.

### 4.4 Como as peças encaixam

```
Commercial Engine Assessment (4 semanas, 12.000€)
   semana 1 ──▶ registo de uso de IA (entregável)
        └─ crédito 50% ──▶ Transformação (camada 2)
                                  └──▶ Advise (camada 3)

AI Literacy Programme (Art. 4) ──▶ em qualquer ponto: antes, durante ou depois do assessment;
                                   sozinho, quando a empresa só precisa de cumprir e formar.
```

O programa de literacia não canibaliza o assessment: quem o compra sozinho tinha uma obrigação legal e não um problema de negócio; quem tem o problema de negócio chega ao assessment com o registo já feito ou pede os dois.

## 5. Regras de honestidade — inegociáveis

Estas não são cautelas de estilo. Quebrar qualquer uma delas destrói mais valor do que a oferta inteira gera.

1. **Nunca dizer "tornamo-lo conforme".** O que se produz é o inventário e o mapa do que se aplica. O parecer jurídico fica com os advogados do cliente. A Bluewright não é uma sociedade de advogados — e dizê-lo em voz alta é um diferenciador face a quem deixa a fronteira por esclarecer.
2. **Nunca usar o prazo de alto risco como urgência.** Foi adiado, publicamente, para dezembro de 2027. Quem o invocar em agosto de 2026 é apanhado.
3. **Nunca inflacionar as coimas.** Os 35 M€ / 7% aplicam-se a práticas proibidas. Não é o que acontece a quem se esqueceu de identificar um chatbot.
4. **Nunca vender a review como fim.** É uma porta. Se o cliente só precisar da review, entrega-se a review e vai-se embora — e diz-se isso à partida.

---

## 6. Momento — revisto em novembro

A janela do Art. 50 fechou em agosto de 2026; o artigo «o prazo que se moveu e os dois que não se moveram» perdeu a atualidade. O que não perdeu, e ganhou, foi o Art. 4: uma obrigação de formação em vigor há vinte e um meses, aplicável a todo o deployer, que quase ninguém cumpriu e que nenhuma data futura desculpa.

E o artigo da tese e o artigo do AI Act continuam a ser o mesmo artigo. A tese diz que a tecnologia não transforma nada sem processo e sem pessoas. O AI Act, na prática, obriga as empresas a fazer exatamente duas coisas: **saber o que estão a usar** (processo) e **preparar quem o usa** (pessoas). A lei europeia tornou obrigatório aquilo que a Bluewright já dizia ser o que faltava.

Ângulos para o artigo de lançamento, por ordem de força em novembro de 2026:
1. *A obrigação que está em vigor há vinte e um meses e quase ninguém cumpriu.* Art. 4. Leva ao AI Literacy Programme sem o mencionar.
2. *Ninguém sabe que IA tem dentro de casa.* O argumento do inventário, que leva ao registo de uso de IA da semana 1.
3. *O que o adiamento do alto risco não adiou.* Útil como terceiro parágrafo, não como título.

## 7. Decisões

- [x] Camada 0: **não avança** (5 nov 2026, `ops/decisions.md` #16). `strategy/positioning.md` §4 atualizado.
- [x] Inventário de IA: **entregável nomeado da semana 1** do assessment, «registo de uso de IA» / *AI use register*.
- [x] AI Literacy Programme: **adotado** como produto de Capacitação. One-pager em `offers/ai-literacy-programme.md`.
- [ ] **Preço e formato do AI Literacy Programme** — Alexandre, a frio. Bloqueia o PDF.
- [ ] Confirmar o estado da Lei Orgânica espanhola e o arranque efetivo da supervisão nacional (ANACOM, AESIA). **[VERIFICAR]** antes de qualquer sessão de câmara ou artigo.
- [ ] Decidir se o one-pager do programa se produz antes ou depois do artigo de lançamento.

## Fontes

Gibson Dunn — [EU AI Act Omnibus Agreement: postponed high-risk deadlines](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/) · Sidley — [EU lawmakers reach provisional agreement to delay key AI Act obligations](https://datamatters.sidley.com/2026/06/22/eu-lawmakers-reach-provisional-agreement-to-delay-key-eu-ai-act-obligations/) · Freshfields — [The final Digital Omnibus on AI](https://www.freshfields.com/en/our-thinking/blogs/technology-quotient/eu-ai-act-unpacked-34-the-final-digital-omnibus-on-ai-key-amendments-to-the-a-102nber) · [Article 50 transparency: the deadline that was not postponed](https://www.aiactblog.nl/en/posts/article-50-transparency-deadline-2-august-2026) · [Artigo 4.º — Literacia em IA](https://artificialintelligenceact.eu/article/4/) · Latham & Watkins — [Mandatory training and prohibited practices](https://www.lw.com/en/insights/upcoming-eu-ai-act-obligations-mandatory-training-and-prohibited-practices) · Andersen — [ANACOM assume supervisão em Portugal](https://pt.andersen.com/2025/10/03/ai-act-anacom-assume-supervisao-em-portugal/) · PwC Portugal — [AI Act: o que muda para as empresas em Portugal em 2026](https://www.pwc.pt/pt/sala-imprensa/artigos-opiniao/2026/ai-act-muda-empresas-portugal-2026.html) · Economist & Jurist — [Ley de gobernanza de la IA: deber de inventariar](https://www.economistjurist.es/zbloque-1/ley-de-gobernanza-de-la-ia-el-deber-de-inventariar-y-supervisar-el-uso-de-inteligencia-artificial-recae-sobre-las-empresas-con-sanciones-de-hasta-35-millones-de-euros/) · Groath — [AI governance consulting: where Big-4 frameworks fall short](https://groath.ai/strategy/ai-governance-consulting)
