"""Install a fully audited collection at the existing stable download paths."""
import hashlib
import json
from pathlib import Path
import shutil

from books.revised_edition import inventory
from revised_book_records import stem, verify_record

ROOT = Path(__file__).resolve().parent


def install():
    slugs = ['cultural-leadership-us-branches', *inventory()]
    report = json.loads((ROOT / 'tmp/pdfs/revised-audit/staged.json').read_text())
    if report['failures']:
        raise ValueError('Resolve all staged-book audit failures before installation.')
    passed = {item['slug']: item for item in report['results']}
    if set(passed) != set(slugs):
        raise ValueError('Audit the complete collection before installation.')
    for slug in slugs:
        meta = verify_record(slug, staged=True)
        if passed[slug]['sha256'] != meta['sha256'] or not passed[slug]['geometry_checked']:
            raise ValueError('Repeat the full PDF audit after editing: ' + slug)
    for slug in slugs:
        for suffix in ('.pdf', '-manifest.json', '-layout.json'):
            source = ROOT / 'output/pdf' / (stem(slug, True) + suffix)
            target = ROOT / 'output/pdf' / (stem(slug) + suffix)
            temporary = target.with_name(target.name + '.installing')
            shutil.copyfile(source, temporary)
            temporary.replace(target)
    from work_books import publish_books
    publish_books()
    summary = dict(edition='2026-10-14', automated_checks=report,
                   independent_subject_review=False, learner_pilot=False, physical_print_proof=False)
    (ROOT / 'books/REVISED-2026-10-results.json').write_text(json.dumps(summary, indent=2) + '\n')


if __name__ == '__main__':
    install()
