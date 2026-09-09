"""Offline search publishing: honest metadata, learning-resource graphs and discovery.

No ranking services, AI calls, fabricated reviews, or new PDF exports are involved.
Run this file after source changes, or use the existing editorial publishing path.
"""
from __future__ import annotations

import hashlib
import html
import json
import os
import re
from datetime import date
from functools import lru_cache
from pathlib import Path
from urllib.parse import urlparse, urljoin
from xml.etree import ElementTree as ET

from bs4 import BeautifulSoup
from PIL import Image
from seo_content import PAGES, WORK_TOPICS, CATEGORIES, FUNCTION_GRAMMAR
from seo_lessons import RELATED_GRAMMAR, lesson_image, fingerprint
from work_icons import card_icon

ROOT = Path(__file__).resolve().parent
ORIGIN = 'https://englishladder.com/'
LEVELS = {'beginner': 'A1–A2', 'intermediate': 'B1–B2', 'advanced': 'C1+'}
NOINDEX = {'404.html', 'continue.html'}
SITEMAP_NS = 'http://www.sitemaps.org/schemas/sitemap/0.9'
IMAGE_NS = 'http://www.google.com/schemas/sitemap-image/1.1'
ET.register_namespace('', SITEMAP_NS)
ET.register_namespace('image', IMAGE_NS)


def published_pages():
    return sorted([*ROOT.glob('*.html'), *ROOT.glob('grammar-concepts/*.html'),
                   *ROOT.glob('english-for-work/*.html'), *ROOT.glob('stories/*/*.html'), *ROOT.glob('news/*/*.html')])


def canonical(relative):
    return ORIGIN + ('' if relative == 'index.html' else relative)


def concise(text, limit=185):
    text = ' '.join(str(text).split())
    if len(text) <= limit:
        return text
    return text[:limit-1].rsplit(' ', 1)[0].rstrip(' ,;:.') + '…'


@lru_cache(maxsize=256)
def _json(path, modified):
    return json.loads(Path(path).read_text())


def read_json(relative):
    path = ROOT / relative
    return _json(str(path), path.stat().st_mtime_ns)


@lru_cache(maxsize=1)
def tracks():
    from work_curriculum import load_tracks
    return {t['slug']: t for t in load_tracks()}


def grammar():
    return {c['number']: c for c in read_json('content/grammar-curriculum.json')['concepts']}


def grammar_url(number):
    return f'grammar-concepts/concept-{number:02d}.html'


def category_url(name):
    return f'english-for-work/{CATEGORIES[name]["slug"]}.html'


def local_link(path, relative):
    return os.path.relpath(ROOT / relative, path.parent).replace(os.sep, '/')


