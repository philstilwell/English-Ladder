# Grammar Concept Item Banks

The public grammar concept pages use the original lesson practice by default.
Generated assessment banks are kept out of the visible site until they are
curated and explicitly enabled.

## Directories

- `public/`: hand-approved item banks that may be rendered by setting
  `ENGLISH_LADDER_USE_PUBLIC_ITEM_BANK=1`.
- `experimental/`: generated or draft item banks that are not rendered on the
  public site.

## Item Metadata

Every generated item should include:

- `focus_area`: `grammar`, `vocabulary`, or `mixed`
- `item_type`: assessment format such as `gap_fill` or `sentence_choice`
- `cefr_level`: `A1`, `A2`, `B1`, `B2`, `C1`, or `unrated`
- `difficulty`: `easy`, `medium`, `hard`, or `unrated`
- `subskill`: the specific skill being assessed
- `weakness_tag`: the learner weakness targeted by the item
- `source_status`: `original`, `revised`, `new`, `retired`, or `experimental`

Only banks in `public/` are eligible to replace source practice, and even then
only when the environment flag is enabled.
