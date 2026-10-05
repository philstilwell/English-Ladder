# Professional Course Illustrations

`professional-icons.png` is original artwork created with the native OpenAI image generator on 9 September 2026. It replaces the former hand-coded line symbols.

The image is a seven-column, six-row atlas. The 41 occupied cells follow the explicit order in `work_icons.py`; the final cell is empty. CSS displays one cell at a time without modifying the original generated image. Keep the atlas and its mapping together.

Art direction: crisp editorial miniatures on white, with dark outlines, blue and teal, restrained coral and gold accents, and recognizable tools and workplace situations. Profession-specific cues include a silicon wafer for semiconductors, a clinical trial clipboard with medicine for pharmaceuticals, a consultation for financial advice, payment transfers for banking operations, and a commercial aircraft for aviation.

To refresh existing card illustrations after changing the mapping, run `python3 work_icons.py`. Both regular page generators also use the same mapping.

## Occupation Illustrations

`occupation-icons.png` was generated with Google Gemini on 28 September 2026,
using the existing signed-in subscription without a separately billed API call.
The original 1024-pixel square PNG is preserved here. Its five-column, five-row
order follows `OCCUPATION_SLUGS` in `work_occupations.py`.

The art direction follows the original atlas: recognizable occupational tools,
navy outlines, blue and teal objects, and restrained coral highlights on white.
Gemini retained captions despite revision requests. `icon_bottom_trim` excludes
those captions in both the web and PDF presentation without altering the source
artwork. Keep the shared crop mapping with the atlas when updating it.

## Directory hero collage

`industry-collage-66.png` is a single transparent illustration generated with
the built-in OpenAI Imagegen tool on 5 October 2026. It combines all 41
professional fields and 25 occupations into eleven rows of six, without captions.
The reference atlases and course-card illustrations remain unchanged.

The directory uses `industry-collage-66.webp`, a smaller web copy with the same
1196 × 1315 dimensions and transparency. The artwork takes 42% of the hero width
on desktop and stacks below the introduction at widths of 900 pixels or less.
See [the generation prompt](hero-collage-prompt.md) for the full icon order and
art direction.
