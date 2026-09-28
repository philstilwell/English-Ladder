# Occupation Courses

Each occupation is authored once in a JSON file and rendered into its webpage,
teacher guide, learner workbook, conversation lab, and phrasebook. The explicit
inventory and illustration order live in `work_occupations.py`.

## Authoring Contract

Top-level keys: `course`, `lesson_conversations`, and `dialogues`.

`course` contains `slug`, `title` (ending in English), `summary`, `roles`,
`category`, `scope_note`, `sources` (title/url objects), `modules` (eight),
and `jargon` (at least 32 distinct term/definition/group objects). Use direct,
occupation-specific definitions, not `definition_key`. No PDF paths are needed.

Each module contains:

- `title` and four `terms` matching the course jargon exactly.
- `collocations`: four natural field-specific expressions with meanings or
  short examples, as strings. Vary them across lessons.
- `case`: `function`, `brief`, and `model`. Use a real function key from
  `work_curriculum.WORKSHOPS`. The brief supplies concrete fictional facts,
  constraints, and known unknowns. The 35-65 word model performs the function
  using those facts without making unsupported promises.
- `workshop`: `title`, `goal`, `explanation`, three `frames`, `before`, `after`,
  `reason`, two `questions`, `role_b`, and `challenge`. Each question is a
  short authentic role-labelled dialogue with one `____` gap, four distinct
  `options`, a zero-based `correct_index`, and four option-specific `feedback`
  strings. There must be one defensible answer; alternatives should be
  plausible language or meaning confusions, not absurd misconduct. Match the
  grammar and punctuation surrounding the gap to the answer.

`lesson_conversations` maps `module-1` through `module-8` to:

- `conversations`: exactly three original conversations, each with a distinct
  descriptive `title`, a concrete `setting`, and exactly ten `turns` of
  `[role, speech]`. Use alternating professional/customer roles and 100-150
  spoken words per script. At least one script practices the module's case;
  the others explore distinct situations in that lesson. Every script must
  actually perform its communication function, not just plan a later exchange.
- `additional_scenario`: `title`, `brief`, `role_a`, `role_b`, `opening_line`,
  `complication`, and three `success_checks`. This is a second supported oral
  scenario, distinct from the original case, with enough stated facts to play
  both roles. Do not request open-ended writing.

`dialogues` contains eight further original extended dialogues (one per module),
each with `title`, `setting`, `dialogue` (12 alternating `[role, speech]` turns,
140-200 spoken words), and two `notes` explaining actual useful language.
Do not duplicate or lightly paraphrase the three ten-turn scripts.

## Quality and Safety

Use natural, challenging workplace English with enough support for intermediate
learners. Do not build scripts by substituting job nouns into a generic pattern.
Cases, conversations, scenarios, questions, and definitions must agree. All
numbers and incidents are fictional. Expand unfamiliar abbreviations. Safety,
clinical, legal, financial, and licensed technical decisions belong to authorized
people and local procedures; do not teach hazardous technical steps, clinical
treatment, or universal legal rules. Cite two verified primary occupational
sources per course and explain the language-practice boundary in `scope_note`.

Use the existing six category names. Do not edit shared sources when authoring
an occupation. Validate JSON syntax, counts, ten-turn exchanges, and the
case/question logic before handing it off for review.
