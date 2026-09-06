"""Lesson imagery, curriculum relationships, and stable search change tracking."""
import hashlib
import json
from pathlib import Path
from urllib.parse import urljoin
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parent
ORIGIN='https://englishladder.com/'
LEVELS={'beginner':'A1–A2','intermediate':'B1–B2','advanced':'C1+'}

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


def clean(value):
    return ' '.join(str(value).split())


def url(relative):
    return ORIGIN + ('' if relative == 'index.html' else relative)


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


def fingerprint(soup):
    # Relative lesson ages and runtime status text do not make an article new.
    main=BeautifulSoup(str(soup.main),'html.parser')
    for tag in main.select('.lesson-age, [role="status"], .site-footer, script, input, textarea'):
        tag.decompose()
    meaningful=[soup.title.get_text(),soup.select_one('meta[name="description"]')['content'],main.get_text(' ',strip=True),
                [(i.get('src'),i.get('alt')) for i in main.select('img')],
                [a.get('href') for a in main.select('a[href]')]]
    return hashlib.sha256(json.dumps(meaningful,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
