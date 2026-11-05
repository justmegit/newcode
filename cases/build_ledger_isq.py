"""Builds the evidence ledger for case 02 (ISQ Espana).
Raw values come from the ISQ ES project record (memory files written at the time of each
measurement) and from read-only API reads of the autoisq n8n instance on 24 Oct 2026.
Every ratio is recomputed from numerator/denominator so check_ledger_isq.py can verify it."""
import csv, os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "evidence-ledger-isq.csv")
MEM = "ISQ ES project memory"

# id, claim, numerator, denominator, kind, display, source, source_date, confidence, provenance
R = [
 ("I01", "Birthday greetings missed while the old flow reported success", 38, 1, "int", "38",
  f"{MEM}, isq-es-roadmap (project A): 119 iterations, zero sends, 16 Apr-12 Aug 2026", "2026-08-12", "high", "own-work"),
 ("I02", "Inflation of the July competitor panel in the old manual report", 235, 220, "more0", "7%",
  f"{MEM}, isq-es-clipping: July recounted from 235 to 220 panel posts", "2026-08-16", "high", "own-work"),
 ("I03", "LinkedIn page visits in 90 days", 141, 1, "int", "141",
  "LinkedIn page exports 15 May-12 Aug 2026 (visitors)", "2026-08-14", "high", "operational-access"),
 ("I04", "LinkedIn organic impressions in the same 90 days", 16156, 1, "int", "16,156",
  "Same exports (posts)", "2026-08-14", "high", "operational-access"),
 ("I05", "Share of followers located in Spain", 193, 763, "pct0", "25%",
  "Followers export: Spain ~193 of ~763", "2026-08-14", "medium", "operational-access"),
 ("I07", "Decision-makers (Director+VP+CXO) among followers", 9, 100, "pct0", "9%",
  "Followers export, seniority breakdown (reported as 9%)", "2026-08-14", "medium", "operational-access"),
 ("I09", "Proposed content topics claiming services outside the published catalogue", 5, 9, "frac", "5 of 9",
  f"{MEM}, isq-es-roadmap: rebalanced plan checked against isq.es/servicios", "2026-08-14", "high", "own-work"),
 ("I11", "Greetings sent on schedule and logged in the first three weeks of the rebuilt flow", 3, 1, "int", "three greetings",
  "SharePoint list Log Cumpleanos, 12 Aug-1 Sep: 94 rows read/day, 3 sends, 0 errors", "2026-09-01", "high", "operational-access"),
 ("I16", "Artefact jump the report refused to publish", 167, 100, "text", "+167%",
  f"{MEM}, isq-es-clipping: August vs under-sampled July would have read +167% panel volume", "2026-09-02", "high", "own-work"),
 ("I17", "Seconds from approval send to live-post confirmation, first publication", 49, 60, "text", "under a minute",
  f"{MEM}, isq-es-sistema-conteudo: send 08:03:41 -> confirmation 08:04:30 on 13 Sep = 49 s (the memory's own '57 s' is an arithmetic slip)", "2026-09-13", "medium", "own-work"),
 ("I18", "Impressions of the inspector-named post vs the best dense post", 2150, 2278, "pct0", "94%",
  "LinkedIn post analytics: 26 Aug (2,150) vs 8 Jul (2,278)", "2026-09-01", "high", "operational-access"),
 ("I19", "Page visits from the inspector-named post vs the dense post", 15, 3, "mult0", "5x",
  "Same analytics: 15 vs 3 page visits", "2026-09-01", "high", "operational-access"),
 ("I20", "New followers from one post vs all new followers in August", 16, 31, "frac", "16 of 31",
  "LinkedIn followers and post analytics, August 2026", "2026-09-01", "high", "operational-access"),
 ("I25", "Weeks with zero field photos received", 3, 1, "int", "three weeks",
  "SharePoint library Contenido de Campo at 0 items, 1 Sep", "2026-09-01", "high", "operational-access"),
]

with open(OUT, "w", newline="\n", encoding="utf-8") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(["id", "claim", "numerator", "denominator", "kind", "computed", "display", "source", "source_date", "confidence", "provenance", "used_in"])
    for r in R:
        i, claim, n, d, kind, disp, src, date, conf, prov = r
        w.writerow([i, claim, n, d, kind, round(n / d, 6), disp, src, date, conf, prov, "c2"])
print(f"{len(R)} rows -> {OUT}")
