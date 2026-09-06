"""Shared offline publishing checks and durable learner-facing pages."""
import html
import json
from pathlib import Path
from urllib.parse import urljoin
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parent
ORIGIN='https://englishladder.com/'
LEVELS=('beginner','intermediate','advanced')
def e(s):return html.escape(str(s),quote=True)

def enhance_page(soup,path,prefix):
    relative=path.relative_to(ROOT).as_posix()
    if not soup.select_one('script[src*="site.js"]'):
        tag=soup.new_tag('script',src=prefix+'site.js?v=20260906b',defer=True);soup.head.append(tag)
    if not soup.select_one('link[href*="site.css"]'):
        soup.head.append(soup.new_tag('link',rel='stylesheet',href=prefix+'site.css?v=20260906b'))
    for a in soup.select('.site-links a'):
        if a.get_text(strip=True)=='Daily news':a['data-level-link']=''
    footer=soup.select_one('.site-footer')
    if footer:
        for target,label in [('archive.html','News archive'),('continue.html','My learning'),('about.html','About & corrections'),('privacy.html','Privacy')]:
            if not footer.find('a',href=prefix+target):
                a=soup.new_tag('a',href=prefix+target);a.string=label;footer.append(a)
    for a in soup.select('a.explore-story'):
        a['data-level-link']=''
    for a in soup.select('.story-levels a'):
        a['data-level-choice']=Path(a.get('href','')).stem
    for textarea in soup.select('.discussion textarea'):
        textarea['data-study-draft']=textarea.get('id','notes')
    for note in soup.select('.note-hint'):
        note.string='Notes stay on this page unless you turn on browser saving below. They are not submitted or graded.'
    if soup.select_one('.daily-lesson, .curriculum-page') or 'curriculum-page' in soup.body.get('class',[]):
        if not soup.select_one('[data-study-controls]'):
            panel=BeautifulSoup('''<details class="study-controls" data-study-controls><summary>Keep your place and notes</summary><label><input type="checkbox" data-save-study> Save my learning in this browser</label><p>Optional. Saves your recent lessons, practice notes, and selected words on this device. It does not create an account or send your writing to us. Shared device? Leave saving off.</p><p data-save-status role="status"></p></details>''','html.parser').details
            soup.main.insert(len(soup.main.contents)-1,panel)
        if 'curriculum-page' in soup.body.get('class',[]):
            panel=soup.select_one('[data-study-controls]');panel.summary.string='Keep your place and answers'
            panel.select_one('p:not([data-save-status])').string='Optional. Saves your recent lessons and multiple-choice selections on this device. It does not create an account. Shared device? Leave saving off.'
    if path.name in [v+'.html' for v in LEVELS] and path.parent==ROOT:
        hero=soup.select_one('.page-hero')
        if hero and not hero.select_one('[data-archive-link]'):
            a=soup.new_tag('a',href='archive.html',attrs={'data-archive-link':'','class':'text-link'});a.string='Browse all dated lessons →';hero.append(a)
        for lesson in soup.select('.daily-lesson'):
            key=lesson.get('data-lesson-key','')
            if not lesson.select_one('.permanent-lesson-link'):
                p=soup.new_tag('p',attrs={'class':'permanent-lesson-link'})
                a=soup.new_tag('a',href=f'news/{key}/{path.name}');a.string='Permanent link to this lesson';p.append(a)
                lesson.select_one('.lesson-content').append(p)
    for textarea in soup.select('textarea'):
        if not textarea.get('maxlength'):textarea['maxlength']='8000'
    from ai_extensions import enhance_page as enhance_ai
    enhance_ai(soup,path,prefix)
    # Give returning readers the current controls instead of cached older files.
    updated_assets={'app.js','learning.js','site.js','tools.js','work.js','us-life.js','styles.css','editorial.css','site.css','work.css','ai-practice.js'}
    for tag in soup.select('script[src],link[rel="stylesheet"][href]'):
        attr='src' if tag.name=='script' else 'href'
        asset=tag[attr].split('?',1)[0]
        if not asset.startswith(('https:','http:','//')) and Path(asset).name in updated_assets:
            version='20260906-seo1' if Path(asset).name in {'site.css','editorial.css'} else ('20260906-ai1' if Path(asset).name=='ai-practice.js' else ('20260906-choices2' if Path(asset).name=='site.js' else '20260906-quality1'))
            tag[attr]=asset+'?v='+version
    from seo import enhance_page as enhance_search
    enhance_search(soup,path,prefix)

