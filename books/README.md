# English for Work Learner Books

The collection contains 80 courses. The approved Cross-Cultural Leadership
pilot is the design reference for the October 14, 2026 edition.

## Content

Each field has eight lessons in website order, 192 defined vocabulary entries
with collocations, 128 distinct phrase examples, eleven 20-turn conversations,
eleven short follow-up exchanges, 142 numbered cloze gaps, 96 multiple-choice
questions, and four cumulative reviews. All questions and gaps have explained
answers. Cloze blanks have equal widths, independent of answer length.

The 79 industry editions retain their independently authored cases, terminology,
and extended conversations. `books/revised_edition.py` adapts those sources to
the approved design; `books/revisions/` holds targeted editorial revisions.
New retrieval questions use that lesson's real terms and conversation turns,
not a generic dialogue with profession names substituted. An additional 18
language-in-context entries introduce the three supplemental conversations.
Original professional scope limitations and reference-check dates are retained.

The Leadership pilot has separately authored cumulative reviews and changed-fact
tasks. Industry reviews instead test terminology and reconstruction of exchanges
using both neighboring turns. No open-ended writing tasks or teacher guide are
included. The books are not professional practice instructions.

## Design And Outputs

The shared HTML print renderer uses white pages, blue/coral/gold accents,
embedded Vera fonts, illustrations at 300 dpi or above, linked contents and
indexes, tagged PDF structure, bookmarks, and live answer-page references.
Pagination follows the length of each field's content rather than a fixed count.
Every page includes English Ladder branding and a clickable website footer.

Canonical PDFs and revision records are in `output/pdf/`. The site serves exact
copies at stable `pdf/efsp/` addresses. `content/work/documents.json` records
hashes, page counts, and actual section pages. Website links use those pages and
a file-hash version parameter. The approved Leadership HTML/EPUB review assets
remain available separately.

65 older cover illustrations were replaced with OpenAI native-generated PNGs
in `assets/work/book-covers/`. The 14 recent medical/specialist illustrations
and approved Leadership illustration were already print-ready. The print masters
are embedded in the PDFs and excluded from the public assets package.

## Build And Publish

Use the project Python environment with pypdf, pdfplumber, ReportLab, Pillow,
and the installed Playwright browser. No paid service is called by these steps.
Set `BOOK_NODE` and `CHROMIUM_EXECUTABLE` if runtime discovery is unavailable.

```sh
python3 build_revised_collection.py --all --skip-current
python3 audit_revised_books.py --staged
python3 install_revised_books.py
python3 generate_efsp_web_pages.py
python3 audit_revised_books.py --published --quick
```

Pass one or more course slugs instead of `--all` for a targeted staged build.
The installer requires a complete, current 80-book full-geometry audit before
replacing the public collection. Editing source content, design, print code, or
cover artwork invalidates the corresponding record. Build and audit again.

The legacy `build_industry_books.py` and `build_leadership_book.py` remain for
historical sources; do not use them to publish this edition.

## Verification

`audit_revised_books.py` checks all printed questions, alternatives, explanations,
vocabulary and phrases; embedded fonts; page margins and text size; image
resolution; consistent blank widths; navigation; and content/file freshness.
Continuation headings retain their original inline formatting, including the
colored section-letter circle. The renderer compares each continued heading
with its source, and the PDF audit checks the printed circle, color, and white
letter against the recorded layout.
`books/REVISED-2026-10-results.json` is the receipt for the exact delivered PDFs.
The focused tests also preserve earlier technical corrections, including the
Cardiology update-time versus review-time distinction.

Automated checks and editorial inspection are not an independent subject-expert
review, learner trial, certified accessibility assessment, or physical print
proof. Those remain prerequisites for a commercial print release. Historical
audit records are retained with their original dates rather than rewritten as
new expert verification.
