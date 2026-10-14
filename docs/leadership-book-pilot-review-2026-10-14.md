# Cross-Cultural Leadership: Revised Book for Approval

This is an isolated revision of the leadership book, not a rollout to the other
79 books. The published PDF, course webpages, shared builders, and existing
download links are unchanged. Work is saved on `codex/leadership-book-pilot`.

## Review Files

- Main review PDF: `output/pdf/cross-cultural-leadership-english-book-revised.pdf`
- Reflowable companion: `output/pdf/cross-cultural-leadership-english-book-revised.epub`
- Paginated HTML: `output/pdf/cross-cultural-leadership-english-book-revised.html`
- Counts and production status: the adjacent `-manifest.json` file.
- Geometry and link checks: the adjacent `-layout.json` file.

The PDF is the primary approval deliverable. The EPUB is a companion edition
with resizable text and internal links, not a certified accessible publication
or a substitute for testing in actual reading applications.

## What Changed

- All eight main 20-turn conversations were rewritten. Two now include three
  speakers. Concrete work, questions, concessions, interruptions, and corrections
  replace excessive explanatory dialogue.
- Three additional 20-turn conversations were retained and refined. The capacity
  case now uses six analyst-days across a team, not six workdays for one analyst
  in an ordinary week. Its unsupported completion promise was replaced by a
  bounded scheduling update.
- Eleven six-turn transfer exchanges apply the language to new facts. Each main
  lesson adds a second-take question that changes one fact and requires an
  updated spoken response.
- The book has 96 four-option questions: 80 in the lessons and 16 in four
  cumulative reviews. Every choice, including each incorrect alternative, has
  an explanation. Options are shuffled deterministically; correct positions
  are A:23, B:25, C:25, D:23.
- Every one of 142 cloze gaps has an explanation. Word banks are shuffled;
  numbered blanks remain exactly 100 points wide regardless of answer length.
  Several interchangeable bank entries were revised to reduce ambiguity.
- The existing 192 vocabulary entries and 128 distinct phrases were preserved.
  There are 191 distinct vocabulary headwords because "impact" is deliberately
  revisited. The index has one entry per headword with all relevant references.
- Thirty-two pronunciation/stress spotlights add contextual examples and usage
  contrasts. Each lesson contrasts everyday speech with written or more formal
  wording. Eight realistic trackers, authority cards, or handoff records anchor
  the briefing questions.
- Cultural notes distinguish disagreement from disrespect without assigning
  personalities to nationalities. The audience remains all international
  managers, not only managers from Japan or China.

## Design and Digital Preparation

- 136 US Letter pages, designed at their actual size, not reduced from a larger
  page. No artwork reaches a trim edge, so this interior requires no bleed.
- Mirrored inner/outer margins of 0.8/0.65 inches; no edge-hugging chapter tabs.
- Blue, coral, gold, and plum accents on white, with pale neutral-blue panels.
  No sea-green background. English Ladder branding remains on every page.
- Three embedded Bitstream Vera fonts. Smallest text is 7.5 points; answer text
  is 9.7 points. Uniform 100-point blanks carry discreet 7.5-point numbers.
- New original cover artwork at 1536 x 1024 pixels, displayed 4.65 inches wide,
  approximately 330 pixels per printed inch. The existing site icon is unchanged.
- The PDF has language metadata, a semantic structure tree, heading tags,
  image description, chapter bookmarks, clickable references, and return links.
  These improvements are not a claim of PDF/UA certification or a completed
  screen-reader audit.
- References include readable publication details and full URLs for print.
  There is no promised audio product, unpublished QR destination, ISBN, or
  claim of independent professional certification.

## Useful Review Stops

- Pages 1-3: cover, book map, cultural framing.
- Pages 4-12: one complete revised lesson and its progression.
- Pages 18-19: three-person discussion with substantive pushback and a boundary.
- Page 40: a guided transfer followed by a changed-fact response.
- Pages 80-88: the additional workplace conversations and transfer exchanges.
- From page 89: explanations, including why each incorrect choice fails.
- From page 130: the consolidated vocabulary index.

