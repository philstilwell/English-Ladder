# Teaching quality review — 8 October 2026

This release improves existing learning activities without adding new features.

## Sentence feedback and diagnostics

Sentence repair preserves the learner's text and explains the limited patterns it can identify. It no longer produces a partly corrected replacement that might alter the intended meaning. Valid constructions such as “The book is interesting in several ways”, “how much people care”, “a report on 2026”, and “in Monday’s meeting” are left alone. Meaning-dependent suggestions explicitly describe the choice. The tool never treats an unmatched sentence as certified correct.

The short diagnostic explains each selected option, including grammatical choices that express a different meaning. Ambiguous questions about “lately” and the position of “only” have been replaced with explicit, answerable tasks. Changing an answer clears stale feedback; the result explains that this is practice guidance, not a placement test.

Direct links open the intended tool. The pronunciation tool now loads sentences from the current lesson when opened. Phrase copying reports success only after the clipboard accepts the text; a failed copy selects the phrase and provides a manual alternative.

## Seven news editions, all three levels

All 21 lessons dated 2–8 October were reviewed against their saved source evidence, including readings, vocabulary, grammar, every answer choice, feedback, and discussion prompts. The per-lesson record is in [the review manifest](teaching-quality-review-2026-10-08.json).

Representative corrections:

- Credit for the safe aircraft landing is shared accurately; recovery and condition descriptions avoid unsupported medical conclusions.
- Concert questions use details visible in the learner's reading and distinguish changes to performances from audience phone rules.
- A damaged bridge remaining standing is not described as structurally sound.
- Planned data centres are distinguished from construction; the reported notification rule is preserved without inventing an approval requirement.
- Claims about bomber withdrawals retain attribution and uncertainty. Arrest and bail do not imply conviction.
- School-protest questions avoid overlapping alternatives such as resources versus teachers; allegations do not imply an absence of evidence.
- “Wanted” is distinguished from “convicted”. The Syrian-official story preserves source attribution and the family spokesperson's conditional response.
- Grammar tasks explicitly distinguish form, intended meaning, and what the story supports. Present continuous in a conditional is not rejected merely because the requested pattern uses present simple; passive questions identify the clause being tested.

These boundaries are also included in the shared instructions used by the daily writer and reviewer. Tests confirm both receive the same instructions; they do not prove that future model judgments will always be correct.

Each revised lesson retains its earlier review under `previous_review`. The current record identifies this as a Codex editorial revision, not a fresh independent model approval. Source facts were checked against archived evidence; this work did not update the stories with later reporting.

## Translations and illustrations

Twenty translation records were refreshed for the revised contexts, covering Japanese, Korean, Simplified Chinese, Spanish, Brazilian Portuguese, French, and German. Existing definitions were retained where the meaning remained appropriate; misleading definitions were rewritten. All 21 lessons have valid current translation records. The new records identify the actual review method and retain the previous review history. This was not a native-speaker certification.

All seven existing illustrations were visually reviewed and retained as conceptual topic images. Six have new context-derived filenames; their image bytes are unchanged. Metadata records the reuse review and original path/digest without claiming a new generation. No paid text, image, translation, or audio service was called.

## Verification

- Python suite: 369 tests passed, followed by all 15 review-policy tests passing after adding the new policy regression.
- JavaScript suite: all 192 tests passed after the final page rebuild. Tool tests were repeated after narrowing the advice-pattern check to preserve “an advice column”.
- JavaScript syntax checks passed.
- Site and search audits passed: 289 pages; local links, metadata, curriculum, and news data checked.
- All 21 revised lessons passed structure and exact-source-excerpt validation. All seven illustration records and 21 translation sets match their current lesson context.
- Browser sessions at a 390-pixel viewport covered news Read → Practice → Discuss, wrong-answer retry, completion/undo, Japanese definitions, a localized AI prompt, Everyday English Spanish explanations, dialogue tabs, saved MP3 playback, next-unit navigation, grammar practice/completion, and work-course search, quizzes, prompt copying, and next-lesson navigation.
- Representative news, tools, Everyday English, grammar, and work-course pages also fit a 320-pixel viewport without horizontal overflow.
- New tool regressions cover valid sentence constructions, multiple errors, safe display of learner text, all diagnostic options, changed answers, clipboard failure, direct links, and current-lesson loading.

Browser checks use Chromium at phone dimensions, not physical iOS or Android devices. Microphone recording and native speech synthesis were not exercised. The review is not a full accessibility certification or a fresh editorial review of every older lesson, grammar lesson, work course, and PDF.

Reference for retaining accepted “recommend someone to do something” constructions: [Oxford Learner's Dictionaries: recommend](https://www.oxfordlearnersdictionaries.com/us/definition/english/recommend).
