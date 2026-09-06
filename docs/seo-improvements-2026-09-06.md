# English Ladder search improvements

English Ladder now explains each page's teaching purpose to search engines, connects related lessons with visible links, and publishes a complete map of its public HTML pages and PDF guides. These changes apply to existing material and to future daily lessons.

## Before and after

| Check | Before | After |
| --- | ---: | ---: |
| Pages in duplicate title groups | 29 | 0 |
| Pages in duplicate description groups | 66 | 0 |
| HTML pages with structured information | 0 | 305 |
| Sitemap addresses | 296 | 555 |
| Linked PDF guides listed in the sitemap | 0 | 252 |

There are 303 indexable HTML pages, including six professional subject directories and a browsable directory of all lessons. My learning and the error page have explicit `noindex, follow` instructions and are excluded from the sitemap. The [machine-readable audit](seo-audit-2026-09-06.json) contains counts and representative titles, descriptions, and canonical addresses.

## What changed

- Search titles and descriptions identify the grammar topic, workplace field, or reading level. News titles and descriptions identify the release date and describe a reading exercise, so future releases can reuse a headline without creating duplicate metadata. Older long advanced headlines can use the same story's shorter beginner headline in the search title; the actual advanced lesson heading and text remain intact. Workplace descriptions use the field-specific introduction, replacing category-only descriptions.
- The homepage has a stable, visible introduction to free English lessons above the changing featured story. Existing links and level selection continue to open the current lesson.
- Breadcrumb navigation appears on inner pages, with matching structured breadcrumb information. All 44 grammar lessons have deliberately chosen related topics. Reading lessons link to the grammar library and matching concepts where available; workplace pages connect to useful communication grammar. Everyday English links to the related story readings.
- Structured information identifies the English Ladder website and publisher, collections of lessons, learning resources, study levels, source citations where available, and linked PDF editions. It does not invent teacher credentials, ratings, enrolments, or news bylines. `LearningResource` describes the self-study materials; no claim of eligibility for Google's instructor-led Course rich result is made.
- Every page has a consistent HTTPS canonical address, matching Open Graph information, and Twitter/X preview fields. Internal home links use the root address. Different reading levels remain separate canonical pages because their content differs. The rolling seven-lesson pages remain collection pages, with permanent links to dated lessons.
- Relevant existing photographs and saved daily illustrations appear on permanent lesson pages and supply sharing previews. Original credits and the distinction between photographs and generated illustrations remain visible. Pages without a relevant large image use the actual brand mark with a small-card preview.
- Repeated AI tutoring instructions use `data-nosnippet` on supported HTML containers, reducing the chance that prompt boilerplate becomes the search description. This does not hide the prompts or change the copy controls.
- The sitemap index links to five subject maps covering canonical HTML pages, all linked PDF guides, and visible content images. Page modification dates follow changes to meaningful content, descriptions, or links, not routine rebuilds or elapsed-age labels. PDF dates retain their known edition dates and change when the document bytes change. The daily workflow saves this history in `content/seo-index.json`.

## Integrated workplace additions

The release preserves the independently published six professional subject directories, their course links, and the HTML directory at `sitemap.html`. It also retains 3,360 complete workplace prompts and all 41 downloadable prompt collections. Workplace grammar recommendations follow each course’s communication functions; the 44 grammar pages use a separate curated map of related patterns. These additions share one metadata publisher and one sitemap history, avoiding competing search descriptions or duplicate structured data.

## Validation and limits

The integrated release passed 91 Python checks and 54 JavaScript interaction checks. The complete site audit covers 305 pages, local links and fragments, unique metadata, structured-data consistency, image files, canonical addresses, and the 555 sitemap entries. Automated tests cover level distinctions, future lessons, safe structured-data serialization, repeat publishing, related links, relevant images, homepage identity, and stable modification dates. Existing grammar, workplace, saving, and AI prompt interaction checks remain part of the release checks. Browser checks covered the homepage and representative curriculum pages at desktop and 320-pixel phone widths, including long archive headlines, breadcrumb wrapping, and the absence of horizontal overflow.

These are publishing and browser checks, not a claim that Google has indexed the revised pages or awarded rich results. Search Console performance and field Core Web Vitals were not available through a connected account. No traffic, ranking, or speed improvement is invented. Existing teaching content and PDF files were not rewritten as part of this search release.

For subsequent measurement, use the verified English Ladder property in Google Search Console: submit the sitemap, inspect the homepage plus a grammar, work, and dated reading page, and compare impressions and clicks by curriculum over comparable periods after recrawling. Keep branded searches separate when assessing discovery by new learners. Review excluded-page reasons before treating them as defects; deliberate `noindex` pages and alternate homepage addresses are expected.

## References used

- [Google's title-link guidance](https://developers.google.com/search/docs/appearance/title-link): descriptive titles that reflect visible page content.
- [Google's snippet guidance](https://developers.google.com/search/docs/appearance/snippet): unique, useful descriptions and supported `data-nosnippet` containers; there is no fixed character limit guaranteeing a particular result.
- [Google's sitemap guidance](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap): canonical addresses and meaningful, accurate modification dates.
- [Google's breadcrumb guidance](https://developers.google.com/search/docs/appearance/structured-data/breadcrumb): a useful user path and corresponding structured information.
- [Google's site-name guidance](https://developers.google.com/search/docs/appearance/site-names) and [general structured-data policies](https://developers.google.com/search/docs/appearance/structured-data/sd-policies): consistent site identity and claims supported by the page.
- [Schema.org LearningResource](https://schema.org/LearningResource): describe educational materials without misrepresenting self-study pages as an enrolled, instructor-led course.
