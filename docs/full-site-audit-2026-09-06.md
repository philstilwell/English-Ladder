# English Ladder audit and improvement recommendations

September 6, 2026 · Reference revision `b66f076` · Live site and repository review

English Ladder has a strong visual foundation and a substantial teaching library. The compact ladder mark, warm white background, cobalt controls, readable story pages, and newer English for Work materials are worth retaining. The most valuable next investment is instructional reliability: correct the older grammar explanations and text tools, strengthen the evidence behind daily news, and update the older downloadable materials.

Keep English Ladder cobalt blue and English Road green. Continue using the shared design guide for typography, spacing, navigation, and controls.

## What was checked

| Area | Coverage and result |
| --- | --- |
| Published pages | All 100 HTML pages returned HTTP 200 and matched the local files byte for byte. |
| Linked local assets | All 309 distinct linked assets returned HTTP 200, including all 252 PDFs. |
| Local links and structure | No missing local files, broken local fragments, or duplicate IDs. Every page has one main heading, a main-content region, a skip link, and an English language declaration. Every image has an alternative-text attribute; this is not a judgment that every description is sufficient. |
| Responsive layout | All 100 pages at 320, 390, 768, and 1280 pixels: 400 automated layout checks. Seven pages exceed 320 pixels, including three one-pixel cases; one exceeds 390 pixels. None exceeds 768 or 1280 pixels. No failed already-loaded images were observed. Off-screen lazy images were not forced to load. |
| Browser review | Visually reviewed Discover, beginner and advanced news, grammar directory/detail, a work course, practice tools, and everyday English. Tested daily reading/practice/discussion navigation, wrong-answer feedback, level routing, tool shortcuts, sentence rewriting, the grammar diagnostic, and the diagram dialog's keyboard behavior. |
| Teaching content | Reviewed stored evidence and all seven current beginner and advanced news readings; sampled intermediate content and current beginner comprehension questions. Also reviewed detailed grammar samples 05/07/16/28, library summaries, and eight workplace cases/checks/models across four courses. This is a targeted editorial review, not a line-by-line certification of every lesson. |
| PDFs | Structural inspection of all 252 PDFs, totaling 3,251 pages. Checked text against page edges throughout all 88 grammar PDFs. Visually inspected selected pages of the grammar workbook, a work learner workbook, and a work teacher guide. |
| Existing checks | 53 Python tests and 20 JavaScript tests passed, plus syntax checks for the five browser scripts. |
| Publishing | Inspected the daily workflow and its latest 15 run records. The latest two scheduled runs completed successfully; Discover displayed the September 6 lesson and its matching illustration. |

This audit does not establish full accessibility conformance, measured learning gains, real-device audio compatibility, or professional accuracy across every regulated workplace subject. No learner sessions or analytics reports were available. Recommendations about engagement are design judgments to test with learners. No paid generation services were used and no site behavior was changed.

## Priority order

Small means a focused correction; medium means several connected changes; large includes substantial content work or a new learning feature. These are relative estimates, not delivery commitments.

| Priority | Improvement | Why it matters | Effort |
| --- | --- | --- | --- |
| 1 | Correct misleading grammar rules and examples | Learners can currently learn an incorrect general rule. | Large overall; small for individual corrections |
| 1 | Repair or narrow the older text tools and diagnostic | Confirmed outputs change meaning or overstate a result. | Medium |
| 1 | Strengthen daily-news evidence and review | Format checks do not detect unsupported factual details. | Medium–large |
| 1 | Rebuild the 88 grammar PDFs | Old branding, unembedded fonts, and confirmed clipped text remain. | Medium after content corrections |
| 1 | Fix mobile overflow and diagram keyboard focus | Confirmed barriers affect phone and keyboard users. | Small |
| 1 | Improve beginner scaffolding and story suitability | Short sentences alone do not make an A1–A2 lesson approachable. | Medium |
| 2 | Preserve levels and provide permanent lesson links | Learners lose their chosen level or cannot return to older stories. | Medium |
| 2 | Make grammar and everyday English easier to browse | Large unfiltered pages make useful material difficult to locate. | Medium |
| 2 | Add more meaningful practice and review | Recognition and answer revealing provide limited evidence of transfer. | Medium–large |
| 2 | Finish the visual alignment across teaching materials | Old diagrams and uneven component styles interrupt the new identity. | Large for 44 diagrams |
| 2 | Add consistent continuation and draft controls | Learners need predictable ways to resume and keep their work. | Medium |
| 2 | Improve search previews, trust information, and maintenance checks | These support discovery and prevent repeat defects. | Medium |
| 3 | Add curated listening and measure learner journeys | Valuable expansion after the content and usability corrections. | Medium–large |

