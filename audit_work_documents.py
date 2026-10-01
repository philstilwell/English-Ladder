"""Audit every work PDF for embedded fonts, text bounds, edition, and bookmarks.

Read-only with respect to PDFs. Writes a compact JSON report to docs/.
Requires requirements-documents.txt plus pdfplumber for geometry checks.
"""
from concurrent.futures import ProcessPoolExecutor
import argparse
import hashlib
import json
from pathlib import Path
import re

import pdfplumber
from pypdf import PdfReader
from work_curriculum import ROOT, content_hash


def is_book_margin_tab(char):
    """The approved book places an eight-point lesson number in the outer margin."""
    return (char['text'].isdigit() and abs(char['size'] - 8) < .01
            and 591 <= char['x0'] <= char['x1'] <= 603
            and any(abs(char['top'] - (66.9218752 + unit * 23)) < .01 for unit in range(8)))


def audit_book_footer(page):
    """Check the actual footer text, its alignment, link, and occupied corners."""
    label, url = 'ENGLISHLADDER.COM', 'https://englishladder.com/'
    footer = page.crop((0, page.height - 39, page.width, page.height))
    words = footer.extract_words()
    matches = [word for word in words if word['text'] == label]
    if len(matches) != 1:
        return ['Expected exactly one ENGLISHLADDER.COM footer']
    word = matches[0]
    failures = []
    if abs((word['x0'] + word['x1']) / 2 - page.width / 2) > .5:
        failures.append('Website footer is not centered')
    if word['top'] < page.height - 34 or word['bottom'] > page.height - 20:
        failures.append('Website footer is outside its bottom margin')
    if any(other is not word and other['x0'] < word['x1'] + 10
           and other['x1'] > word['x0'] - 10 for other in words):
        failures.append('Website footer overlaps or crowds corner text')
    if not any(a.get('uri') == url and a['x0'] <= word['x0']
               and a['x1'] >= word['x1'] and a['top'] <= word['top']
               and a['bottom'] >= word['bottom'] for a in page.annots):
        failures.append('Website footer is missing its clickable link')
    return failures


def audit_one(item):
    relative, metadata = item
    path = ROOT / relative
    reader = PdfReader(path)
    fonts, failures, words, pages = set(), [], 0, []
    for page in reader.pages:
        for font_ref in page.get('/Resources', {}).get('/Font', {}).values():
            font = font_ref.get_object()
            descendants = font.get('/DescendantFonts')
            actual = descendants[0].get_object() if descendants else font
            descriptor = actual.get('/FontDescriptor', {})
            if hasattr(descriptor, 'get_object'): descriptor=descriptor.get_object()
            embedded = any(k in descriptor for k in ['/FontFile', '/FontFile2', '/FontFile3'])
            fonts.add((str(font.get('/BaseFont')), embedded))
            if not embedded: failures.append('Unembedded font: ' + str(font.get('/BaseFont')))
    with pdfplumber.open(path) as pdf:
        for i, page in enumerate(pdf.pages, 1):
            text = page.extract_text() or ''
            if metadata.get('kind') == 'Learner book':
                failures.extend(f'Page {i}: {issue}' for issue in audit_book_footer(page))
            body = [c for c in page.chars if 44 <= c['top'] < 746 and c['text'].strip()
                    and not (metadata.get('kind') == 'Learner book' and is_book_margin_tab(c))]
            # The approved books allow a two-point optical overhang for inline cloze numbers.
            # This still leaves a 44-point print margin; the retired guides used 46 points.
            right_edge = 568 if metadata.get('kind') == 'Learner book' else 566
            out = [c for c in body if c['x0'] < 45.99 or c['x1'] > right_edge + .01 or c['bottom'] > 743.01]
            if out: failures.append(f'Page {i}: {len(out)} characters outside body bounds')
            if '\u25a0' in text or '\ufffd' in text: failures.append(f'Page {i}: replacement glyph')
            if any(s in text for s in ['field-specific concept', 'decision variable. Use it', 'Equality theater', 'Idea-Combat']):
                failures.append(f'Page {i}: legacy filler')
            if len(text.split()) < 20: failures.append(f'Page {i}: near-empty page')
            words += len(text.split())
            pages.append(dict(page=i, words=len(text.split()), body_bottom=round(max((c['bottom'] for c in body),default=0),1)))
    if not reader.outline: failures.append('Missing navigation bookmarks')
    if len(reader.pages)!=metadata['pages']: failures.append('Page count does not match download metadata')
    if metadata['sha256']!=hashlib.sha256(path.read_bytes()).hexdigest(): failures.append('File differs from download metadata')
    return dict(path=relative, pages=len(reader.pages), words=words, fonts=sorted(fonts),
                failures=sorted(set(failures)), page_details=pages)


def main(output='docs/work-document-audit-2026-09-05.json'):
    manifest=json.loads((ROOT/'content/work/documents.json').read_text())
    assert manifest['content_hash']==content_hash(), 'Regenerate documents after curriculum changes'
    with ProcessPoolExecutor(max_workers=4) as pool:
        rows=list(pool.map(audit_one,manifest['documents'].items()))
    failures=[{'path':r['path'],'issues':r['failures']} for r in rows if r['failures']]
    summary=dict(files=len(rows),pages=sum(r['pages'] for r in rows),words=sum(r['words'] for r in rows),
                 all_fonts_embedded=all(all(f[1] for f in r['fonts']) for r in rows),failures=failures)
    summary['centered_website_footers_checked'] = sum(
        row['pages'] for row in rows if manifest['documents'][row['path']].get('kind') == 'Learner book')
    (ROOT/output).write_text(json.dumps(dict(summary=summary,documents=rows),indent=2)+'\n')
    print(json.dumps(summary,indent=2))
    if failures:raise SystemExit(1)


if __name__=='__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', default='docs/work-document-audit-2026-09-05.json', help='JSON audit report path relative to the repository.')
    main(parser.parse_args().output)
