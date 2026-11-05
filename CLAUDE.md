# BLUEWRIGHT — project context

This repository holds the repositioning of a consulting practice. Read this file fully before doing anything; it is the working brief.

## Who

**Alexandre Pessoa** — solo senior consultant, Lisbon. Engineer by training (merchant-navy radio officer → sales engineer → a decade leading innovation and new-business units at Portugal's mobile operators, with several world firsts) → founder since 2008 of a boutique B2B digital practice serving Portuguese, Spanish, Belgian and American clients → higher-education lecturer for three decades, holder of the Portuguese state Specialist Title in Business Sciences. Works in EN / ES / PT (plus working FR).

## What is happening

The practice is being repositioned from **Blue Serenity** (full-service digital agency) to **Bluewright** (senior digital strategy and transformation consultancy). Reason: AI has commoditized digital execution; what remains scarce is senior judgement and the ability to make change stick in processes and people.

**Thesis:** technology doesn't transform companies — adopted technology does. Transformation fails at the two layers everyone skips: processes never redesigned, people never brought along.
**Method and tagline:** *from problem to process* (problem → strategy → execution → process).
**Target:** international B2B companies operating in Iberia (subsidiaries of foreign groups) + Iberian industrial/technical SMEs.
**Brand architecture:** Bluewright is the practice, anchored on Alexandre as the face and guarantee; Blue Serenity stays as legacy entity for existing clients during transition.
**Language:** English is the primary brand language. ES/PT versions are derived only when a client relationship justifies it.

## Working rules for Claude in this repo

1. **`brand/brand-book.md` and `brand/tokens.css` are law.** Any new visual artefact derives its colour and type from them. Do not invent a new palette, do not import a new typeface, do not exceed 3px border radius, do not let brass exceed ~5% of a surface.
2. **`strategy/positioning.md` is the decision record.** Sections marked `[DECIDED]` are closed — do not reopen them, do not "improve" the target client or the brand name. If a change is genuinely needed, propose it and wait.
3. **Voice matters more than volume.** Follow §6 of the brand book, including the banned vocabulary list. Copy that sounds like a SaaS landing page is a defect, not a style difference.
4. **Never inflate credentials.** The Specialist Title is written "Portuguese state Specialist Title in Business Sciences, awarded by public examination" — never "doctorate" or "PhD-equivalent" in public materials. Clients are **always anonymized** in public materials, even with permission (administrations change; a text should never need rewriting). The descriptor must not identify the client in five searches, and cases never refer to each other.
5. **Case studies: one client, one challenge.** A case addresses a single business challenge, stated as a general manager would say it. Similar challenges at different clients are separate cases. Technology is a means inside the decision, never the headline. Every case includes what did not work. No absolute figure unless it is credible at any scale; otherwise a ratio, or a measure of the process (time, owner, cadence). See `strategy/cases/CATALOGUE.md`.
6. **`[FILL]` markers are Alexandre's to complete.** Never invent metrics, results or client outcomes to fill them. Ask instead.
7. **Deliverables are files, not chat.** New documents go in the right folder in Markdown; PDFs are generated with Python + reportlab (see `ops/build-notes.md`); the site is a single self-contained HTML file with no build step and no framework.
8. **Ask before publishing anything.** Do not push, deploy, register domains, or send anything on Alexandre's behalf.

## Repository map

```
brand/      brand-book.md (identity system), tokens.css (colour + type tokens)
strategy/   positioning.md (the decision record)
strategy/cases/  11 cases (v4, one client + one challenge each), launch essay, check_v4.py, judges — READ CATALOGUE.md and HANDOFF.md FIRST
cases/      evidence ledgers and build scripts for the cases from ISQ-origin work (06–11); internal only
offers/     assessment-onepager.md + PDF — the Layer 1 product
site/       index.html (one-page site, self-contained), copy.md (approved copy)
bio/        bio-kit.md (About + 3 bios), assets/ CV PDF
ops/        backlog.md (what's next), decisions.md (log), build-notes.md
archive/    superseded documents — reference only, never a source of truth
```

## The offer, in one paragraph

Three layers plus a transversal one. **Assess** — *Digital & AI Readiness Assessment*: four weeks, six dimensions, fixed scope and timeline, **€9,500** all-inclusive, 50% credited against implementation if they proceed within 90 days. **Transform** — strategy plus implementation in short cycles. **Advise** — fractional digital director on retainer. **Enablement** — executive and team training, across all three.

## Commercial discipline (context for any copy you write)

Alexandre's known tendency is to underprice and over-deliver. The materials are deliberately built to counter it: prices are stated plainly and never discounted (scope moves instead, never price); the assessment credit replaces any discount; generosity is always made explicit and quantified. Never write copy that hedges on price, apologizes for it, or adds "starting from".
