# English Ladder and English Road design guide

A shared visual and interaction standard for the English Road redesign

Version 1.0 · September 6, 2026 · Prepared for Phil Stilwell and the implementation team

Use English Ladder’s current editorial style as the starting point for English Road. Both sites should feel like parts of the same learning service: warm white pages, charcoal text, generous spacing, and straightforward language. Keep English Road green and English Ladder cobalt blue so each site remains recognizable. Learners should recognize the navigation and controls immediately when they move between the sites.

This guide specifies the next implementation. It separates the shared design rules from the different learning tasks each site supports. The first priority is to align the page header, neutral colors, typography, buttons, and question presentation across English Road’s three main pages, retaining green as its primary accent.

## The role of each site

| Site | Main purpose | Keep distinctive |
| --- | --- | --- |
| English Ladder | Learn through daily stories, grammar explanations, and workplace lessons. | Editorial story imagery, dated lessons, and the Read → Practice → Discuss sequence. |
| English Road | Estimate a learner’s level and provide focused practice quizzes. | The 100-question level check, 25-question practice quizzes, six CEFR choices, and unofficial reports. |

CEFR means the Common European Framework of Reference for Languages. Its A1 to C2 labels describe language proficiency. English Road also shows its own internal levels; these must remain visually separate from CEFR labels.

## The decisions to carry through

- Keep English Road’s green identity across Home, Level Check, Practice, and reports. Keep English Ladder cobalt blue.
- Use normal body weight for explanations and reserve bold text for headings, labels, and the main action.
- Use the same button appearance and feedback vocabulary for the same kind of action.
- Give the question more visual space than progress statistics or promotional content.
- Keep the current question bank, scoring, answer order rules, language help, and report calculations intact during the style change.
- Make navigation between the two sites explicit and useful, while keeping each site’s name visible.

**Reference hierarchy:** the exact values in this guide are the proposed common standard. English Ladder’s `editorial.css` and `learning.js` provide working examples. Its specialist `work.css` theme is a local variation, not the default for English Road.

<!-- pagebreak -->

# Changes to make on English Road

The following differences were visible in English Road’s live home, practice, and level-check pages on September 6, 2026. The proposed changes apply consistently across those pages.

| Current presentation | Change to make |
| --- | --- |
| Large illustrated title banners occupy much of the header. | Use a compact brand mark and text wordmark. Put the page title in real heading text below the navigation. |
| Olive and cream on Home and Level Check; a separate blue theme on Practice. | Use warm white and charcoal on all three pages, with green primary actions throughout English Road. Keep blue as English Ladder’s identity. |
| Large shaded panels, background gradients, and substantial shadows. | Use flat surfaces, thin gray dividers, and spacing. Reserve bordered cards for questions, controls, and reports. |
| Many introductory sentences and supporting labels are very bold. | Use body weight 400; use 600 or 700 only where emphasis helps the next action. |
| Repeated large introductions and a report column compete with the question. | Compact the introduction after a quiz starts. Make progress secondary and move detailed reporting below the question on narrow screens. |
| Placeholder reports show many empty values before sufficient answers exist. | Show a short, honest empty state; reveal report details when the existing reporting thresholds are met. |

## Use labels that describe the next action

| Current wording or situation | Preferred wording |
| --- | --- |
| Hub | Home |
| Start 25-item quiz | Start practice quiz; show “25 questions” beside the setup controls. |
| Practice these words, when opening a comprehension section | Check your understanding |
| A button that evaluates one selected answer | Check answer |
| A button that moves on after an answer is checked | Next question |
| No grammar problem yet, before there is enough evidence | No results yet |
| Weak areas | Things to practice |
| A control that copies an AI study prompt | Copy study prompt |

Do not rename every quiz button “Check your understanding.” That wording introduces a comprehension activity; “Check answer” describes checking one response. Keep both sites consistent by meaning, not by replacing every label with the same phrase.

<!-- pagebreak -->

# Shared neutrals and distinct primary colors