def profile(path, soup):
    relative = path.relative_to(ROOT).as_posix()
    heading = (soup.h1.select_one('.lesson-title-text') or soup.h1).get_text(' ', strip=True)
    result = dict(relative=relative, name=heading, kind='page', parent='index.html',
                  title='', description='', level='', teaches=[], pdfs=[], date='')
    if relative in PAGES:
        result['title'], result['description'] = PAGES[relative]
        if relative in {'index.html', 'efsp.html', 'grammar-concepts.html', 'archive.html', 'sitemap.html', 'ai-practice.html', *[v+'.html' for v in LEVELS]}:
            result['kind'] = 'collection'
        if relative == 'about.html': result['kind'] = 'about'
        if path.stem in LEVELS: result['level'] = LEVELS[path.stem]
    elif relative.startswith('efsp-'):
        t = tracks()[path.stem.removeprefix('efsp-')]
        result.update(kind='work', track=t, parent=category_url(t['category']), level='B1–C1',
                      title=t['title'] + ': Dialogues & Free PDFs',
                      description=f'Learn English for {WORK_TOPICS[t["slug"]]}. Practice with workplace dialogues, exercises and free PDFs.',
                      teaches=t['outcomes'], pdfs=[(label, href) for label, href in t['pdfs']])
    elif relative.startswith('english-for-work/'):
        name, category = next((n,c) for n,c in CATEGORIES.items() if c['slug'] == path.stem)
        result.update(kind='category', category=name, parent='efsp.html', title=category['title'] + ': Free Courses', description=category['description'])
    elif relative.startswith('grammar-concepts/'):
        c = grammar()[int(path.stem.split('-')[1])]
        result.update(kind='grammar', concept=c, parent='grammar-concepts.html', level=c['level'],
                      title=c['title'] + ': English Grammar Practice',
                      description=f'{c["goal"]} {c["level"]} English grammar with examples, multiple-choice exercises, explained answers, and free PDFs.',
                      teaches=[c['goal']], date=c.get('reviewed', ''),
                      pdfs=[('Learner workbook' if i == 0 else 'Teaching guide', ('pdf/students/' if i == 0 else 'pdf/teachers/')+p) for i,p in enumerate(c['pdfs'])])
    elif relative.startswith('news/'):
        day = path.parent.name; level = path.stem
        data = read_json(f'archive/lessons/{day}.json'); lesson = data['levels'][level]['lesson']
        headline=data['levels']['beginner']['lesson']['title'] if len(lesson['title'])>65 else lesson['title']
        result.update(kind='news', parent='archive.html', level=LEVELS[level], lesson=lesson, archive=data,
                      title=f'{headline} | {level.title()} English · {day}',
                      description=f'{level.title()} English reading ({LEVELS[level]}) · {day}: {headline.rstrip(".")}. Includes vocabulary, grammar, and comprehension exercises.',
                      teaches=[lesson['grammar']['concept'], *[v['term'] for v in lesson['vocabulary']]],
                      date=data.get('editorial_review', {}).get('date', lesson.get('editorial_check', {}).get('date', day))[:10])
    elif relative.startswith('stories/'):
        from story_lessons import STORIES
        story = next(s for s in STORIES if s['slug'] == path.parent.name)
        level = path.stem; lesson = story['levels'][level]
        topic = {'food-market': 'At the Food Market', 'city-trees': 'Can Trees Cool a City?'}[story['slug']]
        result.update(kind='story', parent='index.html', story=story, lesson=lesson, level=LEVELS[level],
                      title=f'{topic} | {level.title()} English Reading',
                      description=f'{level.title()} English reading practice: {lesson["overview"]} Build vocabulary, study grammar and answer comprehension questions.',
                      teaches=[lesson['grammar']['concept'], *[v['term'] for v in lesson['vocabulary']]])
    else:
        raise ValueError('Add search metadata for new page: ' + relative)
    result['title'] = result['title'] + ' | English Ladder'
    result['description'] = ' '.join(result['description'].split())
    return result


@lru_cache(maxsize=128)
def _image_size(path, modified):
    with Image.open(path) as image:
        return image.size


def share_image(path, soup, p):
    # Use an existing image only where it really represents the visible page.
    image = soup.select_one('.feature-photo img, .lesson-cover img, .reading-photo img, .daily-lesson img.daily-news-image, .concept-graphic img')
    if image:
        src = urlparse(image.get('src', '')).path
        target = (ROOT / src.lstrip('/') if src.startswith('/') else path.parent / src).resolve()
        if target.is_relative_to(ROOT) and target.is_file():
            width, height = _image_size(str(target), target.stat().st_mtime_ns)
            if width >= 600:
                return dict(url=canonical(target.relative_to(ROOT).as_posix()), width=width, height=height, alt=image.get('alt',''), large=True)
    return dict(url=ORIGIN+'assets/brand/ladder-mark.png', width=256, height=256,
                alt='English Ladder: free English lessons and practice', large=False)


