"""Structural and page-edge checks for every published workbook and guide."""
import json
from pathlib import Path
import pdfplumber
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parent

def embedded(font):
    font=font.get_object()
    if font.get('/Subtype')=='/Type0':return all(embedded(f) for f in font['/DescendantFonts'])
    desc=font.get('/FontDescriptor')
    return bool(desc and any(desc.get_object().get(k) for k in ['/FontFile','/FontFile2','/FontFile3']))

def main():
    results=[];failures=[]
    paths=sorted((ROOT/'pdf').rglob('*.pdf'))
    for i,path in enumerate(paths,1):
        reader=PdfReader(path);missing=set();bounds=[]
        for page in reader.pages:
            resources=page.get('/Resources',{}).get_object()
            for font in resources.get('/Font',{}).get_object().values():
                if not embedded(font):missing.add(str(font.get_object().get('/BaseFont')))
        with pdfplumber.open(path) as pdf:
            for n,page in enumerate(pdf.pages,1):
                outside=[c for c in page.chars if c['text'].strip() and (c['x0'] < -1 or c['x1'] > page.width+1 or c['top'] < -1 or c['bottom'] > page.height+1)]
                if outside:bounds.append({'page':n,'text':''.join(c['text'] for c in outside)[:120]})
        row={'path':str(path.relative_to(ROOT)),'pages':len(reader.pages),'unembedded_fonts':sorted(missing),'bounds_failures':bounds,'bookmarks':len(reader.outline),'tagged':bool(reader.trailer['/Root'].get('/StructTreeRoot'))}
        results.append(row)
        if missing or bounds or not reader.outline:failures.append(row)
        if i%40==0:print(f'Checked {i}/{len(paths)} PDFs.',flush=True)
    report={'date':'2026-09-06','files':len(results),'pages':sum(r['pages'] for r in results),'failures':failures,'results':results,'limitations':'Text bounds and font checks do not certify PDF accessibility or detect every overlap. The HTML lessons provide readable equivalents; PDFs are not tagged.'}
    (ROOT/'docs/document-validation-2026-09-06.json').write_text(json.dumps(report,indent=2)+'\n')
    print({k:v for k,v in report.items() if k not in ['results','failures']},'failure_count',len(failures))
    if failures:raise SystemExit(1)
if __name__=='__main__':main()
