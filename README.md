# English Ladder

English Ladder is a self-updating ESL website that publishes a daily news lesson at three difficulty levels:

- Beginner: CEFR A1-A2
- Intermediate: CEFR B1-B2
- Advanced: CEFR C1-Higher

Each level keeps a rolling 7-day view; `news/YYYY-MM-DD/LEVEL.html` provides permanent lesson addresses and `archive.html` provides search. Every daily run uses the same news story at three reading levels. All pages share an editorial design with warm white surfaces, charcoal text, cobalt controls, and compact level labels.

Discover features the latest complete daily news lesson, its actual publication date, and a matching Gemini illustration. Its level selector links to that same dated lesson at all three levels. It never labels an older lesson as today's story or selects future-dated or incomplete archives. Two evergreen stories (city trees and a fictional market conversation) remain below the main feature, each with three reading levels. Photography and generated illustrations are served locally; their different origins are explained in `photo-credits.html`.

## Guided lessons

`learning.js` adds Read → Practice → Discuss steps, vocabulary definitions that open when selected, quiz progress, and a completion message. Each lesson starts with a prediction question. Optional discussion notes remain on the current page unless the learner enables browser saving. `site.js` then keeps notes, recent lessons, and selected vocabulary on that device only. `continue.html` provides review, export, and recoverable clearing. No writing is transmitted or automatically graded. Without JavaScript, all reading, vocabulary, questions, and discussion prompts remain visible.

`editorial.py` builds the homepage and six curated lesson pages, and applies shared navigation, design, and accessible labels to the library. `site_quality.py` builds permanent news pages, the searchable archive, About, Privacy, My learning, a 404 page, search metadata, and the sitemap. The daily and library generators call these helpers so later updates retain the redesign. `story_lessons.py` contains the curated lesson content and source references.

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

Conversation Labs include 368 complete professional dialogues across all 41 courses, followed by the existing role-play cases. To rebuild only this collection, use `python3 generate_work_documents.py --kind conversation`, then regenerate the course pages. The authored scripts live in `content/work/dialogues/`; `work_dialogues.py` validates them and `audit_conversation_labs.py` checks the finished PDFs. See [the collection review](docs/conversation-lab-expansion-2026-09-06.md) for coverage and validation.

Every course also includes eight carefully scripted AI practice goals, with all 328 lessons and 368 dialogues available as context. Students can copy or save a complete prompt for their own AI service; no service is called and learner drafts are never added automatically. Each of the 164 PDFs includes two printable prompts and links to the relevant online lesson or dialogue. `work_ai_prompts.py` is the shared prompt source, and `work-ai.js` handles local selection and copying. Rebuild all PDFs and course pages after editing that source. See [the placement and prompt-design review](docs/ai-practice-extensions-2026-09-06.md).

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
4. The script validates the structured lesson and requires an exact evidence excerpt for every reading sentence. A separate Gemini call checks factual support, question correctness, grammar, repetition, and level suitability. Failure leads to a bounded revision attempt; a failed review is never published. All three levels must pass before public pages are changed. Readings may have 3-10 sentences, 3-5 vocabulary terms, and 4-6 purposeful questions, rather than padding a short source to ten sentences and questions.
5. The validated structured lesson data for all three levels is written to `archive/lessons/YYYY-MM-DD.json`.
6. Older lessons leave the seven-day view but remain at permanent addresses in the searchable archive.
7. `daily_images.py` requests one 4:3 conceptual illustration from `gemini-2.5-flash-image`, compresses it to WebP, and saves the image and its generation record in `assets/news/`. The record includes the prompt, model, story fingerprint, dimensions, checksum, and attempt count. The same illustration accompanies all three level choices on Discover, labeled as AI-generated and not a news photograph.
8. GitHub Actions checks the generated pages, then commits the updated lesson pages, homepage, archives, and images. On a push retry it carries changed source data forward and rebuilds HTML from the newest templates; conflicting concurrent source edits fail for review instead of being overwritten. Deployment verification checks Discover's headline, date, all level links, and the exact image file as well as the daily lesson pages.

Push-triggered runs only rebuild existing content with `--refresh-pages`; they never call Gemini. Scheduled runs retain `--skip-existing`, and manual generation remains available. There is now one additional image request per daily story. At Google's published September 6, 2026 rate of approximately $0.039 per image, budget about $1.20 per 30 days plus small prompt charges. The maximum of three attempts per release date bounds image output charges at about $3.60 per 30 days if every attempt were billed. The separate editorial review adds roughly $0.01-$0.03 per day at Gemini 2.5 Flash rates, or up to about $0.08 for nine bounded review calls. Drafting retries can add their existing charges. These are estimates, not a provider billing guarantee. See [Gemini pricing](https://ai.google.dev/gemini-api/docs/pricing#gemini-2.5-flash-image).

