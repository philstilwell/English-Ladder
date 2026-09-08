# English Ladder: site audit and strategic priorities

8 September 2026 · Baseline revision `425e7a9b` · Corrective release

The site has a coherent visual identity and an extensive curriculum. The most urgent weakness is the reliability of teaching judgments: an automated approval can still admit vocabulary that is too difficult, ambiguous grammar questions, or an inference unsupported by the reading. Keep the current design direction and invest next in editorial calibration, clearer learning routes, and evidence of what students actually find useful.

## Corrections made

| Finding | Correction |
| --- | --- |
| Today’s intermediate lesson contained 243 words, a 42-word sentence, dense entertainment quotations, and an unsuitable cluster of ornate vocabulary. | Rewrote the lesson as connected, accessible reporting with transferable vocabulary. Replaced the dependent grammar explanation, questions, feedback, discussion and generated AI context. |
| Today’s advanced quiz accepted a speculation about a sprinter’s baking temperament and treated another valid participial construction as wrong. It also attributed the lesson writer’s wording to a named critic. | Rewrote the advanced lesson and its checks. Questions now distinguish reported facts, a critic’s view, figurative language and unknown outcomes. The grammar task has a single clear answer. |
| The original graphics for concepts 07, 16 and 28 contradict their corrected teaching text. | Added specific corrections immediately before each retained graphic and inside its enlarged view. Their image files remain unchanged. The publication audit now requires these corrections. Replacing the inaccurate image text remains a recommended next step. |
| Discover’s introductory “daily reading” link always opened Beginner. | It now follows the selected level, like the main navigation and story links. |
| Everyday English’s handling of page anchors could reset a chosen unit when using the skip link. Its introductory material also delays reaching the controls on a phone. | Non-unit anchors retain the current unit. A direct “Choose language and unit” link bypasses the introduction. |
| A language-interaction test required a dated lesson’s translations to exist, contradicting the intended English fallback during translation delays. | The interaction test uses its own translation fixture. A separate regression checks that missing definitions remain English while the AI prompt still honors the selected explanation language. This does not waive translation validation. |
| The publishing workflow named many individual source files but omitted several shared scripts and generators. | Added coverage for all root Python, JavaScript, browser-audit and style files, package manifests and archived lesson data. |
| Refreshing translations after a correction had no dedicated recent-only manual option. | Added `translate_recent`: refresh missing translations for the latest three editions under the existing cumulative $0.30 daily cap, with no new lessons or images. |
| The PDF audit overwrote a report labeled 6 September regardless of when it ran. | Reports now use the actual date, with an optional explicit report date. |

Today’s final English material retains all hard requirements:

| Level | Reading sentences | Vocabulary items | Quiz questions |
| --- | ---: | ---: | ---: |
| Beginner | 6 | 6 | 7 |
| Intermediate | 10 | 8 | 9 |
| Advanced | 12 | 10 | 10 |

The three taught vocabulary lists remain separate. All graded questions are multiple choice. Corrections are recorded honestly as manual editorial work; superseded Gemini approvals and content are retained in history rather than relabeled as new model approvals. The conceptual baking illustration still matches the story and requires no regeneration.

The writer and reviewer now receive more concrete guidance on intermediate vocabulary burden, concise original paraphrases, challenging every answer alternative, and avoiding personality predictions from someone’s occupation, sport or background. These instructions strengthen the process; they are not proof that a model will catch every future defect.

The two revised levels require a fresh Gemini translation-and-editing pass. The estimated cost is $0.05–$0.20, capped at $0.30 for the daily translation ledger. Changed reading invalidates old translations automatically. No other paid generation is needed for this audit.

## What was checked

| Area | Coverage and result |
| --- | --- |
| Page structure and links | All **311 HTML pages** passed the maintained checks for local links, anchors, identifiers, headings, main regions, metadata and required learning components. |
| Search foundations | **309 indexable pages**, each with a unique title and description; all reachable through internal links. Sitemaps cover pages, work, grammar, readings and **252 PDFs**. |
| Responsive layout | **1,244 browser checks**: every page at 320, 390, 768 and 1280 pixels. No page-width overflow, browser script errors or failed already-loaded images with actual source addresses. The first feed lesson was opened; permanent readings are already open. Empty image placeholders in unopened enlargement dialogs are not broken images. |
| Visual review | Reviewed desktop and phone views of Discover, daily news, grammar directory and detail, Everyday English, practice tools and the work directory; visually inspected the three conflicting grammar graphics. |
| Interactions | Browser spot checks of grammar feedback, navigation and Everyday English controls, plus the existing automated coverage of all grammar answer options, all work-course initialization, lesson stages, completion toggles, language changes, prompt copying, fallback behavior and storage failures. |
| Documents | All **252 PDFs / 4,445 pages** checked for embedded fonts, text outside page edges and bookmarks. No structural failures. The PDFs remain untagged. |
| Content | Minimums and vocabulary separation checked across all **66 dated editions / 198 daily lesson versions**. Detailed editorial review of the latest two editions, with corrections to today’s intermediate and advanced material; targeted grammar and workplace/US-life samples. This is not a line-by-line editorial certification of the entire historical archive. |
| Translations and prompts | Reviewed the cache, invalidation, language-selection and prompt-localization mechanisms. Current US-life coverage includes 24 units in five languages. The audit does not claim native-speaker certification of every translation. |
| Automated verification | **231 Python tests + 111 JavaScript tests passed**, together with browser-script syntax checks and page/SEO audits. The translation-only workflow branch was exercised with a harmless local substitute to confirm it cannot invoke lesson or image generation. |
| Publishing | Reviewed the latest 12 daily-workflow runs: 11 succeeded, one earlier manual translation-related run failed. The latest six succeeded. The live manifest at audit start matched baseline revision `425e7a9b`. The configured schedule remains 10:00, 13:00 and 16:00 UTC; actual observed starts were delayed. Scheduled execution should be treated as a window, not a precise publication promise. |

