#!/usr/bin/env python3
"""Build offers/assets/Bluewright-Assessment-onepager.pdf from the approved copy.

Conventions (ops/build-notes.md): navy header band with a 3px brass rule, two
columns, price in brass, navy footer band. Helvetica stands in for Archivo.
Run from the repo root or from offers/. Verify afterwards with pdftotext and
pdftoppm — reportlab drops content silently when a frame overflows.
"""
from pathlib import Path

from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, Flowable, FrameBreak, Frame,
                                PageTemplate, Paragraph, Spacer)

HERE = Path(__file__).resolve().parent
OUT = HERE / "assets" / "Bluewright-Assessment-onepager.pdf"

# brand/tokens.css
NAVY, HARBOR, BRASS, DARK_BRASS = (HexColor(c) for c in ("#122C4A", "#0C1F35", "#C9A15A", "#8A6A2F"))
STEEL, FOG, INK, GREY, LINE = (HexColor(c) for c in ("#3E7CB1", "#EFF3F7", "#20293A", "#5A6472", "#D8E0E8"))

W, H = A4
M = 40                      # side margin
HEADER_H = 116              # navy header band
FOOTER_H = 52               # navy footer band
BOX_Y, BOX_H = 66, 88      # investment box (from bottom)
BODY_TOP = H - HEADER_H - 20
BODY_BOTTOM = BOX_Y + BOX_H + 14
COL_GAP = 18
COL_W = (W - 2 * M - COL_GAP) / 2

body = ParagraphStyle("body", fontName="Helvetica", fontSize=8.3, leading=11.2, textColor=INK, alignment=TA_LEFT)
lede = ParagraphStyle("lede", parent=body, fontSize=8.9, leading=12.4)
head = ParagraphStyle("head", fontName="Helvetica-Bold", fontSize=8, leading=11, textColor=STEEL, spaceBefore=9, spaceAfter=4)
item = ParagraphStyle("item", parent=body, spaceAfter=2.5)
fine = ParagraphStyle("fine", parent=body, fontSize=8, leading=10.8, textColor=GREY)
quiet = ParagraphStyle("quiet", parent=body, textColor=GREY, fontName="Helvetica-Oblique")


def sp(text):
    """Section label: uppercase, steel, no letterspacing (keeps the text extractable)."""
    return Paragraph(text.upper(), head)


class Angle(Flowable):
    """Brass right angle (the wright angle) before a paragraph: left stroke
    vertical, bottom stroke horizontal, meeting at bottom-left."""

    def __init__(self, para, size=5, indent=11):
        super().__init__()
        self.para, self.size, self.indent = para, size, indent

    def getSpaceAfter(self):
        return self.para.style.spaceAfter

    def wrap(self, aw, ah):
        self.w, self.h = self.para.wrap(aw - self.indent, ah)
        return aw, self.h

    def split(self, aw, ah):
        return []

    def draw(self):
        c = self.canv
        c.saveState()
        c.setStrokeColor(BRASS)
        c.setLineWidth(1.3)
        x0, y0 = 0.8, self.h - self.para.style.fontSize + 0.6
        c.line(x0, y0, x0, y0 + self.size)
        c.line(x0, y0, x0 + self.size, y0)
        c.restoreState()
        self.para.drawOn(c, self.indent, 0)


def A(text):
    return Angle(Paragraph(text, item))


def P(text, style=body):
    return Paragraph(text, style)


# ----------------------------------------------------------------- content
intro = (
    "For a subsidiary that sells in Iberia what the group makes elsewhere, or for a technical "
    "company whose product is a service, the business <i>is</i> the commercial engine: how the market "
    "hears of you, how a lead becomes a customer, how that customer is served and kept, and how the "
    "people who do all this are hired and equipped. That is where digital and AI either pay or don't. "
    "It is also where most initiatives fail: tools bought and never used, pilots that never scale, "
    "processes nobody redesigned, people nobody brought along. The <b>Commercial Engine Assessment</b> "
    "is a fixed-scope, four-week diagnostic that gives your leadership team a clear, prioritized answer "
    "to three questions: <b>Where do we stand? What is actually worth doing? And in what order?</b>"
)

left = [
    sp("What we examine"),
    P("Six lenses on one engine, working directly with your management and the people who run it.", quiet),
    Spacer(0, 3),
    A("<b>Business context &amp; strategy</b> — market position, the group's priorities for Iberia, what the engine has to deliver."),
    A("<b>Demand &amp; sales</b> — how the market finds you and how a lead becomes a customer: presence, funnel, sales process — including whether AI assistants name you when buyers ask."),
    A("<b>Processes &amp; operations</b> — how marketing, sales, service and communications actually work — and where the friction is."),
    A("<b>Data &amp; systems</b> — CRM, analytics, automation: what talks to what, and what doesn't."),
    A("<b>AI readiness</b> — every AI already in use, bought, embedded or unauthorised; where AI would actually pay, and what must be true first."),
    A("<b>People &amp; adoption</b> — skills, habits and ownership: who will make the change stick."),
    sp("How it works"),
    P("<b>Week 1 — Immersion.</b> Kickoff with leadership, structured interviews with key people, access to systems and data. Delivered by Friday: the <b>AI use register</b> — every AI in use, by function, owner and contract, with the AI Act obligation each one triggers, or none. The legal opinion stays with your lawyers; the inventory is yours.", item),
    P("<b>Weeks 2–3 — Analysis.</b> Audit of presence, funnel, processes and toolset; benchmarking against your market, including what AI assistants say about you and your competitors.", item),
    P("<b>Week 4 — Roadmap &amp; decision.</b> Findings consolidated into a prioritized roadmap, presented in person to your leadership team.", item),
    Spacer(0, 2),
    P("Fixed scope. Fixed timeline. Fixed fee. No open-ended engagement — and no junior staff learning on your budget.", quiet),
]