English Road keeps its olive-green identity. English Ladder keeps cobalt blue. Share the neutral surfaces, type, spacing, and interaction patterns; define the primary action, hover, and selected-surface colors separately for each site. English Road’s green applies to Practice as well as Home and Level Check.

| Role | English Ladder | English Road | Use |
| --- | --- | --- | --- |
| Page background | #FAF9F6 | #FAF9F6 | Main page canvas. |
| Surface | #FFFFFF | #FFFFFF | Answer options, input fields, and reports. |
| Main text | #20242B | #20242B | Body text, headings, and answers. |
| Secondary text | #555E6B | #555E6B | Help, dates, captions, and supporting labels. |
| Primary action | #234DEB | #52651F | Main buttons, current navigation, focus. |
| Action hover | #193CC2 | #35430F | Hover state for the main button. |
| Selected surface | #EDF1FF | #EEF2E2 | Unchecked selected options and contextual panels. |
| Divider | #D8DCE2 | #D8DCE2 | Quiet section dividers and card edges. |
| Control edge | #6B7280 | #6B7280 | Stronger boundary where needed to identify a control. |
| Correct text | #1C5B36 | #1C5B36 | Explicit correct-answer text and check symbol. |
| Correct surface | #E0F0E6 | #E0F0E6 | Background for checked, correct feedback. |
| Incorrect text | #9E3039 | #9E3039 | Incorrect-answer wording and indicator. |
| Incorrect surface | #FBECEE | #FBECEE | Background for corrective feedback. |

**Green remains the brand color.** English Road’s existing #6F7F2A may remain a decorative brand accent. White on that green measures about 4.43:1, just below the normal-text target. The proposed darker button green #52651F gives about 6.48:1. This preserves the olive-green family while improving readability.

**Selection is not a result.** English Road’s green-selected answer needs a radio/check state and border, without a “Correct” label until it has been checked. Success feedback adds explicit wording and a check symbol. English Ladder applies the same rule with a blue selection state. Do not rely on hue alone.

## Contrast targets

Meet Web Content Accessibility Guidelines 2.2 Level AA. Normal text needs at least 4.5:1 contrast against its background; qualifying large text needs at least 3:1. Check the actual combinations used in every state. The palette alone does not establish that a page is accessible. See the W3C references at the end of this guide.

Keep any level-color accents subordinate to the written label. On English Road, neutral level badges help preserve green as the main identity. Never use color alone to identify a level or result.

<!-- pagebreak -->

# Typography layout and components

Use English Ladder’s existing font stack on both sites: **Avenir Next, Segoe UI, Arial, sans-serif**. This uses available device fonts and needs no new paid font service. Font rendering will vary slightly by device; match the stack and weights rather than expecting identical letter shapes everywhere. English Road currently loads Inter; remove that dependency when its replacement is verified.

| Text role | Shared target |
| --- | --- |
| Body and answer text | 16–18 px; weight 400; line height 1.6–1.7. |
| Page title | 36–60 px on desktop; 32–44 px on small screens; line height 1.1–1.2. |
| Section heading | 24–32 px; weight 600 or 700; line height about 1.2. |
| Question prompt | 20–24 px; weight 600; line height at least 1.4. |
| Button or field label | 14–16 px; weight 600 or 700. |
| Caption or secondary metadata | 13–14 px; avoid using this size for instructions or answers. |

Georgia may be used for editorial feature headlines, as on Discover. Keep English Road’s question prompts, scores, forms, and reports in the shared sans-serif stack. Do not turn every heading into a large display headline.

## Dimensions and spacing

Use a 1200 px outer page width, including side padding. Start with 32 px side padding on desktop and 20 px on mobile; use a narrower 720–760 px reading or question column. Use a spacing scale of 4, 8, 12, 16, 24, 32, 48, and 64 px. Separate major sections by 32–48 px.

At about 800 px, stack the question and report columns. At 640 px and below, reduce side padding and let navigation wrap. Test 320, 390, 768, and 1280 px widths. Do not hide layout problems with `overflow-x: hidden`.

