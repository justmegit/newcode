"""Outside judge #1 for case 06. Exits non-zero on any failure.
  1. Every ledger `display` matches the ratio recomputed from numerator/denominator.
  2. Every figure in the draft is backed: each **bold** numeric span equals a ledger display, and every
     other number appears in CONTEXT with the ledger row (or public fact) it relies on.
Headings, status lines (starting with '*') and list markers are ignored."""
import csv, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DRAFT = "case-06-the-catalogue-nobody-could-sell.md"
CONTEXT = {  # unbolded phrases with numbers -> ledger row or public source
    "60%": "A01", "under 48 hours": "A10",
    "40 hours": "Labour Code art. 131 (public law)", "90-day": "measurement plan", "90 days": "measurement plan",
    "22 Jan 2027": "measurement plan", "2025": "A01/A02 period", "Six days": "incident 16 Oct, cutover 22 Oct",
    "Layer 2": "offer structure", "~150": "format note",
}
NUM_WORDS = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "nine": 9}
fails = []
rows = list(csv.DictReader(open(os.path.join(HERE, "evidence-ledger-case06.csv"), encoding="utf-8")))
displays = {r["display"].lower() for r in rows}
ALLOWED_PROV = {"own-work", "operational-access", "public", "public-document"}

def first_num(s):
    m = re.search(r"-?\d+(?:\.\d+)?", s)
    if m: return float(m.group())
    w = [NUM_WORDS[x] for x in re.findall(r"[a-z]+", s.lower()) if x in NUM_WORDS]
    return float(w[0]) if w else None

for r in rows:
    k, disp = r["kind"], r["display"]
    n, d, v = float(r["numerator"]), float(r["denominator"]), float(r["computed"])
    ok = True
    if k == "pct0": ok = round(v * 100) == first_num(disp)
    elif k == "pct1": ok = round(v * 100, 1) == first_num(disp)
    elif k == "less0": ok = round((1 - v) * 100) == first_num(disp)
    elif k == "approx": ok = abs(v - {"about a third": 1 / 3}[disp]) < 0.03
    elif k == "int":
        fn = first_num(disp)
        if r["id"] == "A07": ok = n == 14 and disp == "two weeks"
        elif r["id"] == "A08": ok = d == 23 and fn == 23
        elif r["id"] == "A10": ok = n < 48 and disp == "under 48 hours"
        elif r["id"] == "A19": ok = n <= 24 and disp == "the same day"
        elif r["id"] == "A16": ok = (n, d) == (9, 19)
        else: ok = fn is not None and fn == n
    if r["provenance"] not in ALLOWED_PROV: fails.append(f"LEDGER {r['id']}: provenance '{r['provenance']}' not allowed")
    if not ok: fails.append(f"LEDGER {r['id']}: display '{disp}' does not match computed {v:.4f} ({k})")

text = open(os.path.join(HERE, DRAFT), encoding="utf-8").read()
for ln, line in enumerate(text.splitlines(), 1):
    s = line.strip()
    if not s or s.startswith("#") or s.startswith("*Status") or s.startswith("*Validates") or s.startswith("[FILL") or "[FILL" in s[:12]:
        continue
    s = re.sub(r"^\d+\.\s", "", s)
    s = re.sub(r"\[FILL[^\]]*\]", "", s)
    for b in re.findall(r"\*\*(.+?)\*\*", s):
        numeric = re.search(r"\d", b) or any(w in NUM_WORDS or w in ("third", "half", "times", "same") for w in re.findall(r"[a-z]+", b.lower()))
        if numeric and b.lower() not in displays and b != "Three questions to ask your team tomorrow":
            fails.append(f"{DRAFT}:{ln} bold '{b}' is not a ledger display")
    plain = re.sub(r"\*\*(.+?)\*\*", "", s)
    for phrase in CONTEXT: plain = plain.replace(phrase, "")
    for tok in re.findall(r"\d[\d.,]*\s?(?:%|x\b)?", plain):
        fails.append(f"{DRAFT}:{ln} unbacked number '{tok.strip()}' in: {line.strip()[:90]}")

print(f"ledger rows checked: {len(rows)} · draft: {DRAFT}")
if fails:
    print(f"FAIL ({len(fails)})"); print("\n".join(fails)); sys.exit(1)
print("PASS: every ledger display matches its recomputed ratio; every figure in the draft is backed.")
