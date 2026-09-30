# Learner-Book Expansion

Requested scope: all 65 courses other than the approved Cross-Cultural
Leadership book. Work is sequential; the user declined parallel assistants.

## Completed

- AI Development English: 102 pages, eight original 20-turn dialogues,
  192 vocabulary entries, 128 phrases, 112 uniform-width bank gaps,
  56 multiple-choice questions, and explained keys for all 168 items.
  Output: `output/pdf/ai-development-english-book.pdf`.
- General IT English: 102 pages with the same counts and explained keys,
  eight field-specific extended conversations, and the matching illustration.
  Output: `output/pdf/general-it-english-book.pdf`.

## Remaining

63 books remain. The next course in the canonical inventory is `law`.
Use `work_curriculum.load_tracks()` for the complete course list and module
order. No other course should be represented as converted or complete.

## Checks and Publication

The new renderer reuses the approved design, embedded fonts, English Ladder
branding, existing course illustrations, uniform blanks, and page references.
The leadership book remains unchanged. The new book is stored separately from
published website downloads, which have not been replaced.

Run `python3 -m unittest discover -s tests -p '*book*.py' -v` for the shared
and book-specific checks. Render and inspect every completed book before
marking it complete. Keep content sources separate and field-specific.
