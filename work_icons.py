"""Explicit illustration mappings shared by the course cards, pages, and PDFs."""
from work_occupations import OCCUPATION_SLUGS
from work_medical import MEDICAL_SLUGS

LEGACY_ICON_SLUGS = (
    "cultural-leadership-us-branches",
    "ai-development",
    "general-it",
    "law",
    "finance",
    "financial-advice",
    "marketing",
    "real-estate",
    "corporate-strategy",
    "pharmaceutical",
    "healthcare-administration",
    "nursing-allied-health",
    "biotechnology",
    "medical-devices",
    "manufacturing",
    "supply-chain-logistics",
    "human-resources",
    "project-management",
    "engineering",
    "semiconductor",
    "software-product-management",
    "cybersecurity",
    "data-analytics-business-intelligence",
    "education-administration",
    "higher-education-research",
    "hospitality-tourism",
    "aviation",
    "construction-architecture",
    "energy-utilities",
    "environmental-consulting",
    "insurance",
    "banking-operations",
    "retail-ecommerce",
    "media-entertainment",
    "telecommunications",
    "government-public-administration",
    "nonprofit-ngo",
    "consulting",
    "sales-business-development",
    "customer-success",
    "legal-operations-compliance",
)
ATLAS_ICON_SLUGS = LEGACY_ICON_SLUGS + OCCUPATION_SLUGS
ICON_SLUGS = ATLAS_ICON_SLUGS + MEDICAL_SLUGS

# Visible artwork bounds, with a small allowance for soft edges and shadows.
MEDICAL_ICON_SIZE = 1254
MEDICAL_ICON_CROPS = {
    'general-practitioners': (60, 175, 1175, 903),
    'oncologists': (115, 132, 1090, 998),
    'cardiologists': (121, 126, 1057, 953),
    'x-ray-technicians': (67, 101, 1122, 1066),
    'pediatricians': (59, 55, 1144, 1114),
    'obstetricians': (22, 147, 1211, 957),
}

# Bounds of each complete illustration in the generated directory artwork.
# The webpage supplies the equal cells; generated spacing is not a layout contract.
DIRECTORY_COLLAGE_SIZE = (1196, 1315)
DIRECTORY_COLLAGE_CROPS = (
    ((33, 23, 179, 114), (247, 38, 154, 102), (437, 25, 144, 114), (623, 18, 149, 121), (805, 31, 145, 108), (996, 31, 176, 105)),
    ((35, 154, 160, 99), (232, 147, 169, 113), (431, 147, 143, 106), (618, 148, 121, 111), (802, 152, 161, 108), (1005, 152, 150, 110)),
    ((44, 265, 137, 114), (245, 270, 155, 112), (427, 261, 147, 116), (614, 271, 159, 98), (809, 270, 155, 96), (1010, 272, 159, 104)),
    ((33, 385, 169, 113), (243, 383, 150, 114), (434, 386, 140, 109), (612, 379, 156, 120), (819, 387, 145, 113), (996, 381, 174, 115)),
    ((30, 505, 170, 108), (233, 505, 155, 109), (412, 509, 169, 106), (617, 508, 157, 111), (806, 502, 153, 112), (996, 510, 171, 103)),
    ((35, 615, 159, 121), (241, 620, 150, 114), (430, 627, 140, 109), (624, 626, 142, 109), (814, 625, 158, 112), (1000, 624, 175, 112)),
    ((44, 740, 134, 107), (239, 743, 142, 107), (432, 745, 149, 98), (627, 744, 147, 100), (823, 742, 139, 102), (1013, 743, 155, 105)),
    ((43, 851, 137, 93), (247, 852, 139, 98), (437, 844, 137, 104), (622, 848, 154, 104), (811, 852, 154, 104), (1009, 852, 164, 102)),
    ((46, 948, 140, 110), (244, 957, 132, 104), (425, 958, 146, 102), (634, 960, 124, 96), (813, 956, 153, 100), (1008, 962, 159, 92)),
    ((44, 1064, 142, 93), (231, 1065, 163, 93), (425, 1066, 152, 90), (623, 1065, 152, 92), (820, 1065, 140, 90), (1005, 1067, 161, 88)),
    ((38, 1166, 157, 97), (236, 1169, 158, 92), (432, 1176, 147, 84), (621, 1175, 144, 91), (820, 1172, 139, 95), (1011, 1166, 147, 101)),
)


def collage_art_style(size, crop):
    image_width, image_height = size
    x, y, width, height = crop
    # Square grid cells reserve the same 10% margin on every side.
    scale = min(160 / width, 160 / height)
    return (
        f'width:{width * scale / 200 * 100:.6f}%;'
        f'height:{height * scale / 200 * 100:.6f}%;'
        f'background-size:{image_width / width * 100:.6f}% {image_height / height * 100:.6f}%;'
        f'background-position:{x / (image_width - width) * 100:.6f}% {y / (image_height - height) * 100:.6f}%'
    )


