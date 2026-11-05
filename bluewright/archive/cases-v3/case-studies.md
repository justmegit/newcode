# Bluewright — Case Studies (working drafts v1)

Structure for every case: **Context → Problem → Strategy → Execution → Process installed → Result.**
Client names anonymized by default — replace with real names only with written permission.
`[FILL]` = needs your numbers/details. Notes to you in PT at the end of each case.

---

## Case 1 — Market entry: building a prescriber engine in Spain
*Validates: Layer 2 (strategy + execution) · Thesis: strategy that lands as a programme, not a report*

**Context.** A Belgian building-products manufacturer, part of a European industrial group, with an established catalogue but limited traction in Spain — a market where the buying decision runs through prescribers (architects, installers, distributors) rather than end customers.

**Problem.** No local digital presence to speak of, no systematic way of reaching or nurturing the trade audience, and a head office that needed to decide how much to invest in Spain — without a framework for what different levels of investment would actually buy.

**Strategy.** A full digital B2B prescriber strategy for the Spanish market, centred on a trade-loyalty programme ("Club Pro") designed to give prescribers concrete reasons to specify the brand — content, tools, incentives — rather than generic brand advertising. Deliberately scenario-based: two complete investment scenarios (€15k and €30k media), each with channels, expected outcomes and fee structure, so the board could take a real decision instead of approving a vague budget.

**Execution.** [FILL — what has been / is being implemented: campaigns launched, programme built, materials produced, timeline.]

**Process installed.** [FILL — what now runs without you or with your supervision: nurturing flows, reporting cadence, programme operations.]

**Result.** [FILL — prescribers enrolled, leads, specifications won, pipeline value; even early indicators work. If too early, use: "Programme approved by the group board at scenario X; first results expected Q_ 2026."]

> **Notas (PT):** Este é o caso SOGEM. O ponto forte narrativo é o formato de decisão em dois cenários — mostra consultoria de administração, não "fazer campanhas". Se a execução ainda está no início, o case study pode legitimamente terminar em "estratégia aprovada + primeiros indicadores"; atualizas os resultados daqui a uns meses. Confirma com o cliente ou anonimiza como está.

---

## Case 2 — From manual chaos to running processes: the marketing & communications engine
*Validates: the core thesis "from problem to process" · Layer 2 (automation + AI)*

**Context.** The Spanish subsidiary of an international engineering and inspection group — a technical B2B organization where marketing and communications were consuming senior time on repetitive, manual work: monitoring what the market and the press were saying, moving media between teams, keeping the website fed with the company's LinkedIn activity.

**Problem.** Every one of those tasks was done by hand, was nobody's real job, and stopped whenever the person was busy. The information existed; the process didn't.

**Strategy.** Instead of hiring or buying enterprise software, redesign each task as an automated process on infrastructure the client controls — combining workflow automation (n8n, Power Automate) with AI models for the judgment steps (classifying and summarizing content), and delivering everything into the tools the teams already use (Excel/SharePoint, the website, email).

**Execution.** An AI-powered press-clipping pipeline that scrapes LinkedIn, classifies relevant posts and produces weekly summaries per author — delivered into the team's spreadsheets automatically. Media-routing flows that move field content (e.g., WhatsApp uploads) straight into SharePoint. The company's LinkedIn activity republished automatically on the corporate website. [FILL — confirm which are live, add any others.]

**Process installed.** Communications monitoring, media logistics and website freshness now run on schedule, unattended, with the team consuming outputs instead of producing them. [FILL — hours/week saved, response time, coverage.]

**Result.** [FILL — quantify: e.g., "X hours of senior time recovered weekly; press monitoring coverage from ad-hoc to 100% weekly; website updated daily without manual work."]

> **Notas (PT):** Este é o caso ISQ España — o mais "de problema a processo" dos três, e o que prova a tua tese com AI a sério (classificação com Gemini, pipelines n8n). Vale a pena confirmares o que está efetivamente em produção antes de fechar números. Anonimizado fica forte na mesma ("international engineering & inspection group" tem peso).

---

## Case 3 — The long game: a decade as digital counsel
*Validates: Layer 3 (fractional digital advisor / retainer)*

**Context.** [FILL — pick your longest-standing client: sector, size, since when. E.g., "A Portuguese B2B [sector] company, client since 20__."]

**Problem.** Not one problem — a changing sequence of them over [X] years: [FILL — e.g., first a credible digital presence, then lead generation, then CRM discipline, then automation and AI]. What the company consistently lacked was not suppliers, but a senior digital head it could trust without hiring one.

**Strategy.** A continuous advisory relationship: quarterly priorities set with management, execution done or supervised by us, technology and vendor decisions taken with someone at the table whose incentive is the client's outcome — not selling hours or tools.

**Execution.** Over the years: [FILL — 3–5 milestones, each one line: site generations, campaigns, market expansions, systems introduced].

**Process installed.** Digital is no longer a series of projects but a managed function: [FILL — what runs routinely today].

**Result.** [FILL — the strongest proof is the duration itself: "X years, Y engagements, still the first call." Add one or two hard numbers if available: revenue influenced, markets entered, cost avoided.]

> **Notas (PT):** Aqui a decisão é tua: qual é o cliente com mais anos de casa que melhor conta esta história? O argumento de venda deste caso é a própria longevidade — "clientes não ficam 10+ anos com um fornecedor; ficam com um conselheiro". É também o caso que justifica a avença (camada 3) e o teu preço. Se o cliente for a Conceptance ou outro atual, os detalhes do trabalho recente (CRM, dados, sales enablement) entram nos milestones.

---

## Next steps
1. You fill the `[FILL]` blocks with numbers and confirm what's live (rough is fine — I'll polish the copy).
2. Decide per case: anonymized vs. named-with-permission.
3. I then produce the final EN versions formatted for the one-page site + a short LinkedIn-post version of each.

---

## Cases 4–5 and the launch essay (23 Oct 2026)
Drafts in `strategy/cases/` (v3): `case-04-fix-the-signal.md` (validates Layer 1, the Assessment), `case-05-claims-you-can-defend.md`, `essay-ai-built-it.md` (single client, anonymized: publish only after the relationship ends). Evidence in `evidence-ledger.csv`; `check_ledger.py` passes; two red-team passes in `cases/judges/`. Pending: clean-context re-identification test and the 5-reader test.