Queued runs fetch the latest branch at startup so they see archives and images saved while they were waiting. Scheduled fallback runs never regenerate an existing date's lesson text. They reuse its successful image without another paid call, or retry a missing/failed image once, up to three attempts total per release date. Image failures produce a workflow warning and a useful text preview on Discover, without substituting an unrelated photograph or blocking the lesson. Saved images are checked against the story and file checksum before reuse. After the attempt limit, review `assets/news/YYYY-MM-DD.json` and resolve the provider error before deliberately resetting its attempt count.

To create the first daily feature image (or recover a missing latest image) without regenerating lessons, run the **Daily ESL Lesson Generator** manually with **refresh_feature** enabled. Its command is `python update_site.py --refresh-feature`; it uses the existing `GEMINI_API_KEY` repository secret. Ordinary `python editorial.py` and `npm run build` remain offline. The local checks cover archive rollover, future/incomplete archives, image reuse and failure limits, a changed story on an existing date, escaped markup, no-JavaScript links, and deployment verification.

## Optional AI practice extensions

`ai-practice.html` explains how to use the prompt extensions available throughout the curriculum. Each grammar lesson, workplace case and glossary, daily or evergreen reading, everyday-life unit, and study tool includes copyable prompts. My learning also provides a retrieval-practice starter. The 252 grammar and workplace PDF guides include complete prompts matched to their teaching purpose and direct links to the corresponding web extensions.

`ai_extensions.py` contains the authored teaching instructions and builds the prompts from the published lesson context. It runs locally without calling an AI service. `site_quality.py` applies these extensions during publication, including scheduled daily lessons. Rebuilding replaces old prompt blocks rather than retaining outdated context. `ai-practice.js` copies the selected visible prompt and offers manual text selection if clipboard access fails; it never reads drafts, recordings, saved answers, or account information.

The grammar and general-study prompts specify one question at a time, three answer choices, feedback tied to the selected option, retry handling, and a short transfer activity. The workplace chooser also supports original conversations, writing feedback, complete new scripts, and classroom adaptations. Vocabulary practice includes natural word partnerships and contextual contrasts. Dialogue practice branches from the learner's choices. Reading practice separates evidence, inference, missing information, and clearly labeled fictional extensions. Workplace prompts preserve case facts and remain language practice. Pronunciation prompts do not pretend to assess audio they have not heard. Teacher prompts produce classroom materials with separate answer keys.

AI responses still depend on the student's chosen service. The site does not claim that a prompt guarantees accuracy, diagnose a certified level, upload learner work, or require an AI account to use the curriculum. Students can inspect the complete text before copying it and use the regular lessons without these optional extensions.

When changing the prompt source, rebuild the web pages and both PDF collections. The workplace PDF manifest records the workplace prompt source checksum. Run the regular tests and the document audit; the AI extension tests cover curriculum-wide placement, lesson context, fresh daily publishing, repeatable builds, exclusion of private writing, exact copied text, and clipboard fallback.

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

## Hosting and publishing

Cloudflare Workers Static Assets serves `englishladder.com`. Namecheap remains the registrar, GitHub stores the source, and the existing daily GitHub Actions schedule continues to create lessons. Static hosting adds $0/month at the current scale; existing Gemini generation and domain renewals remain separate.

Cloudflare's existing GitHub integration builds the `main` branch. `wrangler.jsonc` runs JavaScript and site/search checks, then `cloudflare/build.cjs` copies only public assets into ignored `.cf-site/`. Every HTML/CSS local reference is checked against the upload. Python sources, project notes, credentials, tests, and dependencies are excluded. All current `.html`, PDF, image, prompt-text, sitemap, and lesson-data addresses are preserved.

The daily publishing job saves checked lessons to GitHub before Cloudflare builds them. Bot commits intentionally omit `[skip ci]` so Cloudflare receives them; GitHub's own `GITHUB_TOKEN` prevents recursive GitHub Actions runs. The final job waits for the complete deployed file manifest, then verifies every public file byte for byte on both the Cloudflare preview and the main domain. A manual `deploy_only` run checks publishing without generating paid content.

```sh
node cloudflare/build.cjs
node cloudflare/verify.cjs https://englishladder.philstilwell.workers.dev
node cloudflare/verify.cjs https://englishladder.com
```

Preview addresses carry `X-Robots-Tag: noindex, nofollow`. The public domain keeps its authored indexing policy. Missing pages return a real 404; browser caches revalidate files so lessons and scripts stay current. Learner progress stays in the same browser storage on the same public domain. `deployment.json` lists only the deployed source revision and public-file fingerprints.

