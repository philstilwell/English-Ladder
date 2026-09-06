# Grammar practice: multiple-choice responses

The grammar activities previously accepted arbitrary writing and revealed a static model answer. The revealed answer did not evaluate the learner's text, making it possible to mistake the model for feedback on an incorrect response.

All 176 response activities in the 44 grammar lessons now offer three choices and show an explanation for the selected option. This includes the former “Make it your own” activity. No grammar response text boxes remain. Each activity has one correct option among the choices offered; this does not imply that every unlisted expression is wrong.

For Concept 35, “When I was seven, I ___ swim,” selecting “will” explains that it refers to the future. Selecting “could” confirms its use for past ability. “Was able to” is acknowledged as another valid expression and is not offered as an incorrect alternative. The achievement question distinguishes an actual success (“managed to”) from a hope or attempt. See the [British Council's past-ability guidance](https://learnenglish.britishcouncil.org/free-resources/grammar/b1-b2/past-ability).

Learners can change selections and retry. The completion button becomes available after all four activities are answered correctly. Optional browser saving restores both selections and their feedback. A question-content identifier prevents an old selection from being restored against changed options. Old typed answers are not treated as quiz responses.

The shared curriculum produces both the web lessons and all 88 learner/teacher PDFs. Printed activities use lettered choices; teacher editions include explanations for incorrect options. Existing download addresses remain valid. The PDF fonts are embedded, and section bookmarks are retained. The PDFs are printable documents, not interactive forms or fully tagged accessible documents.

## Verification

- 65 Python and 40 JavaScript tests passed, including a check of feedback for all 528 answer options.
- Regression coverage includes the reported “will” example, changed selections, incomplete/correct completion states, optional saving, old typed drafts, and invalid stored selections.
- All 297 site pages passed the link, metadata, and curriculum audit.
- 180 browser layout checks passed: the 44 lessons and grammar directory at 320, 390, 768, and 1440 pixels. Additional narrow-screen checks covered selected-answer feedback and long application choices.
- Browser checks verified radio-button keyboard navigation, retry feedback, completion eligibility, and saved-answer restoration. No console errors or warnings were observed.
- All 88 PDFs (484 pages) passed checks for question and choice text, embedded fonts, bookmarks, and text within page boundaries. Representative practice, application, and answer pages were rendered and visually inspected. File-level results are in [the PDF validation record](grammar-multiple-choice-validation-2026-09-06.json).

## Maintaining this behavior

Author questions in `content/grammar-curriculum.json`. Include a prompt and three unique options, each with its own text, Boolean correctness value, and feedback. Use context to distinguish the answers; never mark a valid alternative incorrect merely because it differs from a preferred model. Keep grammar responses multiple choice when adding or revising lessons.

`grammar_curriculum.py` rejects malformed option sets. `audit_site.py` rejects grammar response text boxes or missing choice groups. The regression tests check the published interaction. Rebuild both web and print editions after changing questions so their choices and explanations stay aligned.
