# Everyday English explanation translations

`source.json` preserves the original 24 Japanese and Simplified Chinese sidebars extracted from the public `us-life.js` on September 8, 2026. The current English lesson supplies context. All source material was already published on English Ladder.

`us_life_translations.py` uses Gemini 2.5 Flash for translation and a separate editing call. Every reviewed record contains all five languages, its complete source, and review provenance. The original English practice sentence remains separate and unchanged. A source change invalidates its cached translations.

The manual **Translate Everyday English explanations** workflow uses the existing Gemini credential and a cumulative $2 initial budget. Successful drafts, reviewed records, and usage reservations are saved for recovery. Repeating completed work makes no requests. Run `python3 us_life_translations.py --check` for an offline coverage check.

These are build inputs, excluded from the website's public assets. Only reviewed explanation text is embedded in the page. Student clicks and ordinary page rebuilding never contact Gemini.
