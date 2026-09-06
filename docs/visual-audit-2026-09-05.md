# Visual audit — 5 September 2026

The site now uses a recognizable Gemini-generated ladder mark, a matching favicon, more open typography, consistent cobalt controls, and restrained neutral surfaces.

## Findings resolved

- Uneven CSS ladder rails and tightly spaced wordmark: replaced by a square, three-rung Gemini symbol with a 40px display size and a separate favicon.
- Crowded homepage at tablet widths: the story and photo now stack below 800px; level choices and navigation wrap naturally.
- Mixed brown/green/blue gradients, oversized shadows, and inconsistent controls: standardized across grammar, work courses, practice tools, and everyday-English modules.
- Unrelated Japanese subway photos introducing US life and workplace English: replaced with useful language examples and a typographic conversation preview.
- Grammar artwork shifting the surrounding content: reserved intrinsic dimensions and a stable frame; placed the enlargement control below the artwork so it cannot cover instructional text. Directory thumbnails load on demand.
- Search label separated from its field: grouped the label and input in the work directory.
- Workbook link extending beyond phone screens on all 41 work courses: allowed the section header and link text to wrap.
- Inconsistent navigation state on nested grammar and work pages: the parent study section is now highlighted.

## Verification

- All 100 published HTML routes rendered at 390px, 768px, and 1280px: 300 checks, with no page-level horizontal overflow, missing brand marks, or failed loaded images. Lazy images outside the viewport were not forced to load by this check; source-file/link validation covers those asset paths.
- Visually inspected representative homepage, news, curated lesson, grammar directory/detail, work directory/detail, tools, US life, and credits templates. Checked the homepage at desktop, tablet, and phone sizes.
- Browser interaction checks: course search filtered to the expected result; lesson steps, correct-answer feedback and progress, discussion, and the grammar enlargement dialog worked. The dialog closed correctly.
- Existing automated checks: 31 Python tests and 13 JavaScript interaction tests passed; script syntax checks passed; all internal links, image paths, and page IDs validated.
- Existing instructional diagrams were preserved and reframed. This pass changes the website presentation; it does not redraw the 44 teaching diagrams or regenerate downloadable PDFs.
- One Gemini web image generation, with no incremental API charge. Only conventional resizing was applied to the generated image.

The adjacent JSON file lists the complete route coverage.
