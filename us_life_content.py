"""Publish the authored Everyday English content without generating paid assets."""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
AUDIO_POLICY = 'en-US-kore-v1'
# Reading order in the Google Gemini icon sheet: four columns, six rows.
ICON_UNITS = (
    'arrival', 'documents', 'housing', 'utilities',
    'money', 'shopping', 'food', 'transportation',
    'health', 'appointments', 'school', 'work',
    'phone', 'mail', 'safety', 'community',
    'laundry', 'dry-cleaning', 'taxis', 'car-care',
    'personal-care', 'clothing-services', 'recreation', 'service-problems',
)


def content():
    units = json.loads((ROOT / 'content/us-life.json').read_text())
    if len(units) != 24:
        raise ValueError('Everyday English must contain all 24 units.')
    for key, unit in units.items():
        sentences, words = unit['sentences'], unit['vocabulary']
        if len(sentences) != 15 or len(set(sentences)) != 15:
            raise ValueError(f'{key}: expected 15 distinct useful sentences.')
        if len(words) != 12 or len({w['term'].casefold() for w in words}) != 12:
            raise ValueError(f'{key}: expected 12 distinct vocabulary terms.')
        if any(not s.strip() for s in sentences) or any(not w['definition'].strip() for w in words):
            raise ValueError(f'{key}: empty learning content.')
        customs, dialogue = unit['customs'], unit['dialogue']
        if len(customs) != 7 or len(set(customs)) != 7 or any(not tip.strip() for tip in customs):
            raise ValueError(f'{key}: expected 7 distinct customs tips.')
        if len(dialogue) != 10 or any(not turn['speaker'].strip() or not turn['text'].strip() for turn in dialogue):
            raise ValueError(f'{key}: expected 10 complete dialogue turns.')
    return units


def audio_path(term):
    slug = re.sub(r'[^a-z0-9]+', '-', term.lower()).strip('-')
    digest = hashlib.sha256((AUDIO_POLICY + ':' + term).encode()).hexdigest()[:12]
    return f'assets/audio/us-life/{slug}-{digest}.mp3'


def terms():
    return {word['term']: word['definition'] for unit in content().values() for word in unit['vocabulary']}


def unit_icon(soup, key):
    index = ICON_UNITS.index(key)
    return soup.new_tag('span', attrs={
        'class': 'life-unit-icon', 'aria-hidden': 'true',
        'data-unit-icon': key,
        'style': f'background-position:{(index % 4) * 100 / 3:.6f}% {(index // 4) * 20:.6f}%',
    })


def enhance_page(soup):
    units = content()
    if {u['id'] for u in soup.select('.us-life-module')} != set(units):
        raise ValueError('Everyday English page and authored units do not match.')
    if set(units) != set(ICON_UNITS):
        raise ValueError('Everyday English units and subject icons do not match.')
    shortcuts = soup.select('.us-life-jump-grid a')
    if len(shortcuts) != len(units) or {a['href'] for a in shortcuts} != {'#' + key for key in units}:
        raise ValueError('Everyday English shortcuts and units do not match.')
    for shortcut in shortcuts:
        for old in shortcut.select('.life-unit-icon'):
            old.decompose()
        shortcut.insert(0, unit_icon(soup, shortcut['href'][1:]))
    for key, unit in units.items():
        main = soup.find(id=key).select_one('.us-life-main')
        heading = main.select_one('.life-unit-heading')
        if heading is None:
            heading = soup.new_tag('div', attrs={'class': 'life-unit-heading'})
            text = soup.new_tag('div', attrs={'class': 'life-unit-heading-text'})
            for node in (main.select_one('.module-kicker'), main.h2, main.select_one('.module-skill')):
                text.append(node.extract())
            heading.append(text)
            main.insert(0, heading)
        for old in heading.select('.life-unit-icon'):
            old.decompose()
        heading.insert(0, unit_icon(soup, key))
        blocks = main.select('.module-block')
        for block, name in zip(blocks, ('life-sentences', 'life-vocabulary-block', 'life-customs', 'life-dialogue')):
            block['class'] = list(dict.fromkeys([*block.get('class', []), name]))
        sentences = blocks[0].select_one('ul, ol')
        sentences.name = 'ol'
        sentences.clear()
        for sentence in unit['sentences']:
            li = soup.new_tag('li'); li.string = sentence; sentences.append(li)
        vocabulary = blocks[1].select_one('dl')
        vocabulary.clear()
        vocabulary['class'] = ['life-vocabulary']
        for word in unit['vocabulary']:
            dt = soup.new_tag('dt')
            label = soup.new_tag('span', attrs={'data-vocabulary-term': ''})
            label.string = word['term']
            link = soup.new_tag('a', href=audio_path(word['term']), attrs={
                'class': 'life-listen', 'data-pronunciation': word['term'],
                'data-pronunciation-ui': '', 'type': 'audio/mpeg',
                'aria-label': f'Listen to {word["term"]} in American English',
                'title': f'Play pronunciation of {word["term"]}'})
            icon = soup.new_tag('span', attrs={'aria-hidden': 'true'}); icon.string = '▶'
            link.append(icon); dt.extend([link, label])
            dd = soup.new_tag('dd'); dd.string = word['definition']
            vocabulary.extend([dt, dd])
        for old in blocks[1].select('[data-pronunciation-player], .life-audio-help'):
            old.decompose()
        help_text = soup.new_tag('p', attrs={'class': 'life-audio-help', 'data-pronunciation-ui': ''})
        help_text.string = 'American English pronunciation'
        vocabulary.insert_before(help_text)
        player = soup.new_tag('div', attrs={'class': 'life-audio-player', 'data-pronunciation-player': '',
                                            'data-pronunciation-ui': '', 'hidden': ''})
        status = soup.new_tag('p', attrs={'data-pronunciation-status': '', 'role': 'status'})
        audio = soup.new_tag('audio', controls='', preload='none', attrs={'aria-label': 'Vocabulary pronunciation'})
        fallback = soup.new_tag('a', attrs={'data-pronunciation-fallback': ''}); fallback.string = 'Open audio file'
        player.extend([status, audio, fallback]); vocabulary.insert_after(player)
        customs = blocks[2].select_one('ul')
        customs.clear()
        for tip in unit['customs']:
            li = soup.new_tag('li'); li.string = tip; customs.append(li)
        for old in blocks[3].select('p, .life-dialogue-lines'):
            old.decompose()
        dialogue = soup.new_tag('div', attrs={'class': 'life-dialogue-lines'})
        blocks[3].append(dialogue)
        for turn in unit['dialogue']:
            paragraph = soup.new_tag('p')
            speaker = soup.new_tag('strong'); speaker.string = turn['speaker'] + ':'
            paragraph.extend([speaker, ' ' + turn['text']]); dialogue.append(paragraph)
    if not soup.select_one('script[src^="us-life-audio.js"]'):
        soup.head.append(soup.new_tag('script', src='us-life-audio.js?v=20260929-1', defer=True))
    if not soup.select_one('link[href^="us-life-audio.css"]'):
        soup.head.append(soup.new_tag('link', rel='stylesheet', href='us-life-audio.css'))
    soup.select_one('link[href^="us-life-audio.css"]')['href'] = 'us-life-audio.css?v=20260930-completion1'