## 1 Correct the older grammar explanations

The grammar library needs a subject-matter editing pass, not just shorter introductions. Several sampled pages teach a useful example as if it were a general grammatical rule.

- **Concept 07, About:** it explains *about* as extending the duration or detail of short actions such as talking, walking, and thinking. This confuses distinct meanings and verb patterns. Teach *talk about* and *think about* as referring to a topic, distinguish *walk about* meaning movement around a place, and teach verbs such as *discuss* through their own patterns. [Current lesson](https://englishladder.com/grammar-concepts/concept-07.html), [Cambridge explanation](https://dictionary.cambridge.org/grammar/british-grammar/about).
- **Concept 16, Recently and lately:** its introduction suggests these words signal a need for the present perfect progressive. Add the distinction between recent single events, repeated events, states, and ongoing activity. A recent single event can use the past simple; the adverb does not mechanically choose a tense. [Current lesson](https://englishladder.com/grammar-concepts/concept-16.html), [Cambridge guidance](https://dictionary.cambridge.org/grammar/british-grammar/late-or-lately).
- **Concept 28, This, that, and it:** the rule tying *this* to one's own idea and *that* to another person's idea is too restrictive. Present these as possible conversational patterns, then explain reference, distance, and context. Include examples where the same speaker uses *that* to refer back. [Current lesson](https://englishladder.com/grammar-concepts/concept-28.html), [Cambridge guidance](https://dictionary.cambridge.org/grammar/british-grammar/that).
- **Concept 05, By and through:** distinguish a useful introductory pattern from a complete account of usage. Replace distracting examples such as “I defeated the ninja by throwing eggs” with situations learners can use. Remove repetitive prose, awkward phrasing, and the duplicated word in the bonus introduction. [Current lesson](https://englishladder.com/grammar-concepts/concept-05.html).

Use a consistent teaching sequence: a practical goal, a concise explanation, a contrast with a common error, realistic examples, a short check, and a task requiring the learner's own sentence. Review the poster, webpage, exercises, answer key, and both PDFs together. A correction in only one edition leaves contradictory teaching available.

**Success check:** an editor can identify the scope and exceptions of each rule; examples sound natural; answer keys accept legitimate alternatives where context permits them.

## 2 Repair the practice tools before expanding them

Three failures were reproduced on the live [Practice page](https://englishladder.com/tools.html).

| Action | Observed result | Recommended correction |
| --- | --- | --- |
| Repair “The little people in the story built a tiny village.” | Rewrites *little people* as *few people*, changing the intended meaning. | Offer a contextual suggestion instead of automatically substituting the phrase. Explain the distinction and let the learner choose. |
| Transform “I work in London.” into academic English | Lowercases *I* and *London* and invents a claim that further analysis and revision may be required. | Preserve names, capitalization, factual content, and intent. Restrict the feature to supported examples until broader rewriting is reliable. |
| Answer only the first diagnostic question correctly | Displays “Strong diagnostic result” and recommends a harder daily lesson. | Show “1 of 10 answered,” distinguish incomplete from completed results, and give recommendations only for the material actually assessed. |

`tools.js` uses a small collection of text replacements and fixed sentence wrappers. This can still support useful targeted exercises, but its presentation should clearly describe that limited scope. Avoid implying that arbitrary writing has been comprehensively checked. No paid AI service is necessary to correct the three failures above.

The existing automated checks initialize these tools but do not test the meaning of these outputs. Add regression cases for correct sentences, names, negation, obligations, incomplete diagnostics, and ambiguous uses of words.

## 3 Strengthen evidence behind the daily news

The current generator receives a headline and an RSS summary, a short feed description of the article. Across the seven current releases, that evidence contains only **26–40 words per story**, while the advanced readings contain **167–214 words**.

Expansion alone is not an error. The problem is unsupported specificity. For example, the September 5 advanced reading includes biographical, medical, and courtroom details absent from its stored source evidence. The September 2 advanced reading also adds meeting and response details absent from the stored headline and summary. These details may or may not be true; this pipeline does not establish them.

`validate_lesson_data` checks the structure, counts, vocabulary inclusion, grammar quotation, and answer formatting. It does not verify factual claims against evidence or independently assess whether the correct answer and feedback are sound.

Recommended changes:

1. Use sufficient permitted source material and record the source publication date and retrieval date separately from the lesson release date.
2. Require specific factual claims to be traceable to that material. Remove unsupported names, numbers, events, diagnoses, quotations, and attributed positions.
3. Preserve uncertainty. Do not turn a source's possibility into a definite prediction during simplification.
4. Review each question and feedback explanation against the passage, including whether more than one answer could reasonably fit.
5. Allow the reading length to follow the evidence. A fixed ten-sentence requirement should not force filler or invented context.
6. Give readers a clear correction route and keep a short correction history when a published lesson changes.

Review the current seven releases retrospectively. The live source article was not fully retrievable through the audit's web tool, so the finding is **unsupported by the stored generation evidence**, not a declaration that every additional detail is false.

**Success check:** a reviewer can account for every specific factual claim using the saved evidence, and all three reading levels preserve the same central facts and uncertainty.

## 4 Make beginner lessons easier to enter

The August 31–September 6 beginner readings are short, at 62–80 words, but their supporting language often exceeds what a new learner can comfortably use. Examples in the current week include legal liability, sabotage, and global economies. The September 6 prediction and discussion questions also require more complex English than much of the passage.

Retain the three reading tracks, but edit every part of the beginner experience for its intended learner: headline, introduction, prediction, vocabulary definitions, grammar explanation, options, feedback, and discussion. Add short sentence frames such as “My flight was late because ___” and an alternative for students who have never flown.

The current archive includes a child-murder trial, forced returns to Afghanistan, attacks, and a fatal disaster. The recently added feed rotation and distress-word preference are useful improvements, but the existing week still makes a difficult introduction to the site. Offer a clear everyday-life alternative, topic labels, and an explicit editorial policy for choosing a general-audience lead story. A topic label should describe the content accurately rather than hide a difficult subject behind a vague headline.

For advanced learners, prioritize precise and natural language over inflated wording. Increase the reasoning challenge through supported inference, paraphrase, qualification, and comparisons.

## 5 Rebuild the grammar PDFs

The site has **88 grammar PDFs** and **164 work PDFs**.

- All 88 grammar PDFs contain unembedded font resources. In the sampled workbook, the actual body and heading text uses unembedded Helvetica and Helvetica Bold.
- Both Concept 05 PDFs have text beyond the right edge on their first page: the topic strip reaches approximately **679 points on a 612-point-wide page**. This was confirmed visually in the learner workbook and by inspecting text coordinates in both files.
- The sampled grammar workbook retains the old peach/brown theme and the previous three-dimensional ladder characters.
- All 164 work PDFs have embedded fonts and bookmarks. Their files match the current download manifest; the previous complete work-layout audit reports no failures. The sampled work pages are substantially cleaner.
- None of the 252 PDFs has a tagged document structure. Tags identify headings and reading order for assistive technology; embedded fonts alone do not make a PDF accessible.

Use the newer work-document quality standard for grammar: white paper, restrained cobalt accents, the current mark, clear hierarchy, wrapped headings, usable writing space, separate answers, embedded fonts, and bookmarks. Add document tags where the production tools support them and preserve equivalent readable HTML. Consider fillable fields for learner workbooks intended for digital use; currently none of the PDFs has form fields.

Correct the teaching content before regenerating every edition. Verify all pages after rebuilding, including long title and topic strips.

## 6 Fix the confirmed access problems

### Narrow screens

At a 390-pixel viewport, [Telecommunications English](https://englishladder.com/efsp-telecommunications.html) produces a 436-pixel-wide document. The long heading forces the grid column wider, clipping the introduction and adjoining panel. At 320 pixels, additional overflow appears on Concept 15, Pharmaceutical English, and Semiconductor English. Three other courses register only one pixel of overflow and should be checked for rounding before treating them as substantial defects.

Make grid children shrinkable, allow long words to wrap where necessary, and adjust the smallest-screen heading size. Keep the text readable. Hiding horizontal overflow would conceal the symptom.

### Enlarged diagrams

Opening the Concept 05 diagram focuses its Close button. Pressing Tab then moves focus to the **Photo credits** link behind the still-open dialog. The shared code does not contain focus inside the modal or make the background inactive.

Use a native modal dialog or implement the full keyboard behavior, including Tab, Shift+Tab, Escape, and focus return. Confirm that the background is unavailable while the diagram is enlarged. [W3C modal-dialog guidance](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/).

Continue testing the existing strengths: skip links, visible focus, status messages, labeled inputs, reduced-motion support, and text feedback. Add a screen-reader pass and zoom/text-spacing checks; page-width checks alone are insufficient.

## 7 Preserve the learner's level and place

On Discover, choosing **Advanced** changes the main lesson link correctly. The two evergreen story links and the Daily news navigation still lead to Beginner. Give level selection a clear scope or carry it consistently through relevant links. Let the learner change it easily.

The news level-switch links also omit the current lesson date. Switching level while reading an older story can therefore lose that story. Preserve its date where another version exists.

The three news pages retain only seven lessons. Older structured archives exist, but there are no corresponding permanent lesson pages for readers. A previously shared dated fragment stops identifying a lesson after it leaves the rolling page. Publish stable dated lesson URLs and provide a searchable archive by date, topic, level, vocabulary, and grammar focus.

After completion, offer one useful next action: review missed questions, practice the lesson's grammar, try another story at the same level, or continue a relevant work lesson.

## 8 Help learners find useful material

The [grammar directory](https://englishladder.com/grammar-concepts.html) is a list of 44 large cards with no topic search or level filter. At 320 pixels it is approximately 32,563 pixels tall. Several titles are cumbersome, and Concept 20 is named only by its number.

Add keyword search, plain topic names, broad level guidance, and categories such as time, prepositions, sentence structure, and easily confused words. Rewrite card descriptions as specific learning outcomes instead of clipped introductions. Show duration and a suggested starting sequence.

The [everyday-English page](https://englishladder.com/us-life.html) contains 24 units on one page, approximately 64,606 pixels tall at 320 pixels. Split it into individual units or let students reveal one unit at a time while retaining direct links. Offer an English-only view as well as Japanese and Mandarin support. Add a small activity and next-unit action to each unit.

The work directory already offers search, categories, useful goals, and clear download roles. Reuse those successful patterns. Shorten its longest course descriptions and make shared communication skills searchable alongside industries. Consider making the long course glossary a searchable disclosure below the lessons.

## 9 Make practice test useful learning

The current daily lesson contains ten checks after a short reading. Several September 6 questions revisit essentially the same fact about disruption. Add a deliberate mix: main idea, detail, vocabulary in context, grammar application, and a short supported inference where appropriate.

Grammar practice mainly reveals an answer. Add an optional response before revealing it, an explanation of the choice, and a brief transfer task. Avoid ambiguous blanks with only one accepted answer when several readings are possible.

The work courses intentionally reuse 12 language workshops across industries, while their cases and model responses differ. Keep that useful recurring foundation. Pair it with a case-specific question or a fresh application so someone taking several courses meets more than the same checks. Make advanced distractors plausible: choosing a respectful answer over an obviously insulting one often tests common sense more than English.

Allow retries for learning, but distinguish a first attempt from the latest corrected result if scores are shown. Completion should describe the activity finished, not imply a validated proficiency gain. Provide worked examples and self-check criteria for discussion and writing rather than suggesting that ungraded drafts have been assessed.

## 10 Finish the visual alignment

Keep the current homepage composition, compact mark, restrained borders, and cobalt identity. The main remaining visual mismatch is in the instructional assets.

Refresh the 44 grammar diagrams as a coherent series after the language review. Use larger type, fewer examples per image, a consistent grid, simple marks, and color tied to a grammatical distinction. Preserve the actual teaching content in HTML so images support access rather than carry essential text alone.

Reduce repeated layers of titles on lesson pages: a page heading, story headline, technical topic subtitle, and section heading can all appear before the reading. Give the story and its immediate learning goal priority. Use a consistent distinction between primary and secondary actions; both backward and forward lesson buttons currently use the same strong treatment.

Bring work-course button shapes and primary accents closer to the shared site standard while retaining a restrained specialist tone in secondary panels. A documented common component set will make that easier than adding further overrides.

Create actual small thumbnails for the grammar directory. It currently uses the full poster files; the largest is about 1.25 MB. Lazy loading is already present, but appropriately sized previews would reduce unnecessary downloads.

For any commissioned images, follow the standing Gemini preference and estimate generation costs before work starts. No new artwork is required to make the immediate content, layout, and keyboard corrections.

## 11 Make continuation and saving predictable

News discussion notes stay only on the current page; work-course drafts can be saved in the browser by opting in. Both behaviors are explained, but a returning learner has no common continuation area.

Add a modest “Continue learning” view, a saved-word list, and an optional review queue. Use browser-only saving initially if that meets the product's needs, explain its limits, and provide copy/export controls. Keep the meaning of “practiced,” “completed,” and “correct” consistent.

For work drafts, add an undo or other recoverable safeguard to the control that clears an entire course's notes and progress. Preserve fictional practice details and avoid sending draft text to analytics.

## 12 Improve listening deliberately

Reading lessons have no integrated listening control. The separate shadowing tool uses browser speech synthesis and lets the learner record and compare a sentence, but recording and audio quality were not tested in this audit.

Add approved model audio beside the reading, with normal/slower playback and a transcript, then a short listen-and-retrieve activity. Keep controls explicit and make the lesson usable without audio. Under the owner's standing preference, future produced audio should not use local/native voices without explicit instructions; estimate any external production cost first.

Before extending recording, test supported audio formats on iPhone/Safari and Android, stop microphone tracks on failures and navigation, revoke replaced recording URLs, and state clearly whether recordings remain on the device. These are code-review recommendations, not reproduced cross-browser failures.

## 13 Improve discovery and trust

**Search and sharing:** 50 of 100 pages lack a description for search previews. None has a canonical URL declaration or an Open Graph title for shared-link previews. `sitemap.xml` and `robots.txt` return 404. A missing robots file does not prevent indexing, and a missing canonical is not automatically an error, but explicit metadata and a sitemap will make the growing library easier to understand and maintain. Add unique descriptions, preferred URLs, relevant preview images, and a useful not-found page. Stable dated lesson pages should come before extensive news-specific search optimization.

**Trust:** provide an About page, a plain explanation of how lessons are produced and checked, an error-reporting route, and a short privacy page. Describe Cloudflare analytics, browser-only drafts, recordings, and any external services accurately. The honest AI-image caption and photo credits are good foundations.

**Measurement:** establish a baseline for starting a lesson, reaching practice, completing an activity, opening a related lesson, and returning later. Evaluate navigation changes with actual learners. Do not collect their written answers or recordings for these measurements. This audit does not claim current conversion, retention, or speed scores.

## 14 Protect quality during publishing

The daily workflow already has useful safeguards: scheduled fallback attempts, current-branch checkout, structural lesson validation, image reuse, bounded image retries, and live deployment verification. Keep them.

Add checks that address the failures found here:

- Run generated-page checks after producing new content, as well as tests before generation.
- Include the 320-pixel layout cases, the diagram focus sequence, incomplete diagnostic behavior, and meaning-preserving text-tool examples in automated checks.
- Extend PDF checks to grammar as well as work documents, including fonts, text boundaries, navigation, and edition consistency.
- Add an editorial evidence check for new news content and its answer feedback.
- Review the push-retry step: it refreshes the branch, then restores saved generated-page snapshots. Rebuild from the newest templates if those templates changed during the run, so an older snapshot cannot restore an outdated interface. This is a code-level race risk, not an observed failed deployment.
- Monitor whether the latest expected release actually appears and whether images or content checks fail. GitHub schedule times are requests, not exact publication guarantees.

Consolidate shared visual values gradually. `styles.css` and `editorial.css` together contain about 99 KB before compression, with additional work styles and many generated inline styles. This is primarily a maintenance issue. The tools also fetch all three news archive pages at startup; load only the needed data when a tool requires it. The static homepage itself is small, and this audit provides no evidence that a heavy application framework would improve it.

## Suggested implementation sequence

**First correction pass:** fix the three reproduced tool failures, the diagram modal, mobile text wrapping, and the two clipped PDF covers. Correct the highest-risk grammar rules and review unsupported specifics in the current news archive.

**Content and print pass:** edit all 44 grammar concepts and their answer keys, rebuild both PDF editions with embedded fonts and navigation, and strengthen daily-news source and difficulty checks. Refresh diagrams only after their teaching content is stable.

**Learning-flow pass:** preserve selected levels and dated stories, add searchable archives and library filters, divide everyday English into manageable units, and improve completion/next-step guidance.

**Expansion pass:** add optional continuation and vocabulary review, carefully produced listening, and learner-based measurement. Keep English Ladder blue and English Road green throughout.

The first release should be judged by concrete corrected outputs and successful learner actions. The later feature work should be judged by whether learners find relevant lessons, understand what to do, and return to practice.

## Evidence files and visual samples

The accompanying `full-site-audit-2026-09-06.json` records page/asset coverage, PDF structural results, the page-boundary failures, and the responsive findings. Source files most relevant to implementation are `tools.js`, `app.js`, `learning.js`, `update_site.py`, `editorial.py`, `editorial.css`, `work.css`, `generate_grammar_concepts.py`, `generate_english_ladder_pdfs.py`, and `.github/workflows/cron.yml`.

Visual PDF samples were the Concept 05 learner workbook, pages 1–2 :codex-file-citation{path="/Users/philstilwell/Documents/New project 8/English-Ladder/pdf/students/concept-05-grammar-concepts-using-by-and-through-student-workbook.pdf" purpose="source"}; the Software Product Management learner workbook, page 2 :codex-file-citation{path="/Users/philstilwell/Documents/New project 8/English-Ladder/pdf/efsp/efsp-software-product-management-english-participant-workbook.pdf" purpose="source"}; and the Hospitality and Tourism teacher guide, page 3 :codex-file-citation{path="/Users/philstilwell/Documents/New project 8/English-Ladder/pdf/efsp/efsp-hospitality-tourism-english-instructor-guide.pdf" purpose="source"}.
