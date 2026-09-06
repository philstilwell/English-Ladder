# English Ladder: search discovery and finished prompts

The release gives each lesson a distinct search identity, makes all lessons reachable through ordinary links, and puts complete AI prompt text beside the work material. Search visibility and ranking changes require subsequent crawl and search-performance evidence; this audit measures the published implementation.

## Search audit and changes

| Area | Initial audit | Implemented |
| --- | --- | --- |
| Page titles | 29 pages in 10 repeated-title groups | Distinct titles for every indexable page; news and stories identify the reading level |
| Descriptions | 66 pages in 14 repeated-description groups; 72 descriptions under 50 characters | Page-specific descriptions based on the actual teaching material |
| Structured data | None | Publisher and website identity, page descriptions, visible breadcrumbs, collection lists, and 283 learning resources |
| Work discovery | One large course directory | Six subject pages with original guidance, all 41 courses, and relevant grammar links |
| Site navigation | No complete subject index | A browsable lesson index and consistent breadcrumb navigation |
| Search sitemaps | 295 HTML addresses in one file | Five organized maps covering 303 indexable HTML pages and all 252 PDFs |
| Sharing previews | Basic metadata with a single small logo | Consistent Open Graph and Twitter metadata, actual image dimensions and alternative text, and large-image cards where a relevant existing image is available |
| Utility pages | Excluded from sitemap only | Explicit noindex on the missing-page and private saved-learning pages |
| Rebuild protection | Titles and descriptions could revert during generation | Shared publishing integration, persistent content fingerprints, and an automated search audit |

The final inventory contains 305 HTML pages, including the concurrently published AI practice directory. All 303 indexable pages have unique titles and descriptions and are reachable from the homepage. Existing lesson and PDF addresses are preserved.

Titles describe the page rather than repeat a generic site label. Descriptions summarize the actual content; Google may still choose another snippet. See Google's [title guidance](https://developers.google.com/search/docs/appearance/title-link) and [snippet guidance](https://developers.google.com/search/docs/appearance/snippet).

Structured data uses Schema.org [LearningResource](https://schema.org/LearningResource) for self-study materials. It does not claim instructor-led enrollment, qualifications, reviews, or ratings. Google's [course-list requirements](https://developers.google.com/search/docs/appearance/structured-data/course) describe a narrower instructor-led format. Visible breadcrumbs match their [structured representation](https://developers.google.com/search/docs/appearance/structured-data/breadcrumb). This is local syntax and consistency validation, not a claim that Google has awarded a rich result.

The sitemap index separates general pages, work courses, grammar, reading, and PDFs. Modification dates change when the significant published content changes, not when a file is checked out or rebuilt. The process follows [sitemap guidance](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap) and Google's [explanation of accurate lastmod values](https://developers.google.com/search/blog/2023/06/sitemaps-lastmod-ping).

AI instruction panels use `data-nosnippet` on supported section or div elements, helping search snippets describe the lesson rather than repeat directions addressed to an AI. See [Google's supported metadata attributes](https://developers.google.com/search/docs/crawling-indexing/special-tags).

## Complete prompts at the point of use

- Each of 328 work lessons has four complete prompts beneath it: vocabulary, grammar, interactive role-play, and writing feedback.
- Each of 368 Conversation Lab dialogues has two complete prompts: interactive rehearsal and additional professional scenario dialogues. The full original exchange is included.
- These 2,048 directly available prompts start with the actual task instructions. Lesson facts, language guidance, roles, and relevant source material are already filled in. Students do not need to compose or improve a prompt.
- Each of the 41 courses also has a downloadable text collection. Across the collections there are 3,360 finished prompts, including all eight practice modes for every lesson.
- Copy buttons copy the exact displayed text. If clipboard access is unavailable or denied, the complete text is selected for manual copying. Without JavaScript, the full text remains accessible through native disclosure controls.
- The existing adjustable workshop and the newer reading, grammar, everyday-English, and study-tool extensions are preserved. Private drafts are never added to the copied text.

The original Conversation Lab PDFs and their embedded-font prompt appendices remain intact. The newer grammar PDF editions from the current main branch are retained. This release does not render or alter PDFs, generate images, or contact an AI service.

## Validation and next measurements

`audit_site.py` checks the page structure and local links. `audit_seo.py` checks unique metadata, canonical addresses, sharing images, structured-data references, breadcrumb consistency, subject coverage, homepage reachability, sitemap contents, and index exclusions. Tests also cover stable modification dates, the complete material in every published work prompt, all downloadable prompt blocks, and clipboard success and failure.

All 133 automated tests pass: 79 Python tests and 54 browser-interaction tests. A full unchanged rebuild leaves every search-content record and modification date unchanged.

Real Chrome checks cover desktop and 375-pixel mobile layouts, exact clipboard contents, denied clipboard access, native disclosures with JavaScript disabled, and the new subject navigation. These checks do not certify comprehensive accessibility or professional subject-matter accuracy.

The remaining measurement step is in the owner's Google Search Console property: submit `https://englishladder.com/sitemap.xml`, inspect representative course, grammar, news, and subject pages, then compare indexing, impressions, queries, and click-through rates after recrawling. Search Console access was not available in this task, so no submission or traffic improvement is claimed. Use observed query and engagement data to guide future content priorities rather than guessing search volume.

To maintain the release without paid generation:

```sh
python3 generate_efsp_web_pages.py
python3 update_site.py --refresh-pages
python3 audit_site.py
python3 audit_seo.py
npm test
npm run check:js
```

Metadata and subject copy live in `seo_content.py`; shared search publishing lives in `seo.py`. Keep `content/seo-index.json` under version control to preserve honest modification dates. Finished work prompts are published by `work_ready_prompts.py` using the existing authored practice instructions and curriculum.
