# Reading-page layout stability — September 15, 2026

The supplied Cloudflare report showed 67% good, 10% needing improvement, and 23% poor cumulative layout shift (CLS). Individual examples were about 0.69–0.73 on dated lesson disclosures and 0.13 on reading panels. The displayed counts are small; these percentages do not establish a stable rate across all visitors.

## Confirmed causes and changes

A feed link such as `beginner.html#lesson-2026-09-14` initially painted a collapsed list. Deferred JavaScript then opened the requested lesson, moving the following disclosures. The listed shifted elements were affected by that expansion, rather than necessarily causing it.

The browser also inserted step navigation, word-help hints, vocabulary-language controls, and action buttons after initial rendering, and changed emphasized words into differently sized buttons.

The publisher now includes those controls in the HTML. A small parser-time initializer selects the initial reading view and opens the requested dated disclosure before it can paint closed. Controls retain their final space while their behavior downloads; JavaScript enables and reuses them. Initial vocabulary emphasis has the same dimensions as the interactive word buttons. All 228 current feed, permanent news, and evergreen reading pages use this publisher, including future daily editions.

Without JavaScript, all three lesson sections remain readable through the native disclosures and inactive controls remain hidden. A failed learning-script download restores this plain view. Print styling exposes all lesson sections. Repeated publishing does not duplicate controls or include interface labels in the copyable AI lesson prompts.

The two explicit late fragment-scroll calls were also removed when the requested disclosure is already open. Normal browser fragment positioning can still happen when document loading completes; the site does not override that native behavior.

## Measurements

Installed Chrome, 900-pixel viewport height, fresh browser contexts, and 1.5-second delays on the deferred interaction scripts. No paid generation was used.

| Reproduced page | Width | Before CLS | After CLS |
| --- | ---: | ---: | ---: |
| Beginner, September 14 fragment | 390 | 0.5980 | 0.0000 |
| Intermediate, September 9 fragment | 390 | 0.5730 | 0.0000 |
| Advanced, September 7 fragment | 390 | 0.5164 | 0.0000 |
| Beginner, September 14 fragment | 1280 | 0.6061 | 0.0000 |
| Intermediate, September 9 fragment | 1280 | 0.5936 | 0.0000 |
| Advanced, September 7 fragment | 1280 | 0.4615 | 0.0000 |
| September 14 permanent Advanced lesson | 390 | 0.0597 | 0.0000 |
| September 14 permanent Advanced lesson | 1280 | 0.0270 | 0.0000 |

The broader audit checks nine routes at 320, 390, 768, and 1280 pixels, with both fresh settings and saved Japanese definitions plus completion markers. All 72 initial-load measurements were within 0.1. Fresh-setting measurements were 0.0000; the maximum with saved settings was 0.0782 (rounded upward). Saved completion marks can still cause small shifts. These are controlled browser results, not a claim that historical Cloudflare measurements have changed.

[Google's CLS guidance](https://web.dev/articles/optimize-cls) defines 0.1 or less as good and explains both dynamically inserted content and the distinction between laboratory measurements and visitors' real experiences. Review new visits after deployment; a reporting window containing older visits will still contain earlier failures.

## Verification and reproduction

- 243 Python checks and 127 JavaScript checks passed.
- Site and search audits passed for 333 pages.
- Browser checks cover step navigation, no-JavaScript and failed-download fallbacks, overflow, browser errors, and repeated script-driven scrolling. A separate print check confirms all three sections display and inactive controls do not.
- The durable browser audit is `audit_reading_layout.cjs`; results are in `docs/reading-layout-audit-2026-09-15.json`.

Start a local static server with `python3 -m http.server 8768 --bind 127.0.0.1`, then run `node audit_reading_layout.cjs`. It uses the project's existing Playwright dependency and installed Google Chrome. Set `AUDIT_ORIGIN` to check another deployment and `AUDIT_WIDTHS` to choose a smaller set of widths. Reports default to `output/playwright/reading-layout.json`.
