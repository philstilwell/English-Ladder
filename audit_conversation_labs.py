"""Read every Conversation Lab PDF and audit fonts, page bounds and metadata."""
from concurrent.futures import ProcessPoolExecutor
import json
from audit_work_documents import audit_one
from work_dialogues import ROOT, validate_dialogues, load_dialogues, dialogue_hash


def main():
    manifest=json.loads((ROOT/'content/work/documents.json').read_text())['documents']
    items=[(path,meta) for path,meta in manifest.items() if meta['kind']=='Conversation lab']
    with ProcessPoolExecutor(max_workers=4) as pool:
        rows=list(pool.map(audit_one,items))
    summary=validate_dialogues(load_dialogues())
    summary.update(pdf_files=len(rows), pages=sum(r['pages'] for r in rows),
                   all_fonts_embedded=all(all(f[1] for f in r['fonts']) for r in rows),
                   dialogue_hash=dialogue_hash(),
                   failures=[{'path':r['path'],'issues':r['failures']} for r in rows if r['failures']])
    path=ROOT/'docs/conversation-lab-audit-2026-09-06.json'
    path.write_text(json.dumps(dict(summary=summary,documents=rows),indent=2)+'\n')
    print(json.dumps(summary,indent=2))
    if summary['failures']:raise SystemExit(1)


if __name__=='__main__':main()
