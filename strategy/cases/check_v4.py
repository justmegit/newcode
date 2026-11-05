"""Judge 1 for the v4 cases: every figure in a case must appear in an evidence ledger.

Run: python -I check_v4.py   (from strategy/cases/)
"""
import csv
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
LEDGERS = [
    HERE / "evidence-ledger.csv",
    HERE / "evidence-ledger-v4.csv",
    ROOT / "cases" / "evidence-ledger-isq.csv",
    ROOT / "cases" / "evidence-ledger-case06.csv",
]
NUM = re.compile(r"\+?\d[\d,.]*\s?(?:%|x)?")
WORDS = ["more than seven times", "about one fifth", "about a third", "under a minute",
         "three weeks", "two weeks", "the same day", "first eight days", "zero",
         "more than ten times", "more than three times", "about twelve", "about one a week", "two a week", "about 3%"]


def ledger_displays():
    displays = []
    for path in LEDGERS:
        with path.open(encoding="utf-8") as f:
            for row in csv.DictReader(f):
                displays.append(row["display"])
    return displays


def figures(text):
    out = []
    for line in text.splitlines():
        if line.startswith(("#", "*")) or "[FILL" in line:
            continue
        line = re.sub(r"^\d+\.\s", "", line)
        out += [m.group().rstrip(".,").replace(" ", "") for m in NUM.finditer(line)]
    return out


def main():
    displays = ledger_displays()
    flat = [d.replace(" ", "") for d in displays]
    failures = 0
    for case in sorted(HERE.glob("case-*.md")):
        text = case.read_text(encoding="utf-8")
        missing = [n for n in figures(text) if not any(n in d for d in flat)]
        missing += [w for w in WORDS if w in text and not any(w in d for d in displays)]
        status = "ok" if not missing else "MISSING " + ", ".join(missing)
        print(f"{case.name}: {status}")
        failures += bool(missing)
    copy = (ROOT / "site" / "copy.md").read_text(encoding="utf-8")
    work = copy[copy.index("## 5. WORK"):copy.index("## 6. ABOUT")]
    missing = [n for n in figures(work) if not any(n in d for d in flat)]
    print("site/copy.md section 5:", "ok" if not missing else "MISSING " + ", ".join(missing))
    failures += bool(missing)
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
