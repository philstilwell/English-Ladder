"""Audit every work PDF for embedded fonts, text bounds, edition, and bookmarks.

Read-only with respect to PDFs. Writes a compact JSON report to docs/.
Requires requirements-documents.txt plus pdfplumber for geometry checks.
"""
from concurrent.futures import ProcessPoolExecutor
import hashlib
import json
from pathlib import Path
import re

import pdfplumber
from pypdf import PdfReader
from work_curriculum import ROOT, content_hash


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
            body = [c for c in page.chars if 44 <= c['top'] < 746 and c['text'].strip()]
            out = [c for c in body if c['x0'] < 46 or c['x1'] > 566 or c['bottom'] > 743]
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


def main():
    manifest=json.loads((ROOT/'content/work/documents.json').read_text())
    assert manifest['content_hash']==content_hash(), 'Regenerate documents after curriculum changes'
    with ProcessPoolExecutor(max_workers=4) as pool:
        rows=list(pool.map(audit_one,manifest['documents'].items()))
    failures=[{'path':r['path'],'issues':r['failures']} for r in rows if r['failures']]
    summary=dict(files=len(rows),pages=sum(r['pages'] for r in rows),words=sum(r['words'] for r in rows),
                 all_fonts_embedded=all(all(f[1] for f in r['fonts']) for r in rows),failures=failures)
    (ROOT/'docs/work-document-audit-2026-09-05.json').write_text(json.dumps(dict(summary=summary,documents=rows),indent=2)+'\n')
    print(json.dumps(summary,indent=2))
    if failures:raise SystemExit(1)


if __name__=='__main__':main()
