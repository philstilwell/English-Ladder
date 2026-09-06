# AI practice extensions for English for Work

The 41 courses now carry the learner's chosen case or complete dialogue into a carefully scripted AI exercise. Students copy the prompt into their own AI service; the website does not call an AI, transmit drafts or require an account.

## Placement and purpose

| Placement | What the learner gets | Why here |
| --- | --- | --- |
| After each lesson's attempt, reflection and retry | Direct links for vocabulary, grammar, role-play and writing feedback, already set to that lesson | Extension follows an attempt, so the AI does not replace the first practice |
| Each course's AI workshop, after the vocabulary section | Eight goals, all eight lessons, every Conversation Lab script, and B1/B2/C1 practice settings | One accessible place to change the goal or context, copy, save or link to a prompt |
| Each complete dialogue and each PDF role-play case | A link to rehearse that exact scenario with the AI as a counterpart | The learner can continue the conversation they just studied |
| Each workbook lesson, teaching note and phrasebook model | A context-specific link for feedback, adaptation or vocabulary retrieval | Help is available where the learner or teacher needs it |
| End of all 164 work PDFs | Usage guidance and two fully written, course-specific starter prompts | Printed and downloaded materials remain usable without reconstructing a prompt |

The course introduction links directly to the workshop. The course directory explains the new option. The selectors are optional enhancement: without JavaScript, the complete default Lesson 01 role-play prompt remains selectable.

## Eight authored task scripts

1. **Vocabulary and collocations:** four source terms, four relevant extensions, word combinations, examples and likely misuses, followed by one-at-a-time recall and production.
2. **Grammar in context:** a narrow target from the actual workshop or dialogue, meaning contrasts, an attempt, a hint, a revision and transfer.
3. **Interactive role-play:** the learner chooses a professional role; the AI plays the counterpart and waits. It responds to the learner's actual contributions, then provides focused feedback and a replay.
4. **New scenario dialogues:** six distinct scenario proposals, followed by selected 12–18-turn scripts with two or three professionals, natural terminology, a credible outcome, expression notes and withheld comprehension answers.
5. **Writing feedback:** the AI requests the learner's own draft and purpose, waits, prioritizes meaningful improvements and asks for revision before presenting a full alternative.
6. **Tone and register:** preserve meaning while adapting a real utterance for different audiences; distinguish style preferences from errors.
7. **Recall and transfer:** six staged questions, hints before models, and a reusable review card. Practice performance is not presented as a certified level score.
8. **Teacher adaptation:** a timed session, separate professional role cards, support and stretch options, teacher notes and an observation checklist.

Print pairings are teacher adaptation + register, grammar + writing, role-play + new dialogues, and vocabulary + review. These are eight authored task designs reused with original context, not thousands of independently written prompts. Across the website, the context choices cover all 328 lessons and 368 complete dialogues.

## Content and interaction decisions

- The reference block contains the actual course scope, case facts, language target, terms and definitions, tasks, and comparison model. For a dialogue, it includes every speaking turn and the actual roles.
- The prompts explicitly distinguish reference material from instructions and invented scenario variations from the original facts. An AI should preserve uncertainty, authority and responsibility rather than making a message sound more certain.
- Support settings change the exercise, not the learner's assessed level. Natural alternatives are accepted; error correction and optional stylistic suggestions remain distinct.
- A writing prompt does not read or automatically append the browser's draft fields. It asks the learner to supply a fictional or anonymized draft in their chosen service.
- Copying has a manual-selection fallback if the browser blocks clipboard access. Text downloads and links retain the selected goal, context and support level.
- Long prompts are intentional: the context travels with the exercise, so the learner does not need an AI that can open a PDF or browse the course website.

The use of explicit tasks, bounded output and clearly separated context is informed by the official [Google prompt-design guidance](https://ai.google.dev/gemini-api/docs/prompting-strategies) and [Anthropic prompting guidance](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices). The teaching scripts themselves are original and use no provider-specific features.

## Validation and practical limits

Automated checks compare the published web context to every original case and dialogue, verify printable prompt endings and links, exercise copying and its failure path, and check that learner drafts are not included. The complete PDF audit checks font embedding, text bounds, glyphs, page counts, bookmarks and file checksums. Representative printed pages and desktop/mobile layouts are inspected visually.

No paid AI calls are required to compose or publish these materials. Actual tutoring behavior has not been benchmarked across external AI services; a script is a carefully specified request, not a guarantee that every model will follow it. A useful future evaluation would run the same anonymized learner attempts through selected services and assess factual preservation, waiting for responses, terminology and feedback quality.

General grammar lessons, news reading and other parts of the site are natural later locations for the same approach. Their extensions should carry their own source passage and learning target rather than reuse a workplace case. This release concentrates on the English for Work materials and their four companion guides.

## Maintenance

`work_ai_prompts.py` owns the task scripts, context composition, web markup and printable appendices. `work-ai.js` composes the selected prompt locally; `work-ai.css` handles layout. Regenerate the work PDFs and pages together after changing the prompt source. Each PDF's manifest entry records the prompt edition, source hash and count. The test suite detects a stale print or web edition.
