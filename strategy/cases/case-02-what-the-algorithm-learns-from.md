# Check what the algorithm learns from
*Challenge: "The platforms say the account is healthy. I don't know what the media is buying."*
*Layer 1, Assess · dimensions: data and systems, processes · draft v4, 24 Oct 2026 · anonymized · figures in `evidence-ledger.csv`*

---

**Context.** A specialist installer of high-ticket home products, working within a manufacturer's network. Months between first contact and signature, and most new contacts arriving through paid search and paid social.

**The challenge.** Management asked what the media was buying. The ad platforms reported a healthy account. Nobody had checked whether the number the bidding algorithms were learning from was true.

**What was underneath.** The algorithms were learning from a signal that was mostly invented, partly missing and too thin to learn from.

- **Invented.** **83.5%** of the conversion value the search platform reported came from one CRM import that gave every lead the same default value. Another **16.5%** came from a second import that counted the same deals again at a later stage. Together: **99.99%**. A bidding strategy set to maximise value was maximising a default.
- **Missing.** At one campaign launch, a third-party consent script failed silently. For **20 days** the landing pages sent no lead events to the platforms, while **55%** of that campaign's spend went out.
- **Too thin.** Between **31%** and **47%** of the actions allowed to steer bidding had recorded nothing in the period. On the social platform, **3 of 72** campaigns were live, split so finely that each ad set got about **3.6%** of the weekly conversions an algorithm needs to stop guessing.

**The decision.** Make the signal true before touching the budget. Removed the default value, moved the double-counting import to observation only, and switched the main search campaign to bid on conversions while a real value signal was rebuilt. Hosted the consent manager ourselves, so a third party could not switch the measurement off again.

**Process, and who runs it.** One conversion map with a single primary action per platform. Before every launch, a test lead sent through each path and checked in the ad platform, not only in the CRM. Once a month, ad platform, CRM and signed deals reconciled side by side, so the next corrupted signal shows up in weeks, not quarters. We ran the checks ourselves.

**Result.** Within the first month, the platforms were bidding on real contacts instead of a default value, and no launch went out without a test lead through each path. The question management had asked could finally be answered from the CRM rather than from the platforms' own reports. What the media is worth is a separate question, and a separate decision.

**What did not work.** We found the consent failure on day 20. A test lead at launch would have found it on day one; that check did not exist yet. It exists now because of those 20 days. The other gap is ownership. The monthly reconciliation stayed with us and the handover to the client never happened. A process only the consultant runs is not yet installed.

---

**Three questions to ask your team tomorrow**
1. What share of the conversion value your ad platforms report comes from a default value?
2. Which of the actions steering your bids recorded nothing last month?
3. When did someone last submit a test lead and check that it reached the ad platform?
