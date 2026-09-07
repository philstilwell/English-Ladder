"""No network or paid calls: validate generated pages, links, and reviewed data."""
import json
from pathlib import Path
from urllib.parse import urlparse,unquote
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parent

def audit():
    from seo import published_pages
    failures=[];paths=published_pages();documents={}
    for path in paths:
        s=BeautifulSoup(path.read_text(),'html.parser');documents[path.resolve()]=s
        if len(s.select('h1'))!=1:failures.append(f'{path.name}: expected one main heading')
        if not s.select_one('main, [role="main"]') or not s.select_one('.skip-link'):failures.append(f'{path.name}: missing main region or skip link')
        if not s.select_one('meta[name="description"]') or not s.select_one('link[rel="canonical"]'):failures.append(f'{path.name}: missing search metadata')
        ids=[tag['id'] for tag in s.select('[id]')]
        if len(ids)!=len(set(ids)):failures.append(f'{path.name}: duplicate page identifier')
        for image in s.find_all('img'):
            if not image.has_attr('alt'):failures.append(f'{path.name}: image lacks alternative text')
        if s.select('[data-save-study],[data-study-controls],[data-learning-dashboard],.save-word'):
            failures.append(f'{path.name}: retired browser-learning controls remain')
        for owner in s.select('.work-module,.us-life-module,.tool-panel,.daily-lesson'):
            if not owner.select_one('[data-ai-extension],[data-ai-preset]'):failures.append(f'{path.name}: a learning activity has no AI extension')
        for button in s.select('[data-ai-copy-text]'):
            prompt=s.find(id=button['data-ai-copy-text'])
            if not prompt or not prompt.get_text(strip=True):failures.append(f'{path.name}: a copy button has no prompt text')
        if 'curriculum-page' in s.body.get('class',[]):
            expected=f'../assets/grammar-concepts/{path.stem}.png'
            graphic=s.select_one('.concept-graphic img')
            if graphic is None or graphic.get('src')!=expected:failures.append(f'{path.name}: original concept graphic missing or mismatched')
            if not s.select_one('[data-ai-extension]'):failures.append(f'{path.name}: grammar AI extension missing')
            if s.select('textarea,input[type="text"],[contenteditable="true"]'):failures.append(f'{path.name}: grammar answers must be multiple choice')
            questions=s.select('[data-choice-question]')
            if len(questions)!=4:failures.append(f'{path.name}: expected four multiple-choice activities')
            for q in questions:
                if len(q.select('input[type="radio"]'))!=3 or len(q.select('[data-choice-correct="true"]'))!=1:failures.append(f'{path.name}: invalid grammar answer choices')
    for path,s in documents.items():
        for tag in s.find_all(['a','img','script','link']):
            value=tag.get('href',tag.get('src',''));url=urlparse(value)
            if not value or url.scheme or url.netloc:continue
            target=(ROOT/url.path.lstrip('/') if url.path.startswith('/') else path.parent/unquote(url.path)).resolve() if url.path else path
            if target==ROOT.resolve():target=ROOT/'index.html'
            if not target.is_file():failures.append(f'{path.relative_to(ROOT)}: missing {value}');continue
            if url.fragment and target.suffix=='.html' and not url.fragment.startswith('lesson-'):
                doc=documents.get(target)
                if doc is not None and not doc.find(id=unquote(url.fragment)):failures.append(f'{path.name}: missing fragment {value}')
    from grammar_curriculum import load_curriculum
    from update_site import validate_lesson_data,validate_reading_length,normalize_text,LEVELS
    from news_quality import validate_evidence
    load_curriculum()
    for path in sorted((ROOT/'archive/lessons').glob('*.json')):
        data=json.loads(path.read_text())
        for config in LEVELS:
            level=config['name'].lower();lesson=data['levels'][level]['lesson']
            failures.extend(f'{path.name}/{level}: {issue}' for issue in validate_reading_length(lesson.get('news_brief_sentences'),config))
            expected=' '.join(normalize_text(sentence) for sentence in lesson['news_brief_sentences']).split()
            # Check the visible reading itself, so lost/truncated HTML cannot pass
            # just because the JSON source has enough sentences.
            for page in [ROOT/config['file_path'], ROOT/'news'/data['release_date']/f'{level}.html']:
                doc=documents.get(page.resolve())
                if doc is None:continue
                node=doc.select_one(f'.daily-lesson[data-lesson-key="{data["release_date"]}"]')
                if node is None:
                    if page.parent!=ROOT:failures.append(f'{page.relative_to(ROOT)}: daily reading missing')
                    continue
                reading=node.select_one('.learning-panel[data-stage="read"] .section > p')
                if reading is None:
                    reading=node.select_one('.section > p')
                if reading is None or reading.get_text().split()!=expected:
                    failures.append(f'{page.relative_to(ROOT)}: {data["release_date"]} reading does not match its checked sentence data')
        if not data.get('editorial_review') and not all(v['lesson'].get('editorial_check') for v in data['levels'].values()):continue
        for config in LEVELS:
            lesson=data['levels'][config['name'].lower()]['lesson']
            failures.extend(f'{path.name}/{config["name"]}: {issue}' for issue in [*validate_lesson_data(lesson,config),*validate_evidence(lesson,data['source'])])
    from audit_seo import audit as audit_search
    audit_search()
    if failures:raise AssertionError('\n'.join(failures[:60]))
    print(f'Passed: {len(paths)} pages, local links, metadata, grammar curriculum, and reviewed news data.')
    return len(paths)
if __name__=='__main__':audit()
