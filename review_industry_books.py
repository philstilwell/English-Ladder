"""Render completed learner books to temporary numbered visual-review sheets."""
import argparse
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw

from build_leadership_book import unit_page

ROOT = Path(__file__).resolve().parent


def render(slug, phrases_only=False):
    pdf = ROOT / f'output/pdf/{slug}-english-book.pdf'
    if not pdf.is_file():
        raise FileNotFoundError(pdf)
    target = ROOT / 'tmp/pdfs/books' / slug
    if phrases_only:
        target /= 'phrases'
    target.mkdir(parents=True, exist_ok=True)
    if phrases_only:
        for number in [unit_page(i) + offset for i in range(8) for offset in (3, 4)]:
            subprocess.run(['pdftoppm', '-f', str(number), '-l', str(number), '-scale-to', '1000',
                            '-png', str(pdf), str(target / 'page')], check=True)
    else:
        subprocess.run(['pdftoppm', '-scale-to', '1000', '-png', str(pdf), str(target / 'page')], check=True)
    pages = sorted(target.glob('page-*.png'))
    for start in range(0, len(pages), 12):
        sheet = Image.new('RGB', (1600, 1716), '#d6d6dc')
        draw = ImageDraw.Draw(sheet)
        for n, path in enumerate(pages[start:start + 12]):
            with Image.open(path) as page:
                page.thumbnail((380, 526))
                x, y = n % 4 * 400 + 10, n // 4 * 572 + 24
                sheet.paste(page, (x, y))
                draw.text((x, y - 18), str(int(path.stem.split('-')[-1])), fill='black')
        sheet.save(target / f'contact-{start // 12 + 1}.png')
    print(target)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('slug')
    parser.add_argument('--phrases', action='store_true', help='Review only the sixteen phrase pages.')
    args = parser.parse_args()
    render(args.slug, args.phrases)
