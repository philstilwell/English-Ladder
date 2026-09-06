"""Search metadata and discovery links derived from the published curriculum.

Offline only. No invented reviews, qualifications, course enrolments, or dates.
The final publishing pass writes sitemaps after every page has been decorated.
"""
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote, urljoin, urlparse
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent
ORIGIN = 'https://englishladder.com/'
LEVELS = {'beginner': 'A1–A2', 'intermediate': 'B1–B2', 'advanced': 'C1+'}
NOINDEX = {'404.html', 'continue.html'}
STATE_PATH = 'content/seo-state.json'
NS = 'http://www.sitemaps.org/schemas/sitemap/0.9'
IMAGE_NS = 'http://www.google.com/schemas/sitemap-image/1.1'

HUBS = {
    'index.html': ('Free English Lessons: Grammar, News & Work',
        'Learn English with daily news at three levels, 44 grammar lessons, workplace conversations, everyday English, free PDF workbooks, and ready-to-copy AI prompts.'),
    'grammar-concepts.html': ('English Grammar Lessons, Exercises & Free PDFs',
        'Explore 44 English grammar lessons with clear examples, multiple-choice exercises, answer explanations, free learner workbooks, and teaching guides.'),
    'efsp.html': ('English for Work: 41 Fields & Free Workbooks',
        'Practice workplace English in 41 fields with 328 lessons, realistic dialogues, professional vocabulary, AI practice prompts, and 164 free PDF guides.'),
    'archive.html': ('English News Reading Lessons by Date & Topic',
        'Browse English news lessons by date, topic, vocabulary, or grammar. Choose beginner, intermediate, or advanced readings with comprehension exercises.'),
    'tools.html': ('Free English Practice Tools: Grammar, Speaking & Writing',
        'Practice English grammar, sentence editing, pronunciation, reading, workplace phrases, and formal or casual language with six free study tools.'),
    'us-life.html': ('Everyday English: 24 Lessons for Life in the US',
        'Learn everyday English for housing, shopping, transport, appointments, and life in the US. Explore 24 units with useful vocabulary and model conversations.'),
    'ai-practice.html': ('AI Prompts for Learning English: Ready to Copy',
        'Copy complete AI prompts for English vocabulary, grammar, reading, workplace dialogues, and review. Lesson context is included; no prompt writing is needed.'),
    'about.html': ('About English Ladder & Our Teaching Approach',
        'Meet English Ladder, maintained by Phil Stilwell. Learn how our English lessons are produced, what level labels mean, and how to report a correction.'),
    'privacy.html': ('Privacy, Saved Practice & Optional AI Use',
        'Understand how English Ladder handles browser saving, practice notes, recordings, analytics, and optional copy-and-paste AI prompts.'),
    'photo-credits.html': ('Photo Credits & AI Illustration Information',
        'Find photographers, source links, and licenses for English Ladder images, plus information about the clearly labeled AI illustrations in daily lessons.'),
    'continue.html': ('My Learning: Saved English Lessons & Vocabulary',
        'Return to English lessons and review saved vocabulary on this device. Browser saving is optional and does not create an account.'),
    '404.html': ('Page Not Found — Find Your English Lesson',
        'Find an English Ladder lesson by topic or date using the news archive, grammar library, or Discover page.'),
}

