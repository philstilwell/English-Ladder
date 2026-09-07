# Daily vocabulary separation and reliable lesson repairs

September 7, 2026

Every daily edition now has separate vocabulary targets for Beginner, Intermediate and Advanced. The archive review replaced **602 targets across all 64 editions**: 293 Intermediate and 309 Advanced. All 192 lessons retain at least 6, 8 and 10 vocabulary items respectively, each drawn from that lesson’s own reading. Reading and quiz minimums remain unchanged.

The review considered each edition’s three lists together, retained useful distinct targets, and selected replacements from the existing readings. It also corrected contextual meanings and word classes—for example, “atmosphere” as the mood of an event and “transport” as a verb meaning to move supplies. Existing source, reading, question and editorial history records remain intact. Each archive records the vocabulary review separately; these edits were not sent to a paid independent model review.

For the September 6 aviation story, the progression includes:

| Level | Examples of its own vocabulary targets |
| --- | --- |
| Beginner | delays, routes, pilots, passengers |
| Intermediate | severe, departures, congested, forecasts, radar |
| Advanced | usable airspace, fuel consumption, operating costs, diversions, storm cells |

## Future editions

The writer and reviewer use the same versioned language policy. After Beginner passes, its targets are reserved. Intermediate must choose other targets; Advanced must avoid the targets of both earlier levels. The policy still requires appropriate vocabulary, register, teaching language and challenge at each level.

The local comparison catches case and punctuation differences, ordinary inflections, common spelling variants, an explicit set of common derivatives, and borrowed teaching words inside different phrases. Examples rejected include “community / communities,” “congested / congestion,” and “retaliatory tariffs / retaliatory measures.” Common grammatical words inside different phrases do not count as borrowing. Shared words are allowed in the reading itself; the prohibition concerns the taught target lists within that edition. Later dates may revisit a useful word.

This comparison is deliberately conservative, not a complete linguistic analysis. The independent editorial review still checks subtle variants, actual meaning, relevance and level suitability. Numeric compliance never substitutes for that review.

Separation is enforced during drafting, before an archive is written, before existing pages are rebuilt, and in the final site audit. A borrowed target does not count towards the minimum. An invalid edition cannot overwrite the previously published archive.

## Fixing drafts without introducing fresh mismatches

The September 7 failed run repeatedly selected vocabulary absent from its reading. A later complete rewrite repaired the vocabulary but introduced a grammar quotation absent from the story. Previously, retries started the whole lesson again with error messages alone.

The process now preserves the previous draft. When the reading and its source evidence pass and the failures are confined to vocabulary, grammar or quizzes, the next attempt replaces only those sections. Vocabulary repairs choose numbered references to exact words or phrases in the reading, excluding targets reserved for other levels. Grammar repairs choose a numbered reading sentence, which the program copies exactly. The model still writes the contextual definition and explanation; the program does not guess meanings or silently change word forms.

A patch cannot alter locked sections, add unexpected fields or use an invalid reference. If the reading itself needs work, evidence is missing, the independent review rejects the lesson, or no suitable repair menu is available, the model receives the previous draft and specific errors for a full revision. Every merged result must pass all local, evidence and independent editorial checks before publication.

The existing limit remains three drafting attempts per level. There are no extra repair calls outside that limit, no additional scheduled runs, and no automatic approval of failed material. Real language and factual problems can still stop publication; the change prevents avoidable regressions during mechanical repairs.

## Verification

Regression tests use saved lesson data and synthetic model responses. They cover absent word forms, exact grammar references, locked-section protection, invalid references, missing source evidence, failed independent reviews, vocabulary reservations, archive protection and rebuild rejection. All stored editions are checked for count, source-text matching and cross-level separation. The regular site audit also compares published vocabulary, definitions and quizzes with the archive data.

No paid generation or image requests were used for this change.

## Live-run review calibration

A subsequent September 7 run exposed contradictory editorial demands: a reviewer treated six quiz questions as a maximum, rejected reused source excerpts, and asked for a grammar example absent from the reading. The reviewer now explicitly distinguishes the curriculum’s requirements from optional stylistic preferences. Additional useful questions, shared supporting excerpts for different reading facts, exact reading quotations, contextual vocabulary/grammar questions and natural beginner sentence frames are permitted. A misleading factual distinction still blocks publication. The writer also receives clearer verbatim-evidence and answer-feedback instructions. No failed review is ignored or automatically converted to approval.

A further run passed Beginner and Intermediate but exhausted Advanced’s attempts on copied-evidence mismatches and an invalid discussion prompt. `lesson_evidence.py` now supplies a stable numbered menu of original source passages. The writer returns the selected index for each reading sentence; the program copies that passage exactly before all existing checks and semantic review. Selecting a real source passage is not treated as proof that it supports a claim. Source errors are reported even when other sections also fail, and discussion formatting can be repaired independently with the existing two-prompt, 10–220-character limits. The three-attempt limit and every publication gate remain intact.
