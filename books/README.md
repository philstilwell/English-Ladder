# English for Work Learner Books

The approved leadership book is the design and content-depth reference. New
books are independently authored, not noun substitutions in a common scenario.

Each `<slug>_content.py` exports `BOOK`, containing the course metadata and eight
units in the existing webpage order. `books.authoring.unit` accepts compact
tables of explicitly authored material. It does not generate teaching prose.

Each unit contains 24 defined terms with natural collocations, 16 phrases,
six language notes, three briefing questions, four language questions, a
coherent 20-turn dialogue of 350-520 words with ten numbered cloze gaps, and
a four-turn transfer cloze with a separate situation. Every question and gap
has an explanation. Cloze answers use one shuffled bank and identical blanks.

Each complete book is 102 pages, including an illustrated cover, linked
contents, professional communication notes, explained keys, quick phrases,
linked vocabulary index, sources, and the author's copyright. Fonts are
embedded. No teacher guide, open-ended writing task, or sea-green background
is included. Primary references are checked during authoring.

Build: `python3 build_industry_books.py ai-development`

Final books are in `output/pdf/`. Existing website downloads are not changed
by this workflow. Incomplete sources must never be represented as completed
books or published downloads. The complete inventory remains `load_tracks()`
in `work_curriculum.py` (66 courses, including the approved leadership book).
