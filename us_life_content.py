"""Publish the authored Everyday English content without generating paid assets."""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
AUDIO_POLICY = 'en-US-kore-v1'


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
    return units


def audio_path(term):
    slug = re.sub(r'[^a-z0-9]+', '-', term.lower()).strip('-')
    digest = hashlib.sha256((AUDIO_POLICY + ':' + term).encode()).hexdigest()[:12]
    return f'assets/audio/us-life/{slug}-{digest}.mp3'


def terms():
    return {word['term']: word['definition'] for unit in content().values() for word in unit['vocabulary']}


def enhance_page(soup):
    units = content()
    if {u['id'] for u in soup.select('.us-life-module')} != set(units):
        raise ValueError('Everyday English page and authored units do not match.')
    for key, unit in units.items():
        blocks = soup.find(id=key).select('.us-life-main .module-block')
        sentences = blocks[0].select_one('ul')
        sentences.clear()
        for sentence in unit['sentences']:
            li = soup.new_tag('li'); li.string = sentence; sentences.append(li)
        vocabulary = blocks[1].select_one('dl')
        vocabulary.clear()
        vocabulary['class'] = ['life-vocabulary']
        for word in unit['vocabulary']:
            dt = soup.new_tag('dt')
            label = soup.new_tag('span', attrs={'data-vocabulary-term': ''})
            label.string = word['term']; dt.append(label)
            link = soup.new_tag('a', href=audio_path(word['term']), attrs={
                'class': 'life-listen', 'data-pronunciation': word['term'],
                'data-pronunciation-ui': '', 'type': 'audio/mpeg',
                'aria-label': f'Listen to {word["term"]} in American English'})
            link.string = '▶ Listen'; dt.append(link)
            dd = soup.new_tag('dd'); dd.string = word['definition']
            vocabulary.extend([dt, dd])
        for old in blocks[1].select('[data-pronunciation-player], .life-audio-help'):
            old.decompose()
        help_text = soup.new_tag('p', attrs={'class': 'life-audio-help', 'data-pronunciation-ui': ''})
        help_text.string = '12 useful terms · Select Listen for American English pronunciation.'
        vocabulary.insert_before(help_text)
        player = soup.new_tag('div', attrs={'class': 'life-audio-player', 'data-pronunciation-player': '',
                                            'data-pronunciation-ui': '', 'hidden': ''})
        status = soup.new_tag('p', attrs={'data-pronunciation-status': '', 'role': 'status'})
        audio = soup.new_tag('audio', controls='', preload='none', attrs={'aria-label': 'Vocabulary pronunciation'})
        fallback = soup.new_tag('a', attrs={'data-pronunciation-fallback': ''}); fallback.string = 'Open audio file'
        player.extend([status, audio, fallback]); vocabulary.insert_after(player)
    if not soup.select_one('script[src^="us-life-audio.js"]'):
        soup.head.append(soup.new_tag('script', src='us-life-audio.js?v=20260929-1', defer=True))
    if not soup.select_one('link[href^="us-life-audio.css"]'):
        soup.head.append(soup.new_tag('link', rel='stylesheet', href='us-life-audio.css?v=20260929-1'))