# The relationships are teaching choices, not arbitrary adjacent lesson numbers.
RELATED_GRAMMAR = {
    1:[15,19,31], 2:[1,11,19], 3:[6,34,38], 4:[14,9,32], 5:[1,15,29],
    6:[21,34,38], 7:[33,19,36], 8:[35,26,44], 9:[4,30,32], 10:[3,18,40],
    11:[2,19,36], 12:[28,25,42], 13:[29,17,41], 14:[4,26,35], 15:[1,16,31],
    16:[14,15,26], 17:[44,29,36], 18:[25,28,37], 19:[1,2,11], 20:[21,22,31],
    21:[27,23,37], 22:[20,21,43], 23:[21,27,37], 24:[36,41,9], 25:[18,23,32],
    26:[14,16,35], 27:[21,23,37], 28:[12,18,42], 29:[13,17,30], 30:[9,29,40],
    31:[1,15,20], 32:[9,25,30], 33:[7,36,39], 34:[3,6,38], 35:[8,14,26],
    36:[11,24,42], 37:[21,23,27], 38:[6,34,43], 39:[3,33,36], 40:[10,27,30],
    41:[13,24,36], 42:[12,28,36], 43:[16,22,38], 44:[8,17,29],
}
GRAMMAR_MATCHES = [
    (r'past perfect',26), (r'past continuous|past progressive',14),
    (r'could|able to',35), (r'might|possibility|may ',8),
    (r'cause|because',9), (r'purpose|so that',30), (r'relative clause',12),
    (r'countable|uncountable',21), (r'quantity|quantifier',23),
    (r'preposition.*time|in, on|in/on',1), (r'deadline|duration',15),
    (r'recommend|suggest',17), (r'advice',44), (r'reporting verb|reported speech',36),
    (r'contrast|although|even though',32), (r'trend|comparative',43),
]


def clean(value):
    return ' '.join(str(value).split())


def url(relative):
    return ORIGIN + ('' if relative == 'index.html' else relative)


def pages(root=ROOT):
    return sorted([*root.glob('*.html'), *root.glob('grammar-concepts/*.html'),
                   *root.glob('stories/*/*.html'), *root.glob('news/*/*.html')])


def concepts(root=ROOT):
    return json.loads((root/'content/grammar-curriculum.json').read_text())['concepts']


def reading_data(relative, root=ROOT):
    parts = Path(relative).parts
    if len(parts) != 3 or parts[0] not in {'news', 'stories'}:
        return None, None
    level = Path(relative).stem
    if level not in LEVELS:
        return None, None
    if parts[0] == 'news':
        data = json.loads((root/'archive/lessons'/f'{parts[1]}.json').read_text())
        return data['levels'][level]['lesson'], data
    from story_lessons import STORIES
    story = next(s for s in STORIES if s['slug'] == parts[1])
    return story['levels'][level], None


def metadata(soup, relative, root=ROOT):
    heading = clean(soup.h1.get_text(' ', strip=True))
    info = {'name': heading, 'type': 'WebPage', 'level': '', 'teaches': []}
    if relative in HUBS:
        title, description = HUBS[relative]
        info['name'] = title
        if relative in {'index.html','grammar-concepts.html','efsp.html','archive.html','ai-practice.html'}:
            info['type'] = 'CollectionPage'
        elif relative == 'about.html':
            info['type'] = 'AboutPage'
        elif relative in {'tools.html','us-life.html'}:
            info['resource'] = True
            info['teaches'] = ['English communication', 'English vocabulary']
    elif relative in {f'{v}.html' for v in LEVELS}:
        level = Path(relative).stem
        title = f'{level.title()} English News Lessons & Reading Practice'
        description = f'Read the latest seven news lessons in {level} English ({LEVELS[level]}). Build vocabulary, explore grammar, and check comprehension with explained answers.'
        info.update(type='CollectionPage', level=LEVELS[level], name=title)
    elif relative.startswith('grammar-concepts/'):
        number = int(Path(relative).stem.split('-')[-1])
        c = concepts(root)[number-1]
        title = f'{c["title"]}: Grammar & Exercises'
        description = f'{c["goal"]} {c["level"]} English grammar with examples, multiple-choice exercises, explained answers, and free PDFs.'
        info.update(resource=True, level=c['level'], teaches=[c['goal']], category=c['category'], number=number)
    elif relative.startswith('efsp-'):
        intro = soup.select_one('.work-intro')
        title = f'{heading}: Lessons & Free PDFs'
        description = intro.get_text(' ', strip=True)
        if ' curriculum for ' in description:
            description = f'Practice {heading} for '+description.split(' curriculum for ',1)[1]
        description += ' Includes free PDF guides.'
        info.update(resource=True, level='B1–C1', teaches=[heading])
    else:
        lesson, archive = reading_data(relative, root)
        if lesson:
            level = Path(relative).stem
            # Long advanced headlines can use the same story's concise beginner
            # headline; the visible article heading and teaching text stay intact.
            headline = archive['levels']['beginner']['lesson']['title'] if archive and len(heading)>65 else heading
            title = f'{headline} | {level.title()} English'
            if archive:title += ' · '+archive['release_date']
            # Describe the lesson, rather than amplifying claims from old reports.
            when = f' · {Path(relative).parent.name}' if archive else ''
            description = f'{level.title()} English reading ({LEVELS[level]}){when}: {headline.rstrip(".")}. Includes vocabulary, grammar, and comprehension exercises.'
            info.update(resource=True, level=LEVELS[level], teaches=[lesson['grammar']['concept'], 'Reading comprehension'], lesson=lesson)
            if archive:
                info.update(published=archive['release_date'], source=archive.get('source',{}))
        else:
            title = heading
            p = soup.select_one('main p:not(.eyebrow)')
            description = p.get_text(' ', strip=True) if p else heading
    info.update(title=title+' | English Ladder', description=clean(description), canonical=url(relative))
    return info


