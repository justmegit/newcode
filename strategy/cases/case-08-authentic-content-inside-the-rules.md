# Content that stalled in approval
*Challenge: "We pay for two posts a week and publish one."*
*Layer 2, Transform · dimensions: AI readiness, processes, people and adoption · draft v4, 24 Oct 2026 · anonymized · figures in `evidence-ledger-v4.csv` and `evidence-ledger-isq.csv`*

---

**Context.** A company whose deliverable is a formal technical document that its clients rely on for regulatory reasons. Much of its work happens on clients' sites, under confidentiality, and management wanted AI to speed up its content.

**The challenge.** The company had contracted two posts a week and was publishing about half of that. Adding AI to a process that stalled would only produce more drafts waiting for approval, with three new risks: claims the company could not stand behind, images that reveal a client, and an AI process it could not defend under the AI Act.

**What was underneath.** The problem was the decision process, not the writing.

- Each piece was approved one by one, by message, and most stalled: **3 of 8** pieces in one plan were approved, and output ran at **about one a week**.
- An AI-assisted plan, checked against the published service catalogue, proposed **5 of 9** topics that claimed services the company does not sell.
- The real risk with field photos was not consent. It was a photo showing a client's plant, a nameplate or a screen.
- AI was limited to the tools the company had already approved, and client material could not leave its own environment.

**The decision.** Build the process on how the company decides, in layers. Management sets themes every two months, reviews the month's plan, and can edit, reschedule or stop any piece until it goes out. The service catalogue decides what the company may claim, before a topic enters the plan. The team supplies what AI cannot: field photos through a simple form, used only when marked suitable, and expert texts published under the author's name with the body left intact. AI drafts; a model from another vendor critiques; neither may produce a figure, a regulatory reference or a service claim that has not been checked against a source. Images are illustrative, never documentary, and keep the metadata that identifies them as AI-generated, by choice; real photos never pass through AI.

The architecture follows the same logic. Approvals, the calendar and the audit trail live in the company's own office platform. Orchestration is portable. Text and image models both come from the company's approved AI gateway and do the drafting only. If the company changes provider tomorrow, the models change and the process does not.

**Process, and who runs it.** Every piece moves through draft, editorial review by our operator and approval by the country manager; nothing is published without that approval on record. The process is designed for human review and editorial responsibility on every AI-assisted piece, on record.

**Result.** Since the first publication in mid-September, the company has published **two a week**, as contracted, each with its approval on record. None of the five topics outside the catalogue was published.

**What was harder than planned.** Contributions from the field. Technicians were asked to send photos of their work through a simple form, and after **three weeks** none had arrived. This is a change of culture, not of tools, and it is still under way: the aim is a few champions in field operations who make it normal. Until then, generated illustrations keep the content going without putting a client's site at risk.

---

**Three questions to ask your team tomorrow**
1. Who decides what your company may claim, and does that check come before or after the draft?
2. Could you show, piece by piece, who approved what you published with AI assistance?
3. If your AI provider changed tomorrow, would your process change, or only a setting?
