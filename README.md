# English Ladder

English Ladder is a self-updating ESL website that publishes a daily news lesson at three difficulty levels:

- Beginner: CEFR A1-A2
- Intermediate: CEFR B1-B2
- Advanced: CEFR C1-Higher

Each level keeps a rolling 14-day view; `news/YYYY-MM-DD/LEVEL.html` provides dated lesson addresses and `archive.html` provides search across the last 50 calendar days (today plus the previous 49 fixed-EST dates). Older daily news editions and their public pages, illustrations, and associated translation caches are removed daily. Evergreen stories, grammar, and work courses are unaffected. Every daily run uses the same news story at three reading levels. All pages share an editorial design with warm white surfaces, a white sticky menu, charcoal text, blue brand details, and compact controls. Leveled reading lessons use yellow, green, or blue action buttons to match the selected level. Callouts, vocabulary highlights, definitions, and practice panels share matching pale surfaces and readable dark accents.

Discover features the latest complete daily news lesson, its actual publication date, and a matching AI-generated conceptual illustration. Its level selector links to that same dated lesson at all three levels. It never labels an older lesson as today's story or selects future-dated or incomplete archives. Two evergreen stories (city trees and a fictional market conversation) remain below the main feature, each with three reading levels. Photography and generated illustrations are served locally; their different origins are explained in `photo-credits.html`.

## Guided lessons

The [8 October teaching-quality review](docs/teaching-quality-2026-10-08.md) records corrections to the latest seven news editions, sentence feedback, diagnostic explanations, and existing learning interactions. Its review history distinguishes the current editorial revisions from earlier model approvals.

Story titles aim for **10 words or fewer**. This is a soft editing target, not a word-count rejection rule: a slightly longer title is allowed when an essential name or qualification improves clarity or accuracy. The writer, response schema, and independent reviewer receive the same guidance. Titles omit proficiency labels and padded lesson-analysis subtitles; they are never automatically truncated. Existing title copyedits are recorded separately from the original lesson reviews.

Vocabulary boxes offer English, Japanese, Korean, Simplified Chinese, Spanish, Brazilian Portuguese, French, and German definitions. The English terms and grammar labels stay visible. Language buttons use the lesson palette, update inline word-help definitions too, and remember only the chosen language. The daily producer creates the seven translations in one ChatGPT-plan session and edits them in a separate session before `plan_daily.py` validates and saves them in `data/vocabulary-translations/`. Page rebuilds and student clicks make no AI calls. Missing, damaged, unreviewed, or outdated translations fall back to English with an explicit message. Each run resumes missing translations for the latest three editions without a paid API fallback. See the translation directory README for offline coverage and validation commands.

Everyday English in the US uses that same language preference. An eight-button selector replaces How to Study, with English only plus the seven explanation languages. It controls all 24 unit sidebars and the ready-to-copy AI prompts; the English practice remains unchanged. `us_life_translations.py` prepares and separately edits the explanations with Gemini, and `us_life_language_ui.py` embeds only reviewed records into the page during offline rebuilding. This is a separate manual workflow with a cumulative $2 budget per spending key; it no longer fills daily-news vocabulary records. Normal publishing and student language changes incur no Gemini charges. Original Japanese/Mandarin preferences migrate to the shared setting without replacing a newer preference. Missing translations show an explicit message rather than a different foreign language.

Each Everyday English unit contains **15 useful expressions and 12 vocabulary terms**, authored in `content/us-life.json`. `us_life_content.py` republishes them during the ordinary page rebuild. Every vocabulary term has a direct MP3 link and an optional inline player. Recordings are requested only when selected, never autoplay on arrival, and stop when the learner changes units. Repeated terms share one file. AI practice prompts use the expanded vocabulary without copying audio-control labels.

