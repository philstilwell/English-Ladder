# Existing-feature quality review — 8 October 2026

This second approved pass improves existing lessons and controls. The detailed coverage, performance samples, changed translation records and PDF checks are saved in [the review record](quality-second-pass-review-2026-10-08.json).

## Accessibility and browser behavior

Opening an inline vocabulary definition now announces its text and actual language through an existing live region, and associates the explanation with the focused word. Escape closes it while preserving focus. Changing languages clears the old announcement. The full news lesson was completed with keyboard controls, including the skip link, a wrong answer and retry, all six correct answers, stage changes, completion and undo.

Nested AI-prompt disclosures no longer inherit the outer tool's minus sign or layout. Their independent open/closed state remains visible. Initializing English AI prompts preserves the published text and any existing selection rather than needlessly replacing it.

Native Safari checks covered recorded pronunciation playback, Spanish explanations, dialogue tabs, copy success feedback, same-page Back restoration, navigating to a grammar lesson and back, enlarged text, and the reused speaker drawing. Safari zoom was increased four steps and restored; the precise zoom percentage was not measured. Exact copied text is covered by automated tests; Safari's check observed the success message only.

Chromium checks covered five page types at 320, 390, 768 and 1280 pixels with no horizontal overflow: news, Everyday English, grammar, a work course and tools. The 320-pixel nested-prompt and Everyday layouts were visually inspected.

These are browser and simulated phone-size checks, as requested. Firefox was unavailable and was not installed. No physical phone or full screen-reader session was used; keyboard, accessibility-tree and live-region checks are not an accessibility certification. Microphone recording and synthesized audio production were not used.

## Everyday English size and speed

Translation data is embedded as compact UTF-8 JSON while retaining the escape that prevents source text from ending its script element. All 288 pronunciation links reuse the original speaker drawing from one SVG symbol. Content remains in the page, including the no-JavaScript fallback.

The HTML decreased from 966,537 to 875,918 bytes (9.4%). Local gzip compression decreased from 146,151 to 106,502 bytes (27.1%). These gzip measurements are an estimate of compression savings, not an observed hosting transfer size.

Three cold-cache Chromium samples before and after used a 390 × 844 viewport, four-times CPU slowdown, 150 ms latency and 200,000 bytes/second download speed. The local server sent uncompressed HTML. Median document-ready time changed from 9.514 to 9.091 seconds (about 4.4% faster). This small local sample does not predict every phone or connection. CPU task time did not improve measurably; SVG instances also introduce internal browser nodes, so this is not a claim of fewer rendered nodes.

## Teaching content and translations

All 44 grammar lessons were reviewed: rules, comparison cards, questions, all choices and feedback, and application questions. Seven needed corrections:

- 02: removed a plausible alternative from the museum preposition question.
- 05: repaired the wording of “followed by.”
- 06: accepted both “discuss” and “discussed” where tense was unspecified.
- 08: specified that the task asks for uncertainty rather than a prediction.
- 24: aligned the card label and rule with “blame something on someone.”
- 33: described “no preference” accurately.
- 43: clarified the stated starting and ending values, and explained why “rose by 500 to 600” is grammatical for a different starting value.

The 14 corresponding learner/teacher PDFs were rebuilt. All fonts are embedded, all 105 pages passed text-boundary checks, and 28 rendered sample pages were visually inspected. Footers now show the lesson's actual review date. Existing grammar graphics were preserved.

The eight cases in each of six work courses were reviewed: project management, software development, medical assisting, restaurant service, childcare, and warehouse/distribution. Review covered 48 cases, model responses, workshop notes, question prompts, options and keys; project management and software development also received detailed vocabulary and every-answer-feedback review. This was not a line-by-line review of six complete books. Shared work practice now asks an unambiguous document-version question and acknowledges the willingness meaning of “if you will.” Medical and warehouse examples explicitly distinguish afternoon deadlines. Corresponding book passages already gave explicit times, so all 66 work PDF contents remain unchanged.

Translation review covered all seven supported languages for today's 25 news vocabulary entries (175 translations) and six Everyday units' headings and explanation points (168 segments). Corrections address naturalness, respectful address, terminology and mixed Spanish/Portuguese. A check for the discovered mixed-language patterns across 156 active news/story source records found one additional October 5 advanced definition, now corrected in both the dated and rolling pages. Previous review history is retained. This is a Codex editorial review, not a fresh independent-model or native-speaker certification.

## Verification and cost

The complete suite passed: 370 Python tests and 194 JavaScript tests. After the final announcement reset and archived translation rebuild, all 14 focused browser-script tests and 15 translation tests passed again. Syntax and publication checks passed for 289 pages, 154 PDFs and 1,008 public files. No paid text, image, translation or audio generation was called; additional generation cost was $0.

Reference guidance: [W3C accessibility easy checks](https://www.w3.org/WAI/test-evaluate/easy-checks/), [W3C disclosure pattern](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/), [MDN lazy loading](https://developer.mozilla.org/en-US/docs/Web/Performance/Guides/Lazy_loading), and [MDN SVG use](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/use).
