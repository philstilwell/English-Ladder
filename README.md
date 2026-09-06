# English Ladder

English Ladder is a self-updating ESL website that publishes a daily news lesson at three difficulty levels:

- Beginner: CEFR A1-A2
- Intermediate: CEFR B1-B2
- Advanced: CEFR C1-Higher

Each level keeps a rolling 7-day archive. Every daily run uses the same news story at three reading levels. All pages share an editorial design with warm white surfaces, charcoal text, cobalt controls, and compact level labels.

The homepage features a short illustrated story, links to the latest daily news at each level, and routes into the existing study library. Two evergreen stories (city trees and a fictional market conversation) each have three distinct reading levels. These are clearly separated from current news. Photography is served locally; sources and reuse details are recorded in `assets/editorial/credits.json` and shown on `photo-credits.html`.

## Guided lessons

`learning.js` adds Read → Practice → Discuss steps, vocabulary definitions that open when selected, quiz progress, and a completion message. Each lesson starts with a prediction question. Optional discussion notes remain in the current page only and are never transmitted or stored. Without JavaScript, all reading, vocabulary, questions, and discussion prompts remain visible.

`editorial.py` builds the homepage and six curated lesson pages, and applies shared navigation, design, and accessible labels to the library. The daily and library generators call these helpers so later updates retain the redesign. `story_lessons.py` contains the curated lesson content and source references.

To rebuild without paid calls:

```bash
npm run build
npm run check:js
npm test
```

Tests cover content consistency, local links and anchors across every page, news selection, and learning interactions using a simulated document environment. They do not substitute for browser layout testing.

## English for Work

The directory at `efsp.html` links to 41 courses containing 328 authored workplace cases and 164 PDFs. Every lesson includes relevant vocabulary, a communication workshop, two language checks with explanations, partner speaking, a written message, a model response, and revision criteria. The 12 shared language workshops recur intentionally across fields for retrieval practice. The cases and model responses are individually authored for each lesson.

`content/work/courses.json` stores the course inventory, lesson topics, vocabulary alignment, and stable download paths. `content/work/cases.txt` contains the 328 original fictional cases and responses. `content/work/glossary.txt` supplies the shared plain-English definitions referenced by the inventory. `work_curriculum.py` combines them with teaching workshops and validates completeness. The culture course now focuses on individual preferences, inclusive participation, and observable behavior rather than national stereotypes.

`generate_efsp_web_pages.py` publishes the complete lessons as readable HTML. `work.js` adds search, answer feedback, word counts, lesson navigation, and optional local draft/progress storage. Saving is off by default; nothing is sent to a grading service. The materials remain readable without JavaScript.

`generate_work_documents.py` publishes four distinct PDFs per course: a teacher's guide, learner workbook, conversation lab, and vocabulary/phrasebook. All fonts are embedded, with licensed Bitstream Vera files in `assets/fonts`. Original download URLs remain valid. Earlier PDF generator command-line entry points now delegate to this shared curriculum, so they cannot silently restore the old published lessons.

To rebuild the complete work-course edition locally, without paid services:

```bash
python3 -m pip install -r requirements-documents.txt
python3 generate_work_documents.py
python3 generate_efsp_web_pages.py
python3 audit_work_documents.py
npm test
npm run check:js
```

`--course manufacturing` (repeatable) limits PDF generation for a local proof. Rebuild the full set before publication after changing shared content. `content/work/documents.json` records the page counts, file checksums, and curriculum checksum; tests reject stale PDFs. The PDF audit checks every page for embedded fonts, text outside the content area, replacement glyphs, missing bookmarks, and leftover filler. Render representative pages as images and review the actual browser layout as well.

The courses provide intermediate-to-advanced language practice. Suggested B1, B2, and C1 adaptations are teaching guidance, not certified level ratings. Regulated and safety-related courses distinguish fictional communication practice from actual professional procedures.

## Site Structure

- `index.html`
  The hub page. Learners choose Beginner, Intermediate, or Advanced from the level selector and can jump into the study library.

- `tools.html`
  A static ESL tools page with diagnostics, sentence repair, pronunciation shadowing, news-skill prompts, workplace phrase coaching, and register practice.

- `beginner.html`
  The beginner archive page for A1-A2 learners.

- `intermediate.html`
  The intermediate archive page for B1-B2 learners.

- `advanced.html`
  The advanced archive page for C1-higher learners.

- `styles.css`
  Existing component styling. `editorial.css`, loaded afterward, defines the shared redesign.

- `app.js`
  Shared quiz interaction for every lesson page.

- `tools.js`
  Client-side behavior for the ESL study tools.

- `archive/lessons/YYYY-MM-DD.json`
  Durable JSON archive files for each generated daily lesson set. Each file stores the source news item, release metadata, model name, and the validated structured lesson data for Beginner, Intermediate, and Advanced.

## Automation

- `.github/workflows/cron.yml`
  Runs the daily automation at `10:00 UTC`, with no-op fallback attempts at `13:00 UTC` and `16:00 UTC` in case GitHub does not assign a hosted runner. It supports manual runs with `workflow_dispatch`, installs pinned dependencies, and runs the test suite before publishing lesson updates.

- `update_site.py`
  Rotates BBC feeds through science (Monday/Sunday), culture (Tuesday/Saturday), technology (Wednesday), business (Thursday), and world news (Friday). It avoids recently used source links and prefers less distressing stories within each feed, falling back to world news if necessary. It requests structured JSON lesson data from Gemini, renders and validates the lessons locally, and updates the three rolling archive pages plus the homepage.

- `requirements.txt`
  Pins the runtime dependencies used by GitHub Actions.

- `tests/test_update_site.py`
  Covers lesson validation, summary parsing, duplicate-day replacement, and legacy markup cleanup.

## How the Daily Update Works

1. GitHub Actions starts the workflow.
2. `update_site.py` chooses a new headline and summary from the day's topic feed.
3. Gemini creates:
   - one beginner lesson
   - one intermediate lesson
   - one advanced lesson
   - a prediction question and two discussion prompts within each lesson, using the same three requests
4. The script validates the JSON lesson data, renders safe HTML from fixed templates, and replaces any same-day lesson instead of creating duplicates.
5. The validated structured lesson data for all three levels is written to `archive/lessons/YYYY-MM-DD.json`.
6. Older lessons beyond the newest 7 are removed from the live lesson pages automatically.
7. GitHub Actions commits the updated lesson pages, homepage, and JSON archive files back to the repository.

Push-triggered runs only rebuild existing content with `--refresh-pages`; they never call Gemini. Scheduled runs retain `--skip-existing`, and manual generation remains available. The redesign adds no paid image or audio service and makes no extra model requests per daily run.

Scheduled fallback runs use `--skip-existing`, so if the primary run already created that date's JSON archive, the fallback exits before calling Gemini and only continues through the live Pages verification.

## Local Run

Set your Gemini API key, then run:

```bash
python3 update_site.py
```

This updates:

- `beginner.html`
- `intermediate.html`
- `advanced.html`
- `archive/lessons/YYYY-MM-DD.json`

To normalize existing lesson markup without calling Gemini:

```bash
python3 update_site.py --refresh-pages
```

## Deployment Notes

- `CNAME`
  Points the site to `englishladder.com`.

The hub page remains the root entry point, and the three lesson pages stay linked from there.
