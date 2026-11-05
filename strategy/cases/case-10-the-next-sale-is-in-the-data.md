# The next sale is already in your data
*Challenge: "Who should we be calling, and aren't?"*
*Layer 2, Transform · dimensions: data and systems, commercial engine · draft v4, 24 Oct 2026 · anonymized · figures in `evidence-ledger-case06.csv`*

---

**Context.** A training provider serving a manufacturer's channel partners. Installers must renew technical certifications to keep working, and the academy also sells sales, service and management courses.

**The challenge.** Cross-selling existed, but by memory: someone remembered a customer, or built a spreadsheet for a campaign. Nobody could answer, on demand, who had trained here, what they had not taken, and whose certification was due.

**What was underneath.** Years of enrolment history that should have been the academy's best asset were leaking.

- **4.5%** of past orders carried a buyer tax number that failed validation. The error was found at invoicing, weeks after the sale.
- Behind **15%** of historical enrolments the course could no longer be identified, because past events had been deleted to tidy the calendar.

The data could not be trusted, so nobody used it, so nobody noticed it getting worse.

**The decision.** Fix the data where it enters, rebuild the history once, and turn it into a list of people to call. Trainee details are now validated as they are typed, so a wrong tax number stops at the form, not at the invoice. The enrolment history was rebuilt into a trainee base, and a standing list of opportunities sits on top of it: lapsed certifications, next-level courses never taken, people who have only ever taken technical courses.

**Process, and who runs it.** The list is recalculated from every new sale and lives in the back office, with name, company, the course to propose and its list price. Nobody needs to build a spreadsheet first. Until now, nobody worked it on a regular basis: calling customers was occasional, and had not been tried recently. From here on, the academy's project manager owns the list and works it with the channel contact at the manufacturer.

**Result.** In its first week, all **30** renewal opportunities on the list had one thing in common: the certification had already lapsed. That is the measure of what the old way missed: every renewal had lapsed before anyone called. It is also the most urgent call and the most expensive to miss, because a lapsed certification usually means repeating the longer initial course. [FILL at 90 days: enrolments that came from contacts on the list, as a share of all enrolments.]

**What was harder than planned.** Making history usable took two passes, not one: for the first days the list was empty, until the archived records were linked to the new course editions. And early on, our automation acted on old orders where the decision belonged to the client. It was reverted the next day, with no customer affected, and the platform now prevents it from happening again.

---

**Three questions to ask your team tomorrow**
1. Which of your customers have a certification, licence or contract expiring this quarter, and who is calling them?
2. When a customer types a wrong tax number, where do you find out: at the form, or at the invoice?
3. If you wanted a list of who to call tomorrow, would someone have to build a spreadsheet first?