def breadcrumbs(soup, relative, info):
    if relative == 'index.html':
        return []
    trail = [('English Ladder', ORIGIN)]
    if relative.startswith('grammar-concepts/'):
        trail.append(('English grammar', url('grammar-concepts.html')))
    elif relative.startswith('efsp-'):
        trail.append(('English for Work', url('efsp.html')))
    elif relative.startswith('news/'):
        trail.extend([('News lessons', url('archive.html')),
                      (Path(relative).stem.title()+' English', url(Path(relative).name))])
    elif relative.startswith('stories/'):
        trail.append(('Everyday English', url('us-life.html')))
    trail.append((info['name'], info['canonical']))
    # Replace the old grammar-only trail with the same hierarchy used in schema.
    for old in soup.select('nav.breadcrumb, [data-seo-breadcrumb]'):
        old.decompose()
    nav = soup.new_tag('nav', attrs={'class':'search-breadcrumb','aria-label':'Breadcrumb','data-seo-breadcrumb':''})
    ol = soup.new_tag('ol')
    for i,(label,href) in enumerate(trail):
        li=soup.new_tag('li')
        child=soup.new_tag('span',attrs={'aria-current':'page'}) if i == len(trail)-1 else soup.new_tag('a',href=urlparse(href).path or '/')
        child.string=label
        li.append(child);ol.append(li)
    nav.append(ol);soup.main.insert(0,nav)
    return trail


def add_related(soup, relative, info, root):
    for old in soup.select('[data-seo-related]'):
        old.decompose()
    numbers = RELATED_GRAMMAR.get(info.get('number'), [])
    label = 'Build on this grammar'
    if info.get('lesson'):
        focus = info['lesson']['grammar']['concept'].lower()
        numbers = list(dict.fromkeys(n for pattern,n in GRAMMAR_MATCHES if re.search(pattern,focus)))[:2]
        label = 'Keep practicing this English'
    if relative.startswith('efsp-'):
        numbers = [17,30,44]
        label = 'Useful grammar for work'
    if not (info.get('resource') or relative in {'index.html','archive.html'}):
        return
    curriculum=concepts(root)
    links=[(url(f'grammar-concepts/concept-{n:02}.html'),curriculum[n-1]['title']) for n in numbers]
    if info.get('lesson'):
        links.extend([(url('grammar-concepts.html'),'Explore the grammar library'),(url('archive.html'),'More English reading lessons')])
    elif not numbers:
        links=[(url('grammar-concepts.html'),'English grammar exercises'),(url('archive.html'),'English reading practice'),(url('efsp.html'),'Workplace English lessons')]
        if relative=='us-life.html':
            links=[(url('stories/food-market/beginner.html'),'English conversation at a food market'),
                   (url('stories/city-trees/beginner.html'),'Read about trees in the city'),
                   (url('grammar-concepts.html'),'English grammar exercises')]
    section=soup.new_tag('section',attrs={'class':'search-related','data-seo-related':''})
    h=soup.new_tag('h2');h.string=label if numbers or info.get('lesson') else 'Choose your next English lesson';section.append(h)
    ul=soup.new_tag('ul')
    for href,text in links:
        li=soup.new_tag('li');a=soup.new_tag('a',href=urlparse(href).path);a.string=text;li.append(a);ul.append(li)
    section.append(ul)
    footer=soup.select_one('.site-footer')
    footer.insert_before(section) if footer else soup.main.append(section)


