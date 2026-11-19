"""Publish the reviewed Power Grammar transcription as native HTML accordions.

Square brackets in correction strings identify blue additions; ^ is the red
deletion marker used by the original worksheets. Original learner errors remain
intentional. The first answer is the clean corrected version; the remaining
answers are alternatives. All are correct examples, never quiz distractors.
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'content/power-grammar.json'


def load_exercises():
    data = json.loads(SOURCE.read_text(encoding='utf-8'))
    exercises = data['exercises']
    if [item['number'] for item in exercises] != list(range(1, 201)):
        raise ValueError('Power Grammar requires exactly exercises 1–200, in order.')
    for item in exercises:
        number = item['number']
        expected = f'{(number-1)//10+1:02}-{(number-1)%10+1:02}.jpg'
        if item['source'] != expected or not item['original'].strip():
            raise ValueError(f'Exercise {number}: missing or mismatched original.')
        if not item.get('reviewed') or not item['alternatives'] or not item['correction'].strip():
            raise ValueError(f'Exercise {number}: review and alternatives are required.')
        if len(item['alternatives']) != item['source_alternative_count']:
            raise ValueError(f'Exercise {number}: an original alternative is missing.')
        if item['correction'].count('^') != item['source_caret_count']:
            raise ValueError(f'Exercise {number}: an original caret is missing.')
        plain = re.sub(r'\[[^\[\]]+\]', '', item['correction'])
        if '[' in plain or ']' in plain:
            raise ValueError(f'Exercise {number}: invalid correction annotation.')
        if any(not text.strip() for text in item['alternatives']):
            raise ValueError(f'Exercise {number}: empty alternative.')
    return exercises


def marked_text(value):
    """Escape all source text; accept only the two documented annotations."""
    parts = re.split(r'(\[[^\[\]]+\]|\^)', value)
    result = []
    for part in parts:
        if part == '^':
            result.append('<span class="pg-caret" aria-label="removed wording">^</span>')
        elif part.startswith('[') and part.endswith(']'):
            result.append(f'<span class="pg-added">{html.escape(part[1:-1])}</span>')
        else:
            result.append(html.escape(part))
    return ''.join(result)


def section_html():
    exercises = load_exercises()
    groups = []
    for start in range(0, 200, 10):
        items = []
        for item in exercises[start:start+10]:
            number = item['number']
            clean_version = html.escape(item['alternatives'][0])
            alternatives = ''.join(f'<li>{html.escape(text)}</li>' for text in item['alternatives'][1:])
            note = f'<p class="pg-note">{html.escape(item["note"])}</p>' if item.get('note') else ''
            items.append(f'''<article class="pg-exercise" id="power-grammar-{number}" aria-labelledby="pg-title-{number}">
<h3 id="pg-title-{number}">Exercise {number}</h3>
<p class="pg-original">{html.escape(item['original'])}</p>
<details class="pg-answer"><summary>Corrections and alternative sentences<span class="sr-only"> for exercise {number}</span></summary>
<div class="pg-answer-content"><h4>Marked correction</h4><p class="pg-correction">{marked_text(item['correction'])}</p>
<ul class="pg-alternatives pg-clean-version"><li><strong>{clean_version}</strong></li></ul>
<h4>Alternative correct sentences</h4><ul class="pg-alternatives">{alternatives}</ul>{note}</div></details></article>''')
        groups.append(f'''<details class="pg-set" id="power-grammar-set-{start//10+1}"><summary><span>Set {start//10+1}</span><span class="pg-range">Exercises {start+1}–{start+10}</span></summary>
<div class="pg-set-content">{''.join(items)}</div></details>''')
    return f'''<section id="power-grammar" class="power-grammar" aria-labelledby="power-grammar-heading">
<div class="pg-heading"><p class="eyebrow">Find it. Fix it. Say it another way.</p><h2 id="power-grammar-heading">Power Grammar</h2>
<p>200 sentence-correction exercises in 20 sets. Open a set, try correcting each sentence, then expand the answer to see the marked correction, a clean corrected version in bold, and alternative correct sentences.</p></div>
<p class="pg-legend"><span><span class="pg-caret" aria-hidden="true">^</span> Red caret: removed wording</span><span><span class="pg-added">Blue text</span>: added or replacement wording</span></p>
<p class="pg-help">The first sentence contains deliberate errors. A vertical bar (|) separates acceptable word choices; parentheses show optional wording. Alternatives may change the emphasis or phrasing; more than one way of expressing the idea can be correct.</p>
<div class="pg-sets">{''.join(groups)}</div></section>'''


def enhance_page(soup, relative, prefix=''):
    if str(relative) != 'grammar-concepts.html':
        return
    from bs4 import BeautifulSoup
    for existing in soup.select('#power-grammar, [data-power-grammar-jump]'):
        existing.decompose()
    library = soup.select_one('[data-library]')
    if library is None:
        raise ValueError('The Grammar directory is missing its lesson library.')
    library.insert_before(BeautifulSoup(section_html(), 'html.parser').section)
    if not soup.select_one('link[href*="power-grammar.css"]'):
        soup.head.append(soup.new_tag('link', rel='stylesheet', href=prefix+'power-grammar.css'))
    if not soup.select_one('script[src*="power-grammar.js"]'):
        soup.head.append(soup.new_tag('script', src=prefix+'power-grammar.js', defer=True))
    hero = soup.select_one('.page-hero')
    if hero:
        nav = BeautifulSoup('<nav class="stage-actions" data-power-grammar-jump aria-label="Grammar practice"><a class="primary-button" href="#power-grammar">Try Power Grammar</a><a class="secondary-button" href="#grammar-topics">Browse grammar topics</a></nav>', 'html.parser').nav
        hero.append(nav)
    library['id'] = 'grammar-topics'


if __name__ == '__main__':
    from editorial import decorate_page
    decorate_page(ROOT / 'grammar-concepts.html')
