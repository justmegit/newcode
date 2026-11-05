"""Builds the evidence ledger for cases 04, 05 and the essay.
Raw values come from primary sources read between July and 23 Oct 2026 (see `source`).
The script computes every ratio from numerator/denominator so that
check_ledger.py can verify the published figures against them."""
import csv, os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "evidence-ledger.csv")

# id, claim, numerator, denominator, kind, display, source, source_date, confidence, provenance, used_in
R = [
 ("L01", "Share of reported conversion value from one CRM import with a fixed default value", 1570000.00, 1880738.57, "pct1", "83.5%",
  "Google Ads conversions table, account level, 1 Jan-25 Jul 2026 (Mapa_Conversoes_GoogleAds_jul2026.md, row 21)", "2026-07-26", "high", "own-work", "c4"),
 ("L02", "Share of reported conversion value from a second import counting the same deals again", 310476.22, 1880738.57, "pct1", "16.5%",
  "Same table, row 20 (HubSpot - Opportunity, primary). Audit note: later stage of the same deal, each opportunity counted a second time", "2026-07-26", "high", "own-work", "c4"),
 ("L03", "Share of reported conversion value that was a default value or a duplicate", 1880476.22, 1880738.57, "pct2", "99.99%",
  "Rows 20+21 over account total", "2026-07-26", "high", "own-work", "c4"),
 ("L04", "Bid-steering conversion actions that had never recorded a conversion (upper bound)", 7, 15, "pct0", "47%",
  "Conversion map: 7 of 15 primary rows at 0 conversions (47%)", "2026-07-26", "medium", "own-work", "c4"),
 ("L05", "Bid-steering conversion actions that had never recorded a conversion (lower bound)", 4, 13, "pct0", "31%",
  "Conversion diagnosis memo: 4 of 13 primaries at 0 (31%)", "2026-07-26", "medium", "own-work", "c4"),
 ("L06", "Live campaigns on the social ad account", 3, 72, "pct0", "3 of 72",
  "Meta Ads Manager audit, act 24580236, window 28 Jun-27 Jul 2026", "2026-07-28", "medium", "own-work", "c4"),
 ("L07", "Weekly conversions per live ad set vs the 50/week learning threshold", 1.8, 50, "pct1", "3.6%",
  "Same audit: 46 leads/month over 6 ad sets = ~1.8 per ad set per week", "2026-07-28", "medium", "own-work", "c4"),
 ("L08", "Paid-social contacts (H1, home market) with no defined next step", 345, 423, "pct1", "81.6%",
  "CRM filtering annex, project country = home market, contacts created 2026, paid origin", "2026-07-31", "high", "own-work", "c4"),
 ("L09", "Paid-search contacts (H1, home market) with no defined next step", 46, 108, "pct1", "42.6%",
  "Same annex", "2026-07-31", "high", "own-work", "c4"),
 ("L10", "Cost per contact, paid search vs paid social (H1, home market)", 235, 31, "mult1", "7.6x",
  "Same annex: EUR 235 vs EUR 31 per contact", "2026-07-31", "high", "own-work", "c4"),
 ("L11", "Catalogue requests among paid-search contacts with no next step", 19, 46, "pct0", "41%",
  "Same annex", "2026-07-31", "high", "own-work", "c4"),
 ("L12", "Days of zero lead events on landing pages at a campaign launch", 20, 1, "int", "20 days",
  "Landing-page consent CDN returning 503; self-hosted, published and validated in production on 21 Aug", "2026-08-21", "high", "own-work", "c4"),
 ("L13", "Share of that campaign's spend that ran during the blind days", 606.24, 1093.70, "pct0", "55%",
  "Meta campaign spend at day 20 vs campaign spend to 28 Aug (August report)", "2026-08-28", "medium", "own-work", "c4"),
 ("L14", "Lead-to-sale rate, home market, H1", 42, 816, "pct1", "5.1%",
  "Funnel Review H1 2026 v2 (816 leads -> 42 sales)", "2026-07-30", "high", "own-work", "c4"),
 ("L15", "Marketing cost per closed sale as share of average deal value", 1025, 22200, "pct1", "4.6%",
  "Funnel Review H1 2026 v2 (EUR 1,025 per sale vs EUR 22.2k average ticket)", "2026-07-30", "high", "own-work", "c4"),
 ("L16", "Estimated margin per lead vs what a lead cost, best corridor: home-market 5.1% rate x corridor average project x 37.5% gross margin (lower bound)", 760, 100, "gt", "more than seven times",
  "Lead economics memo: 5.1% x corridor average project x 37.5% gross margin vs < EUR 100 per lead", "2026-07-30", "medium", "own-work", "c4"),
 ("L17", "Proposed cost-per-lead ceiling as share of lead margin", 150, 760, "approx", "about one fifth",
  "Lead economics memo: ceiling EUR 150 vs ~EUR 760", "2026-07-30", "medium", "own-work", "c4"),
 ("L18", "Media spent vs plan in the month after the fixes", 5076.62, 5100, "pct1", "99.5%",
  "August report: Google + Meta spend 1-28 Aug vs ~EUR 5,100 plan", "2026-08-28", "high", "own-work", "c4"),
 ("L19", "New home-market contacts from paid channels that month", 60, 76, "pct0", "79%",
  "CRM query, contacts created 1-31 Aug, project country = home market, source paid search/social", "2026-10-23", "high", "operational-access", "c4"),
 ("L20", "Contacts from that month that reached a quote or later stage within ~7 weeks", 6, 76, "pct1", "7.9%",
  "CRM: 6 deals at Quote Presentation or later from August contacts", "2026-10-20", "high", "operational-access", "c4"),
 ("L21", "Signed offer value with a paid source vs that month's media (conservative)", 19294, 5076.62, "mult1", "3.8x",
  "CRM: Offer Signed deal from a paid-social contact; the second signed offer (organic social) excluded", "2026-10-20", "high", "operational-access", "c4"),
 ("L22", "Daily contact pace in the first 22 days after media was cut, vs the previous month", 23 / 22, 39 / 30, "pct0", "80%",
  "CRM: 23 contacts 1-22 Oct vs 39 in September (project country = home market)", "2026-10-23", "high", "operational-access", "c4"),
 ("L23", "Media after the cut vs the previous month, per day", 30, 91, "approx", "about a third",
  "Budgets 3 x EUR 10/day from 28 Sep vs ~EUR 2,540 over 4 weeks in September", "2026-10-06", "high", "own-work", "c4"),
 ("L24", "Bulk email send rejected by the receiving server (unauthenticated domain)", 257, 429, "pct1", "59.9%",
  "Email platform send report, 19 Aug", "2026-08-28", "high", "own-work", "c4"),
 ("L25", "Wind-speed figures in the 18-page design attestation", 0, 18, "text", "no wind-speed figure",
  "Design conformity attestation read in full (18 pages)", "2026-08-07", "high", "public-document", "c5"),
 ("L26", "Salt-fog resistance test duration in the attestation", 96, 1, "int", "96-hour",
  "Same attestation, test reports listed", "2026-08-07", "high", "public-document", "c5"),
 ("L34", "Page count of the attestation read in full", 18, 1, "int", "18-page",
  "Design conformity attestation, 18 pages", "2026-08-07", "high", "public-document", "c5"),
 ("L35", "Single configuration on which rain and wind performance was tested", 4, 1, "int", "4 x 4 m",
  "Attestation: test report on a 4000 x 4000 mm pergola", "2026-08-07", "high", "public-document", "c5"),
 ("L36", "Business days promised for a first reply in the acknowledgement email", 2, 1, "int", "one to two business days",
  "Acknowledgement email received by the lead, 13 Oct", "2026-10-20", "high", "operational-access", "essay"),
 ("L37", "Public launches of the in-house rebuild (social page 5 Oct, portal by 15 Oct, mailing 19 Oct, full site 23 Oct)", 0, 1, "text", "within three weeks",
  "Public pages: Facebook page transparency (created 5 Oct), site and portal observed 15 and 23 Oct, mailing received 19 Oct; AI-assisted generation is an inference from code patterns", "2026-10-23", "medium", "public", "essay"),
 ("L27", "Coastal series, first 9 days: cost per form lead vs warm retargeting the month before", 22.56, 38.56, "less0", "41% lower",
  "Meta reporting 5-13 Oct (EUR 90.23 / 4 leads) vs September retargeting (EUR 38.56 per lead)", "2026-10-15", "high", "own-work", "c5"),
 ("L28", "Coastal series, 18 days: cost per form lead vs warm retargeting (same basis as L27)", 45.18, 38.56, "more0", "17% higher",
  "Meta reporting 5-22 Oct (EUR 180.70 / 4 form leads, none after 12 Oct) vs EUR 38.56", "2026-10-23", "high", "own-work", "c5"),
 ("L29", "Coastal series link click-through rate, 18 days", 177, 17461, "pct2", "1.01%",
  "Meta reporting 5-22 Oct: 177 link clicks / 17,461 impressions", "2026-10-23", "high", "own-work", "c5"),
 ("L30", "Coastal series clicks that reached the landing page", 16, 177, "pct0", "9%",
  "Meta reporting 5-22 Oct: 16 landing-page views / 177 link clicks", "2026-10-23", "high", "own-work", "c5"),
 ("L31", "Window in which all five coastal-series contacts arrived (out of 18 days)", 8, 18, "int", "first eight days",
  "CRM: 5 contacts 5-12 Oct, none 13-22 Oct", "2026-10-23", "high", "operational-access", "c5"),
 ("L32", "First reply to one traced website lead, in business days after the acknowledgement (13 Oct -> 19 Oct)", 4, 2, "int", "four business days",
  "CRM timeline of one lead (11 Oct form -> 19 Oct first reply); promise in the acknowledgement email", "2026-10-20", "high", "operational-access", "essay"),
 ("L33", "Leads in a month with no follow-up recorded in the system that captured them", 21, 22, "approx", "all but one",
  "CRM: 21 of 22 home-market contacts 1-20 Oct with zero emails, calls, notes, meetings or tasks", "2026-10-20", "high", "operational-access", "essay"),
 ("L45", "Same lead: calendar days from form (Sun 11 Oct) to first reply (Mon 19 Oct)", 8, 1, "int", "eight calendar days",
  "CRM timeline of the traced lead", "2026-10-20", "high", "operational-access", "essay"),
 ("L38", "Main search campaign switched from 'maximise conversion value' to 'maximise conversions' and default value removed", 0, 1, "text", "switched to conversions",
  "Google Ads change history export: 28 Jul 2026 09:30 bid strategy change; 09:36 value EUR 10,000 -> EUR 1", "2026-07-28", "high", "own-work", "c4"),
 ("L39", "Wind performance attested by reference to the manufacturer country's national annex, not the market's", 0, 1, "text", "another country's design standard",
  "Attestation text: 'vents de type France Metropolitaine' per NF EN 1991-1-4/NA", "2026-08-07", "high", "public-document", "c5"),
 ("L40", "The attestation applies to the design only, not to each product made", 0, 1, "text", "the design, not each unit",
  "Attestation text: 'ne s'applique qu'a la conception du systeme'", "2026-08-07", "high", "public-document", "c5"),
 ("L41", "Coastal series ran on a saved prospecting audience, not retargeting", 0, 1, "text", "prospecting audience",
  "Campaign build notes (README, 4 Oct): saved audience 'high end ... 35+'", "2026-10-04", "high", "own-work", "c5"),
 ("L42", "New in-house site carried no Google tag, GTM or Meta pixel", 0, 1, "text", "no ad-platform tags",
  "Page inspection 23 Oct: no gtag/GTM/fbq; only the platform's built-in analytics", "2026-10-23", "high", "public", "essay"),
 ("L43", "Site copy translated word for word (calques)", 0, 1, "text", "read as word-for-word translations",
  "Page text 23 Oct, e.g. 'laminas orientaveis ao grau perto', 'nunca o deixa'", "2026-10-23", "high", "public", "essay"),
 ("L44", "The one signed paid-sourced offer came from a contact created 23 Aug, after the consent fix (21 Aug)", 0, 1, "text", "after the consent fix",
  "CRM: contact created 23 Aug (paid social); deal Offer Signed 2 Sep", "2026-10-20", "high", "operational-access", "c4"),
 ("L46", "Unsupported claims had also been in copy and landing pages we built", 0, 1, "text", "including pages we had built",
  "Own copy file (Aug) carried the rating; removed from both landing pages 20 Aug", "2026-08-20", "high", "own-work", "c5"),
]


def compute(num, den, kind):
    if kind in ("int", "text"):
        return num
    return num / den


with open(OUT, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(["id", "claim", "numerator", "denominator", "kind", "computed", "display",
                "source", "source_date", "confidence", "provenance", "used_in"])
    for i, c, n, d, k, disp, s, sd, conf, prov, use in R:
        w.writerow([i, c, n, d, k, f"{compute(n, d, k):.6f}", disp, s, sd, conf, prov, use])
print("ledger rows:", len(R), "->", OUT)
