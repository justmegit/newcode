# A catalogue nobody could update
*Challenge: "Online sales have fallen. Why invest in a channel that is shrinking?"*
*Layer 2, Transform · dimensions: commercial engine, processes, people and adoption · draft v4, 24 Oct 2026 · anonymized · figures in `evidence-ledger-case06.csv`*

---

**Context.** A training provider serving a manufacturer's channel partners. Part of the programme is recurring certification; around it sits a catalogue of sales, service and management courses, sold through the academy's own online shop.

**The challenge.** Online revenue had fallen **60%** in a year. Procurement asked the obvious question, and the client had paid for a rebuild before that had not changed the outcome.

**What was underneath.** The team's own reading was that demand had not disappeared; the catalogue had gone quiet. Publishing a new course date meant fighting tools that no longer fitted together, on an editor its maker had abandoned. Each new date needed a developer, so fewer dates were published. A catalogue the team cannot update is a catalogue customers never see.

**The decision.** Treat the shop as a symptom. The question was not what the new site should look like, but what the academy needs to publish the next course, and the one after it, without calling anyone. Two things followed. The platform was built around the team's own work: one place to create a course edition, with seats managed like stock. And the integration with the group's finance system stayed out of scope, in writing, because that is where projects of this kind stall.

**Process, and who runs it.** Course dates are published by the business team. Fixes reach production through a versioned release that can be rolled back in minutes. Backups run daily to a second provider. The operations manual is written for the people who run the academy, not for developers. The client's business owner and IT department validated the platform against a closed list of functions agreed in the contract.

**Result.** Six days before the cutover, the old shop broke on a new course. Once fixed, that one course sold out in **under 48 hours**: the plainest argument for the change. The earlier rebuild had changed how the shop looked; this one changed who can publish. The cutover ran overnight, with **zero** orders lost. The commercial result will be measured against a baseline agreed with the client, not against a year the old shop had already started to recover on its own. [FILL at 90 days: share of course editions published by the team without support; online revenue against the agreed baseline.]

**What was harder than planned.** Third parties set part of the calendar. Go-live slipped **two weeks** while we waited for a partner's feedback that did not come in time. Launching without it was right; the plan should have set a written deadline for outside input from the start.

---

**Three questions to ask your team tomorrow**
1. If the person who updates your catalogue left today, how long before customers stopped seeing new dates?
2. Which routine change on your website still needs a developer?
3. When a channel shrinks, have you checked whether demand fell or your ability to supply it did?
