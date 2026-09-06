# English for Work quality review - September 5, 2026

## Coverage

Reviewed the full directory, 41 course pages, their curriculum sources, and all 164 linked PDFs. The original PDFs contained 2,330 pages and approximately 747,110 words. All 164 used unembedded standard fonts.

## Problems addressed

- The 31 batch courses used essentially the same model response and decision exercise with industry nouns substituted. Some multiple-choice distractors were fragments unrelated to the question.
- Several specialist courses assigned vocabulary by its position in a long list rather than by lesson topic. For example, the AI context-window lesson and legal intake lesson received unrelated term groups.
- 697 distinct terms had keyword-generated or placeholder-style definitions. The new shared glossary replaces those explanations; 834 course entries now reference the authored glossary, with additional precise inherited definitions retained.
- Guided selections had displaced useful speaking and writing. Learners had little opportunity to construct, revise, or compare their own messages.
- The culture material overgeneralized behavior by nationality. It now teaches checking preferences, making responsibilities explicit, including quieter participants, and discussing observable behavior.
- Dense tables, small type, and repeated passages made the PDFs harder to use. Their purposes were insufficiently differentiated.

## Revised learning experience

- 328 distinct fictional cases and 328 context-specific model responses, covering the existing eight topics in each course.
- Twelve communication workshops: clarification, explanation, qualification, comparison, updates, requests, negotiation, handoffs, repair, facilitation, feedback, and constructive disagreement.
- 656 short language checks with answer-specific explanations. The shared patterns recur intentionally; the page tells learners why they repeat.
- Speaking roles, follow-up questions, a harder second round, short writing tasks, four feedback criteria, and a final integrated challenge.
- 1,525 defined course vocabulary entries, plus 48 additional semiconductor terms. Related courses now share a relevant professional category.
- Searchable course directory and vocabulary, readable lessons without JavaScript, and optional browser-only drafts and practice progress. No model-based grading or paid service was added.
- Four rebuilt document types with writing space, answer sections, navigation bookmarks, current brand mark, and embedded fonts. Existing PDF URLs are unchanged.

## Validation

- 41 Python tests and 19 JavaScript tests pass, including all course initialization, search, quiz correction, optional storage, malformed/blocked storage, navigation, local links, content coverage, and PDF checksum synchronization.
- Every one of the 164 PDFs passed the automated document audit: 2,477 pages, approximately 548,946 words, all fonts embedded, no detected out-of-bounds body text, no replacement glyphs, and navigation bookmarks present. Detailed results are in `work-document-audit-2026-09-05.json`.
- Rendered document proofs were inspected for covers, lesson content, writing space, answer sections, vocabulary, and long titles. The new material has fewer words despite more writing space and larger type.
- The Mac was locked during the attempted browser review. Browser layout inspection remains a separate limitation; simulated-document tests do not verify appearance on screen.

## Maintenance

The website and PDFs now share the same authored content. Legacy PDF command-line entry points delegate to the current generator. Publication tests reject changed curriculum with stale PDF files. Paid image, audio, or content-generation services were not used for this revision.
