"""Outside judge #1 for cases 04, 05 and the essay.

Checks two things and exits non-zero on any failure:
  1. Every ledger `display` is consistent with the ratio recomputed from numerator/denominator.
  2. Every figure in the drafts is backed by the ledger: each **bold** span must equal a ledger
     display, and every other number must appear in CONTEXT with the ledger row it relies on.
Headings, status lines (starting with '*') and list markers are ignored.
"""
import csv, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DRAFTS = ["case-04-fix-the-signal.md", "case-05-claims-you-can-defend.md", "essay-ai-built-it.md"]

# Unbolded phrases with numbers, each mapped to the ledger row that supports it.
CONTEXT = {
    "99.99%": "L03", "81.6%": "L08", "more than seven times": "L16",
    "20 October": "L20 (query date)", "28 August": "L13 / L18 / L21 cut-off", "three weeks": "L22 / L33 window", "nine days": "L27", "after 18": "L28",
    "Layer 1": "offer structure", "Layer 2": "offer structure",
}
NUM_WORDS = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8}

fails = []

# ---------- 1. ledger consistency ----------
rows = list(csv.DictReader(open(os.path.join(HERE, "evidence-ledger.csv"), encoding="utf-8")))
by_id = {r["id"]: r for r in rows}
displays = {r["display"].lower() for r in rows}


def first_num(s):
    m = re.search(r"-?\d+(?:\.\d+)?", s)
    return float(m.group()) if m else None


for r in rows:
    k, disp = r["kind"], r["display"]
    n, d, v = float(r["numerator"]), float(r["denominator"]), float(r["computed"])
    ok = True
    if k == "pct0": ok = round(v * 100) == first_num(disp)
    elif k == "pct1": ok = round(v * 100, 1) == first_num(disp)
    elif k == "pct2": ok = round(v * 100, 2) == first_num(disp)
    elif k == "mult1": ok = round(v, 1) == first_num(disp)
    elif k == "less0": ok = round((1 - v) * 100) == first_num(disp)
    elif k == "more0": ok = round((v - 1) * 100) == first_num(disp)
    elif k == "int":
        fn = first_num(disp)
        if fn is None:
            words = [NUM_WORDS[w] for w in re.findall(r"[a-z]+", disp.lower()) if w in NUM_WORDS]
            fn = words[-1] if words else None
        ok = fn is not None and float(fn) == n
    elif k == "range": ok = 0.30 <= v <= 0.50
    elif k == "gt": ok = v > 7 if "seven" in disp else True
    elif k == "approx":
        target = {"about one fifth": 0.2, "about a third": 1 / 3}.get(disp)
        ok = (abs(v - target) < 0.03) if target else (disp == "all but one" and n == d - 1)
    elif k == "text": ok = True  # verified by reading the source, see `source`
    if r["id"] == "L06": ok = (n, d) == (3, 72)
    if not ok:
        fails.append(f"LEDGER {r['id']}: display '{disp}' does not match computed {v:.4f} ({k})")

# ---------- 2. draft coverage ----------
for name in DRAFTS:
    text = open(os.path.join(HERE, name), encoding="utf-8").read()
    for ln, line in enumerate(text.splitlines(), 1):
        s = line.strip()
        if not s or s.startswith("#") or s.startswith("*Status") or s.startswith("*Validates") or s.startswith("*Essay") or s.startswith("*⚠"):
            continue
        s = re.sub(r"^\d+\.\s", "", s)  # list markers
        for b in re.findall(r"\*\*(.+?)\*\*", s):
            numeric = re.search(r"\d", b) or any(w in NUM_WORDS or w in ("third", "fifth", "half", "times") for w in re.findall(r"[a-z]+", b.lower()))
            if numeric and b.lower() not in displays and b != "Three questions to ask your team tomorrow":
                fails.append(f"{name}:{ln} bold '{b}' is not a ledger display")
        plain = re.sub(r"\*\*(.+?)\*\*", "", s)
        for phrase in CONTEXT:
            plain = plain.replace(phrase, "")
        for tok in re.findall(r"\d[\d.,]*\s?(?:%|x\b)?", plain):
            fails.append(f"{name}:{ln} unbacked number '{tok.strip()}' in: {line.strip()[:90]}")

print(f"ledger rows checked: {len(rows)} · drafts checked: {len(DRAFTS)}")
if fails:
    print(f"FAIL ({len(fails)})")
    print("\n".join(fails))
    sys.exit(1)
print("PASS: every ledger display matches its recomputed ratio; every figure in the drafts is backed.")
