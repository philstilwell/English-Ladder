# Revised Learner Books on the Web

The 80 English for Work course pages now expose the teaching content of the
approved October 2026 learner books. The PDF files and their print sources are
unchanged by this web release.

## Content

- Eight lessons retain the A-F sequence, 192 vocabulary entries and collocations,
  128 purpose-based phrases, eleven extended cloze conversations, and the
  existing 24 shorter web conversations.
- Each lesson adds four spoken-expression examples, two wording comparisons,
  two accuracy questions, and a second-take response question from its book.
- Four cumulative reviews follow lessons 2, 4, 6, and 8, with four questions each.
- Each page has 96 book questions plus 44 follow-up dialogue choices: 140
  questions in total. The eleven long conversations remain separate cloze tasks.
- Follow-up exchanges retain every turn, including the ungapped lines in the
  Leadership book. A complete-script disclosure supports spoken rehearsal.
- The 79 field books' additional cases include their 18 language-in-context
  entries. Leadership retains its revised case facts, records, and delivery notes.
- Professional communication notes and actual PDF page links accompany the
  activities. All new supplementary disclosures start closed.
- Where the book supplies distinct explanations for alternatives, selecting an
  answer displays that alternative's explanation. Shuffling preserves the
  association between a choice and its explanation.

## Illustrations and Navigation

The new page illustrations are uncropped WebP derivatives of the exact approved
book-cover assets. `assets/work/course-art/manifest.json` records the source and
derivative hashes. Two sizes per course support small screens and sharper large
displays; print-master images are still excluded from public deployment.

The existing small profession icons, compact sticky menu, six subsection dots,
Prompts link, and open-lesson borders remain in place. Course activities do not
save answers or completion records. Answers, explanations, and complete scripts
remain readable without JavaScript.

## Rebuilding and Checking

Run `python3 generate_efsp_web_pages.py` after publishing approved book revisions.
It checks book publication records, prepares the web illustrations, and rebuilds
the pages and search metadata. `work_web_content.py` is the adapter between book
sources and web activities; do not replace this material with generic scenarios.

`tests/test_work_web_books.py` checks every course's dialogue text, word banks,
questions, explanations, new reviews, page references, and cover derivatives.
The browser audit in `audit_work_browser.cjs` checks the 87 work pages at 320,
390, 768, and 1280 pixels, expanded content, review interactions, deep links,
and access to answers without JavaScript. Its report explicitly describes the
limits of the checks; it is not professional-content or accessibility certification.

Release checks passed: 61 focused Python tests, 15 search/history tests, eight
editorial-quality tests, and 46 browser-script tests. The site audit passed for
305 pages. The browser audit recorded 348 default layouts, 320 expanded layouts,
240 review/accuracy interactions, 160 cloze interactions, and 87 no-JavaScript
pages, with no errors. See `work-book-web-audit-2026-10-14.json`.
