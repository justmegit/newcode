# Case 4 — Fix the signal before you buy more media
*Validates: Layer 1, the Digital & AI Readiness Assessment · Dimensions: data and systems, commercial engine, processes, people and adoption*
*Status: draft v3, 23 Oct 2026 · anonymized · revised after two red-team passes · every figure traced in `evidence-ledger.csv`*

---

**Context.** A premium outdoor-living installer in Europe, an authorised partner of a European manufacturer. High-ticket projects, months between first contact and signature, and most new contacts arriving through paid search and paid social.

**Problem.** Management asked what the media was actually buying. The ad platforms reported a healthy account. Nobody had checked whether the number the bidding algorithms optimised on was true.

**What we found.**

- **83.5%** of all conversion value the search platform reported came from one CRM import that gave every lead the same default value. Another **16.5%** came from a second import that counted the same deals again, at a later stage. Together, these two imports made up **99.99%** of the reported value. A bidding strategy set to maximise conversion value was optimising mostly on a flat default.
- Of the actions allowed to steer bidding, between **31%** and **47%** had recorded no conversion in the period, depending on the snapshot.
- On the social platform, **3 of 72** campaigns were live. They were split so thin that each ad set produced about **3.6%** of the weekly conversions the algorithm needs to leave its learning phase.
- At one campaign launch, a third-party consent script failed silently. For **20 days** the landing pages sent no lead events to the ad platforms, while **55%** of that campaign's spend went out in the same period.
- Downstream, **81.6%** of paid-social contacts in the half-year had no next step recorded in the CRM; in paid search it was **42.6%**, at a cost per contact **7.6x** higher. **41%** of that search group were requests for product information.

**Strategy.** Make the signal true before touching the budget. Then replace "we need more leads" with "what is a lead worth". With a **5.1%** lead-to-sale rate and marketing at **4.6%** of deal value, we estimated that a lead in the best segment would produce, at gross margin, **more than seven times** what it cost (home-market conversion rate, segment project values). We proposed a cost-per-lead ceiling of **about one fifth** of that margin: a number management could hold us to.

**Execution.** In month one, removed the fixed default value, moved the double-counting import to observation only, and **switched to conversions** as the bidding target on the main search campaign while the value signal was rebuilt. In month two, after the consent failure, self-hosted the consent manager and validated it in production. From then on, every launch started with synthetic test leads sent through each path, checked in the ad platform and not only in the CRM.

**Process installed.** One conversion map with a single target primary action. A test-lead check before every launch. A monthly reconciliation of ad platform, CRM and signed deals, so the next corrupted signal is found in weeks, not quarters.

**Result.** In the month the fixes went in, media ran at **99.5%** of plan, and **79%** of new contacts came from paid channels. By the time of writing, **7.9%** of that month's contacts had reached a quote or a later stage. One signed offer from a paid-sourced contact, created **after the consent fix**, was worth **3.8x** that month's media, in offer value: one deal, not a trend. When the client later cut media to **about a third**, daily contact volume fell only to **80%** of the previous month's pace over the first three weeks. That is early, and part of it is the tail of earlier spend.

**What did not work.** The follow-up gap was diagnosed but sat with the sales organisation and was never redesigned. A bulk email send had **59.9%** of its messages rejected because the sending domain had never been authenticated: a DNS fix, not a budget question.

---

**Three questions to ask your team tomorrow**
1. What share of the conversion value your ad platforms report comes from a default value?
2. For every paid contact last quarter, who owned the next step, and how many days did it take?
3. When did someone last submit a test lead and check that it reached the ad platform?

---

### LinkedIn version (~150 words)

A client asked what their media was actually buying.

The ad platforms said the account was healthy. Their bidding ran on a value signal that came 99.99% from two CRM imports: one gave every lead the same default value, the other counted the same deals again at a later stage. The algorithm was optimising mostly on a flat default.

Further down, 81.6% of paid-social contacts had no next step recorded in the CRM.

We fixed the signal before touching the budget, then reframed the question: not "how many leads?" but "what is a lead worth?" In the best segment, we estimated a lead would produce more than seven times its cost in margin. That turns a complaint into a decision.

Before you buy more media, find out what your platforms are optimising on.

*From problem to process.*
