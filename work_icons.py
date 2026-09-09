"""Original profession illustrations generated with the native image generator.

The atlas has seven columns and six rows; the last cell is intentionally empty.
Order is explicit so changes to the course directory cannot swap illustrations.
"""

ICON_SLUGS = (
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


def card_icon(track):
    """Select the profession's atlas cell without adding a screen-reader label."""
    index = ICON_SLUGS.index(track["slug"])
    x = (index % 7) * 100 / 6
    y = (index // 7) * 100 / 5
    # A few illustrations extend close to the neighboring cell's boundary.
    right_trim = {
        "general-it": 2,
        "finance": 6,
        "financial-advice": 2,
        "pharmaceutical": 2,
        "hospitality-tourism": 12,
        "aviation": 2,
        "retail-ecommerce": 2,
        "consulting": 2,
        "sales-business-development": 2,
    }.get(track["slug"], 0)
    clip = f";clip-path:inset(0 {right_trim}px 0 0)" if right_trim else ""
    return (
        '<span aria-hidden="true" class="work-card-icon" '
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
