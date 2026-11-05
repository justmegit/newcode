# Build notes

## The site

`site/index.html` is a **single self-contained file**: no build step, no framework, no bundler, no node_modules. Fonts load from Google Fonts; everything else is inline. This is deliberate — it deploys anywhere by copying one file, and it will still work in five years.

Preview locally:
```bash
cd site && python3 -m http.server 8000   # then open http://localhost:8000
```

Deploy: copy `index.html` to the web root, plus `Bluewright-Assessment-onepager.pdf` alongside it (the Assessment section links to it relatively).

Rules when editing: derive every colour and size from `brand/tokens.css`; keep the reveal-on-scroll behaviour respecting `prefers-reduced-motion`; keep visible keyboard focus; check it at 380px width before declaring it done.

## PDFs

Generated with **reportlab** (`pip install reportlab --break-system-packages`), platypus for flowing text plus canvas drawing for the header/footer bands. Poppler (`pdftoppm`, `pdftotext`) is used to verify output.

The non-negotiable verification step — reportlab silently drops content that doesn't fit its frame:

```bash
python build-onepager.py
pdftotext output.pdf - | grep -c "last sentence of the last block"   # must be 1
pdftoppm -png -r 80 output.pdf preview                               # then LOOK at it
```

If a block is missing, shorten the copy or tighten `spaceBefore` — do not silently let it disappear.

Layout conventions shared by every PDF: navy header band with a 3px brass rule beneath it; Helvetica as the PDF-safe stand-in for Archivo (embedding Newsreader is possible via `pdfmetrics.registerFont` if a future piece needs the display serif); price in brass; navy footer band with contact details.

The assessment one-pager is rebuilt by `offers/build-onepager.py` (rewritten 5 Nov 2026; the copy lives inside the script and must be kept in step with `offers/assessment-onepager.md`). The CV build script was lost when the original session's container reset — the PDF in `bio/assets/` is the current artefact. Regenerate from the Markdown source when the copy changes, following the conventions above.

## Fonts

Newsreader, Archivo and IBM Plex Mono are all Google Fonts under the Open Font License — free for commercial use, embeddable in PDFs, self-hostable. If self-hosting for the site, download the static instances rather than the variable fonts for smaller payloads: Newsreader at `opsz=72, wght=300/500`, Archivo at `wdth=100, wght=400/600` plus `wdth=125, wght=600` for the logotype.