def lesson_image(soup, relative, root):
    """Use an existing, visible, relevant image. Never generate an image here."""
    for old in soup.select('[data-seo-lesson-image]'):
        old.decompose()
    if relative.startswith('news/'):
        _, archive = reading_data(relative, root)
        from daily_images import image_for_lesson
        image = image_for_lesson(archive, root)
        if image:
            figure=soup.new_tag('figure',attrs={'class':'lesson-cover','data-seo-lesson-image':''})
            figure.append(soup.new_tag('img',src='/'+image['path'],width=image['width'],height=image['height'],alt=image['alt'],loading='lazy',decoding='async'))
            caption=soup.new_tag('figcaption');caption.string='AI-generated illustration inspired by this lesson; not a photograph of the reported event.';figure.append(caption)
            soup.select_one('.page-hero').insert_after(figure)
    elif relative.startswith('stories/'):
        slug=Path(relative).parent.name
        credits=json.loads((root/'assets/editorial/credits.json').read_text())
        credit=next((c for c in credits if c['key']==slug),None)
        if credit and (root/f'assets/editorial/{slug}.webp').is_file():
            figure=soup.new_tag('figure',attrs={'class':'lesson-cover','data-seo-lesson-image':''})
            figure.append(soup.new_tag('img',src=f'/assets/editorial/{slug}.webp',width=credit['width'],height=credit['height'],alt=credit['alt'],loading='lazy',decoding='async'))
            caption=soup.new_tag('figcaption');caption.append('Photograph by ')
            link=soup.new_tag('a',href=credit['source_page']);link.string=credit['creator']+' / Unsplash';caption.append(link)
            caption.append('. ');license_link=soup.new_tag('a',href=credit['license_url']);license_link.string=credit['license'];caption.append(license_link)
            figure.append(caption);soup.select_one('.page-hero').insert_after(figure)
    selected=soup.select_one('.feature-photo img, .lesson-cover img, .story-image img, img.story-image')
    if not selected:
        selected=next((i for i in soup.select('main img') if 'brand' not in i.get('src','')),None)
    if selected:
        return {'url':urljoin(url(relative),selected['src']), 'width':int(selected['width']),
                'height':int(selected['height']), 'caption':selected.get('alt','')}
    return {'url':url('assets/brand/ladder-mark.png'),'width':256,'height':256,'caption':'English Ladder logo'}


def collection_items(soup, relative):
    selectors={
        'grammar-concepts.html':'.library-card h2 a', 'efsp.html':'[data-work-course-link]',
        'archive.html':'.library-card h2 a', 'ai-practice.html':'article h2 a',
        'index.html':'.path-link, .explore-story',
    }
    selector=selectors.get(relative,'.permanent-lesson-link a' if relative in {f'{v}.html' for v in LEVELS} else '')
    items=[]
    if selector:
        for a in soup.select(selector):
            href=urljoin(url(relative),a['href'])
            title=a.select_one('h2,h3')
            name=title.get_text(' ',strip=True) if title else a.get_text(' ',strip=True)
            if relative in {f'{v}.html' for v in LEVELS}:
                owner=a.find_parent('details',class_='daily-lesson')
                name=owner.select_one('.lesson-title-text').get_text(' ',strip=True)
            items.append({'@type':'ListItem','position':len(items)+1,'name':name,'url':href})
    return items


