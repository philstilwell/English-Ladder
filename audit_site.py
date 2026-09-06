"""No network or paid calls: validate generated pages, links, and reviewed data."""
import json
from pathlib import Path
from urllib.parse import urlparse,unquote
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parent

def audit():
    failures=[];paths=sorted([*ROOT.glob('*.html'),*ROOT.glob('grammar-concepts/*.html'),*ROOT.glob('stories/*/*.html'),*ROOT.glob('news/*/*.html')]);documents={}
    for path in paths:
        s=BeautifulSoup(path.read_text(),'html.parser');documents[path.resolve()]=s
        if len(s.select('h1'))!=1:failures.append(f'{path.name}: expected one main heading')
        if not s.select_one('main, [role="main"]') or not s.select_one('.skip-link'):failures.append(f'{path.name}: missing main region or skip link')
        if not s.select_one('meta[name="description"]') or not s.select_one('link[rel="canonical"]'):failures.append(f'{path.name}: missing search metadata')
        ids=[tag['id'] for tag in s.select('[id]')]
        if len(ids)!=len(set(ids)):failures.append(f'{path.name}: duplicate page identifier')
        for image in s.find_all('img'):
            if not image.has_attr('alt'):failures.append(f'{path.name}: image lacks alternative text')
        for textarea in s.select('.discussion textarea'):
            if not textarea.has_attr('data-study-draft'):failures.append(f'{path.name}: lesson notes lack the shared saving control')
    for path,s in documents.items():
        for tag in s.find_all(['a','img','script','link']):
            value=tag.get('href',tag.get('src',''));url=urlparse(value)
            if not value or url.scheme or url.netloc:continue
            target=(ROOT/url.path.lstrip('/') if url.path.startswith('/') else path.parent/unquote(url.path)).resolve() if url.path else path
            if not target.is_file():failures.append(f'{path.relative_to(ROOT)}: missing {value}');continue
            if url.fragment and target.suffix=='.html' and not url.fragment.startswith('lesson-'):
                doc=documents.get(target)
                if doc is not None and not doc.find(id=unquote(url.fragment)):failures.append(f'{path.name}: missing fragment {value}')
    from grammar_curriculum import load_curriculum
    from update_site import validate_lesson_data,LEVELS
    from news_quality import validate_evidence
    load_curriculum()
    for path in sorted((ROOT/'archive/lessons').glob('*.json')):
        data=json.loads(path.read_text())
        if not data.get('editorial_review') and not all(v['lesson'].get('editorial_check') for v in data['levels'].values()):continue
        for config in LEVELS:
            lesson=data['levels'][config['name'].lower()]['lesson']
            failures.extend(f'{path.name}/{config["name"]}: {issue}' for issue in [*validate_lesson_data(lesson,config),*validate_evidence(lesson,data['source'])])
    if failures:raise AssertionError('\n'.join(failures[:60]))
    print(f'Passed: {len(paths)} pages, local links, metadata, grammar curriculum, and reviewed news data.')
    return len(paths)
if __name__=='__main__':audit()