## Reusable components

- **Header:** compact 40 × 40 px mark, readable wordmark, quiet navigation, and a thin bottom divider. Indicate the current page with the site’s primary color and an underline: green on English Road, blue on English Ladder.
- **Buttons:** site-colored main action with white text, 8 px corners, minimum height 46 px, about 12 × 22 px padding. Secondary actions use an outline or text treatment. Avoid lift animations and heavy shadows.
- **Answer options:** full-width clickable labels, 8 px corners, minimum 44 px height, and enough vertical padding for wrapped text. Keep the radio control visible and keyboard accessible.
- **Cards and fields:** white surface, thin border, 8–10 px corners, and 20–24 px internal padding. Separate unrelated sections with whitespace rather than nesting several cards.
- **Focus:** visible 3 px outline in the site’s primary color with separation from the component. Test that it remains visible against selected and error states.

<!-- pagebreak -->

# Question and feedback behavior

Keep the question, answer choices, and checking action together. Use this sequence in both sites wherever the underlying activity supports it: read the prompt, choose an answer, check the answer, then continue. Keep the learner’s place when content expands.

| State | Required presentation |
| --- | --- |
| Nothing selected | Neutral options. “Check answer” is unavailable with a nearby instruction, or activating it gives “Choose an answer first.” No score is recorded. |
| Selected but unchecked | Site-colored selection border and pale fill, plus the native checked state. Do not add a correctness label before checking. |
| Correct | “Correct” with an indicator and a brief explanation of why the answer fits. Show the next action clearly. |
| Incorrect | “Not quite” or “Incorrect,” the correct answer, and a short explanation. Preserve the learner’s chosen answer visibly. |
| Completed | A clear completion heading, truthful answered/correct totals, useful next steps, and the existing report or study-prompt controls. |

**Example feedback:** “Not quite. Use ‘do’ before the subject in this present-simple question: ‘How often do you check your email?’” The explanation should help the learner answer a similar question later. Color changes alone are insufficient.

Preserve English Road’s current scoring and feedback timing. The style work must not add retries that improve a placement score, change when answers are locked, or reveal information earlier in an assessment. If a separate practice retry is introduced later, distinguish it from the original scored attempt.

## Progress and reporting

Show “Question 7 of 25” or “7 of 25 answered,” depending on what is being counted. Label correct answers separately. Before any answers, use an empty state such as “Your results will appear as you answer” rather than presenting 0/25 as a finished performance.

Keep English Road’s first estimate after five answers and final report after 100 answers. Explain those milestones once near the progress area. Preserve the “unofficial” label and distinguish an English Road estimate from an official examination score. Do not add new score-conversion or accuracy claims as part of a redesign.

## Input and feedback access

Use real buttons for actions and links for navigation. Group related radio options with a visible question label. Announce newly displayed answer feedback to screen readers, for example through a polite status region. Keep a visible keyboard focus indicator, allow text to wrap, and avoid automatic scrolling that loses the current question.

<!-- pagebreak -->

# English Road page plans

## Home

Replace the illustrated “English Level Check” banner with the shared compact header and the wordmark **English Road**. The home page represents both tools, so its main heading should describe the choice: **“Find your level. Choose what to practice.”** Use two equally styled tool summaries, with one clear action in each: “Start level check” and “Start practice quiz.”

State the question count and purpose in ordinary language. Put the 4,200-item bank detail in supporting copy rather than making it the dominant selling point. Retain a compact English Ladder link below the tools: “Read today’s English lesson.” Keep privacy and unofficial-report information available without making it the main visual feature.

## Level check

Keep the active question in the main column and the estimate in a secondary column. On mobile, show the question and its action before the estimate. Use a compact instructions disclosure and preserve the existing language-help choices. Do not require learners to scroll past empty report tables to reach a question.

Before the first estimate, show “Answer 5 questions to see your first estimate.” Before the final report, show “Your report will be available after 100 answers.” Expand the relevant information at the existing milestones. Preserve working resume behavior, progress data, scoring, and the current report fields.