def breadcrumbs(p):
    if p['relative'] == 'index.html': return []
    chain = [('English lessons', 'index.html')]
    if p['kind'] == 'work':
        chain += [('English for Work', 'efsp.html'), (CATEGORIES[p['track']['category']]['title'], p['parent'])]
    elif p['parent'] != 'index.html':
        names = {'efsp.html': 'English for Work', 'grammar-concepts.html': 'Grammar lessons', 'archive.html': 'News lesson archive'}
        chain.append((names[p['parent']], p['parent']))
    chain.append((p['name'], p['relative']))
    return chain


def item_list(items, identity):
    return {'@type': 'ItemList', '@id': identity, 'numberOfItems': len(items),
            'itemListElement': [{'@type':'ListItem', 'position':i, 'name':name, 'url':canonical(url)} for i,(name,url) in enumerate(items,1)]}


def collection_items(p, soup):
    if p['kind'] == 'category':
        return [(t['title'], f'efsp-{t["slug"]}.html') for t in tracks().values() if t['category'] == p['category']]
    if p['relative'] == 'efsp.html':
        return [(t['title'], f'efsp-{t["slug"]}.html') for t in tracks().values()]
    if p['relative'] == 'grammar-concepts.html':
        return [(c['title'], grammar_url(n)) for n,c in grammar().items()]
    if p['relative'] in {'archive.html', *[v+'.html' for v in LEVELS]}:
        from update_site import LESSON_LIMIT
        level = Path(p['relative']).stem
        level = level if level in LEVELS else 'beginner'
        files = sorted((ROOT/'archive/lessons').glob('*.json'), reverse=True)
        if p['relative'] != 'archive.html': files = files[:LESSON_LIMIT]
        return [(read_json(f'archive/lessons/{f.name}')['levels'][level]['lesson']['title'], f'news/{f.stem}/{level}.html') for f in files]
    if p['relative'] in {'index.html', 'sitemap.html'}:
        return [('English grammar', 'grammar-concepts.html'), ('English for Work', 'efsp.html'),
                ('English news lessons', 'archive.html'), ('Everyday English in the US', 'us-life.html'), ('English practice tools', 'tools.html')]
    return []


def structured_data(p, soup, image):
    url = canonical(p['relative']); website = ORIGIN+'#website'; publisher = ORIGIN+'#publisher'
    graph = [
        {'@type':'Organization', '@id':publisher, 'name':'English Ladder', 'url':ORIGIN,
         'logo':{'@type':'ImageObject','url':ORIGIN+'assets/brand/ladder-mark.png','width':256,'height':256}},
        {'@type':'WebSite','@id':website,'name':'English Ladder','url':ORIGIN,'inLanguage':'en','publisher':{'@id':publisher}},
    ]
    page_type = 'CollectionPage' if p['kind'] in {'category','collection'} else ('AboutPage' if p['kind']=='about' else 'WebPage')
    page = {'@type':page_type,'@id':url+'#webpage','url':url,'name':p['title'],
            'description':p['description'],'inLanguage':'en','isPartOf':{'@id':website},'publisher':{'@id':publisher}}
    if image['large']:
        page['primaryImageOfPage'] = {'@type':'ImageObject','url':image['url'],'width':image['width'],'height':image['height'],'caption':image['alt']}
    crumbs = breadcrumbs(p)
    if crumbs:
        page['breadcrumb'] = {'@id':url+'#breadcrumbs'}
        graph.append({'@type':'BreadcrumbList','@id':url+'#breadcrumbs','itemListElement':[
            {'@type':'ListItem','position':i,'name':name,'item':canonical(href)} for i,(name,href) in enumerate(crumbs,1)]})
    if p['kind'] in {'work', 'grammar', 'news', 'story'}:
        # Independent self-study materials do not claim Google's instructor-led
        # Course-list eligibility, ratings, qualifications or enrollment counts.
        resource = {'@type':'LearningResource','@id':url+'#learning-resource','url':url,
                    'name':p['name'],'description':p['description'],'inLanguage':'en','isAccessibleForFree':True,
                    'educationalLevel':p['level'],'learningResourceType':{'work':'Workplace English course materials','grammar':'Grammar lesson','news':'News-based English reading lesson','story':'English reading lesson'}[p['kind']],
                    'teaches':p['teaches'],'publisher':{'@id':publisher}, 'mainEntityOfPage':{'@id':url+'#webpage'}}
        if p['date']: resource['dateModified'] = p['date']
        if p['kind'] == 'news':
            resource['datePublished'] = p['archive'].get('release_iso', p['archive']['release_date'])
            source = p['archive'].get('source',{})
            if source.get('link'): resource['citation'] = source['link']
        if p['kind'] == 'grammar': resource['timeRequired'] = 'PT15M'
        if p['kind'] == 'story': resource['timeRequired'] = 'PT5M'
        if p['kind'] == 'work':
            resource['hasPart'] = [{'@type':'LearningResource','name':m['title'],'url':url+'#'+m['id'],
                'learningResourceType':'Workplace case lesson','teaches':m['workshop']['goal']} for m in p['track']['modules']]
        if p['pdfs']:
            resource['encoding'] = [{'@type':'MediaObject','name':label,'contentUrl':canonical(href),'encodingFormat':'application/pdf'} for label,href in p['pdfs']]
        page['mainEntity'] = {'@id':resource['@id']}; graph.append(resource)
    else:
        items = collection_items(p,soup)
        if items:
            listing = item_list(items,url+'#lesson-list'); graph.append(listing); page['mainEntity'] = {'@id':listing['@id']}
    graph.append(page)
    return {'@context':'https://schema.org','@graph':graph}