def directory_collage():
    """Center the native-generated artwork in identical responsive cells."""
    crops = [crop for row in DIRECTORY_COLLAGE_CROPS for crop in row]
    cells = []
    for slug, crop in zip(ATLAS_ICON_SLUGS, crops, strict=True):
        style = collage_art_style(DIRECTORY_COLLAGE_SIZE, crop)
        cells.append(
            f'<span class="work-collage-cell" aria-hidden="true" data-collage-field="{slug}">'
            f'<span class="work-collage-art" style="{style}"></span></span>'
        )
    for slug in MEDICAL_SLUGS:
        style = collage_art_style((MEDICAL_ICON_SIZE, MEDICAL_ICON_SIZE), MEDICAL_ICON_CROPS[slug])
        cells.append(
            f'<span class="work-collage-cell" aria-hidden="true" data-collage-field="{slug}">'
            f'<span class="work-collage-medical work-medical-icon" data-work-icon="{slug}" style="{style}"></span></span>'
        )
    return (
        '<div class="work-directory-collage" role="img" '
        f'aria-label="Illustrated tools and people representing all {len(ICON_SLUGS)} professional fields and occupations.">'
        + ''.join(cells) + '</div>'
    )


def icon_asset(slug):
    if slug in MEDICAL_SLUGS:
        return (f'assets/work/medical/{slug}.png', 1, 1, 0)
    if slug in OCCUPATION_SLUGS:
        return ('assets/work/occupation-icons.png', 5, 5, OCCUPATION_SLUGS.index(slug))
    return ('assets/work/professional-icons.png', 7, 6, LEGACY_ICON_SLUGS.index(slug))


def icon_right_trim(slug):
    """Shared crop boundary in units of the 104-pixel web illustration."""
    return {
        "general-it": 2,
        "finance": 6,
        "financial-advice": 2,
        "pharmaceutical": 2,
        "hospitality-tourism": 12,
        "aviation": 2,
        "banking-operations": 4,
        "retail-ecommerce": 2,
        "consulting": 4,
        "sales-business-development": 2,
    }.get(slug, 0)


def icon_bottom_trim(slug):
    """Exclude neighboring artwork and generated captions from displayed cells."""
    if slug not in OCCUPATION_SLUGS:
        return {"energy-utilities": 6}.get(slug, 0)
    two_line_captions = {
        'hairdressers-barbers', 'hvac-refrigeration', 'bookkeeping-payroll',
        'software-quality-assurance', 'medical-laboratory-technicians',
    }
    return 22.88 if slug in two_line_captions else 15.6


def card_icon(track):
    """Select the profession's atlas cell without adding a screen-reader label."""
    if track['slug'] in MEDICAL_SLUGS:
        return (f'<span aria-hidden="true" class="work-card-icon work-medical-icon" '
                f'data-work-icon="{track["slug"]}"></span>')
    _, columns, rows, index = icon_asset(track['slug'])
    x = (index % columns) * 100 / (columns - 1)
    y = (index // columns) * 100 / (rows - 1)
    right_trim = icon_right_trim(track["slug"])
    bottom_trim = icon_bottom_trim(track['slug'])
    clip = f";clip-path:inset(0 {right_trim}px {bottom_trim}px 0)" if right_trim or bottom_trim else ""
    kind = ' work-occupation-icon' if track['slug'] in OCCUPATION_SLUGS else ''
    return (
        f'<span aria-hidden="true" class="work-card-icon{kind}" '
        f'style="background-position:{x:.6f}% {y:.6f}%{clip}"></span>'
    )


def refresh_published_cards():
    """Update only card artwork in existing pages, preserving other published content."""
    from pathlib import Path
    from bs4 import BeautifulSoup

    root = Path(__file__).resolve().parent
    pages = [root / "efsp.html", *sorted((root / "english-for-work").glob("*.html"))]
    count = 0
    for path in pages:
        original = path.read_text()
        soup = BeautifulSoup(original, "html.parser")
        for card in soup.select(".work-course-card"):
            slug = Path(card["href"]).stem.removeprefix("efsp-")
            icon = card.select_one(".work-card-icon")
            if icon is None:
                raise ValueError(f"Missing existing card icon: {path.name}: {slug}")
            replacement = card_icon({"slug": slug})
            icon.replace_with(BeautifulSoup(replacement, "html.parser").span)
            count += 1
        path.write_text(str(soup))
    print(f"Updated {count} illustrations across {len(pages)} pages.")


def refresh_published_industry_pages():
    """Add or refresh the heading artwork without rebuilding lesson content."""
    from pathlib import Path
    from bs4 import BeautifulSoup

    root = Path(__file__).resolve().parent
    for slug in ICON_SLUGS:
        path = root / f"efsp-{slug}.html"
        soup = BeautifulSoup(path.read_text(), "html.parser")
        heading = soup.select_one(".work-hero > div")
        if heading is None or heading.find("h1") is None:
            raise ValueError(f"Missing industry heading: {path.name}")
        for icon in heading.select(".work-card-icon"):
            icon.decompose()
        heading.insert(0, BeautifulSoup(card_icon({"slug": slug}), "html.parser").span)
        path.write_text(str(soup))
    print(f"Updated {len(ICON_SLUGS)} industry page illustrations.")


if __name__ == "__main__":
    refresh_published_cards()
    refresh_published_industry_pages()
