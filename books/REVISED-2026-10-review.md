# Revised collection review: October 14, 2026

## Delivered scope

80 learner books: the approved Cross-Cultural Leadership edition and 79
field-specific editions using its design system. The collection totals 14,154
pages; individual books range from 136 to 200 pages. Pagination accommodates
the actual content rather than forcing every profession into a fixed length.

Each book contains eight core lessons, eleven extended 20-turn conversations,
eleven short follow-up exchanges, 142 numbered cloze gaps, 96 multiple-choice
questions, 192 core vocabulary entries with collocations, 128 phrase examples,
and four cumulative reviews. The 79 field editions also include 18 additional
language-in-context entries introducing the supplemental dialogues.

## Editorial changes

- Retain each profession's authored situations, responsibilities, terminology,
  figures, and limitations. No universal dialogue with swapped job names.
- Replace repeated phrase examples within a book with intact wording from
  that lesson's own conversation.
- Add terminology retrieval and missing-response exercises using the actual
  field dialogue, its preceding turn, and its following turn.
- Explain all new alternatives, including the original conversational context
  of incorrect missing-response options.
- Preserve the original answer rationales and print the complete corrected
  lines in the short-exchange answer keys.
- Apply targeted wording repairs in `books/revisions/editorial.py` and a
  rewritten cafe handoff conversation in `books/revisions/baristas_cafe_staff.py`.
- Preserve previously checked numerical and professional-scope corrections,
  including the Cardiology timing distinction.

The Leadership pilot's changed-fact reviews remain individually authored.
The other editions use field-specific terminology and exchange-reconstruction
reviews; they are not represented as 79 independently rewritten pilot books.

## Artwork and layout

65 older illustrations were replaced using OpenAI's native image generator.
The approved Leadership illustration and 14 recent medical/specialist
illustrations were retained. All cover illustrations meet at least 300 dpi
at their printed size. The cybersecurity arm/monitor issue was corrected;
additional repairs removed invented packaging claims, an inappropriate child
in a dispensing workspace, an extra hand, a laboratory hand near a face, and
missing kitchen head coverings.

All 80 covers were inspected in rendered PDFs, alongside a dialogue page and
an explained-answer page from each book. These 240 page samples were reviewed
in 20 contact sheets. Enlarged spot checks included the AI answer layout,
vocabulary layout, and corrected Cardiology transfer exercise. This visual
sampling is supplemented by automated checks on every page; it is not a claim
that every page received a separate human visual review.

## Verification receipt

`REVISED-2026-10-results.json` records successful checks for the exact 80 PDF
hashes, with zero failures. All 14,154 pages were checked for embedded fonts,
text boundaries and minimum size, branding, navigation destinations, and
consistent cloze widths. Printed vocabulary, phrases, questions, alternatives,
answers, and explanations were compared with the edition's source material.

The website retains its existing download addresses and uses the new books'
actual section-page map. File-hash version parameters distinguish the new
downloads from cached older editions.

All 163 focused book/course tests passed across the initial run and targeted
reruns after updating three legacy-format expectations. An additional 39-test
run covered the web/book correspondence, publication safety, search metadata,
and deployment verification. All 196 JavaScript interaction tests passed.
The combined site audit passed for 305 pages and 172 PDFs across the whole site.
Desktop (1440 px) and phone (390 px) browser checks covered AI Development,
Cardiology, Cafe Staff, and Leadership, including answering a question and
completing a ten-gap conversation. No horizontal overflow, broken visible
images, or browser script errors were detected in those checks.

A clean export of the staged files packaged 1,099 public assets (620.77 MiB)
with validated local links and hosting size limits. Temporary build duplicates
were removed after byte-for-byte comparison with the installed books.

## Remaining publication gates

These are revised educational PDFs, not certified professional guidance.
Independent subject-specialist review, learner trials, an accessibility
assessment with assistive technology, and a physical print proof have not been
performed. Those checks, plus final trim/bleed and rights review, remain
necessary before a commercial print-book release.
