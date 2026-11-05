# Kickoff — paste this into Claude Code on the first run

Open a terminal in this folder and run `claude`. Then paste:

---

> Read `CLAUDE.md`, then `brand/brand-book.md`, `strategy/positioning.md` and `ops/backlog.md`. Don't summarize them back to me — just confirm in three lines what this project is, what's already decided, and what you think the single highest-value next task is. Then wait for me.

---

## Prompts for the tasks that are actually next

Use these one at a time — each is written to be pasted as-is.

**Finish the case studies** (after you've filled the `[FILL]` blocks)
> I've filled the `[FILL]` markers in `strategy/case-studies.md`. Polish the three cases into final English versions following the brand voice in §6 of the brand book. Keep the context → problem → strategy → execution → process installed → result structure. Then produce a short LinkedIn-post version of each (150–200 words) in `strategy/case-posts.md`. Don't invent any numbers I haven't given you.

**Wire the finished cases into the site**
> Replace the three placeholder case cards in `site/index.html` with the final versions from `strategy/case-studies.md`, and add a case detail section for each. Keep the single-file structure, the tokens, and the existing section rhythm. Show me the diff before writing.

**LinkedIn kit**
> Write `bio/linkedin-kit.md`: a headline (under 220 characters), an About section in the brand voice, the Experience entry for Bluewright, and a spec for the banner image (1584×396) using the brand book's rules. My current LinkedIn About is generic executive language from years ago — this must read as the Bluewright thesis instead.

**Client transition script**
> Write `ops/transition-script.md`: a conversation guide for telling existing Blue Serenity clients about Bluewright. Framing is upgrade, not change — "formalizing what I already do with you". Include the opening, the answers to the three objections you'd expect, and the natural bridge to moving them onto the Advise retainer. One version in English, one in Portuguese.

**Content plan** (only after the site is live)
> Write `ops/content-plan.md`: five or six content pillars derived from the thesis, a fortnightly cadence I can actually sustain solo, and ten specific article titles I'm uniquely qualified to write. Then draft the launch article in full.

**Regenerate a PDF after editing copy**
> The copy in `offers/assessment-onepager.md` changed. Regenerate the PDF with reportlab following `ops/build-notes.md`, keep the layout identical, render it to PNG and check visually that nothing overflowed before you tell me it's done.

## Ground rules worth repeating to Claude if it drifts

- Decisions marked `[DECIDED]` in `strategy/positioning.md` are closed.
- Never fabricate client results or metrics.
- Never register, deploy, publish or send anything — propose, then wait.