## Practice quizzes

Keep all six CEFR options from A1 to C2. Use a labeled native select or an accessible compact selector; do not replace it with English Ladder’s three broader tracks. Before starting, show the level choice, “25 questions,” and “Start practice quiz.” Once active, reduce the introduction to a compact level and progress summary.

Keep the question prominent and provide explicit feedback after “Check answer.” Keep “New quiz” secondary so it is not mistaken for the next step. Make a restart warn about losing the current attempt if it would discard answers. Put detailed review and study-prompt controls after the quiz or in a clearly labeled expandable section, preserving their current availability.

## Reports and study prompts

Use the same typography and spacing in on-screen and printable reports, carrying English Road’s green accent through its reports. Show the date, completion status, level labels, results, and next steps in a clear order. Preserve copyable report text. If a PDF export is added, embed fonts and check every page for clipped content.

Explain that “Copy study prompt” copies text for the learner to paste into an AI service. It must not silently send answers to another service. Report where progress is stored accurately: English Road’s saved level-check progress, its page-only practice answers, English Ladder’s page-only news notes, and optional saved work-course drafts are different behaviors.

<!-- pagebreak -->

# Connections levels and imagery

## Navigation between the sites

English Road’s navigation should read **Home · Level check · Practice quizzes**, with an explicit secondary link to **English Ladder**. English Ladder keeps its task-based navigation and offers **“Check your English level”** as the route to English Road. Use the same header geometry and active-page treatment without forcing identical navigation items.

Recommended direct destinations are `https://englishroad.com/level-check.html`, `https://englishroad.com/practice.html`, and `https://englishladder.com/`. Preserve existing filenames and working URLs. Display the brand as “English Road” and “English Ladder”; this does not require changing either domain.

| English Road choice | English Ladder reading destination |
| --- | --- |
| A1 or A2 | Beginner · A1–A2 — `beginner.html` |
| B1 or B2 | Intermediate · B1–B2 — `intermediate.html` |
| C1 or C2 | Advanced · C1+ — `advanced.html` |

This is a broad reading-track suggestion, not a new examination-score conversion. Let the learner change tracks. Do not assume that a B1 learner and a B2 learner have identical needs.

Do not assume browser-saved progress is shared across the two domains. A level suggestion may be passed in a documented link parameter only if the receiving site supports it. Do not put names, answer histories, or reports into URLs.

## Images and identity

English Ladder’s daily cover is a 4:3 Gemini-generated illustration tied to the published lesson. It has a real release date, an honest AI label, and a text fallback if the image is unavailable. Preserve that relationship when linking to it; never hard-code a stale headline as “today’s lesson.”

English Road needs little imagery inside its assessment screens. Use a compact wordmark immediately; a distinct road symbol can be commissioned later in the same visual family as the ladder mark: similar scale, a green field for English Road, simple white form, and comparable corner shape. The ladder mark retains its cobalt field. Do not reuse the ladder symbol as the road logo.

If a new image or mark is commissioned, use Google Gemini under the owner’s standing preference and provide a cost estimate before paid generation. There is no need for a new daily-image service on English Road to achieve visual harmony. Keep essential instructions and page titles as real text. Give informative images useful descriptions and decorative images empty alternative text.

<!-- pagebreak -->

# Implementation and acceptance

## A practical rollout

1. **Create the shared foundation.** Put common neutral colors, type sizes, spacing, and component styles in one documented source, with separate green and blue accent settings for the two sites. Adapt English Road’s `hub.css`, `styles.css`, and `practice.css` to it. Do not paste English Ladder’s entire stylesheet into another application.
2. **Align Home and navigation.** Establish the compact header, wordmark, page background, text weights, and tool summaries. Approve the desktop and mobile appearance before applying the system throughout the quiz screens.
3. **Align questions and reports.** Update option states, feedback, progress, empty states, and report presentation while preserving assessment behavior and data. Keep element identifiers and event connections working.
4. **Verify and publish.** Complete the checks below, update asset versions to avoid stale styles or scripts, and confirm the live pages after deployment. Keep a record of any intentional variation from this guide.

