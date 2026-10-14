"""Build the approved book design for field-specific industry editions.

Output uses a revision suffix until the entire collection is ready to publish.
"""
import argparse
from pathlib import Path

import build_leadership_pilot as design
from books.revised_edition import inventory, load_edition, validate

ROOT = Path(__file__).resolve().parent


def configure(slug):
    if slug == 'cultural-leadership-us-branches':
        from books import leadership_pilot as leadership
        for name in ('UNITS', 'SUPPLEMENTS', 'CHECKPOINTS', 'TITLE', 'SUBTITLE', 'COURSE_URL', 'validate'):
            setattr(design, name, getattr(leadership, name))
        design.BOOK = None
        design.FOOTER_TITLE = 'Cross-Cultural Leadership'
        design.KEYWORDS = 'English Ladder, international managers, workplace English, cross-cultural leadership'
        design.STEM = 'cross-cultural-leadership-english-book-revised'
        design.ART = ROOT / 'assets/work/leadership-book-cover-2026.png'
        return dict(units=design.UNITS, supplements=design.SUPPLEMENTS, checkpoints=design.CHECKPOINTS)
    book = load_edition(slug)
    art = ROOT / 'assets/work/book-covers' / (slug + '.png')
    if not art.exists():
        for folder in ('medical', 'specialists'):
            candidate = ROOT / 'assets/work' / folder / (slug + '.png')
            if candidate.exists():
                art = candidate
                break
    if not art.exists():
        raise FileNotFoundError('A print-resolution cover illustration is required: ' + slug)
    design.BOOK = book
    design.UNITS = book['units']
    design.SUPPLEMENTS = book['supplements']
    design.CHECKPOINTS = book['checkpoints']
    design.TITLE = book['title']
    design.SUBTITLE = book['tagline']
    design.COURSE_URL = f'https://englishladder.com/efsp-{slug}.html'
    design.FOOTER_TITLE = 'English for Work'
    design.KEYWORDS = 'English Ladder, workplace English, ' + book['title']
    design.STEM = slug + '-english-book-revised'
    design.ART = art
    design.validate = lambda: validate(book)
    return book


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('slugs', nargs='*')
    parser.add_argument('--all', action='store_true')
    parser.add_argument('--finalize', action='store_true')
    args = parser.parse_args()
    for slug in inventory() if args.all else args.slugs:
        configure(slug)
        design.finalize() if args.finalize else design.build()
