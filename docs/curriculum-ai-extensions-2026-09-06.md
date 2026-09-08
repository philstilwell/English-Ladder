# Ready-to-paste AI extensions across the curriculum

Students receive complete authored prompts, including instructions and the relevant published lesson material. They choose a focus and copy the finished text. They do not need to write a prompt, upload a lesson, or fill in a lesson-context template.

## Placement

- All 44 grammar concepts: fresh examples, branching dialogue choices, and retrieval practice. The grammar extensions retain multiple-choice checks, option-specific feedback, retries, and guidance against marking another valid expression wrong.
- Daily news, its permanent archives, and the six evergreen story editions: vocabulary, evidence-based reading questions, and dialogue extensions. New daily releases automatically receive prompts drawn from their own reading and language focus.
- All 24 everyday-English units: vocabulary, conversations, and message choices based on the unit's phrases and situation.
- All six study tools: grammar, sentence work, pronunciation, reading, workplace phrases, and register practice using supplied examples. My learning includes a complete retrieval-practice starter.
- English for Work: the existing chooser preserves eight prompt modes, B1/B2/C1 support settings, all 328 cases, and all 368 complete Conversation Lab dialogues. Lesson links select the corresponding context automatically. Each full field glossary also has a ready-to-copy vocabulary extension.
- All 252 PDF guides contain complete prompts. Grammar guides include a learner or teacher extension with the lesson context; workplace guides retain two purpose-specific prompts and direct lesson/dialogue links.

The [AI practice page](https://englishladder.com/ai-practice.html) explains copying and points students to each area. Prompts are optional. Copying does not contact an AI service, read learner drafts, or include saved answers or recordings. The chosen service controls what happens after the student pastes a prompt there.

## Teaching design

The grammar and general-study scripts request short explanations, one question at a time, plausible choices, feedback tied to the selected option, and a final transfer task. They distinguish a correct first attempt from a retry. Vocabulary work includes word partners and contextual contrasts. Reading scripts distinguish supported information, inference, and what the text does not establish. Added scenarios are explicitly fictional.

Workplace scripts also support producing original language, drafting messages, adapting tone, creating substantial new dialogues, and preparing classroom activities. Their richer case/dialogue selector and existing printable prompts were preserved when integrating the curriculum-wide release. The grammar lesson response controls remain multiple choice.

The actual wording lives in `ai_extensions.py` for general study and field-glossary extensions, and `work_ai_prompts.py` for the workplace chooser. Prompts are generated from published curriculum text, never from private notes. Republishing replaces old blocks so a revised lesson cannot keep stale prompt context.

## Explanation language (September 8, 2026)

The definition-language buttons also set the explanation language for web AI prompts: Japanese, Korean, Simplified Chinese, Spanish, or Brazilian Portuguese. The remembered choice applies across levels and curriculum pages. English restores the original authored prompt without an added language instruction.

`ai-practice.js` adds an authored instruction block asking for deeper, contextual explanations of meaning, grammar, word partners, tone, and reading evidence in the selected language. It explicitly replaces brief-explanation limits while retaining the lesson's English difficulty, activity length, response format, pacing, and evidence boundaries. Examples, dialogue lines, and practice options remain English. Feedback explains the learner's actual response and preserves hints and retries without revealing withheld answers.

The visible prompt is the exact text copied, including manual-copy fallback. The workplace chooser, its individual text download and print view, and the complete lesson/dialogue prompt cards use the same guidance. Static PDF guides and prebuilt course text packs remain in their published English edition; they cannot read a browser language preference.

Language changes update open pages immediately, including changes from another tab and restored pages. If browser storage is blocked, buttons still update prompts on the current page. There are no translation requests, external AI calls, or additional API charges for this feature. New lessons automatically use the shared behavior when published.

## Validation

- 75 Python checks and 51 JavaScript checks passed after integration, along with the 298-page link, metadata, and curriculum audit.
- Tests cover complete context, future daily publishing, repeated rebuilding, escaped content, exclusion of private writing, exact copy payloads, clipboard fallback, and the existing workplace chooser and grammar interactions.
- Browser checks covered narrow-screen prompt previews across all 44 grammar pages, 41 workplace pages, and 24 daily-life units, plus representative reading and workplace chooser interactions. A clipboard success message was verified in the browser; exact copy payloads and selection fallback were checked in the automated interaction tests.
- All 252 PDFs (4,445 pages) passed embedded-font, bookmark, and page-boundary checks. The [document audit](document-validation-2026-09-06.json) records the results. Representative grammar prompt pages were rendered and inspected; the unchanged workplace PDF release retains its separate [workplace audit](work-ai-document-audit-2026-09-06.json).

No paid AI calls were made to author or publish these extensions. The prompts specify desired tutoring behavior; they have not been benchmarked across external AI services and cannot guarantee that every service follows every instruction. PDF checks do not certify tagged-PDF accessibility.