Pronunciations are generated once with Google's cloud text-to-speech service (Gemini TTS, Kore, American English), compressed to MP3, and committed under `assets/audio/us-life/`. No local/system voice synthesis is used. The manual **Translate Everyday English explanations** workflow accepts `include_audio=true` and `review_audio=true`; it does not run speech generation during the daily cron job. An optional `audio_limit` prepares a small pilot; `audio_model` selects the Google speech model while retaining valid recordings from earlier models. The converter accepts both validated PCM and WAV speech responses. The default prepares eight-term word lists with Gemini 3.8 Flash-Lite TTS, then separates them only at checked silent boundaries. Spoken text and delivery instructions use separate fields, following Google's [speech-generation format](https://ai.google.dev/gemini-api/docs/speech-generation). This path calls the documented REST endpoint because the pinned daily-generation SDK predates the new speech fields. Its spending reserve uses the higher published 2027 price, rather than relying on the temporary 2026 discount. Each extracted file must pass the independent transcript check. This reduces daily request usage; individual mode remains available for small corrections. Rate-limit cooldowns pause the whole request pool, and a reported daily quota stops further retries. Preview-model request errors receive bounded retries without silently changing models. Keep the same `budget_key` when resuming: generation and independent transcription share a cumulative $2 audio cap, separate from the $2 sidebar cap. Failed requests retain their spending reservations. The workflow saves completed files, review results, and spending records even after a partial failure. Work on a branch until all recordings and explanations pass; then rebuild the page and publish. Google rate limits and generation latency can slow preparation; reuse the same spending key and saved checkpoints when resuming. Listening uses saved files and makes no paid AI requests.

Check a completed Everyday English update without paid calls:

```sh
python3 us_life_audio.py --check
python3 us_life_audio_review.py --check
python3 us_life_translations.py --check
python3 -m unittest discover -s tests -p 'test_us_life_content.py'
node --test tests/us-life-audio.test.cjs tests/us-life-languages.test.cjs
```

Audio reviews transcribe the clips without being given their expected text. A mismatch, unclear recording, or extra narration needs review before publishing; never change a failed review to passed without checking the recording. The review is tied to the exact file hash, so replacing a recording invalidates its old review. Translation contexts include the expanded English lesson but exclude playback controls. After editing lesson text, refresh the sidebar translations before rebuilding the final page.

`learning.js` adds Read → Practice → Discuss steps, vocabulary definitions that open when selected, quiz progress, and a completion message. Each lesson opens directly with its story. Share your ideas contains six speaking activities: two story questions followed by level-specific vocabulary, grammar, role-play, and follow-up activities using the lesson’s own words and grammar example. The discussion writing box and its notes message have been removed. Grammar selections remain on the current page. The general browser-saving feature and its saved-word/history controls have been removed; `site.js` never reads or writes those retired learning records. Selecting Finish lesson now saves only a completion flag for that story and level in this browser. Circular yellow, green, and blue checkmarks identify all completed levels for the story in the dated feed and archive, regardless of the level currently open. The Completed button stays active: select it again to mark only that level unfinished; the other levels remain marked. Feed and permanent news URLs share the same marker; evergreen stories use separate keys. Markers survive return visits, refresh across open tabs, and stay on the current page if browser storage is blocked. No answers or notes are included, and markers do not sync between browsers or devices. `continue.html` provides a guided review activity with a complete AI prompt. Work courses keep answers and lesson position only while the page is open; they do not save drafts or completion records. No writing is transmitted or automatically graded. Without JavaScript, all reading, vocabulary, questions, and discussion prompts remain visible.

`editorial.py` builds the homepage and six curated lesson pages, and applies shared navigation, design, and accessible labels to the library. `site_quality.py` builds permanent news pages, the searchable archive, About, Privacy, guided review, a 404 page, search metadata, and the sitemap. The daily and library generators call these helpers so later updates retain the redesign. `story_lessons.py` contains the curated lesson content and source references.

To rebuild without paid calls:

```bash
npm run build
npm run check:js
npm test
```

Tests cover content consistency, local links and anchors across every page, news selection, and learning interactions using a simulated document environment. They do not substitute for browser layout testing.

## English for Work

The directory at `efsp.html` links to 80 courses containing 640 authored workplace lessons and 80 consolidated learner books. Every web lesson includes relevant vocabulary, structured language checks with explanations, three collapsed ten-turn conversations, and supported speaking scenarios. Activities use supplied cases and language choices rather than open-ended writing. Individual profession illustrations appear in the directory, page headings, sticky lesson menus, and PDF covers; the directory places all 80 illustrations in equal cells in an 8-column, 10-row grid.

`content/work/courses.json`, `content/work/cases.txt`, and `content/work/glossary.txt` store the original 41-course inventory, cases, and definitions. Each file in `content/work/occupations/` authors one complete occupation course, including its cases, definitions, workshops, collocations, conversations, speaking scenarios, and occupational references. `work_occupations.py` validates those sources against the explicit 25-course inventory. `work_medical.py` supplies six medical courses and `work_specialists.py` supplies eight further specialist courses from their book sources, with separate short conversations in `books/*_short.py`. `work_curriculum.py` combines these collections for publication. The culture course focuses on individual preferences, inclusive participation, and observable behavior rather than national stereotypes.

`generate_efsp_web_pages.py` publishes the complete lessons as readable HTML. `work.js` adds course and vocabulary search, answer feedback, and lesson navigation. Course answers and lesson position are not saved; nothing is sent to a grading service. The materials remain readable without JavaScript.

`generate_work_documents.py` publishes one complete learner book per course through `work_books.py`. Each expanded 114-page book contains eleven original 20-turn cloze conversations, eleven short transfer exchanges, 192 vocabulary entries and collocations, 128 reusable phrases, structured practice, and explained answer keys. The eight web-aligned lessons are followed by three additional workplace scenarios. All fonts are embedded, with licensed Bitstream Vera files in `assets/fonts`. The approved PDFs in `output/pdf/` are copied unchanged to `pdf/efsp/`; their hashes and content, including the additional dialogues, are verified before publication. The former four-guide PDFs and duplicate asset copies have been removed. Earlier PDF generator command-line entry points now publish the consolidated books instead of restoring the retired guides. See `books/AUDIT-2026-10.md` for the field-by-field editorial review and run `python3 audit_work_books.py` for structural checks.

To rebuild the complete work-course edition locally, without paid services:

```bash
python3 -m pip install -r requirements-documents.txt
python3 generate_work_documents.py
python3 generate_efsp_web_pages.py
python3 audit_work_documents.py
npm test
npm run check:js
```

The learner-book sources live in `books/`. After editing them, rebuild leadership with `python3 build_leadership_book.py` or another course with `python3 build_industry_books.py COURSE-SLUG`, review the PDF, and run the publication commands above. The older dialogue collection remains available as website AI-practice context in `content/work/dialogues/` and the occupation course sources; it is not the new book edition. Legacy `--kind` options publish the complete book, not a separate guide.

Every course also includes four carefully scripted AI practice goals on its webpage, with 640 lesson contexts and 680 dialogue contexts available. Students can copy or save a complete prompt for their own AI service; no service is called and learner drafts are never added automatically. These prompts remain on the website rather than in the consolidated learner books. The occupation courses use supported choices and speaking for vocabulary and grammar practice. `work_ai_prompts.py` is the shared prompt source, and `work-ai.js` handles local selection and copying. Regenerate course pages after editing that source. See [the original placement and prompt-design review](docs/ai-practice-extensions-2026-09-06.md).

`--course manufacturing` (repeatable) publishes selected completed books after a local revision. Rebuild and review affected books before republishing shared content changes. `content/work/documents.json` records the page counts, file checksums, and curriculum checksum; tests reject stale PDFs. The PDF audit checks every page for embedded fonts, text outside the content area, replacement glyphs, missing bookmarks, and leftover filler. Render representative pages as images and review the actual browser layout as well.

The courses provide intermediate-to-advanced language practice. Suggested B1, B2, and C1 adaptations are teaching guidance, not certified level ratings. Regulated and safety-related courses distinguish fictional communication practice from actual professional procedures.

See the [25-occupation expansion review](docs/occupation-expansion-2026-09-28.md) for content coverage, illustrations, editorial corrections, and release checks.

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

- `.agents/skills/english-ladder-daily-producer/SKILL.md`
  Defines the sole daily producer. A daylight-saving-aware local Codex task requests starts at `22:30`, `23:30`, and `00:30 America/New_York`. The 22:30 start targets the following New York calendar date; both recovery opportunities remain pinned to that edition across midnight. It uses the supported local checkout mode because this static site is too large to duplicate safely with the Mac's current free space. It resumes recognized current-date artifacts and stops when it finds unrelated checkout changes. Later attempts resume missing stages and exit without changes when the complete edition is already live. The Mac and ChatGPT app must be awake, running, and signed in.

- `.github/workflows/cron.yml`
  Runs offline tests, audits, and deployment verification after a push. It has no schedule, model credential, lesson-generation path, translation-generation path, or image-generation path.

  An [independent monitor](docs/daily-recovery.md) on Phil's Mac checks every 15 minutes. From 01:00 America/New_York it records `needs_attention` when the saved or public edition is missing. It never dispatches generation or changes remote state.

- `plan_daily_runner.py` and `plan_daily.py`
  Rotate the BBC feeds through the existing source selector, invoke fresh ChatGPT-authenticated Codex sessions for writing and independent review, validate every imported artifact, and rebuild the three rolling level pages plus the homepage. Common model API-key variables are removed from every Codex subprocess.
  A per-edition lock serializes model/build work, and a persistent handoff blocks later opportunities until the first task verifies publication. Valid lesson drafts resume at review, and saved translation and image stages are imported rather than regenerated after an operational interruption.

- `requirements.txt`
  Pins the runtime dependencies used by GitHub Actions.

- `tests/test_update_site.py`
  Covers lesson validation, summary parsing, duplicate-day replacement, and legacy markup cleanup.

## How the Daily Update Works

Before expensive tests or page rebuilding, `daily_publication.py` checks whether the intended daily edition is complete and already live. The shortcut requires all three saved lessons and pages, a matching illustration, complete reviewed translations for the latest three editions, and live checks of the dated lesson data, homepage, feeds, lesson pages, illustration bytes, and private-path 404s. It reads and hashes only those files; it does not render or package the site. A missing component or inconclusive live check keeps recovery enabled. Archive cleanup and final hosting verification still run; an intentional generation skip does not send a failure alert.

Use the manual **verify_only** option to run the tests and this live check without rebuilding, generation, or email. It fails if the complete edition cannot be verified and never falls through to generation.

1. The local scheduled Codex task reads the repository skill and checks for an already complete live edition.
2. `plan_daily.py` chooses a new BBC article from the day's topic feed and saves the source before any model work.
3. Separate ChatGPT-authenticated Codex sessions create:
   - one beginner lesson
   - one intermediate lesson
   - one advanced lesson
   - two story-specific discussion prompts within each lesson, using the same three requests; the offline publisher adds four scripted, level-specific speaking activities to every existing and future lesson
4. The script retrieves the linked article as well as the feed summary, trying another candidate if there is insufficient accessible article text. It requires an exact evidence excerpt for every reading sentence. Grammar examples are copied from the reading by sentence index. A separate Codex session checks factual support, question correctness, grammar, repetition, and level suitability. Failure produces concrete feedback for a bounded revision; a failed review is never published. Each level has at most three attempts in one scheduled run, with resumable state retained for the later daily attempts. All three levels must pass before public pages change. Daily readings, vocabulary, and quizzes must contain at least **6 items for Beginner, 8 for Intermediate, and 10 for Advanced**. The schemas, local validators, independent review, archive writer, rebuild preflight, and hosting audit enforce the requirements.
5. The validated structured lesson data for all three levels is written to `archive/lessons/YYYY-MM-DD.json`.
6. The rolling level pages show up to 14 editions. The searchable archive retains only the last 50 calendar days. Each final refresh prunes expired source records, public lesson pages, dated images, and provably associated translation caches before rebuilding feeds and search listings. Git history retains earlier versions for recovery.
7. A separate plan-authenticated image session uses ChatGPT's built-in image tool. `daily_images.import_daily_image` validates and compresses the result to WebP. Metadata records the provider, ChatGPT surface, the exact model when exposed (otherwise that it was not exposed), prompt, story fingerprint, dimensions, output checksum, source checksum, and attempt count. The same illustration accompanies all three level choices on Discover, labeled as AI-generated and not a news photograph.
8. The scheduled task commits and pushes the checked files. GitHub Actions then runs only offline tests, the audit, and deployment verification. Conflicting concurrent source edits fail for review instead of being overwritten.

### Final-attempt monitoring

The production cycle starts at 22:30 New York time for the following local date. Recovery starts at 23:30 and 00:30 for that same edition. From 01:00 New York time, the independent macOS monitor records `needs_attention` if the complete saved edition, seven-language translations, or matching image is absent or has not reached the public site after its publication grace period. A held local producer lock is reported as `producer_running` instead of a false failure. The monitor is deliberately read-only: it never starts generation, repeats model calls, or dispatches a GitHub workflow. The scheduled Codex task's run record and the offline GitHub publication check provide the diagnostics.

The offline workflow retains a manual **test_email** connection check for the existing Gmail SMTP configuration. It is not an automatic daily-generation trigger or failure-recovery mechanism. `python failure_alert.py --test --dry-run` previews that setup message without network calls.

To preview cleanup without changing files, run `python lesson_retention.py --json`. Use `python update_site.py --refresh-pages` to apply cleanup and rebuild the site without paid AI calls. Do not publish after using the source-only `lesson_retention.py --apply` command until pages and search files have been rebuilt and audited.

### Language and register for future daily lessons

The writer and independent reviewer share the versioned policy in `lesson_levels.py`. It applies to titles, readings, vocabulary selection and definitions, grammar explanations, questions, all answer choices, feedback, and discussion prompts.

| Level | Vocabulary and register | Learning focus |
| --- | --- | --- |
| Beginner · A1–A2 | Common, reusable words and short expressions; neutral everyday English for teen and adult learners. Essential news terms get simple explanations. | Clear details, basic contextual meaning and accessible grammar practice. |
| Intermediate · B1–B2 | Broader general news and work vocabulary, useful word combinations, and manageable abstract terms; natural connected prose with explained tone differences. | Relationships between details, causes, comparisons, common word partnerships and grammar application. |
| Advanced · C1+ | Precise terms, contextual meanings, connotations and register distinctions; polished natural language suited to the audience. | Supported inference, qualification, stance, subtle meaning and appropriate language choices. |

These are English Ladder’s teaching policies, informed by the Council of Europe’s [CEFR Companion Volume](https://rm.coe.int/cefr-companion-volume-with-new-descriptors-2020/16809ea0d4), especially vocabulary range and sociolinguistic appropriateness. CEFR means Common European Framework of Reference for Languages. The policy uses context and teaching judgement; it is not a certified assessment or a fixed word-level lookup. Advanced language should remain natural, and beginner language should respect adult learners. Definitions must make a term easier to understand. The three vocabulary target lists must be separate within each daily edition. Beginner targets are reserved before Intermediate is drafted; both lists are reserved before Advanced is drafted. Natural words may recur in the readings, but a taught target cannot be borrowed by another level. Local checks catch exact reuse, ordinary inflections, common derivatives, spelling variants and reused teaching words inside different phrases; the independent reviewer also checks semantic variants and level suitability. The archive writer, rebuild preflight and final hosting audit enforce separation, including for historical editions. Common grammatical words inside otherwise different phrases are allowed. This rule applies between levels of the same edition; useful vocabulary may recur on later dates for practice.

The review also tries to justify each incorrect option before approving a quiz, rejects unsupported personality inferences, and checks that B1–B2 readings are not dominated by dense quotations or ornate entertainment-review vocabulary. Concise original paraphrases and useful target words matter more than simply making higher levels longer. These instructions improve the review contract but do not guarantee that a model will judge every lesson correctly.

The existing separate review request must return an explicit decision and a reason for **vocabulary, register, teaching language, and challenge**. A missing, malformed or failed assessment blocks approval even when the reviewer reports an overall pass. Real lesson defects feed into the bounded revision process, while temporary reviewer failures retain the same draft for review. Successful future lessons retain the policy version, target level and four assessments in their archive record. Existing historical lessons are not retroactively marked as passing this new review. Tests use synthetic reviewer responses without paid generation; they verify policy delivery, rejection, revision and retained records, not the model’s ability to judge every real language choice correctly.

Push-triggered GitHub runs are offline-only and never call a model. Scheduled and manual plan runs preserve a completed edition and resume missing stages from ignored `.daily-agent/YYYY-MM-DD/` state. Reuse requires unchanged generation policy and a matching approval for the exact source, content, level, and vocabulary reservations.

Generation, independent review, translations, multilingual editing, and the daily illustration use ChatGPT plan allowance or credits through Codex sign-in. There is no paid-API fallback. Offline tests, page rebuilding, and reuse of completed artifacts do not consume model allowance. Bounded attempts prevent accidental repeated work but are not a guarantee of plan capacity.

Later requested starts fetch current `main`, see artifacts saved by an earlier attempt, and never regenerate a complete date's lesson text. Saved images are checked against the story, dimensions, path, and checksum before reuse. To recover a missing stage, run `.venv/bin/python plan_daily_runner.py --date YYYY-MM-DD`; it resumes rather than replacing complete stages. A successful build records `publication-pending.json`; later tasks stop until the publishing owner verifies the live edition and runs `--finish-publication`. The runner stops before model work when less than 512 MiB is free. Ordinary `.venv/bin/python editorial.py` and page rebuilding remain offline.

## Optional AI practice extensions

`ai-practice.html` explains how to use the prompt extensions available throughout the curriculum. Each grammar lesson, workplace case and glossary, daily or evergreen reading, everyday-life unit, and study tool includes copyable prompts. The guided review page also provides a retrieval-practice starter. The 252 grammar and workplace PDF guides include complete prompts matched to their teaching purpose and direct links to the corresponding web extensions.

`ai_extensions.py` contains the authored teaching instructions and builds the prompts from the published lesson context. It runs locally without calling an AI service. `site_quality.py` applies these extensions during publication, including scheduled daily lessons. Rebuilding replaces old prompt blocks rather than retaining outdated context. `ai-practice.js` copies the selected visible prompt and offers manual text selection if clipboard access fails; it never reads drafts, recordings, saved answers, or account information.

The grammar and general-study prompts specify one question at a time, three answer choices, feedback tied to the selected option, retry handling, and a short transfer activity. The workplace chooser also supports original conversations, writing feedback, complete new scripts, and classroom adaptations. Vocabulary practice includes natural word partnerships and contextual contrasts. Dialogue practice branches from the learner's choices. Reading practice separates evidence, inference, missing information, and clearly labeled fictional extensions. Workplace prompts preserve case facts and remain language practice. Pronunciation prompts do not pretend to assess audio they have not heard. Teacher prompts produce classroom materials with separate answer keys.

AI responses still depend on the student's chosen service. The site does not claim that a prompt guarantees accuracy, diagnose a certified level, upload learner work, or require an AI account to use the curriculum. Students can inspect the complete text before copying it and use the regular lessons without these optional extensions.

When changing the prompt source, rebuild the web pages and both PDF collections. The workplace PDF manifest records the workplace prompt source checksum. Run the regular tests and the document audit; the AI extension tests cover curriculum-wide placement, lesson context, fresh daily publishing, repeatable builds, exclusion of private writing, exact copied text, and clipboard fallback.

## Local Run

Use the signed-in Codex plan runner:

```bash
.venv/bin/python plan_daily_runner.py --date YYYY-MM-DD
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

### Private student portal

The separate `englishladder-students` Worker serves student subdomains, starting with `kh26.englishladder.com`. It provides case-insensitive student/teacher sign-in and a responsive dashboard with empty assessment, session-summary, and feedback sections. Credentials and student names are Cloudflare secrets, never public assets. The public lesson site's publishing remains independent. See [student portal setup, checks, and publishing](student-portal/README.md).

Cloudflare Web Analytics uses **Automatic setup** for the public domain. Cloudflare injects the beacon as pages are served; do not embed it in HTML or page generators. The earlier manual analytics record is retained for historical traffic, while new visits appear in the automatic record.

Cloudflare Workers Static Assets serves `englishladder.com`. Namecheap remains the registrar, GitHub stores the source, and the local scheduled Codex task creates lessons. GitHub Actions performs offline checks and publishing verification only. Static hosting adds $0/month at the current scale; ChatGPT plan allowance and domain renewals remain separate.

Cloudflare's existing GitHub integration builds the `main` branch using `npm run deploy:cloudflare`. The deployment wrapper uses the exact Wrangler version in `package-lock.json`, runs JavaScript and site/search checks once, then `cloudflare/build.cjs` copies only public assets into ignored `.cf-site/`. `audit_site.py` already includes the full search audit, so publishing does not run `audit_seo.py` a second time. Preflight has a seven-minute limit and logs its elapsed time; the publishing verifier allows fifteen minutes for the build and upload. Failed uploads retry the same prepared files up to three times, with 10- and 30-second waits and a two-minute limit per upload attempt. Failed preflight checks stop before uploading. Every HTML/CSS local reference is checked against the upload. Python sources, project notes, credentials, tests, and dependencies are excluded. All current `.html`, PDF, image, prompt-text, sitemap, and lesson-data addresses are preserved.

The scheduled task saves checked lessons to GitHub before Cloudflare builds them. The push-triggered offline workflow checks out that exact commit, waits for the complete deployed file manifest, then verifies the current lesson archive, the three lesson pages, the three level feeds, the homepage/root mapping, and private-file 404 responses. The Cloudflare preview check is the blocking deployment gate; the main-domain check uses the same verifier but treats a Cloudflare 403 to the GitHub runner as a warning, since that is edge protection rather than evidence of stale lesson content. A failed publishing check can be rerun without lesson, translation, image, or page generation. It retains expected/live revisions, file differences, and verification logs as a 14-day workflow artifact. See [Publishing recovery](docs/publishing-recovery.md) for Cloudflare settings and recovery steps.

```sh
node cloudflare/build.cjs
node cloudflare/verify-current-lesson.cjs https://englishladder.philstilwell.workers.dev
ALLOW_PUBLIC_EDGE_BLOCK=1 node cloudflare/verify-current-lesson.cjs https://englishladder.com
```

Preview addresses carry `X-Robots-Tag: noindex, nofollow`. The public domain keeps its authored indexing policy. Missing pages return a real 404; browser caches revalidate files so lessons and scripts stay current. Work courses remove retired draft and progress records without reading their contents or changing other site preferences. `deployment.json` lists only the deployed source revision and public-file fingerprints.

Cloudflare retains previous Worker versions for rollback. Keep the existing GitHub Pages deployment available during domain migration; the previous Namecheap DNS points to GitHub's four apex A addresses (`185.199.108.153` through `185.199.111.153`) and `www` points to `philstilwell.github.io`. Check the intended origin before restoring DNS.

## Reviewed grammar and site validation

`content/grammar-curriculum.json` is the authoritative teaching source for all 44 concepts. `grammar_curriculum.py` includes the original numbered graphic from `assets/grammar-concepts/` in each of the 44 lessons, with an enlarged view, a full-resolution link, and matching directory previews. It also builds readable comparison cards, explanations, three multiple-choice checks, a multiple-choice application activity, and the searchable directory. The build requires every original graphic; the site audit rejects missing or mismatched graphics. `grammar_documents.py` builds the 88 matching PDF editions at their established URLs. The former grammar generator entry points delegate to these builders, so rebuilding keeps both the reviewed teaching text and the original graphics.

The PDFs use embedded licensed fonts and bookmarks. They do not claim tagged-PDF conformance; the HTML provides readable equivalents. The comparison cards keep the explanations available as selectable text alongside the original graphics in the web lessons.

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

`news_quality.py` adds a separate automated editorial gate; it is a safeguard, not proof of truth. Source evidence, release dates, available source publication dates, and retrieval dates are retained separately. Older permanent archive pages clearly identify editions that have not received the new editorial review. The latest seven releases were revised against their stored evidence on September 6, then expanded against their linked full articles on September 7 to meet the 6/8/10 minimums. The expansion records editor-written factual notes and retains the earlier review history. All 64 daily editions also received expanded vocabulary lists on September 7, with 618 additional items. A subsequent review replaced 602 targets (293 Intermediate and 309 Advanced) to separate the level lists, corrected contextual definitions and word classes, and preserved the 6/8/10 counts. The per-edition `vocabulary_separation_review` records this work without claiming a paid independent review. See [the vocabulary and generation repair notes](docs/daily-vocabulary-and-repairs-2026-09-07.md). The latest seven editions also received 84 additional quiz questions on September 7, bringing all 192 daily lessons to the 6/8/10 quiz minimums. Existing evergreen practice stories keep their separate six-sentence, three-item vocabulary and five-question format. The existing climate-and-aviation illustration was visually reviewed and reused for the corrected version of the same story, with that decision recorded in its metadata.

The practice text tools provide contextual suggestions and edited sample comparisons. Custom text is preserved rather than silently rewritten. Audio recording chooses a supported format, releases the microphone on errors or navigation, and removes obsolete playback URLs; no new produced audio or paid imagery was added in this edition.

### Grammar answers are multiple choice

All 44 grammar lessons now use four multiple-choice activities each (176 in total). Every option has its own explanation; selecting an incorrect option cannot display generic model feedback as if the written answer had been checked. There are no grammar text-answer fields, including in the application activity. Completion requires all four current selections to be correct. Answers and feedback apply to the current page only; previous browser records are not restored or used for grading.

The 88 corresponding PDFs use the same choices and answer keys. Keep questions, options, correctness flags, and feedback together in `content/grammar-curriculum.json`; the loader and site audit reject missing or ambiguous answer-key structures. Editorial review is still needed to ensure only one offered choice fits the actual language and context. `tests/grammar-choices.test.cjs` covers the reported could/will case, attempts versus successful results, all 528 choice interactions, completion, and fresh attempts without restoring or saving choices.

## Search publishing and complete work prompts

Every indexable page has a distinct title and description, canonical address, sharing metadata, and structured data appropriate to its actual content. Six professional subject pages and `sitemap.html` provide ordinary links through the curriculum. `sitemap.xml` points to five maps covering HTML lessons and PDFs. `content/seo-index.json` preserves modification dates across unchanged rebuilds; keep it in version control.

Run `python3 seo.py` to refresh search metadata and discovery pages, or use the normal editorial build. `python3 audit_seo.py` verifies metadata, structured-data references, indexing policy, category coverage, reachability, and the complete sitemap inventory. The publishing workflow runs it before saving generated pages.

`python3 generate_efsp_web_pages.py` also publishes complete prompts beneath each work lesson and for every Conversation Lab dialogue. The 80 downloadable collections in `prompts/work/` contain 3,920 fully assembled prompts with their actual reference material. `work_ready_prompts.py` handles this presentation without changing the shared PDF prompt source. Read the [September 6 audit and maintenance notes](docs/seo-improvements-2026-09-06.md) for the earlier scope, checks, and remaining search-performance measurements.

`seo_lessons.py` supplies existing credited lesson imagery, the related-grammar map, and content fingerprints that ignore elapsed-age labels and runtime status text. News search titles include their release date so future stories can reuse a headline without duplicating metadata. The final sitemap pass synchronizes page modification dates and includes lesson images in the XML maps.

During a DNS handover, the verifier accepts an optional third argument containing the new server IP address. This bypasses old DNS cache entries for the check while still validating the real domain’s HTTPS certificate. Normal daily checks use public DNS.

The September 8 audit and prioritized next steps are recorded in [the site audit](docs/full-site-audit-2026-09-08.md). `node audit_browser.cjs` checks every published page at four screen widths against a running local preview; `python3 audit_documents.py` writes a dated font and page-boundary report. Original grammar graphics 07, 16 and 28 retain visible corrections in both their page and enlarged views.

### Reading-page stability

Dated lesson links open during parsing, and the publisher includes the reading controls before deferred scripts enable them. This prevents large load-time jumps while keeping the full lesson available without JavaScript. See [the September 15 layout-shift review](docs/layout-shift-fix-2026-09-15.md) for measurements and the repeatable browser audit.

### Paused accounts and deletion

On the private administrator page, paused students appear in a closed section below the main list. Searching or choosing the paused filter opens matching accounts.

Each saved account has a Delete student account button. Its confirmation window names the student, explains the permanent changes, and requires the saved student ID (or full name for drafts without an address). Cancellation leaves records unchanged. Only an administrator session on `phil.englishladder.com` can submit deletion; student sessions, other hosts, stale revisions, and mismatched confirmation are rejected.

Deletion first closes the site and stops automatic updates, then removes the private profile, password, feedback, assessments, quizzes, and quiz history. Original Zoom transcripts and spreadsheet rows remain unchanged. A failed cleanup leaves a paused “Deletion pending” account that can be retried. Minimal deletion receipts, retired addresses, and import fingerprints prevent duplicate requests, delayed publishing, and future spreadsheet imports from restoring a deleted account. Retired student addresses cannot be reused. All destructive verification uses fictional accounts in the automated tests.
