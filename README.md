# BLUEWRIGHT

Repositioning of a senior B2B digital consulting practice — Lisbon & Madrid.
*From problem to process.*

## Start here

```bash
cd bluewright
claude
```

Then paste the first prompt from `KICKOFF.md`. Claude Code reads `CLAUDE.md` automatically at session start; it contains the brief, the working rules, and the repository map.

## What's in here

| Path | What it is | State |
|---|---|---|
| `CLAUDE.md` | The brief and working rules | Current |
| `KICKOFF.md` | Prompts for the next tasks | Current |
| `brand/brand-book.md` | Identity system — name, mark, colour, type, voice | v1, law |
| `brand/tokens.css` | Colour and type tokens | v1, law |
| `strategy/positioning.md` | Decision record: thesis, target, offer, transition plan | v2, current |
| `strategy/case-studies.md` | Three case studies | Drafts — needs `[FILL]` |
| `offers/assessment-onepager.md` + `assets/` | The €9,500 Layer 1 product | Approved, PDF built |
| `site/index.html` | One-page website, self-contained | Built, needs final cases |
| `site/copy.md` | Approved website copy | Approved |
| `bio/bio-kit.md` | About section + three bio lengths | v1 |
| `bio/assets/` | CV in English, two pages | Built |
| `ops/` | Backlog, decision log, build notes | Current |
| `archive/` | Superseded — reference only | Do not use as source |

## Before anything goes public

Three checks belong to Alexandre and block everything else: domain availability (`bluewright.com`, `.pt`), the LinkedIn handle, and a trademark search at EUIPO/INPI in classes 35 and 41. See `ops/backlog.md`.

## Preview the site

```bash
cd site && python3 -m http.server 8000
```
