"""Render staged revised books sequentially using the installed browser."""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys

import build_leadership_pilot as design
from build_revised_books import configure
from books.revised_edition import inventory

ROOT = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('slugs', nargs='*')
    parser.add_argument('--ready', action='store_true', help='Build only books with their final cover on disk.')
    parser.add_argument('--all', action='store_true')
    parser.add_argument('--skip-current', action='store_true')
    args = parser.parse_args()
    slugs = ['cultural-leadership-us-branches', *inventory()] if args.all or args.ready else args.slugs
    node = os.environ.get('BOOK_NODE', 'node')
    env = os.environ.copy()
    if not env.get('CHROMIUM_EXECUTABLE'):
        for candidate in [Path.home() / 'Library/Caches/ms-playwright/chromium_headless_shell-1234/chrome-headless-shell-mac-arm64/chrome-headless-shell',
                          Path('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')]:
            if candidate.exists():
                env['CHROMIUM_EXECUTABLE'] = str(candidate)
                break
    result = []
    for slug in slugs:
        try:
            configure(slug)
        except FileNotFoundError:
            if args.ready:
                continue
            raise
        if args.skip_current:
            from revised_book_records import verify_record
            try:
                meta = verify_record(slug, staged=True)
                result.append(dict(slug=slug, status='current', pages=meta['pdf_pages']))
                print(json.dumps(result[-1]), flush=True)
                continue
            except (FileNotFoundError, ValueError, KeyError):
                pass
        design.build()
        completed = subprocess.run([node, str(ROOT / 'print_leadership_pilot.cjs'), design.STEM],
                                   cwd=ROOT, env=env, capture_output=True, text=True)
        if completed.returncode:
            print(slug + ': ' + completed.stderr, flush=True)
            result.append(dict(slug=slug, status='layout-failed'))
            continue
        design.finalize()
        meta = json.loads((design.OUT / (design.STEM + '-manifest.json')).read_text())
        result.append(dict(slug=slug, status='rendered', pages=meta['pdf_pages']))
        print(json.dumps(result[-1]), flush=True)
    report = ROOT / 'tmp/pdfs/revised-build-results.json'
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(json.dumps(result, indent=2) + '\n')
    if any(item['status'] not in ('rendered', 'current') for item in result):
        sys.exit(1)


if __name__ == '__main__':
    main()