The browser checks block external requests and do not measure real visitor loading times. No microphone recording, iPhone/Safari session, screen-reader certification, learning-gain study or exhaustive external-link check is claimed. Narrow-screen checks support reflow review but do not establish full accessibility compliance. See [W3C’s reflow guidance](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html).

Machine-readable evidence: [browser results](browser-audit-2026-09-08.json) and [PDF results](document-validation-2026-09-08.json). Reproduce locally with `node audit_browser.cjs` while serving the site at `http://127.0.0.1:8878`, or set `AUDIT_ORIGIN`; PDF checks use `python3 audit_documents.py`.

## Recommended next investments

### 1. Make editorial calibration the first priority

Use a small, carefully edited reference set at each level. Review the three versions of a story side by side before accepting the edition. Compare actual reading difficulty, the usefulness of target words, grammar accuracy, and the evidence for every correct answer. A second model call is useful but can repeat the writer’s assumptions.

Start with a weekly human review of recent lessons and a targeted pass through older lessons receiving traffic. Include deliberately flawed examples—two grammatical answers, an unsupported motive, an intermediate list dominated by rare terms—in the editorial evaluation set. Measure how often the process catches these errors before publication. Keep strict numeric minimums, but never use them as a quality score.

**Success measure:** fewer published corrections, a growing set of calibrated examples, and no recurrence of the confirmed quiz and level errors.

### 2. Replace the contradictory graphics, then refresh the remaining visual library

First update concepts 07, 16 and 28 so the image itself agrees with the teaching text. Keep the recognizable visual reference function while replacing overbroad rules, distracting decorative elements and text that is difficult to read on a phone. Review each graphic’s wording before generating its replacement. Use Gemini for new imagery, with an estimate before paid work.

For the other concepts, use consistent typography and a small number of focused examples; pair every image with selectable text. The current correction notes are a practical safeguard, not the ideal permanent presentation.

**Success measure:** every image, webpage and corresponding guide teaches the same qualified rule; students can use the explanation without reading tiny image text.

### 3. Turn the large library into a few clear study routes

The library offers many choices but few sequences. Offer short routes such as “My first week in the US,” “Speak more clearly at work,” and “Build a daily reading habit,” each with a goal, suggested starting point, next activity and approximate time. Keep browsing available.

Test the Everyday English introduction and course controls on phones. The new shortcut helps now; a later layout pass should reduce repeated introductory material and keep language choice close to the unit picker.

**Success measure:** a new learner can choose a relevant first activity within 30 seconds and identify what to do next without returning to Discover.

### 4. Add retrieval and listening before adding more generic AI prompts

Students already have extensive copyable AI support. A more valuable next layer is revisiting previously taught language in new, clearly contextualized questions, with short model dialogues and matching transcripts. Completion circles should remain a record of activity, not a claim of mastery.

Begin with a small pilot using approved recorded voices or human recordings. Give students a clear sequence: listen, check meaning, repeat, then try a variation. Reuse the language support already available. Do not reintroduce saved answers or the retired general browser-saving feature.

**Success measure:** students can recognize and use several target expressions in a new situation on a later visit. Evaluate this with volunteers before expanding the feature.

### 5. Improve accessibility and loading through targeted measurement

Keep HTML as the primary reading format and plan properly tagged PDFs—documents whose headings, paragraphs and reading order are identified for assistive software. Current font and boundary checks do not provide those tags.

Measure actual loading on a modest phone before making architectural changes. Several pages contain roughly 0.5–0.7 MB of uncompressed HTML because they embed complete lessons, language data and repeated prompt context. Consider loading optional prompt content from local files only when opened, while keeping the English lesson available without JavaScript and retaining complete one-click copying. Optimize image delivery without removing the requested originals.

**Success measure:** measured improvement in slow-phone reading readiness, keyboard and screen-reader task completion, and no regression in offline/static lesson access.

### 6. Shift SEO work from metadata quantity to usefulness and discovery

The technical foundations are already extensive. The next opportunity is original evergreen material, useful topic collections, visibly maintained explanations and links between related readings and grammar. There are only two evergreen story topics alongside a much larger daily archive.

Prioritize a small set of well-edited, reusable lessons over more nearly identical landing pages. Use Search Console data, when available, to identify what learners seek and where current pages fail to answer them. This direction is consistent with [Google’s guidance on helpful, reliable content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content).

Measure starts, reaching practice and useful next-page choices only if an appropriately scoped measurement plan is agreed. Do not send student answers, notes or recordings into analytics. No traffic or conversion improvements are claimed by this audit.

## Suggested order

1. Calibrate editorial review and replace the three contradictory graphics.
2. Pilot one guided study route with a few representative learners.
3. Add a small retrieval/listening sequence and test its usefulness.
4. Use observed learner behavior and loading measurements to choose the next accessibility, performance and evergreen-content work.

Avoid another broad cosmetic redesign until these higher-value changes have been tested.
