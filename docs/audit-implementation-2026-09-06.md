# English Ladder: audit improvements implemented

6 September 2026 · Implements the audit recorded at revision `fd67384`.

English Ladder retains its cobalt identity, warm white background, compact ladder mark, and editorial photographs. English Road remains green. This release concentrates on dependable teaching, readable materials, useful practice, and continuity between visits.

## What changed

| Area | Delivered improvement |
| --- | --- |
| Grammar | Rewrote all 44 concepts from one maintained curriculum. Each has a practical goal, qualified rules, three readable comparison cards, three response-and-explanation checks, and an original-sentence task. Replaced the old image posters with selectable HTML text. Corrected misleading explanations of **about**, **recently/lately**, **this/that/it**, **by/through**, and other patterns. |
| Grammar downloads | Rebuilt all 88 learner workbooks and teaching guides at their established addresses. White pages, cobalt accents, wrapped headings, writing space, separate model answers, embedded fonts, and bookmarks replace the old branding and clipped text. |
| English for Work | Added a case-specific transfer checkpoint to all 328 cases across 41 courses, strengthened weak multiple-choice alternatives, and put the searchable glossary in a disclosure. Rebuilt all 164 matching PDFs. Clearing saved course work now offers an undo action. |
| Practice tools | Sentence feedback preserves the learner's original wording and explains ambiguous cases. Register practice compares edited examples and preserves custom writing. The grammar diagnostic requires all 10 answers before giving a study plan and does not certify a level. The news practice tool loads a compact data file when needed; if unavailable, it clearly labels a fictional practice scenario. |
| Daily news | Revised August 31–September 6 at all three levels against the evidence already saved with each story. Removed unsupported details, preserved uncertainty, reduced repetitive checks, and added beginner sentence frames. New generation requires exact evidence excerpts and a separate automated review of facts, teaching, answers, and difficulty before any of the three levels is published. |
| Permanent archive | Published 64 dated editions at three levels: 192 permanent lesson pages, plus a searchable archive. Older editions carry a clear review-status note. Permanent pages open directly to the reading. |
| Learning continuity | The chosen level follows the learner across Discover, daily-news navigation, and everyday stories. Level changes retain the story date. Optional browser saving keeps recent lessons, selected words, and writing drafts; notes follow a daily lesson into its permanent archive page. My learning offers word review, export, and clear-with-undo. |
| Finding material | Grammar has topic search, category filters, level guidance, duration, and suggested starting points. Everyday English shows one of its 24 units at a time, supports direct unit links, defaults to English-only explanations, and adds a short speaking/writing activity and next-unit action. |
| Visual and keyboard access | Fixed narrow-screen overflow, long headings, and inconsistent action-button emphasis. Existing diagram dialogs now contain keyboard focus, deactivate the background, close with Escape, and return focus to the opener. |
| Trust and discovery | Added About and corrections, Privacy, a useful missing-page response, descriptions and preferred addresses for search engines, sharing metadata, a sitemap, and robots.txt. |
| Publishing reliability | Daily publishing checks page integrity and reviewed lesson data. A retry carries forward only new source data and images, then rebuilds using the latest templates. It refuses to overwrite a concurrent source correction. Push-triggered builds use existing content and do not call paid generation services. |

The September 6 aviation illustration was visually checked against the corrected story and reused without changing its image bytes. Its metadata records that decision. No new imagery or produced audio was commissioned for this release.

## Verification

- **61 Python tests and 34 JavaScript tests passed**, including semantic tool regressions, independent-review rejection, source-topic notices, source-conflict protection, level routing, optional drafts, cross-page note restoration, vocabulary definitions, undo, and keyboard focus.
- All six browser scripts passed syntax checks. The workflow configuration parsed successfully.
- All **297 HTML pages** passed the local page, metadata, link, and reviewed-content audit.
- Checked all 297 pages at **320, 390, 768, and 1280 pixels**: 1,188 checks. No page-width overflow or failed already-loaded image was found. After opening archive readings by default, repeated all 768 archive checks with the reading content visible; no failures.
- Visually reviewed key phone and desktop pages and tested the reading/practice/discussion flow, grammar search, level links, saved words, restored notes, and clearing temporary learning data in a browser.
- Checked all **252 PDFs, totaling 2,961 pages**, for embedded font resources, bookmarks, and text beyond page edges. No failures. Rendered and visually reviewed representative covers, practice pages, long titles, and teacher pages. The [complete document check](document-validation-2026-09-06.json) lists every PDF and its result.

Published verification: all **297 HTML pages and 267 linked assets**, including every PDF, returned HTTP 200 and matched the tested files byte for byte. Both [Pages deployment](https://github.com/philstilwell/English-Ladder/actions/runs/34059735256) and [the daily publishing workflow](https://github.com/philstilwell/English-Ladder/actions/runs/34059735745) passed for implementation revision `f1e5921`. See the [live-file verification record](live-validation-2026-09-06.json).

The reproducible checks are `npm test`, `npm run check:js`, `python3 audit_site.py`, and `python3 audit_documents.py`. PDF checks require the document dependencies. `python3 update_site.py --refresh-pages` rebuilds existing lessons without paid calls.

## Costs and remaining limits

No paid generation calls were made while implementing or testing this release. The additional daily editorial review is estimated at **$0.01–$0.03 per day**, up to approximately **$0.08 with nine review attempts**, using the published Gemini 2.5 Flash rates. Existing drafting and illustration charges remain separate. See [Google's pricing](https://ai.google.dev/gemini-api/docs/pricing).

The following remain deliberate limits rather than claimed completions:

- **Historical editorial review:** the latest seven dates were revised; the other 57 archived dates were preserved with review-status notices. They have not received the same complete editorial pass.
- **Source depth:** the current generator still starts with saved feed evidence. Short evidence now produces a proportionate reading. Exact excerpts and a separate model review reduce unsupported expansion but do not prove factual accuracy or replace a qualified editor.
- **PDF accessibility:** fonts and bookmarks are fixed, but the PDFs are not tagged and do not contain fillable form fields. Their HTML equivalents remain readable. The checks do not certify accessibility conformance or catch every possible overlap.
- **Audio:** no new model recordings were produced. The existing recorder now selects a supported format, releases microphone tracks after failures/navigation, and disposes of obsolete playback links. Actual microphone capture, iPhone/Safari and Android behavior, and audio quality were not tested. New recorded lessons need a separate production budget and approved voices.
- **Learning evidence:** no proficiency claims, measured learning gains, retention improvements, screen-reader certification, or professional accuracy across every regulated work subject are asserted. Learner trials and measurement remain a next phase; this release does not send written answers or recordings to analytics.
- **Device storage:** saving is optional and specific to a browser/device. Work courses retain separate saving controls. There is no account synchronization or automatic grading of writing.

## Maintaining the improvements

Edit `content/grammar-curriculum.json`, then rebuild its pages and PDF editions together. Edit workplace curriculum and cases, then rebuild the web and downloadable editions together. Keep the new regression and publishing checks in the daily workflow. Corrections to daily stories should update their archived source data and rebuild the rolling and permanent pages; an illustration must still match the corrected story.

The design direction remains shared typography, spacing, controls, and reading layouts across the sister sites, with blue for English Ladder and green for English Road.