## Remaining Publication Gates

These require actual people, publishing choices, or a physical object. They
have not been represented as completed:

1. An experienced ESL teacher and a working international manager should check
   naturalness, ambiguity, cultural nuance, and difficulty.
2. Pilot representative units with learners; record ambiguous responses,
   completion times, and unsupported assumptions about proficiency.
3. Choose the printer, final trim size, paper, and color option. Obtain a cost
   estimate before ordering a physical proof or commissioning paid services.
4. Review that proof for readability, color, binding comfort, and image quality.
   Then create the printer-specific back/spine/front wrap. The included cover
   is the learner-book title page, not an upload-ready wraparound cover file.
5. Test reading order with a screen reader and the EPUB in actual reader apps;
   run formal accessibility and EPUB conformance checks before claiming them.
6. Decide distribution, identifiers, licensing, and any audio production.
   The book records AI-generated text and illustration; publisher forms still
   require accurate disclosure. No paid reviewer, voice generation, print
   order, repository installation, or external API service was used here.

## Verification Completed

- All 10 new pilot tests pass, including every printed question and explanation,
  actual PDF link destinations versus printed page references, all embedded fonts,
  all 136 pages' text boundaries and minimum type size, and EPUB structure/links.
- All 14 existing leadership-book tests pass against the untouched original.
- Browser layout checks report no overflowing text, missing link targets, or
  duplicate identifiers. All 142 blanks have the same rendered width.
- Actual PDF renders of the cover, a complete extended conversation, a transfer
  page, answer explanations, and the index were visually inspected. Additional
  layout previews covered the case record, vocabulary, and phrase pages.
- This is production checking, not independent subject-matter validation,
  formal accessibility certification, or evidence from a learner trial.

## Rebuild and Verify

Use the existing document dependencies and Playwright. No new dependency or
external repository installation is needed.

```sh
python3 build_leadership_pilot.py
node print_leadership_pilot.cjs
python3 build_leadership_pilot.py --finalize
python3 -m unittest tests.test_leadership_pilot -v
```

`CHROMIUM_EXECUTABLE` can point the print step to an already-installed Chrome
or Chromium executable. The print step fails rather than exporting a PDF if
text overflows, link targets are missing, or IDs are duplicated. Answer keys
and indexes paginate according to their actual content. The finalization step
adds author metadata and a concise, nested bookmark outline while preserving
the existing semantic tags and links.

## Cover Artwork Record

- Tool: OpenAI native image generator, explicitly selected by the user after
  notice that it uses the account's image-generation allowance and that a dollar
  estimate was unavailable.
- Asset: `assets/work/leadership-book-cover-2026.png`.
- One generation; no paid API fallback and no post-generation image editing.
- Prompt:

> Use case: illustration-story. Create a high-resolution, print-quality editorial illustration for the English Ladder Cross-Cultural Leadership English learner-book cover. A diverse group of four adult international managers in contemporary business-casual clothing around a shared table, in constructive, attentive discussion of a small project schedule: one person makes a measured open-hand point, one listens, one indicates a document, one takes notes. Equal professional status, no exaggerated hostility, no national flags or stereotypes. Elegant crisp hand-illustrated miniature with fine dark outlines, softly modeled forms, realistic adult proportions and hands, polished educational publishing style. Palette: cobalt and clear medium blue, restrained coral and gold, neutral white and charcoal; no sea-green background. A few relevant objects only: laptop, paper schedule, pen, water glass. Entire group and table visible with generous white negative space, no enclosing frame. Landscape composition at least 1536 by 1024 pixels if supported. Pure white background. No text, no letters, no watermark, no logo; the real English Ladder brand will be placed separately in layout. Visually clear when printed 4.5 inches wide.