def add_navigation(soup, path, p):
    for node in soup.select('[data-seo-breadcrumbs], [data-seo-breadcrumb], [data-seo-related], .work-breadcrumb, nav.breadcrumb'):
        node.decompose()
    crumbs = breadcrumbs(p)
    if crumbs and p['relative'] not in NOINDEX:
        nav = soup.new_tag('nav', attrs={'class':'seo-breadcrumbs','aria-label':'Breadcrumb','data-seo-breadcrumbs':''})
        ol = soup.new_tag('ol'); nav.append(ol)
        for index,(name,href) in enumerate(crumbs):
            li = soup.new_tag('li')
            if index == len(crumbs)-1:
                label = soup.new_tag('span',attrs={'aria-current':'page'}); label.string=name
            else:
                label = soup.new_tag('a',href=local_link(path,href)); label.string=name
            li.append(label); ol.append(li)
        soup.main.insert(0,nav)
    links = []
    if p['kind'] == 'grammar':
        links=[(grammar()[n]['title'],grammar_url(n)) for n in RELATED_GRAMMAR[p['concept']['number']]]
        heading,intro='Build on this grammar','Compare a related pattern, then apply it in a new situation.'
    elif p['kind'] == 'work':
        numbers = []
        for m in p['track']['modules']:
            for number in FUNCTION_GRAMMAR.get(m['function'],[]):
                if number not in numbers: numbers.append(number)
        links = [(grammar()[n]['title'], grammar_url(n)) for n in numbers[:4]]
        heading, intro = 'Grammar for your workplace conversations', 'Review a language pattern, then use it in a case from this course.'
    elif p['kind'] in {'news','story'}:
        # Explicit term matching avoids misleading automatic topic associations.
        target = p['lesson']['grammar']['concept'].casefold()
        for term,number in [('recently',16),('lately',16),('past perfect',26),('even if',32),('even though',32),('relative clause',12),('causal',9),('cause and effect',9),('could',35),('able to',35),('might',8),('suggest',17),('recommend',17)]:
            if term in target and (grammar()[number]['title'],grammar_url(number)) not in links:
                links.append((grammar()[number]['title'],grammar_url(number)))
        if not links: links=[('Explore all 44 grammar lessons', 'grammar-concepts.html')]
        links += [('Choose another news lesson', 'archive.html'), ('Practice everyday conversations', 'us-life.html')]
        heading, intro = 'Keep practicing your English', 'Choose a grammar lesson or another reading activity for your next session.'
    if links:
        section = soup.new_tag('section',attrs={'class':'seo-related','data-seo-related':''})
        h = soup.new_tag('h2');h.string=heading;section.append(h)
        text = soup.new_tag('p');text.string=intro;section.append(text)
        ul = soup.new_tag('ul')
        for name,href in links:
            li=soup.new_tag('li');a=soup.new_tag('a',href=local_link(path,href));a.string=name;li.append(a);ul.append(li)
        section.append(ul)
        footer=soup.select_one('.site-footer')
        if footer: footer.insert_before(section)
        else: soup.main.append(section)
    footer=soup.select_one('.site-footer')
    if footer and not footer.select_one('[data-all-lessons]'):
        link=soup.new_tag('a',href=local_link(path,'sitemap.html'),attrs={'data-all-lessons':''});link.string='All lessons';footer.append(link)


