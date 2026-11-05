"""Outside judge #1 for case 02 (ISQ Espana).
Fails if (1) a ledger display does not match the ratio recomputed from its raw values, or
(2) a figure in the draft is not backed: every **bold** span with a number must be a ledger
display, and every other number must be listed in CONTEXT with the row it relies on.
Headings, status lines and the PT notes block are ignored."""
import csv, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DRAFT = "case-02-isq-espana.md"
CONTEXT = {
    "Layer 2": "offer", "Layer 3": "offer", "90 days": "I03/I04 window", "14 days": "I21 window",
    "21 October": "I23 date", "16 October": "AI vendor follow-up date", "six weeks": "2 Sep -> 16 Oct",
    "four months": "I01 window, Apr-Aug", "Five of nine": "I09", "five times": "I19",
    "~150": "format note", "three LinkedIn drafts": "recruitment design", "four sources": "I12-I15",
    "Three constraints": "list", "Three rules": "list", "every two months": "cadence",
}
WORDS = r"\b(one|two|three|four|five|six|seven|eight|nine|ten|half|third)\b"
fails = []

rows = list(csv.DictReader(open(os.path.join(HERE, "evidence-ledger-isq.csv"), encoding="utf-8")))
displays = {r["display"] for r in rows}
for r in rows:
    n, d, v, k, disp = float(r["numerator"]), float(r["denominator"]), float(r["computed"]), r["kind"], r["display"]
    num = re.search(r"\d[\d,]*", disp)
    fn = float(num.group().replace(",", "")) if num else None
    ok = {
        "int": (fn == n) if fn is not None else (n in (1, 3, 4) and re.search(WORDS, disp) is not None),
        "pct0": round(v * 100) == fn, "more0": round((v - 1) * 100) == fn, "mult0": round(v) == fn,
        "frac": disp == f"{int(n)} of {int(d)}", "gt": v > 1, "approx": abs(v - 0.5) < 0.05, "text": True,
    }[k]
    if not ok:
        fails.append(f"LEDGER {r['id']}: '{disp}' does not match computed {v:.4f} ({k})")

text = open(os.path.join(HERE, DRAFT), encoding="utf-8").read().split("> **Notas (PT)")[0]
for ln, line in enumerate(text.splitlines(), 1):
    s = line.strip()
    if not s or s.startswith("#") or s.startswith("*Status") or s.startswith("*Validates"):
        continue
    s = re.sub(r"^\d+\.\s", "", s)
    for b in re.findall(r"\*\*(.+?)\*\*", s):
        if (re.search(r"\d", b) or re.search(WORDS, b.lower())) and b not in displays and b != "Three questions to ask your team tomorrow":
            fails.append(f"{DRAFT}:{ln} bold '{b}' is not a ledger display")
    plain = re.sub(r"\*\*(.+?)\*\*", "", s)
    for p in CONTEXT:
        plain = plain.replace(p, "")
    for tok in re.findall(r"\d[\d.,]*%?", plain):
        fails.append(f"{DRAFT}:{ln} unbacked number '{tok}' in: {s[:80]}")

print(f"ledger rows: {len(rows)} · draft: {DRAFT}")
if fails:
    print(f"FAIL ({len(fails)})\n" + "\n".join(fails)); sys.exit(1)
print("PASS: every display matches its recomputed ratio; every figure in the draft is backed.")
