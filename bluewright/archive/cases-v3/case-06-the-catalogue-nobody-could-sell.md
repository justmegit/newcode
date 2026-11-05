# Case 6 — The catalogue nobody could sell
*Validates: Layer 2, Transform (strategy plus implementation in short cycles) · Dimensions: commercial engine, data and systems, processes, people and adoption*
*Status: draft v2, 24 Oct 2026 · client named (ISQ, public), partner brand anonymised · revised after one red-team pass · every figure traced in `evidence-ledger-case06.csv` · client approval of the text pending*

---

**Context.** ISQ Academy, the training arm of a Portuguese engineering and certification group, runs an academy for the reseller and installer network of a gas distribution brand. Part of the programme is recurring: installers must refresh their technical certifications to keep working. Around it sits a catalogue of sales, service and management courses. The academy sells through its own online shop.

**Problem.** Online revenue had fallen **60%** in a year. The procurement question was blunt: why invest in a channel that is shrinking? The client had paid for a rebuild before, and wanted to know why this one would be different.

**What we found.**

- The team's own reading was that demand had not gone away; the catalogue had gone quiet. Publishing a course date meant working through plugins that no longer fitted together, on an editor its maker had abandoned. A catalogue the team cannot update is a catalogue customers never see.
- The old site ran **47** active plugins and could not move to a current software version because two of them would not run on it.
- The data that should have been an asset was leaking. **4.5%** of past orders carried a buyer tax number that failed the checksum, so the error surfaced at invoicing. Behind **15%** of historical enrolments, the course could no longer be identified, because past events had been deleted to tidy the calendar.
- Cross-selling existed, but by hand and now and then: someone remembered a customer, or built a spreadsheet for a campaign. Nobody could answer, on demand, "who trained here, what did they not take, and whose certification is due?"

**Strategy.** Treat the shop as a symptom. The question was not "what should the new site look like" but "what does the academy need to sell the next course, and the one after it, without calling a developer". Three decisions followed. First, build before selling: the platform was demonstrable on the client's own catalogue before anyone signed, so the client bought a delivery, not a promise. Second, accept every protection the client asked for and write it ourselves: full code ownership, portability to any provider, a **30/40/30** payment schedule tied to validation, and a **9 months** warranty. Third, keep the integration with the group's finance system out of scope, in writing: that is where projects of this kind stall.

**Execution.**

- A training-management layer on the shop the team already knew: one "Training" menu, dated editions where seats are stock, and a form per trainee validated on the server, so a wrong tax number is stopped at the form, not found at the invoice.
- The enrolment history rebuilt into a trainee base, and an Opportunities Radar on top of it, recalculated from every new sale: lapsed certifications, next-level courses never taken, people who only ever took technical courses, and companies whose staff fall short of the 40 hours of annual training the Labour Code sets, counting only hours done at the academy.
- A catalogue by profession as well as by subject, at the partner brand's request: "what does my counter staff need?" is how a reseller thinks.
- Validation by the client's business owner and IT department, against a closed list of functions agreed in the contract.

**The week it went live.** Six days before the cutover, the old shop broke: a new course had been set up with a ticket type tied to a payment module that was switched off. We fixed it on the old platform within a day, and the course sold out its **23 seats** in **under 48 hours**. It was the plainest argument for the migration: the catalogue sells when the machinery works. The cutover itself took **about 70 minutes** of maintenance, overnight, with **zero** orders lost and a real payment confirmed end to end before morning.

**Process installed.** Course dates published by the business team. Trainee data checked when it is typed. Releases from a versioned repository with an update screen, so a fix reaches production in minutes and can be rolled back. Daily encrypted backups to a second provider. An operations manual written for the people who run the academy, not for developers.

**Result.** The twist is not the shop. Cross-selling used to depend on someone's memory and a spreadsheet. It is now a standing list in the back office, refreshed by every sale, with name, company, course to propose and list price. In its first week, the renewal list held only one kind of case: in **100%** of them, the certification had already lapsed. That is the most urgent call and the most expensive one to miss, because a lapsed certification usually means repeating the longer initial course. The commercial result will be measured against a baseline agreed with the client, not against a year that the old shop had already started to recover on its own.

**What did not work.**

- Go-live slipped **two weeks** while the business side waited for the partner brand's feedback, which did not arrive in time. Launching without it was right; the plan should have had a written deadline for third-party input.
- On launch day, the client's mail server rejected the platform's notification e-mails because of a technical sender address. The client found it, not us. Fixed **the same day**, but the test plan had only checked delivery to one outside mailbox.
- The history migration needed a second pass. In the first days, past editions and their trainees were not visible in the back office, and the Radar showed no renewals, because the archived history had not yet been linked to the new editions. Linking it fixed both. One side effect of our own automation: **35** old unpaid orders were marked as expired, a decision we had left to the client. Reverted the next day, with no customer contacted.

---

**Three questions to ask your team tomorrow**
1. If the person who updates your catalogue left today, how long before customers stopped seeing new dates?
2. Which of your customers have a certification, licence or contract expiring this quarter, and who is calling them?
3. When a customer types a wrong tax number, where do you find out: at the form, or at the invoice?

---

### LinkedIn version (~150 words)

A training academy's online sales had fallen 60% in a year.

The obvious answer was a new website. The real problem was that nobody could publish a course date without fighting the tools, and the catalogue went quiet.

We rebuilt the machinery behind the shop. Then we turned years of messy enrolment history into something the team never had: a standing list of who to call. Lapsed certifications, next-level courses never taken, people who only ever did technical training. Cross-selling used to depend on someone's memory and a spreadsheet. Now every sale updates the list.

Six days before go-live, the old shop broke on a new course. Once fixed, the course sold out in under 48 hours.

The catalogue sells when the machinery works. The next sale is already in the data.

*From problem to process.*