def schema(soup, relative, info, trail, image, root):
    canonical=info['canonical']
    organization={'@type':'Organization','@id':ORIGIN+'#organization','name':'English Ladder',
                  'url':ORIGIN,'logo':{'@type':'ImageObject','url':url('assets/brand/ladder-mark.png'),'width':256,'height':256}}
    website={'@type':'WebSite','@id':ORIGIN+'#website','url':ORIGIN,'name':'English Ladder',
             'alternateName':'EnglishLadder','inLanguage':'en','publisher':{'@id':ORIGIN+'#organization'}}
    page={'@type':info['type'],'@id':canonical+'#webpage','url':canonical,'name':info['title'],
          'description':info['description'],'inLanguage':'en','isPartOf':{'@id':ORIGIN+'#website'}}
    graph=[organization,website,page]
    if trail:
        node={'@type':'BreadcrumbList','@id':canonical+'#breadcrumb','itemListElement':[
            {'@type':'ListItem','position':i+1,'name':label,'item':href} for i,(label,href) in enumerate(trail)]}
        graph.append(node);page['breadcrumb']={'@id':node['@id']}
    image_node={'@type':'ImageObject','@id':canonical+'#primaryimage',**image,'contentUrl':image['url']}
    graph.append(image_node);page['primaryImageOfPage']={'@id':image_node['@id']}
    if info.get('resource'):
        resource={'@type':'LearningResource','@id':canonical+'#lesson','name':info['name'],
                  'description':info['description'],'url':canonical,'inLanguage':'en','isAccessibleForFree':True,
                  'learningResourceType':'English language lesson','teaches':info['teaches'],
                  'provider':{'@id':ORIGIN+'#organization'},'mainEntityOfPage':{'@id':page['@id']}}
        if info.get('level'):resource['educationalLevel']=info['level']
        if info.get('published'):resource['datePublished']=info['published']
        source=info.get('source',{}).get('link','')
        if source.startswith('https://'):resource['citation']=source
        downloads=[]
        seen=set()
        for a in soup.select('a[href]'):
            href=urljoin(canonical,a['href']).split('?',1)[0]
            if not href.endswith('.pdf') or not href.startswith(ORIGIN) or href in seen:continue
            seen.add(href)
            title=a.select_one('strong')
            downloads.append({'@type':'LearningResource','name':info['name']+' — '+(title.get_text(' ',strip=True) if title else a.get_text(' ',strip=True)),
                              'url':href,'encodingFormat':'application/pdf','inLanguage':'en','isAccessibleForFree':True})
        if downloads:resource['hasPart']=downloads
        graph.append(resource);page['mainEntity']={'@id':resource['@id']}
    items=collection_items(soup,relative)
    if items:
        listing={'@type':'ItemList','@id':canonical+'#lessons','numberOfItems':len(items),'itemListElement':items}
        graph.append(listing);page['mainEntity']={'@id':listing['@id']}
    return {'@context':'https://schema.org','@graph':graph}


