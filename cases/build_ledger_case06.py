"""Builds the evidence ledger for case 06 (ISQ Academy reseller academy relaunch).
Raw values were read from primary sources between July and 24 Oct 2026 (see `source`):
the production database of the new platform (queried 24 Oct 2026), the old server, project documents.
Every ratio is computed here from numerator/denominator so check_case06.py can verify the text."""
import csv, os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "evidence-ledger-case06.csv")

DB = "Production DB (WooCommerce orders, status completed/processing, tests excluded), queried 24 Oct 2026"

# id, claim, numerator, denominator, kind, display, source, source_date, confidence, provenance
R = [
 ("A01", "Site revenue 2025 vs 2024 (fall)", 5799.45, 14633.93, "less0", "60%",
  DB + ": full year 2025 / full year 2024", "2026-10-24", "high", "operational-access"),
 ("A02", "Site revenue 1 Jan-20 Jul 2026 vs same period 2025 (fall)", 2001.83, 4692.45, "less0", "57%",
  DB + ": 2026-01-01..07-20 / 2025-01-01..07-20 (proposal written in July)", "2026-10-24", "high", "operational-access"),
 ("A03", "Active plugins on the old site", 47, 1, "int", "47",
  "Old server (giga3), wp plugin list --status=active", "2026-10-24", "high", "operational-access"),
 ("A04", "Active plugins on the new platform", 5, 1, "int", "five",
  "New server, wp plugin list --status=active (+2 small must-use configuration files)", "2026-10-24", "high", "own-work"),
 ("A05", "Orders in the old data with a buyer tax number that fails the checksum", 7, 156, "pct1", "4.5%",
  "Old production data since 2024: 156 orders with a tax number, 7 invalid (query 25 Sep 2026, project memory)", "2026-09-25", "medium", "operational-access"),
 ("A06", "Historical enrolments whose course could not be recovered", 67, 448, "pct0", "15%",
  "Production: 448 enrolment records in trainee histories; 67 left without a course after the recovery cascade (24 Oct 2026). Cause: the events had been deleted in the old system", "2026-10-24", "high", "own-work"),
 ("A07", "Days between planned and actual go-live", 14, 1, "int", "two weeks",
  "Contract annex III: planned 8 Oct 2026; production DNS switched 22 Oct 2026", "2026-10-22", "high", "own-work"),
 ("A08", "Seats sold on the course whose checkout was broken at creation", 24, 23, "int", "23 seats",
  "Production: course 38366 capacity 23; 24 orders lines incl. 1 unpaid (orders 38375-38405)", "2026-10-24", "high", "operational-access"),
 ("A09", "Share of 2026 site revenue (to 21 Oct) from the four paid orders for that course, placed 19-21 Oct", 2263.20, 7023.31, "approx", "about a third",
  DB + ": orders 38379, 38390, 38400, 38405 / all 2026 to 21 Oct", "2026-10-24", "high", "operational-access"),
 ("A10", "Hours between the first and the last paid order for that course", 44.2, 1, "int", "under 48 hours",
  "First paid order 19 Oct 13:36, last 21 Oct 09:50 (registration closed 21 Oct 14:00)", "2026-10-24", "high", "operational-access"),
 ("A11", "Maintenance window of the cutover (minutes, approximate)", 70, 1, "int", "about 70 minutes",
  "Old site in maintenance ~03:10; production live ~04:20 (22 Oct, Lisbon time). Server logs + project notes", "2026-10-22", "medium", "own-work"),
 ("A12", "Orders lost in the cutover", 0, 1, "int", "zero",
  "Final dump taken after maintenance mode was on; last order 21 Oct 09:50 present in both systems", "2026-10-22", "high", "own-work"),
 ("A13", "Renewal opportunities in which the certification had already lapsed", 30, 30, "pct0", "100%",
  "Production Radar, renewal list (validity 60 months, window 3 months), 24 Oct 2026, after the history was linked (first week)", "2026-10-24", "high", "own-work"),
 ("A14", "Radar potential (renewals + progressions, reseller prices) vs the project fee", 6655, 7000, "pct0", "95%",
  "Production Radar 24 Oct 2026: renewals EUR 4,950 + progressions EUR 1,705; fee from the signed contract", "2026-10-24", "high", "own-work"),
 ("A15", "Reseller companies with staff below the 40-hour legal training minimum (in hours done at the academy)", 31, 1, "int", "31",
  "Production Radar, hours list (Labour Code art. 131, 24-month activity window), 24 Oct 2026", "2026-10-24", "high", "own-work"),
 ("A16", "Good practices absent from the group's main training site", 9, 19, "int", "9 of 19",
  "External reading of academy.isq.pt vs the benchmark: 4 present, 5 partial, 9 absent, 1 not verifiable", "2026-08-26", "medium", "public"),
 ("A17", "Payment schedule demanded by the client (adjudication / pre-production / after stabilisation)", 30, 100, "text", "30/40/30",
  "Signed addendum v2, clause 3", "2026-09-11", "high", "own-work"),
 ("A18", "Warranty demanded by the client (months)", 9, 1, "int", "9 months",
  "Signed addendum v2, clause 5", "2026-09-11", "high", "own-work"),
 ("A19", "Hours from launch to the fix of rejected notification e-mails (approximate)", 15, 1, "int", "the same day",
  "Launch 04:20; client reported mid-afternoon; fix verified ~19:50 (22 Oct)", "2026-10-22", "medium", "own-work"),
 ("A20", "Legacy unpaid orders auto-expired by mistake by the new platform", 35, 1, "int", "35",
  "Production: daily expiry job 23 Oct 03:00 after history was linked; all 35 restored 24 Oct, no e-mails sent", "2026-10-24", "high", "own-work"),
]

with open(OUT, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["id", "claim", "numerator", "denominator", "kind", "computed", "display", "source", "source_date", "confidence", "provenance"])
    for (i, c, n, d, k, disp, s, sd, conf, prov) in R:
        w.writerow([i, c, n, d, k, round(n / d, 6), disp, s, sd, conf, prov])
print(f"{len(R)} rows -> {OUT}")