def build_news_archive():
    from editorial import document,level_links,decorate_page
    from update_site import render_lesson_html,LEVELS as CONFIG,release_datetime_from_date
    cards=[];compact={}
    paths=sorted((ROOT/'archive/lessons').glob('*.json'),reverse=True)
    for path in paths:
        data=json.loads(path.read_text());date=data['release_date'];source=data.get('source',{})
        c=data['levels']['beginner']['lesson'];category=source.get('category','world')
        for config in CONFIG:
            level=config['name'].lower();lesson=data['levels'][level]['lesson']
            lesson_soup=BeautifulSoup(render_lesson_html(lesson,config,release_datetime_from_date(date),source),'html.parser')
            lesson_soup.details['open']=''
            lesson_soup.summary['hidden']=''
            for duplicate in lesson_soup.select('.lesson-description, .lesson-content > .header'):
                duplicate.decompose()
            content=str(lesson_soup)
            reviewed=data.get('editorial_review',{}).get('date') or lesson.get('editorial_check',{}).get('date','')[:10]
            notice=(f'Teaching text revised {reviewed}; this summary is limited to the saved source evidence.' if reviewed else 'Archive lesson. This older lesson has not yet received the September 2026 editorial review. Check the linked source for context.')
            body=f'<section class="page-hero"><p class="eyebrow">News archive · <time datetime="{date}">{date}</time> · {e(category)}</p><h1>{e(lesson["title"])}</h1><p>{e(lesson["overview"])}</p>{level_links(level)}<p class="archive-notice">{e(notice)}</p><a href="../../archive.html">Browse the archive</a></section>{content}'
            target=ROOT/'news'/date/f'{level}.html';target.parent.mkdir(parents=True,exist_ok=True)
            target.write_text(document(lesson['title'],body,f'theme-{level} news-permalink','../../',f'{level}.html'))
            decorate_page(target)
            if not compact.get(level):compact[level]={'headline':lesson['title'],'brief':' '.join(lesson['news_brief_sentences']),'url':f'news/{date}/{level}.html'}
        search=' '.join([c['title'],date,category,c['topic'],c['grammar']['concept'],*[v['term'] for v in c['vocabulary']]])
        links=' · '.join(f'<a href="news/{date}/{level}.html">{level.title()}</a>' for level in LEVELS)
        cards.append(f'<article class="library-card" data-library-item data-search="{e(search)}" data-category="{e(category)}"><p class="eyebrow">{date} · {e(category)}</p><h2><a data-level-link href="news/{date}/beginner.html">{e(c["title"])}</a></h2><p>{e(c["overview"])}</p><p>{links}</p></article>')
    cats=sorted({json.loads(p.read_text()).get('source',{}).get('category','world') for p in paths})
    body=f'<section class="page-hero"><p class="eyebrow">Return to a story</p><h1>News lesson archive</h1><p>Find a date, topic, word, or grammar point. Every story has a permanent link at each level.</p><p>Prefer everyday topics? Try <a href="stories/food-market/beginner.html" data-level-link>the food market</a> or <a href="stories/city-trees/beginner.html" data-level-link>trees in the city</a>.</p></section><section data-library><div class="library-filters"><label>Search the archive<input type="search" data-library-search placeholder="Try 2026-09, travel, or passive"></label><label>Topic<select data-library-category><option value="">All topics</option>{"".join(f"<option>{e(c)}</option>" for c in cats)}</select></label></div><p data-library-count role="status">{len(cards)} stories</p><p data-library-empty hidden>No stories match. Try another word or date.</p><div class="library-grid">{"".join(cards)}</div></section>'
    target=ROOT/'archive.html';target.write_text(document('News lesson archive',body));decorate_page(target)
    (ROOT/'lesson-data.json').write_text(json.dumps(compact,ensure_ascii=False,indent=2)+'\n')