def enhance_page(soup, path, prefix):
    path=Path(path);p=profile(path,soup);url=canonical(p['relative'])
    lesson_image(soup,p['relative'],ROOT)
    image=share_image(path,soup,p)
    soup.title.string=p['title']
    for selector in ['meta[name="description"]','meta[name="robots"]','link[rel="canonical"]','meta[property^="og:"]','meta[name^="twitter:"]','script[data-seo-schema]']:
        for node in soup.select(selector):node.decompose()
    def meta(name,value,property=False):
        soup.head.append(soup.new_tag('meta',attrs={'property' if property else 'name':name,'content':str(value)}))
    meta('description',p['description'])
    meta('robots','noindex, follow' if p['relative'] in NOINDEX else 'index, follow, max-image-preview:large')
    soup.head.append(soup.new_tag('link',rel='canonical',href=url))
    for name,value in {'title':p['title'],'description':p['description'],'url':url,'type':'website','site_name':'English Ladder',
                       'locale':'en_US','image':image['url'],'image:width':image['width'],'image:height':image['height'],'image:alt':image['alt']}.items():
        meta('og:'+name,value,True)
    for name,value in {'card':'summary_large_image' if image['large'] else 'summary','title':p['title'],'description':p['description'],'image':image['url'],'image:alt':image['alt']}.items():
        meta('twitter:'+name,value)
    write_schema(soup,structured_data(p,soup,image))
    if not soup.select_one('link[href*="seo.css"]'):
        soup.head.append(soup.new_tag('link',rel='stylesheet',href=prefix+'seo.css?v=20260906-seo1'))
    for section in soup.select('section[data-ai-workshop], [data-ai-extension] .ai-extension-body'): section['data-nosnippet']=''
    add_navigation(soup,path,p)
    for link in soup.select('a[href]'):
        if urljoin(url,link['href'])==ORIGIN+'index.html':link['href']='/'


