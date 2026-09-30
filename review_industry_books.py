"""Render completed learner books to temporary numbered visual-review sheets."""
import argparse
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent


def render(slug):
    pdf = ROOT / f'output/pdf/{slug}-english-book.pdf'
    if not pdf.is_file():
        raise FileNotFoundError(pdf)
    target = ROOT / 'tmp/pdfs/books' / slug
    target.mkdir(parents=True, exist_ok=True)
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
                draw.text((x, y - 18), str(start + n + 1), fill='black')
        sheet.save(target / f'contact-{start // 12 + 1}.png')
    print(target)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('slug')
    render(parser.parse_args().slug)
