"""Embed reviewed Everyday English explanations; publishing makes no API calls."""
import json

from bs4 import BeautifulSoup
from us_life_translations import LANGUAGES, read_record, sources

INVITATION = 'Choose a language for the unit explanations and deeper explanations in your AI prompts. The lessons and practice stay in English.'


def enhance_page(soup):
    # One shared chooser replaces both How to Study and the older dropdown.
    picker = soup.select_one('#life-language-select')
    if picker:
        (picker.find_parent('label') or picker).decompose()
    for item in soup.select('.us-life-stat-list li'):
        if item.get_text(strip=True) == 'Japanese or Mandarin explanations':
            item.string = 'Explanations in five languages'
    for old in soup.select('[data-us-life-translations]'):
        old.decompose()
    introduction = soup.select_one('.us-life-intro > div')
    introduction.clear()
    introduction['id'] = 'life-language-controls'
    targets = ' '.join('life-explanation-' + unit['id'] for unit in soup.select('.us-life-module'))
    controls = ''.join(f'<button type="button" class="vocabulary-language" data-definition-language="{language}" aria-pressed="{str(language == "en").lower()}" aria-controls="{targets}" disabled>{label}</button>'
                       for language, label in {'en': 'English only', **LANGUAGES}.items())
    introduction.append(BeautifulSoup(f'''<h2>Choose your explanation language</h2><p>{INVITATION}</p>
<div class="vocabulary-languages" role="group" aria-label="Explanation language">{controls}</div>
<p class="vocabulary-language-status" data-life-language-status role="status" aria-live="polite">Language help is optional. Choose any of the five languages if you would like it.</p>
<noscript><p>Enable JavaScript to choose an explanation language. You can read all the English lessons without it.</p></noscript>''', 'html.parser'))
    payload = {}
    for key, source in sources(soup).items():
        unit = soup.find(id=key)
        aside = unit.select_one('[data-explanation]')
        aside.clear()
        aside['data-explanation'] = key
        aside['data-nosnippet'] = ''
        aside.attrs.pop('aria-live', None)
        aside['hidden'] = ''
        if 'english-only' not in unit.get('class', []):
            unit['class'] = [*unit.get('class', []), 'english-only']
        aside.attrs.pop('lang', None)
        markup = f'''<div id="life-explanation-{key}" data-life-explanation-content lang="en"><p>Choose an explanation language above.</p></div>'''
        aside.append(BeautifulSoup(markup, 'html.parser'))
        record = read_record(source)
        payload[key] = {'practice': source['japanese_explanation']['practice'],
                        'translations': record['translations'] if record else {}}
    script = soup.new_tag('script', attrs={'type': 'application/json', 'data-us-life-translations': ''})
    # Prevent source text from ending its JSON script element.
    script.string = json.dumps(payload, ensure_ascii=True).replace('<', '\\u003c')
    soup.body.append(script)