def write_schema(soup,data):
    for old in soup.select('script[data-seo-schema]'):old.decompose()
    script=soup.new_tag('script',type='application/ld+json',attrs={'data-seo-schema':''})
    script.string=json.dumps(data,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c').replace('>','\\u003e').replace('&','\\u0026')
    soup.head.append(script)


def build_category_pages():
    from editorial import document, decorate_page
    target=ROOT/'english-for-work';target.mkdir(exist_ok=True)
    for name,c in CATEGORIES.items():
        group=[t for t in tracks().values() if t['category']==name]
        cards=''.join(f'<a class="work-course-card" href="../efsp-{t["slug"]}.html">{card_icon(t)}<span class="work-kicker">8 lessons · 4 free guides</span><h3>{html.escape(t["title"])}</h3><p>{html.escape(t["summary"])}</p><span class="work-card-footer">Explore lessons and dialogues →</span></a>' for t in group)
        grammar_links=''.join(f'<li><a href="../{grammar_url(n)}">{html.escape(grammar()[n]["title"])}</a></li>' for n in c['grammar'])
        body=f'''<section class="page-hero"><p class="eyebrow">English for Work · {len(group)} professional fields</p><h1>{html.escape(c['title'])}</h1><p>{html.escape(c['intro'])}</p></section>
<section class="work-section work-two-column"><div><h2>Choose the work you do</h2><p>{html.escape(c['choose'])}</p></div><div><h2>Make the practice practical</h2><p>{html.escape(c['practice'])}</p></div></section>
<section class="work-section"><h2>Your professional English courses</h2><p>Each course includes eight cases, vocabulary and grammar, complete professional dialogues, speaking and writing practice, four printable guides and AI extension prompts.</p><div class="work-course-grid">{cards}</div></section>
<section class="work-section work-two-column"><div><h2>Grammar you can use at work</h2><ul>{grammar_links}</ul></div><div><h2>Choose your support</h2><p>These materials suit intermediate to advanced learners. Use B1 sentence frames for support, B2 practice for independence, or C1 challenges for greater precision. These are study suggestions, not certified level assessments.</p><p><a href="../efsp.html">Browse all 41 English for Work courses →</a></p></div></section>'''
        page=target/(c['slug']+'.html')
        page.write_text(document(c['title'],body,'theme-efsp work-page','../','efsp.html').replace('</head>','<link rel="stylesheet" href="../work.css?v=20260906-quality1"></head>'))
        decorate_page(page)


def build_html_sitemap():
    from editorial import document,decorate_page
    def links(items):return '<ul>'+''.join(f'<li><a href="{href}">{html.escape(name)}</a></li>' for name,href in items)+'</ul>'
    body='<section class="page-hero"><p class="eyebrow">Find your next lesson</p><h1>Browse all English lessons</h1><p>Choose a subject, profession or reading level. Lessons and printable guides are free to use without an English Ladder account.</p></section>'
    body+='<section class="seo-directory"><h2>Reading, conversation and practice</h2>'+links([(PAGES[p][0],p) for p in ['study-routes.html','beginner.html','intermediate.html','advanced.html','archive.html','us-life.html','tools.html','ai-practice.html']])+links([('Food market: beginner reading','stories/food-market/beginner.html'),('Food market: intermediate reading','stories/food-market/intermediate.html'),('Food market: advanced reading','stories/food-market/advanced.html'),('City trees: beginner reading','stories/city-trees/beginner.html'),('City trees: intermediate reading','stories/city-trees/intermediate.html'),('City trees: advanced reading','stories/city-trees/advanced.html')])+'</section>'
    body+='<section class="seo-directory"><h2>English grammar lessons</h2><p><a href="grammar-concepts.html">Search and filter all 44 grammar topics</a></p>'+links([(c['title'],grammar_url(n))for n,c in grammar().items()])+'</section>'
    body+='<section class="seo-directory"><h2>English for Work</h2>'
    for name,c in CATEGORIES.items():
        body+=f'<h3><a href="{category_url(name)}">{html.escape(c["title"])}</a></h3>'+links([(t['title'],f'efsp-{t["slug"]}.html')for t in tracks().values()if t['category']==name])
    body+='</section>'
    path=ROOT/'sitemap.html';path.write_text(document('Browse all English lessons',body));decorate_page(path)


def xml_write(path, tree):
    ET.indent(tree,space='  ')
    path.parent.mkdir(parents=True,exist_ok=True)
    ET.ElementTree(tree).write(path,encoding='utf-8',xml_declaration=True)
    with path.open('ab') as out:out.write(b'\n')


def write_sitemaps(today=None):
    today=today or date.today().isoformat()
    manifest_path=ROOT/'content/seo-index.json'
    previous=json.loads(manifest_path.read_text()).get('resources',{}) if manifest_path.exists() else {}
    records={};groups={name:[] for name in ['pages','work','grammar','reading','pdfs']};images={}
    def add(relative,content,group,initial_date=''):
        fingerprint=hashlib.sha256(content).hexdigest();old=previous.get(relative,{})
        modified=old.get('lastmod') if old.get('sha256')==fingerprint else (initial_date if not old and initial_date else today)
        records[relative]={'sha256':fingerprint,'lastmod':modified}
        groups[group].append((canonical(relative),modified))
    for path in published_pages():
        relative=path.relative_to(ROOT).as_posix()
        soup=BeautifulSoup(path.read_text(),'html.parser')
        robots=soup.select_one('meta[name="robots"]')
        if relative in NOINDEX or (robots and 'noindex' in robots.get('content','')):continue
        can=soup.select_one('link[rel="canonical"]')
        if not can or can['href']!=canonical(relative):raise ValueError('Noncanonical sitemap page: '+relative)
        # Deployment timestamps and file mtimes never enter the index. A fresh
        # checkout or an unchanged daily rebuild leaves lastmod untouched.
        content=fingerprint(soup).encode()
        group='work' if relative.startswith(('efsp','english-for-work/')) else 'grammar' if relative.startswith('grammar-concepts') else 'reading' if relative.startswith(('news/','stories/')) else 'pages'
        add(relative,content,group)
        images[canonical(relative)]=sorted({urljoin(canonical(relative),i['src']) for i in soup.select('main img[src]') if 'brand/' not in i['src']})
        schema_tag=soup.select_one('[data-seo-schema]')
        if schema_tag:
            data=json.loads(schema_tag.string)
            for node in data['@graph']:
                if node['@type'] in {'WebPage','CollectionPage','AboutPage','LearningResource'}:node['dateModified']=records[relative]['lastmod']
            write_schema(soup,data);path.write_text(str(soup))
    work=read_json('content/work/documents.json')
    pdfs={p:meta.get('ai_prompt_edition',work['revision']) for p,meta in work['documents'].items()}
    for c in grammar().values():
        pdfs.update({('pdf/students/' if i == 0 else 'pdf/teachers/')+p:c.get('reviewed','') for i,p in enumerate(c['pdfs'])})
    for path,modified in sorted(pdfs.items()):add(path,(ROOT/path).read_bytes(),'pdfs',modified)
    index=ET.Element('{'+SITEMAP_NS+'}sitemapindex')
    for name,items in groups.items():
        tree=ET.Element('{'+SITEMAP_NS+'}urlset')
        for url,modified in sorted(items):
            node=ET.SubElement(tree,'{'+SITEMAP_NS+'}url');ET.SubElement(node,'{'+SITEMAP_NS+'}loc').text=url;ET.SubElement(node,'{'+SITEMAP_NS+'}lastmod').text=modified
            for source in images.get(url,[]):
                item=ET.SubElement(node,'{'+IMAGE_NS+'}image');ET.SubElement(item,'{'+IMAGE_NS+'}loc').text=source
        relative=f'sitemaps/{name}.xml';target=ROOT/relative
        xml_write(target,tree)
        node=ET.SubElement(index,'{'+SITEMAP_NS+'}sitemap');ET.SubElement(node,'{'+SITEMAP_NS+'}loc').text=canonical(relative)
        # Child maps omit index lastmod rather than invent a file publication date.
    xml_write(ROOT/'sitemap.xml',index)
    manifest_path.write_text(json.dumps({'resources':records},indent=2,sort_keys=True)+'\n')
    (ROOT/'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: '+ORIGIN+'sitemap.xml\n')
    return {name:len(items) for name,items in groups.items()}


def main():
    from editorial import decorate_page
    build_category_pages();build_html_sitemap()
    for path in published_pages():decorate_page(path)
    print('Published search metadata:',len(published_pages()),'pages;',write_sitemaps())


if __name__ == '__main__':main()