def write_schema(soup, data):
    for old in soup.select('script[data-seo-schema]'):
        old.decompose()
    tag=soup.new_tag('script',type='application/ld+json',attrs={'data-seo-schema':''})
    # Prevent lesson text containing a closing script tag from escaping JSON-LD.
    tag.string=json.dumps(data,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c').replace('>','\\u003e').replace('&','\\u0026')
    soup.head.append(tag)


def enhance_page(soup, path, prefix, root=ROOT):
    relative=path.relative_to(root).as_posix()
    info=metadata(soup,relative,root)
    soup.title.string=info['title']
    soup.html['lang']='en'
    for old in soup.select('meta[name="description"],link[rel="canonical"],meta[property^="og:"],meta[name^="twitter:"],meta[name="robots"]'):
        old.decompose()
    soup.head.append(soup.new_tag('link',rel='canonical',href=info['canonical']))
    image=lesson_image(soup,relative,root)
    tags=[('name','description',info['description']),('name','robots','noindex, follow' if relative in NOINDEX else 'index, follow, max-image-preview:large'),
          ('property','og:title',info['title']),('property','og:description',info['description']),
          ('property','og:url',info['canonical']),('property','og:type','website'),('property','og:site_name','English Ladder'),
          ('property','og:locale','en_US'),('property','og:image',image['url']),
          ('property','og:image:width',str(image['width'])),('property','og:image:height',str(image['height'])),('property','og:image:alt',image['caption']),
          ('name','twitter:card','summary_large_image' if image['width']>=600 else 'summary'),
          ('name','twitter:title',info['title']),('name','twitter:description',info['description']),
          ('name','twitter:image',image['url']),('name','twitter:image:alt',image['caption'])]
    for key,name,value in tags:soup.head.append(soup.new_tag('meta',attrs={key:name,'content':value}))
    for a in soup.select('a[href]'):
        href=urljoin(info['canonical'],a['href'])
        if href == ORIGIN+'index.html':a['href']='/'
    # Keep repeated tutor instructions out of snippets without hiding lessons.
    for node in soup.select('.ai-extension-body, [data-ai-workshop]'):
        node['data-nosnippet']=''
    trail=breadcrumbs(soup,relative,info)
    add_related(soup,relative,info,root)
    write_schema(soup,schema(soup,relative,info,trail,image,root))


def fingerprint(soup):
    # Relative lesson ages and runtime status text do not make an article new.
    main=BeautifulSoup(str(soup.main),'html.parser')
    for tag in main.select('.lesson-age, [role="status"], .site-footer, script, input, textarea'):
        tag.decompose()
    meaningful=[soup.title.get_text(),soup.select_one('meta[name="description"]')['content'],main.get_text(' ',strip=True),
                [(i.get('src'),i.get('alt')) for i in main.select('img')],
                [a.get('href') for a in main.select('a[href]')]]
    return hashlib.sha256(json.dumps(meaningful,ensure_ascii=False,sort_keys=True).encode()).hexdigest()


def publish_search_assets(root=ROOT, today=None):
    today=today or datetime.now(timezone.utc).date().isoformat()
    state_path=root/STATE_PATH
    old=json.loads(state_path.read_text()).get('pages',{}) if state_path.exists() else {}
    state={};urls=[];pdfs=set()
    for path in pages(root):
        relative=path.relative_to(root).as_posix()
        soup=BeautifulSoup(path.read_text(),'html.parser')
        if relative in NOINDEX:continue
        digest=fingerprint(soup)
        previous=old.get(relative,{})
        # This first release meaningfully revises descriptions, navigation, and lessons.
        modified=previous['modified'] if previous.get('sha256')==digest else today
        state[relative]={'sha256':digest,'modified':modified}
        tag=soup.select_one('script[data-seo-schema]')
        data=json.loads(tag.string)
        for node in data['@graph']:
            if node['@type'] in {'WebPage','CollectionPage','AboutPage','LearningResource'}:
                node['dateModified']=modified
        write_schema(soup,data)
        path.write_text(str(soup),encoding='utf-8')
        images=[urljoin(url(relative),i['src']) for i in soup.select('main img[src]') if 'brand/' not in i['src']]
        urls.append((url(relative),modified,sorted(set(images))))
        for a in soup.select('a[href]'):
            link=urljoin(url(relative),a['href']).split('?',1)[0]
            if link.startswith(ORIGIN) and link.endswith('.pdf'):pdfs.add(link)
    # Include only publicly linked, existing guides. PDF dates use their own bytes.
    for link in sorted(pdfs):
        relative=unquote(link[len(ORIGIN):]);path=root/relative
        if not path.is_file():raise ValueError(f'Missing linked PDF: {relative}')
        digest=hashlib.sha256(path.read_bytes()).hexdigest();previous=old.get(relative,{})
        modified=previous['modified'] if previous.get('sha256')==digest else (today if previous else None)
        state[relative]={'sha256':digest,'modified':modified}
        # First-seen PDFs have no inferred publication/update date.
        urls.append((link,modified,[]))
    ET.register_namespace('',NS);ET.register_namespace('image',IMAGE_NS)
    tree=ET.Element(f'{{{NS}}}urlset')
    for address,modified,images in sorted(urls):
        item=ET.SubElement(tree,f'{{{NS}}}url');ET.SubElement(item,f'{{{NS}}}loc').text=address
        if modified:ET.SubElement(item,f'{{{NS}}}lastmod').text=modified
        for source in images:
            image=ET.SubElement(item,f'{{{IMAGE_NS}}}image');ET.SubElement(image,f'{{{IMAGE_NS}}}loc').text=source
    ET.indent(tree,space='  ')
    ET.ElementTree(tree).write(root/'sitemap.xml',encoding='utf-8',xml_declaration=True)
    (root/'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: '+ORIGIN+'sitemap.xml\n')
    state_path.parent.mkdir(parents=True,exist_ok=True)
    state_path.write_text(json.dumps({'version':1,'pages':state},sort_keys=True,indent=2)+'\n')
    return len(urls)


def audit_search(root=ROOT):
    failures=[];titles=Counter();descriptions=Counter();expected=set();count=0
    for path in pages(root):
        relative=path.relative_to(root).as_posix();s=BeautifulSoup(path.read_text(),'html.parser');count+=1
        for selector in ['title','meta[name="description"]','link[rel="canonical"]','meta[name="robots"]','script[data-seo-schema]',
                         'meta[property="og:image"]','meta[name="twitter:card"]']:
            if len(s.select(selector))!=1:failures.append(f'{relative}: expected one {selector}')
        if not s.select_one('script[data-seo-schema]'):continue
        canonical=s.select_one('link[rel="canonical"]')['href']
        if canonical != url(relative):failures.append(f'{relative}: incorrect canonical')
        if relative not in NOINDEX:
            titles[s.title.get_text()]+=1;descriptions[s.select_one('meta[name="description"]')['content']]+=1;expected.add(canonical)
        elif 'noindex' not in s.select_one('meta[name="robots"]')['content']:failures.append(f'{relative}: must not be indexed')
        data=json.loads(s.select_one('script[data-seo-schema]').string)
        if data.get('@context')!='https://schema.org':failures.append(f'{relative}: invalid schema context')
        ids=[node['@id'] for node in data['@graph']]
        if len(ids)!=len(set(ids)):failures.append(f'{relative}: duplicate schema identifiers')
        for node in data['@graph']:
            if node['@type']=='BreadcrumbList':
                visible=[n.get_text(' ',strip=True) for n in s.select('[data-seo-breadcrumb] li')]
                if visible!=[n['name'] for n in node['itemListElement']]:failures.append(f'{relative}: breadcrumb mismatch')
            if node['@type'] in {'Course','NewsArticle','FAQPage','AggregateRating'}:failures.append(f'{relative}: unsupported claim in schema')
            for field in ['datePublished','dateModified']:
                if field in node:
                    try:datetime.strptime(node[field],'%Y-%m-%d')
                    except ValueError:failures.append(f'{relative}: invalid {field}')
        preview=s.select_one('meta[property="og:image"]')['content']
        if not preview.startswith(ORIGIN) or not (root/unquote(preview[len(ORIGIN):])).is_file():
            failures.append(f'{relative}: missing local sharing image')
        if s.select_one('meta[property="og:url"]')['content']!=canonical:failures.append(f'{relative}: sharing/canonical URL mismatch')
        for a in s.select('a[href]'):
            link=urljoin(canonical,a['href']).split('?',1)[0]
            if link.startswith(ORIGIN) and link.endswith('.pdf'):expected.add(link)
    failures.extend(f'Duplicate title ({n}): {title}' for title,n in titles.items() if n>1)
    failures.extend(f'Duplicate description ({n}): {desc}' for desc,n in descriptions.items() if n>1)
    tree=ET.parse(root/'sitemap.xml');locations=[n.text for n in tree.findall(f'{{{NS}}}url/{{{NS}}}loc')]
    if len(locations)!=len(set(locations)):failures.append('Duplicate sitemap URLs')
    if set(locations)!=expected:failures.append(f'Sitemap differs from indexable pages/linked guides: {set(locations)^expected}')
    for node in tree.findall(f'{{{NS}}}url/{{{IMAGE_NS}}}image/{{{IMAGE_NS}}}loc'):
        if not node.text.startswith(ORIGIN) or not (root/unquote(node.text[len(ORIGIN):])).is_file():failures.append(f'Missing sitemap image: {node.text}')
    if failures:raise AssertionError('\n'.join(failures[:50]))
    return {'html_pages':count,'indexable_html_pages':len(titles),'sitemap_urls':len(locations),
            'duplicate_titles':0,'duplicate_descriptions':0,'failures':[]}


if __name__=='__main__':
    print(json.dumps(audit_search(),indent=2))