## Acceptance checklist

- [ ] English Road uses green throughout Home, Level Check, Practice, and reports. English Ladder remains blue. Shared neutrals, typography, spacing, and component shapes match.
- [ ] The main question is prominent; supporting statistics do not compete with it.
- [ ] Selected, correct, incorrect, disabled, loading, empty, and completed states are distinguishable with text or structure as well as color.
- [ ] Buttons describe their actual actions; comprehension activities use “Check your understanding,” and individual checks use “Check answer.”
- [ ] Keyboard users can select, check, continue, expand help, copy results, and reach every link, with visible focus throughout.
- [ ] The pages work at 320, 390, 768, and 1280 px, at 200% zoom, and with long or translated text. No accidental sideways scrolling or clipped controls.
- [ ] Text contrast meets the stated targets. Aim for at least 44 × 44 px touch targets for primary interactive controls; this is the project’s usability target, not a claim that WCAG requires 44 px everywhere.
- [ ] A complete 25-question practice session and 100-question level check retain their existing scoring, no-repeat rules, progress milestones, resume behavior, and usable reports.
- [ ] Saved-progress, analytics, unofficial-score, and AI-prompt notices accurately describe the actual implementation.
- [ ] Links between sites work and preserve the chosen learning destination where supported. Any downloadable reports remain readable and any PDF fonts are embedded.

**Keep the sites aligned:** use a named version of the shared foundation and update both sites deliberately when a common component changes. Check the same reference screens side by side after future releases. Treat specialist lesson themes as documented exceptions rather than new defaults.

<!-- pagebreak -->

# Brief to give the implementation assistant

Apply the English Ladder and English Road design guide to Englishroad.com. Start by inspecting the current application, then align its home, level-check, practice, and report interfaces with the guide’s colors, typography, spacing, compact header, and shared controls. Use English Ladder’s editorial style as the reference, but keep English Road’s primary color green and English Ladder’s primary color blue. Apply green consistently across English Road’s practice and assessment screens. Preserve English Road’s six CEFR choices and its distinct assessment and practice flows.

Preserve the question bank, scoring, question-selection rules, answer locking, five-answer estimate, 100-answer report, language help, and saved-progress behavior. Make answer feedback understandable without color alone. Use “Check answer” for evaluating one response and “Check your understanding” only for entering a comprehension activity. Keep the unofficial-report and data-storage language accurate.

Do not add paid services or generate new images without first estimating the cost. Use Gemini if image generation is needed. Verify complete practice and level-check sessions, keyboard use, mobile layouts, reports, and links between the sites before publishing. Report what changed, what passed verification, and any remaining limitations.

## References and source files

Observed September 6, 2026. Web sources describe the current applications; the implementation requirements above describe the proposed shared design.

- [English Ladder Discover](https://englishladder.com/) — current editorial feature and daily image presentation.
- [English Ladder daily lessons](https://englishladder.com/beginner.html) — question flow and “Check your understanding” action.
- [English Road Home](https://englishroad.com/) — the two-tool choice and cross-site link.
- [English Road Level Check](https://englishroad.com/level-check.html) — milestones, language help, progress, and report interface.
- [English Road Practice](https://englishroad.com/practice.html) — six-level selector, 25-question flow, and study-prompt interface.
- [W3C contrast guidance](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) — normal and large-text contrast targets.
- [W3C target-size guidance](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) — minimum target size and its exceptions.
- [W3C reflow guidance](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) — content access on narrow displays and at zoom.

**Implementation reference files:** English Ladder `editorial.css`, `editorial.py`, `learning.js`, and `daily_images.py`, using the September 6 revision containing commit `cf7aec9` as the reference. English Road currently serves `hub.css`, `styles.css`, `practice.css`, `app.js`, `practice.js`, `englishroad-title.svg`, and `practice-title.svg`. Confirm current versions before making changes.
