# Power Grammar transcription

Published on the Grammar directory: 200 exercises in 20 sets, with 200 clean corrected versions, 354 alternative answers, and all 654 red carets from the numbered source sheets. The original incorrect sentences remain intentional learning prompts. Corrected wording, including individual added letters, is rendered as blue text.

Source: the owner's `Power Grammar images etc` folder, numbered `01-01.jpg` through `20-10.jpg`. Each content record stores its image filename and SHA-256 fingerprint. Images are not required by the website.

`content/power-grammar.json` is the reviewed source. Brackets identify blue additions in the marked correction; `^` identifies a red deletion mark. `content/power-grammar-review.json` records transcription and proofreading changes. All 200 entries were read for proofreading. Colored fragments flagged by recognition were checked against the images; an independent image-row coverage check identified omitted lines, which were manually restored. Source teaching notes are retained separately from alternatives. Printed answer errors were corrected, including missing articles, agreement, spelling, repeated words, and incomplete sentences.

The source `alternatives` array preserves the printed answer order: its first entry is the clean corrected version, displayed as a bold bullet immediately after the marked correction. The remaining entries appear in regular text below the “Alternative correct sentences” heading.

Run `python3 power_grammar.py` to refresh the Grammar directory. Its existing page-decoration pipeline also reinserts this section, so future topic releases retain it. Native HTML details controls work without scripts; the small script opens the appropriate set for shared exercise links. Existing topic lessons remain in the directory below the new practice section.