def build_information_pages():
    from editorial import document,decorate_page
    pages={
      'about':('About English Ladder','''<p>English Ladder offers practical English for independent learners and teachers: daily news, grammar, everyday conversations, and English for Work. Phil Stilwell maintains the site. English Road, our sister site, helps you check your level.</p><h2>How lessons are made</h2><p>Grammar lessons and work courses use locally maintained teaching material. Daily news lessons use an automated drafting process based on saved source evidence. Automated checks test the lesson structure, evidence references, and question format. These checks reduce errors; they do not replace editorial judgment.</p><p>Level labels are study guidance, not certified assessments. Beginner lessons aim for short, useful language; higher levels add nuance and reasoning. Choose the level where you can understand the main idea and still learn something.</p><h2>News and difficult topics</h2><p>News may cover disasters, violence, or other difficult events. Topic notes help you choose. For a lighter starting point, use the everyday stories on Discover. Source links show where reporting came from; the lesson date is the release date, which may differ from the article date.</p><p>Lesson illustrations are labeled as AI-generated and are not photographs of reported events. Photographs have credits. English Ladder uses blue; English Road uses green so you can recognize where you are.</p><h2 id="corrections">Report a correction</h2><p>Found an unclear rule, incorrect answer, or layout problem? <a href="https://github.com/philstilwell/English-Ladder/issues/new?title=Lesson%20correction">Open a correction report</a> with the page address, the sentence or question, and a brief explanation. GitHub requires an account; please include no private learner information. You can also ask your teacher to submit a report.</p><h2>Recent corrections</h2><p>6 September 2026: revised all 44 grammar concepts and their PDF editions; converted all grammar response activities to multiple choice with feedback for each selected option; repaired incomplete diagnostic feedback; limited sentence tools to contextual suggestions; revised the latest seven news lessons to remove details unsupported by their saved summaries.</p><p>Corrections are also recorded with the affected news lesson data. See <a href="archive.html">the archive</a> for lesson dates.</p>'''),
      'privacy':('Privacy and your practice','''<p>You can read lessons and use practice activities without creating an English Ladder account.</p><h2>Saved learning and notes</h2><p>Your selected level and explanation language may be stored in this browser. Lesson history, saved words, multiple-choice selections, and practice notes are saved only when you turn on the relevant browser-saving control. Work courses have their own saving switch. Saved data is tied to this browser and device; it does not sync to another device and may disappear if browser data is cleared.</p><p>Your writing is not submitted for automatic grading. Do not enter sensitive personal, customer, patient, or employer information. Use fictional details for work practice. On a shared device, leave saving off or clear it when you finish. My learning lets you export or clear its saved data; work courses have separate controls.</p><h2>Optional AI practice</h2><p>AI extension buttons copy published lesson material to your clipboard. They do not include your drafts, saved answers, or recordings, and English Ladder does not send the prompts to an AI service. If you paste a prompt into another service, that service handles it under its own terms. Review its privacy and pricing information and use fictional details. The prompts are optional; the regular lessons work without AI.</p><h2>Audio and recording</h2><p>The optional practice recorder requests microphone permission only when you press Record. Recordings are kept in the current page for playback and are not uploaded by English Ladder. Leaving the page releases the microphone. The older model-voice control uses the browser's speech service; its implementation can vary by browser and device. It is optional.</p><h2>Visits and external services</h2><p>The site includes Cloudflare Web Analytics for aggregate traffic information. The site does not attach practice answers, notes, or recordings to custom analytics events. <a href="https://www.cloudflare.com/privacypolicy/">Cloudflare explains its data practices here</a>. The site is hosted on GitHub Pages; hosting providers may process connection information such as IP addresses in serving the site. External links, including English Road and correction reports on GitHub, have their own privacy practices.</p><p>Daily lesson generation happens separately from your browser practice. It uses news sources and external generation services; your drafts are not included.</p><p>Updated 6 September 2026.</p>'''),
      'continue':('My learning','''<p>Keep a small record of your practice on this device. Browser saving is optional and does not create an account.</p><section data-learning-dashboard><label><input type="checkbox" data-save-study> Save my learning in this browser</label><p data-save-status role="status"></p><h2>Continue a lesson</h2><div data-learning-history><p>Turn on saving, then open a lesson to start your list.</p></div><h2>Words to review</h2><p>Try remembering each meaning before opening it. Save words using the buttons beside a lesson's vocabulary.</p><div data-learning-words></div><div class="stage-actions"><button class="secondary-button" data-export-study type="button">Export my saved learning</button><button class="secondary-button" data-clear-study type="button">Clear saved learning</button></div><p>Work-course drafts have separate saving and clearing controls on their course pages.</p><noscript><p>Saved learning requires JavaScript and available browser storage. You can still use all <a href="grammar-concepts.html">grammar lessons</a> and <a href="archive.html">news lessons</a> without it.</p></noscript></section>'''),
      '404':('Let’s find your lesson','''<p>This address does not point to a published page. You can still find the lesson by topic or date.</p><div class="stage-actions"><a class="primary-button" href="/archive.html">Search news lessons</a><a class="secondary-button" href="/grammar-concepts.html">Browse grammar</a><a class="secondary-button" href="/index.html">Go to Discover</a></div>''')
    }
    for name,(title,copy) in pages.items():
        path=ROOT/f'{name}.html';path.write_text(document(title,f'<section class="page-hero"><p class="eyebrow">English Ladder</p><h1>{title}</h1></section><div class="reading-width information-page">{copy}</div>'));decorate_page(path)
        if name=='404':
            s=BeautifulSoup(path.read_text(),'html.parser')
            for tag in s.find_all(['a','link','script','img']):
                for attr in ['href','src']:
                    value=tag.get(attr,'')
                    if value and not value.startswith(('/','#','https:','http:')):tag[attr]='/'+value
            path.write_text(str(s))

def write_sitemap():
    from seo import write_sitemaps
    return write_sitemaps()

def publish_quality_pages():
    from ai_extensions import build_library
    build_library()
    build_news_archive();build_information_pages()

def rebuild_news_levels():
    """Rebuild rolling pages from archived data using the current renderer."""
    from update_site import render_lesson_html, LEVELS as CONFIG, LESSON_LIMIT, release_datetime_from_date
    archives=sorted((ROOT/'archive/lessons').glob('*.json'),reverse=True)[:LESSON_LIMIT]
    if not archives:return
    for config in CONFIG:
        path=ROOT/config['file_path']
        soup=BeautifulSoup(path.read_text(),'html.parser');container=soup.select_one('#lesson-container')
        if not container:continue
        container.clear()
        for archive in archives:
            data=json.loads(archive.read_text());lesson=data['levels'][config['name'].lower()]['lesson']
            node=BeautifulSoup(render_lesson_html(lesson,config,release_datetime_from_date(data['release_date']),data.get('source')),'html.parser').details
            container.append(node)
        path.write_text(str(soup))