Cloudflare retains previous Worker versions for rollback. Keep the existing GitHub Pages deployment available during domain migration; the previous Namecheap DNS points to GitHub's four apex A addresses (`185.199.108.153` through `185.199.111.153`) and `www` points to `philstilwell.github.io`. Check the intended origin before restoring DNS.

## Reviewed grammar and site validation

`content/grammar-curriculum.json` is the authoritative teaching source for all 44 concepts. `grammar_curriculum.py` builds readable comparison cards, explanations, three multiple-choice checks, a multiple-choice application activity, and the searchable directory. `grammar_documents.py` builds the 88 matching PDF editions at their established URLs. The former grammar generator entry points delegate to these builders, so rebuilding cannot restore the old WordPress explanations or posters.

The PDFs use embedded licensed fonts and bookmarks. They do not claim tagged-PDF conformance; the HTML provides readable equivalents. The new comparison cards contain actual text and replace the old raster diagrams, avoiding both oversized downloads and text locked in images.

```bash
python3 grammar_curriculum.py
python3 grammar_documents.py
python3 update_site.py --refresh-pages
python3 audit_site.py
python3 audit_documents.py
npm test
npm run check:js
```

PDF generation and validation require `requirements-documents.txt`. All commands above run without paid generation. Review representative rendered PDF pages and the browser interface after changing content or styles. The September 6 implementation checked 297 pages at 320, 390, 768, and 1280 pixels, and all 252 PDFs for font embedding, bookmarks, and text beyond page edges. These checks do not certify complete accessibility or professional subject-matter accuracy.

`news_quality.py` adds a separate automated editorial gate; it is a safeguard, not proof of truth. Source evidence, release dates, available source publication dates, and retrieval dates are retained separately. Older permanent archive pages clearly identify editions that have not received the new editorial review. The latest seven releases were revised against their stored evidence on September 6. The existing climate-and-aviation illustration was visually reviewed and reused for the corrected version of the same story, with that decision recorded in its metadata.

The practice text tools provide contextual suggestions and edited sample comparisons. Custom text is preserved rather than silently rewritten. Audio recording chooses a supported format, releases the microphone on errors or navigation, and removes obsolete playback URLs; no new produced audio or paid imagery was added in this edition.

### Grammar answers are multiple choice

All 44 grammar lessons now use four multiple-choice activities each (176 in total). Every option has its own explanation; selecting an incorrect option cannot display generic model feedback as if the written answer had been checked. There are no grammar text-answer fields, including in the application activity. Completion requires all four current selections to be correct. Optional browser saving restores selected options and their feedback, keyed to the question contents so an edited question cannot inherit a stale answer. Old written drafts are not used for grading.

The 88 corresponding PDFs use the same choices and answer keys. Keep questions, options, correctness flags, and feedback together in `content/grammar-curriculum.json`; the loader and site audit reject missing or ambiguous answer-key structures. Editorial review is still needed to ensure only one offered choice fits the actual language and context. `tests/grammar-choices.test.cjs` covers the reported could/will case, attempts versus successful results, all 528 choice interactions, completion, and saved-choice restoration.

## Search publishing and complete work prompts

Every indexable page has a distinct title and description, canonical address, sharing metadata, and structured data appropriate to its actual content. Six professional subject pages and `sitemap.html` provide ordinary links through the curriculum. `sitemap.xml` points to five maps covering HTML lessons and PDFs. `content/seo-index.json` preserves modification dates across unchanged rebuilds; keep it in version control.

Run `python3 seo.py` to refresh search metadata and discovery pages, or use the normal editorial build. `python3 audit_seo.py` verifies metadata, structured-data references, indexing policy, category coverage, reachability, and the complete sitemap inventory. The publishing workflow runs it before saving generated pages.

`python3 generate_efsp_web_pages.py` also publishes complete prompts beneath each work lesson and for every Conversation Lab dialogue. The 41 downloadable collections in `prompts/work/` contain fully assembled prompts with their actual reference material. `work_ready_prompts.py` handles this presentation without changing the shared PDF prompt source. Read the [September 6 audit and maintenance notes](docs/seo-improvements-2026-09-06.md) for scope, checks, and remaining search-performance measurements.

`seo_lessons.py` supplies existing credited lesson imagery, the related-grammar map, and content fingerprints that ignore elapsed-age labels and runtime status text. News search titles include their release date so future stories can reuse a headline without duplicating metadata. The final sitemap pass synchronizes page modification dates and includes lesson images in the XML maps.

During a DNS handover, the verifier accepts an optional third argument containing the new server IP address. This bypasses old DNS cache entries for the check while still validating the real domain’s HTTPS certificate. Normal daily checks use public DNS.
