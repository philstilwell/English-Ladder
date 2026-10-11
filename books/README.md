# English for Work Learner Books

The approved leadership book is the design and content-depth reference. New
books are independently authored, not noun substitutions in a common scenario.

Each `<slug>_content.py` exports `BOOK`, containing the course metadata and eight
units in the existing webpage order. `books.authoring.unit` accepts compact
tables of explicitly authored material. It does not generate teaching prose.

Each unit contains 24 defined terms with natural collocations, 16 phrases,
six language notes, three briefing questions, four language questions, a
coherent 20-turn dialogue of 220-520 words with ten numbered cloze gaps, and
a four-turn transfer cloze with a separate situation. Every question and gap
has an explanation. Cloze answers use one shuffled bank and identical blanks.

Each book also has three separately authored scenarios in `books/additional/`,
each with a 20-turn conversation, six gaps, a four-turn transfer and explained
answers. `books.supplements` parses and validates these authored scenes.
The expanded edition has eleven extended conversations and eleven transfers,
a 37.5% increase over the original eight of each.

Each complete book is 114 pages, including an illustrated cover, linked
contents, professional communication notes, explained keys, quick phrases,
linked vocabulary index, sources, and the author's copyright. Fonts are
embedded. No teacher guide, open-ended writing task, or sea-green background
is included. Primary references are checked during authoring.

Every page, including the cover and answer keys, has a centered, clickable
`ENGLISHLADDER.COM` footer. The course title remains on the left, with the author
and page number on the right. The shared `Book.new_page` template supplies this
footer; the PDF audit checks its presence, position, link, and corner clearance
on every page.

Build: `python3 build_industry_books.py ai-development`

Build all: `python3 build_leadership_book.py`, then
`python3 build_industry_books.py --all`.

Audit the rebuilt masters: `python3 audit_work_books.py`.
Audit current public copies: `python3 audit_work_books.py --published`.
The field-specific editorial record is `books/AUDIT-2026-10.md`.

Final books are in `output/pdf/`. Existing website downloads are not changed
by this workflow. Incomplete sources must never be represented as completed
books or published downloads. The complete inventory remains `load_tracks()`
in `work_curriculum.py` (66 courses, including the approved leadership book).
