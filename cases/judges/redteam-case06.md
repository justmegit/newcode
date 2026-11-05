# Red-team memo: case 06, "The catalogue nobody could sell"

Reviewed from the case, ledger (L = row A##), judge, brand book §6 and CLAUDE.md only. Judge run `python -I check_case06.py`: PASS. Banned-word scan: none (near miss: "end to end", line 27).

## Verdict

**Not publishable as is.** Result is [FILL], the core diagnosis has no row, the Radar figure contradicts the case's own failure list, and the ledger shows 2026 revenue already recovering before launch.
**Publishable after fixes: yes**, once the 90-day result is in, items B1-B6 are fixed, and ISQ (and the partner brand) approve the text in writing.

## Findings

| ID | Sev | Location (quote) | Problem | Fix |
|---|---|---|---|---|
| B1 | blocker | Result, "[FILL — measure at 90 days" | No outcome. The case's own status line says not publishable. What remains are potential and anecdote. | Hold until 22 Jan 2027. Report realised enrolments and euros, not Radar value. |
| B2 | blocker | What we found, "Demand had not gone away. The mandatory refreshes kept selling." | The causal spine (mandatory held up, optional collapsed, because nobody could publish) has no ledger row. There is no split of revenue by course type and no count of dates published per period. Alternative causes are not excluded: co-funding changes, sales moving to direct invoicing, the group site cannibalising sales. | Add rows: revenue or enrolments by mandatory vs optional, 2024/2025/2026; editions published per quarter. Without them, write: "Our reading: the optional catalogue stopped being updated." |
| B3 | blocker | Result, "on the day of launch, the Radar listed renewals" | Contradicts What did not work: "the Radar's renewal lists were empty in production". L13/L14 are dated 24 Oct, two days after launch (22 Oct). | "Two days after launch, once the course pairings were fixed, the Radar listed..." |
| B4 | blocker | Problem, "first half of the next year was down another 57%" | Selective period. Ledger: 2026 to 21 Oct = 7,023 vs full 2025 = 5,799 (+21%), before the new site went live. 21 Jul-21 Oct alone = 5,021. The decline had already reversed on the old platform. A CFO who sees the ledger reads this as concealment. It also inflates any 90-day comparison with Q4 2025. | State both: "down 57% to July; by October, with course dates back, 2026 had already passed 2025." Measure the 90 days against a pre-launch 2026 run-rate as well as Q4 2025; exclude the 19-21 Oct course; state the VAT and co-funding basis. |
| B5 | blocker | Result, "worth **95%** of the project fee" (and LinkedIn "was worth") | Potential dressed as value: list price at reseller rates, gross, not margin, no conversion rate, partner co-funding share not deducted. The renewals are all lapsed contacts (L13, 100%). After 5+ years many will have left the trade. If mandatory refreshes "kept selling" (B2), renewals are what would have happened anyway. This would not survive a board. | "Two days after launch, the Radar listed 30 lapsed certifications and a set of progression candidates; at list price they came to 95% of the fee. The 90-day figure shows how much converted." Remove "worth" everywhere. |
| B6 | blocker | Problem, "paid for a previous rebuild"; Strategy, "an earlier project with this client had failed"; WDNW, "The old shared server" | Three earlier failures with no owner named. The ledger shows operational access to the old production DB and the old server ("giga3"). A journalist will ask whether the firm ran that server or did the earlier rebuild. If yes, the case hides its own track record. If no, it criticises another supplier. | Say who owned each in one neutral line, or cut. If any was ours: "We had hosted the previous site since 20XX; this is what we changed." |
| M1 | major | Context + throughout: ISQ named | The named client is shown with a 60% fall, a paid-for failed rebuild, wrong invoices (a tax issue), deleted records, an unpatched server, a mail server that rejects mail, and a weak main site. A target GM asks: "Would I want to be case 7?" | Written ISQ approval of the final text, or anonymise ("a Portuguese engineering group's training arm"). |
| M2 | major | Context, "a gas distribution brand" | Thin anonymisation. ISQ plus "gas distribution brand" plus "reseller and installer network" identifies the partner in one search. The partner is then blamed ("It never came in time") and its resellers called under-trained (31). | Partner sign-off, or drop the partner blame and the reseller finding from the public version. |
| M3 | major | Week it went live, "about a third of the whole year's online revenue" | Scale leak despite "ratios only": 4 orders = 1/3 of YTD reveals a channel of roughly a dozen orders a year. With the ledger absolutes, the fee (7,000) exceeds 2025 online revenue (5,799, x1.21). A CFO will ask why spend more than the channel's annual revenue. | Drop "about a third"; use "sold out its 23 seats in under 48 hours." Prepare the conversation answer: the value is the trainee base and renewals, not the shop. |
| M4 | major | Week it went live, "the clearest argument for the migration" | Non sequitur: the course sold on the old platform after a one-day fix. It proves the fix, not the migration. One course, chosen after the fact, sold to capped capacity (selection bias). | "The demand was there; the machinery was the bottleneck. One setting fixed one course. Keeping the catalogue running every week was the reason for the migration." |
| M5 | major | Execution, "short of the 40 hours of annual training" | Period and scope mismatch. L15 uses a 24-month window and counts only hours done at the academy. Art. 131 is per year and allows training anywhere. Execution and LinkedIn drop the qualifier, which implies 31 identifiable companies break the law. | Execution: "with fewer hours at the academy than the 40-hour annual minimum." Align the window (12 months) or say "over 24 months". |
| M6 | major | Process installed, "An operations manual the team uses instead of calling us" | Adoption claimed two days after launch, with no row. The same goes for "published by the business team" (the 90-day plan measures exactly this), "a fix reaches production in minutes" and "Daily encrypted backups". This is the firm's thesis (adopted technology), so it must be proven, not asserted. | "Designed so that..." until 90-day data exist. Add rows: dates published by the team, support requests, backup job logs. |
| M7 | major | WDNW, "could not be patched against a critical security flaw" | Publicly flags an unpatched shared server the day after a published flaw. If it still hosts other sites, this is a disclosure risk and a quotable line against the firm. "It happened only because the migration was already ready" presents luck as foresight. | Cut, or publish only after the server is retired: "The old server had reached end of support; the migration removed that exposure." |
| M8 | major | Strategy, "demonstrable with the client's real courses and history before anyone signed" | Implies client personal data (trainee history) was processed before a contract or DPA, which is a GDPR question. It also tells prospects the firm works on spec, against the commercial discipline in CLAUDE.md. | Confirm an NDA/DPA covered it and say so, or use "with the client's real catalogue" and cut "before anyone signed". |
| M9 | major | Strategy, "accept every protection the client asked for" | Discloses a named client's contract terms (L17/L18, signed addendum). It also sets 30/40/30 and a 9-month warranty as public precedent. "Every" reads as a vendor that concedes. | Client consent; reword: "Code ownership, portability, payment tied to validation and a warranty, all in the contract." |
| M10 | major | What we found, "4.5% of past orders ... so invoices went out wrong" | Wrong denominator: L05 is 7 of 156 orders *with a tax number*. n=7, medium confidence, source "project memory". "Invoices went out wrong" has no row, and it implies the named client issued non-compliant invoices. | "7 of the 156 past orders with a tax number (4.5%) had one that fails the checksum." Cut "so invoices went out wrong" unless a row shows corrected invoices. |
| M11 | major | What we found, "deleted to tidy the calendar" | Motive is unverifiable and blames the client's staff. | "because the events had been deleted in the old system." |
| M12 | major | What we found, "9 of 19 good practices" | Medium-confidence own benchmark (L16), used publicly against the named client's main site: a relationship risk. "The small academy was the right place to prove" is adjective-led. | Cut from the public version, or "by our benchmark, ISQ's main site lacked 9 of 19 practices", with ISQ approval. |
| m1 | minor | Result, "the most urgent and the most expensive call" | Spin. 100% lapsed on n=30 may be an artefact of the list definition (window 3 months, all already expired). "Most expensive" is undefined. | "In all 30 renewal cases the certification had already lapsed." |
| m2 | minor | Result, "None of that was visible a month earlier" | Unverifiable. The data existed and could be queried. | "Nobody had put it on one list before." |
| m3 | minor | Week it went live, "**three days**" | L10: 19 Oct 13:36 to 21 Oct 09:50 is about 44 hours. "Within a day" (the fix) and "Six days" have no row (the judge whitelists "Six days" without one). | "in under 48 hours". Add the incident and fix dates to the ledger. |
| m4 | minor | Week it went live, "**zero** orders lost" | Trivially true: no orders between 21 Oct 09:50 and the cutover (L12). "A real payment confirmed end to end" has no row. | Keep, but add a row for the test payment; drop "end to end" (near the banned phrase). |
| m5 | minor | WDNW, "The decision to launch was right" | Self-justification. | Cut; keep "the plan should have had a written deadline for third-party input". |
| m6 | minor | WDNW, four bullets, six defects | Six launch defects in one list reads as sloppy to a GM. The 35 expired orders and the empty Radar share a lesson. | Group under three lessons: third-party deadline, test plan, migration checks in production. |
| m7 | minor | Context, "ISQ Academy ... runs a training academy" | "An academy runs an academy". The "group's main training site" (academy.isq.pt per L16) reads as the same entity. | "ISQ's training arm runs a branded academy for..." |
| m8 | minor | What we found, "two of them would not run"; "three plugins"; "abandoned" | Number words without rows (the judge only checks digits). L04 "five" is unused. | Add rows or cut. Use the backed contrast "47 active plugins, now five". |
| m9 | minor | Problem, "The procurement question was blunt" | The question is posed but never answered with a number. | Answer it in Result once B4 data are shown. |
| m10 | minor | Three questions, Q3 | Narrow (tax numbers) for a subsidiary GM. | "When a customer record is wrong, where do you find out: when it is typed, or when it is invoiced?" |
| m11 | minor | End of case | No next step for a reader whose goal is to book a call. | One line after the questions: "If question 2 has no owner, that is where a four-week assessment starts." |
| L1 | major | LinkedIn, "that list was worth 95% of the project fee" | Same as B5, and dated to launch day (B3). | "Two days after launch that list, at list price, came to 95% of the fee. In January we'll know how much sold." |
| L2 | major | LinkedIn, "about a third of the year's online revenue" | Drops "to that date", so it reads as a full year. Scale leak (M3). | "it sold out its 23 seats in under 48 hours." |
| L3 | major | LinkedIn, "companies short of their legal training hours" | Drops "at the academy" (M5). Defamation risk for an identifiable network. | "companies whose staff had trained fewer hours with the academy than the legal annual minimum" |
| L4 | minor | LinkedIn, "turned years of messy enrolment history" | "years" has no row; "messy" is an adjective doing evidence's work. | "turned every past enrolment into a list of who to call". |
| L5 | minor | LinkedIn, overall (139 words) | No result yet and no question to the reader. Ends on the tagline only. | Close with Q2 from the case as the hook. |

## What the case does well (keep)

- "What did not work" is concrete and owns errors ("The client found it, not us"; 35 orders reverted, no customer contacted). Rare and credible: trim it, do not remove it.
- "The client bought a delivery, not a promise" and the written scope exclusion of the finance integration show judgement, not features.
- The validation against a closed list of functions, by the business owner and by IT, speaks to the target reader's procurement reality.
- Q1 and Q2 are the best lines in the piece. Q2 would make a subsidiary GM pick up the phone.
- "Stopped at the door, not found at invoicing" is a clean before/after.
- Ledger discipline: every bold figure traces to a row, and the judge passes.

## Ratios recomputed (from ledger numerators/denominators)

| Row | Computation | Result | Display | Status |
|---|---|---|---|---|
| A01 | 1 - 5,799.45/14,633.93 | 60.4% fall | 60% | OK (VAT basis unstated) |
| A02 | 1 - 2,001.83/4,692.45 | 57.3% fall | 57% | OK. Text says "first half"; the period is 1 Jan-20 Jul |
| A05 | 7/156 | 4.49% | 4.5% | OK. Text denominator wrong (orders with a tax number, not all orders) |
| A06 | 67/448 | 14.96% | 15% | OK |
| A09 | 2,263.20/7,023.31 | 32.2% | about a third | OK. Share of 21 Jul-21 Oct revenue: 45.1% |
| A10 | 19 Oct 13:36 to 21 Oct 09:50 | about 44 h | three days | Overstated in kind; "under 48 hours" is accurate and stronger |
| A13 | 30/30 | 100% | 100% | OK, n=30 |
| A14 | 6,655/7,000 | 95.1% | 95% | Arithmetic OK. Gross list potential, dated two days after launch |
| A15 | 31 | 31 | 31 | 24-month window vs "annual" in the text |
| A16 | 9/19 (4+5+9+1=19) | 47.4% | 9 of 19 | OK, medium confidence |
| A19 | 04:20 to ~19:50 | about 15.5 h | the same day | OK |
| Derived | 7,023.31 (2026 to 21 Oct) / 5,799.45 (2025) | 1.21 | not in text | 2026 already above 2025 before launch (B4) |
| Derived | 7,000 fee / 5,799.45 | 1.21 | not in text | Fee exceeds 2025 online revenue (M3) |
| Derived | 2,263.20 / 23 seats | about EUR 98/seat | not in text | Inferable if absolutes leak |

Ledger notes: A08 sets numerator 24 lines (1 unpaid) against denominator 23 capacity, so "computed 1.04" is meaningless. Restate it as 23 paid / 23 capacity = sold out. Weak rows carrying public weight: A05 (medium, "project memory"), A11, A16, A19 (medium). A01, A02, A08, A09 and A10 are operational-access data from the client's production DB. A06, A13, A14 and A15 are marked own-work but are computed from the client's personal data. The client owns all of these; get consent to publish even the ratios. The judge checks digits only, so number words ("two of them", "within a day", "a month earlier") pass unbacked.
