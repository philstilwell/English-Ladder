# English for Work audit — 1 October 2026

Audited the directory, all six category pages, and all 66 course pages. The
review covered responsive layout, navigation, search, lesson interactions,
progressive enhancement, course/download descriptions, content structure,
internal links, search metadata, reference-link availability, and the 66
existing learner books. No paid generation was used.

## Changes implemented

- **Consistent directory title.** English for Work now uses the same shared
  `.page-hero` heading rule as Everyday English and Grammar. Browser measurements
  are identical: 34.4 px at 320, 390, and 768 px viewport widths; 56.32 px at
  1280 px. The previous Work title was 54.4 px at 390 px and 89.6 px at 1280 px.
  The introduction retains its existing wording and illustrations.
- **Faster access to courses.** Reduced excess introductory spacing and added a
  prominent “Browse all 66 courses” link to the searchable directory.
- **More forgiving search.** Course and vocabulary searches normalize accents
  and punctuation. Course search also includes field names. “CAFÉ-staff”, for
  example, finds the cafe course. Clear filters recovers from an empty result
  and returns keyboard focus to the search field. Restored form values are
  reapplied when the browser returns to the page.
- **Reliable section links.** Direct glossary links open the glossary and land
  below both sticky menus. Direct links to a complete prompt reveal its enclosing
  lesson and prompt panels before scrolling. Invalid fragments do not interrupt
  lesson controls.
- **Accurate course descriptions.** All 66 category cards now say “1 learner
  book” instead of the retired “4 free guides”. Directory instructions distinguish
  web conversations from the extended conversations and word-bank gaps in the
  learner books. Maintenance documentation no longer describes removed draft
  or progress-saving controls.
- **Useful pages without JavaScript.** Search controls remain hidden until their
  behavior is available. Every course link, lesson, answer explanation, glossary
  entry, PDF link, and complete prompt remains in the readable HTML.
- **Durable publication.** Changes live in the generators and shared styles and
  scripts. Rebuilt all affected pages and their search index; versioned the
  changed browser assets so returning readers receive the current controls.

## Verification

- `npm run check:js`: passed.
- `npm test`: 341 Python tests and 185 JavaScript tests passed. Added regression
  coverage for accent/punctuation search, category text, restored filters,
  clearing filters, no-JavaScript controls, nested fragment links, and current
  category-card book descriptions.
- `python3 audit_site.py`: all 289 published pages passed the existing internal
  link, metadata, curriculum, and news checks.
- `node audit_work_browser.cjs`: 292 default-layout checks and 264 fully expanded
  course-layout checks, across widths 320, 390, 768, and 1280. No detected page
  overflow, clipped teaching labels/text, broken images, duplicate main headings,
  or browser script errors. Checked an answer and glossary filtering on every
  course; checked all 73 pages with JavaScript disabled. Also checked keyboard
  lesson navigation, glossary and nested prompt links, actual clipboard copying,
  and the manual selection fallback. See
  [the browser results](work-browser-audit-2026-10-01.json).
- Visually reviewed desktop/mobile directory and course views. A final directory
  check confirmed matching title sizes and a 20 px gap between its browse action
  and optional AI-practice link after spacing refinement. Screenshots are local
  review artifacts in `output/playwright/work-audit/`.
- Re-ran the full existing PDF audit: 66 books, 6,732 pages, all fonts embedded,
  matching checksums/page counts, navigation bookmarks, no detected text-boundary
  errors or replacement glyphs. The result was byte-identical to
  [the existing publication report](work-book-publication-audit-2026-10-01.json);
  the PDFs were not regenerated.
- Checked all 64 distinct course reference URLs: 25 returned HTTP 200, 37 returned
  HTTP 403, and two connections were reset. There were no observed HTTP 404/410
  responses. Refusals and connection failures are unverified links, not proof of
  dead pages; no reference was replaced solely because it blocked this check.

## Content review and limits

Automated curriculum validation covered all 528 lessons, 2,339 glossary entries,
1,584 ten-turn web conversations, answer-key structures, local links, and learner
book publication consistency. Manual editorial sampling covered one original
course and one occupation course in each of the six categories, comparing case
facts, model responses, language questions, and conversation openings. The
samples retained uncertainty and known facts; specialist courses distinguish
language practice from real professional procedures. No curriculum rewrite was
justified by those samples.

The original courses deliberately reuse some general communication questions
across fields; the newer occupation courses use field-specific dialogue gaps.
Replacing all shared questions would be a separate curriculum revision requiring
its own editorial and book synchronization review. The current audit does not
claim a sentence-by-sentence expert review of every professional domain or full
screen-reader/accessibility certification. External reference availability
remains partly unverified because of the refusals described above.

For future work-page changes, run the existing site/tests plus
`node audit_work_browser.cjs` against a local server on port 8878 (or set
`AUDIT_ORIGIN`). The browser audit closes every browser context it creates.