right = [
    sp("What you get"),
    A("<b>Maturity map</b> — of where you stand across the six lenses."),
    A("<b>AI use register</b> — yours to keep and maintain."),
    A("<b>Prioritized opportunities</b> — qualified by impact and effort — including what <i>not</i> to do."),
    A("<b>90-day quick-wins plan</b> — you can start immediately."),
    A("<b>12-month roadmap</b> — connecting technology, process and people."),
    A("<b>Leadership working session</b> — to turn the roadmap into decisions."),
    Spacer(0, 2),
    P("Every recommendation is executable — by your team, by us, or by any partner. You own the roadmap either way.", fine),
    sp("Who this is for"),
    P("International B2B companies operating in Portugal and Spain that need a senior partner on the ground — and Iberian industrial and technical SMEs that must modernize but lack an internal digital leadership role. If your growth depends on how you win and serve customers in Iberia, and the answer involves technology, process and people at the same time, this was built for you."),
    sp("Why Bluewright"),
    P("Conducted personally by <b>Alexandre Pessoa</b> — engineer, digital practitioner since 2007, former new-business director in telecoms, university lecturer for 30 years. Fluent in EN, ES, FR and PT, he has spent two decades making digital work for international and Iberian B2B companies — in running processes teams actually adopt. We use daily the AI and automation we recommend."),
]


# ------------------------------------------------------------------ chrome
def chrome(c, doc):
    c.saveState()
    # header band
    c.setFillColor(NAVY)
    c.rect(0, H - HEADER_H, W, HEADER_H, stroke=0, fill=1)
    c.setFillColor(BRASS)
    c.rect(0, H - HEADER_H - 3, W, 3, stroke=0, fill=1)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 17)
    c.drawString(M, H - 34, "B L U E W R I G H T")
    c.setFont("Helvetica", 8.2)
    c.setFillColor(HexColor("#C6CDD6"))
    c.drawString(M, H - 47, "Digital Strategy & Transformation  ·  Iberia")
    c.setFont("Helvetica-Oblique", 8.6)
    c.setFillColor(HexColor("#C9A15A"))
    c.drawRightString(W - M, H - 34, "From problem to process.")
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 17.5)
    c.drawString(M, H - 82, "Commercial Engine Assessment")
    c.setFont("Helvetica-Oblique", 9.6)
    c.setFillColor(BRASS)
    c.drawString(M, H - 97, "Digital & AI readiness, applied to how you win, serve and keep customers.")

    # investment box
    c.setFillColor(FOG)
    c.rect(M, BOX_Y, W - 2 * M, BOX_H, stroke=0, fill=1)
    c.setFillColor(BRASS)
    c.rect(M, BOX_Y, 3, BOX_H, stroke=0, fill=1)
    x = M + 16
    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 8.4)
    c.drawString(x, BOX_Y + BOX_H - 16, "I N V E S T M E N T   &   N E X T   S T E P")
    c.setFillColor(DARK_BRASS)
    c.setFont("Helvetica-Bold", 19)
    c.drawString(x, BOX_Y + BOX_H - 40, "€ 12,000")
    c.setFillColor(INK)
    c.setFont("Helvetica", 8.6)
    c.drawString(x + 92, BOX_Y + BOX_H - 38, "fixed fee, all-inclusive  ·  four weeks from kickoff to roadmap")
    para = Paragraph(
        "If you proceed to implementation with us within 90 days, <b>50% of the assessment fee is credited</b> "
        "against the first project. <b>Next step:</b> a 30-minute conversation to confirm fit and scope — "
        "no preparation needed on your side.", body)
    pw, ph = para.wrap(W - 2 * M - 32, BOX_H)
    para.drawOn(c, x, BOX_Y + 10)

    # footer band
    c.setFillColor(HARBOR)
    c.rect(0, 0, W, FOOTER_H, stroke=0, fill=1)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 8.6)
    c.drawString(M, 30, "B L U E W R I G H T")
    c.setFont("Helvetica", 7.6)
    c.setFillColor(HexColor("#C6CDD6"))
    c.drawString(M, 17, "hello@bluewright.com  ·  bluewright.com")
    c.drawRightString(W - M, 30, "Lisbon & Madrid")
    c.drawRightString(W - M, 17, "EN / ES / FR / PT")
    c.restoreState()


def build():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    doc = BaseDocTemplate(str(OUT), pagesize=A4, leftMargin=M, rightMargin=M, topMargin=0, bottomMargin=0,
                          title="Commercial Engine Assessment — Bluewright", author="Bluewright")
    intro_h = 96
    intro_frame = Frame(M, BODY_TOP - intro_h, W - 2 * M, intro_h, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id="intro")
    col_top = BODY_TOP - intro_h - 8
    col_h = col_top - BODY_BOTTOM
    lf = Frame(M, BODY_BOTTOM, COL_W, col_h, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id="left")
    rf = Frame(M + COL_W + COL_GAP, BODY_BOTTOM, COL_W, col_h, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id="right")
    doc.addPageTemplates([PageTemplate(id="one", frames=[intro_frame, lf, rf], onPage=chrome)])
    story = [P(intro, lede), FrameBreak()] + left + [FrameBreak()] + right
    doc.build(story)
    print("wrote", OUT)


if __name__ == "__main__":
    build()
