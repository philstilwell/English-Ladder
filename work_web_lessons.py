"""Accessible web practice from the same authored material as the learner books."""
import hashlib
import html
import json
import re

from work_lesson_conversations import lesson_content
from work_web_content import completed_turn, web_track


def e(value):
    return html.escape(str(value), quote=True)


def heading(letter, title):
    return f'<p class="work-kicker work-activity-heading"><span class="work-activity-letter">{letter}</span> <span>{e(title)}</span></p>'


def book_link(track, page, label):
    from generate_efsp_web_pages import pdf_metadata
    href, _ = pdf_metadata(track)
    return f'<a class="work-book-inline" href="{e(href)}#page={page}">{e(label)} <span aria-hidden="true">↗</span></a>'


def quiz(question, key, number):
    answer = question['options'][question['answer']]
    choices = ''.join(f'<label><input type="radio" name="{e(key)}" value="{i}"><span>{e(option)}</span></label>'
                      for i, option in enumerate(question['options']))
    return f'''<div class="work-quiz" data-work-quiz data-correct="{question['answer']}" data-explanation="{e(question['reason'])}">
<fieldset><legend>{number}. {e(question['prompt'])}</legend>{choices}</fieldset>
<button type="button" class="work-button work-check" data-check-answer hidden>Check answer</button>
<p class="work-feedback" data-quiz-feedback role="status" aria-live="polite"></p>
<details class="work-answer"><summary>Answer and explanation</summary><p><strong>{chr(65 + question['answer'])}. {e(answer)}</strong></p><p>{e(question['reason'])}</p></details></div>'''


def checks(items, prefix, shuffle=False):
    rendered = []
    for i, question in enumerate(items, 1):
        if shuffle:
            answer = question['options'][question['answer']]
            options = sorted(question['options'], key=lambda option: hashlib.sha256(
                f'{prefix}:{i}:{question["prompt"]}:{option}'.encode()).digest())
            question = dict(question, options=options, answer=options.index(answer))
        rendered.append(quiz(question, f'{prefix}-{i}', i))
    return '<div class="work-check-grid">' + ''.join(rendered) + '</div>'


def cloze(scene, key):
    gaps = scene['gaps']
    answers = [g['answer'] for g in gaps]
    bank = sorted(answers, key=lambda answer: hashlib.sha256(f'{key}:{answer}'.encode()).digest())
    if bank == answers:
        bank = bank[1:] + bank[:1]
    speakers = {name: i for i, (name, _) in enumerate(scene['cast'])}
    lines = []
    for turn, (speaker, speech) in enumerate(scene['dialogue'], 1):
        def gap(match):
            number = int(match[1])
            choices = ''.join(f'<option value="{e(word)}">{e(word)}</option>' for word in bank)
            return (f'<span class="work-gap"><sup aria-hidden="true">{number}</sup>'
                    f'<select data-cloze-gap="{number}" aria-label="Gap {number}, turn {turn}, {e(speaker)}" '
                    f'aria-describedby="{key}-feedback-{number}"><option value="">Choose a word or phrase</option>{choices}</select></span>')
        speech_html = re.sub(r'\{\{(\d+)\}\}', gap, e(speech))
        lines.append(f'<li data-speaker="{speakers[speaker]}"><strong>{e(speaker)}</strong><div>{speech_html}</div></li>')
    feedback = ''.join(f'<li id="{key}-feedback-{n}" data-cloze-feedback="{n}" hidden></li>' for n in range(1, len(gaps) + 1))
    key_items = ''.join(f'<li><strong>{e(g["answer"])}</strong> <span class="work-small">Turn {g["turn"]}.</span> {e(g["reason"])}</li>' for g in gaps)
    script = ''.join(f'<li><strong>{e(role)}:</strong> {e(completed_turn(speech, gaps))}</li>' for role, speech in scene['dialogue'])
    data = json.dumps(gaps, ensure_ascii=True).replace('<', '\\u003c')
    cast = ' / '.join(f'{name}: {role}' for name, role in scene['cast'])
    return f'''<div class="work-cloze" data-work-cloze id="{key}">
<p class="work-cast">{e(cast)}</p><p>Complete the numbered gaps. Use each bank entry once, without changing its form.</p>
<div class="work-word-bank"><strong>Word bank</strong><ul>{''.join(f'<li>{e(word)}</li>' for word in bank)}</ul></div>
<ol class="work-extended-lines">{''.join(lines)}</ol>
<div class="work-cloze-actions" hidden><button type="button" class="work-button" data-check-cloze>Check conversation</button><button type="button" class="work-text-button" data-reset-cloze>Try again</button></div>
<p class="work-feedback" data-cloze-status role="status" aria-live="polite"></p><ol class="work-cloze-feedback">{feedback}</ol>
<details class="work-answer"><summary>Answers and explanations</summary><ol>{key_items}</ol></details>
<details class="work-completed-script"><summary>Read the complete conversation</summary><ol>{script}</ol></details>
<script type="application/json" data-cloze-answers>{data}</script></div>'''


def transfer(scene, key):
    return f'<h5>{e(scene["title"])}</h5><p>{e(scene["setup"])}</p><p>Choose one reply for each gap, then read the four turns in order. Check the explanation after each choice.</p>{checks(scene["lines"], key, shuffle=True)}'


def render_practice(track, module):
    track = web_track(track)
    module = track['modules'][module['number'] - 1]
    unit = module['book_unit']
    short = lesson_content(track, module)
    conversations = []
    for item in short['conversations']:
        turns = ''.join(f'<li><strong>{e(role)}:</strong> {e(speech)}</li>' for role, speech in item['turns'])
        conversations.append(f'<details class="work-conversation"><summary>{e(item["title"])}</summary><p>{e(item["setting"])}</p><ol class="work-conversation-lines">{turns}</ol></details>')
    rehearsal = ''.join(f'<li>{e(step)}</li>' for step in unit['rehearsal'][:2])
    return f'''<div class="work-practice"><section class="work-conversations">
{heading('E', 'Conversations')}<h4>{e(unit['scene'])}</h4>
<details class="work-extended-conversation" id="{module['id']}-conversation"><summary>Extended conversation · 20 turns · {len(unit['gaps'])} gaps</summary>
{cloze(unit, module['id'] + '-cloze')}
{book_link(track, module['book_page'] + 6, 'Dialogue in the book, page ' + str(module['book_page'] + 6))}</details>
<h5 class="work-short-heading">Three more conversations at work</h5><p>Each short conversation has its own fictional situation and facts.</p>{''.join(conversations)}</section>
<section class="work-speaking">{heading('F', 'Say it')}<h4>Two scenarios to practice</h4>
<div class="work-speaking-scenario"><h5>{e(unit['scene'])}</h5><ol>{rehearsal}</ol><p class="work-support">On your own: read both roles. With a partner: swap roles after the first reading. Use the completed conversation to check any line you need to repeat.</p></div>
<div class="work-speaking-scenario">{transfer(unit['transfer'], module['id'] + '-transfer')}<p>Read the completed exchange twice, switching roles. Keep the printed facts and professional responsibilities unchanged.</p></div>
{book_link(track, module['book_key_page'] + 1, 'Conversation explanations in the book, page ' + str(module['book_key_page'] + 1))}</section></div>'''


def render_module(track, module):
    from work_ai_prompts import url
    from work_ready_prompts import lesson_prompts
    track = web_track(track)
    module = track['modules'][module['number'] - 1]
    unit = module['book_unit']
    vocabulary = ''.join(f'<div><dt>{e(term)}</dt><dd>{e(meaning)}<span class="work-collocation">{e(phrase)}</span></dd></div>' for term, meaning, phrase in unit['vocabulary'])
    phrases = ''.join(f'<div><dt>{e(purpose)}</dt><dd>{e(phrase)}</dd></div>' for purpose, phrase in unit['phrases'])
    notes = ''.join(f'<div><dt>{e(title)}</dt><dd>{e(note)}</dd></div>' for title, note in unit['language'] + unit['language_extra'])
    ai_links = ''.join(f'<a data-ai-preset href="{e(url(track, mode, module["id"]))}">{label}</a>' for mode, label in [('vocabulary', 'Extend the vocabulary'), ('grammar', 'Practice the grammar'), ('roleplay', 'Rehearse with AI')])
    return f'''<details class="work-module" id="{module['id']}" {'open' if module['number'] == 1 else ''}>
<summary><span class="work-module-number">{module['number']:02d}</span><span><strong>{e(module['title'])}</strong><small>{e(unit['scene'])}</small></span><span class="work-expand" aria-hidden="true">+</span></summary>
<div class="work-module-body"><div class="work-lesson-heading"><p class="work-kicker">Your goal</p><h3>{e(unit['skill'])}</h3><p>{book_link(track, module['book_page'], 'This lesson in the book, page ' + str(module['book_page']))}</p></div>
<section class="work-case">{heading('A', 'Read the situation')}<h4>{e(unit['scene'])}</h4><p>{e(unit['brief'])}</p><p class="work-cast">{e(' / '.join(f'{name}: {role}' for name, role in unit['cast']))}</p>
<details class="work-briefing-checks"><summary>Check the facts · 3 questions</summary><p>Choose the answer supported by the briefing. Do not assume that a proposed action has already happened.</p>{checks(unit['a'], module['id'] + '-briefing')}</details></section>
<section class="work-words">{heading('B', 'Find the words')}<h4>Vocabulary and collocations</h4><p>{e(unit['precision'])}</p>
<details class="work-language-bank"><summary>24 field terms and natural word combinations</summary><dl class="work-vocabulary work-lesson-vocabulary">{vocabulary}</dl><p class="work-precision">{e(unit['precision_extra'])}</p></details></section>
<section class="work-language">{heading('C', 'Notice the language')}<h4>{e(unit['culture'][0])}</h4><p>{e(unit['culture'][1])}</p>
<details class="work-language-bank"><summary>16 useful phrases, grouped by purpose</summary><dl class="work-phrase-list">{phrases}</dl></details>
<details class="work-language-bank"><summary>6 language and precision notes</summary><dl class="work-language-notes">{notes}</dl></details></section>
<section class="work-checks">{heading('D', 'Check your understanding')}<h4>Choose the precise message</h4><p>Choose one best answer using the case facts and the stated purpose.</p>{checks(unit['d'], module['id'] + '-language')}
{book_link(track, module['book_key_page'], 'Check explanations in the book, page ' + str(module['book_key_page']))}</section>
{render_practice(track, module)}
<aside class="work-ai-invitation"><h4>Another round with an AI partner</h4><nav aria-label="AI extensions for lesson {module['number']}">{ai_links}</nav></aside>
{lesson_prompts(track, module)}</div></details>'''


def render_additional(track):
    track = web_track(track)
    scenes = []
    for index, scene in enumerate(track['supplemental_scenarios']):
        key = f'additional-{index + 1}'
        page = 76 + index * 3
        reference = ''
        if scene.get('reference'):
            title, url = scene['reference']
            reference = f'<p class="work-small">Professional context: <a href="{e(url)}">{e(title)}</a></p>'
        scenes.append(f'''<details class="work-additional-scene" id="{key}"><summary>{e(scene['scene'])}</summary>
<p><strong>{e(scene['skill'])}</strong></p><p>{e(scene['brief'])}</p>{cloze(scene, key + '-cloze')}
<div class="work-follow-up">{transfer(scene['transfer'], key + '-transfer')}</div>
<p>Check the answers, then read both exchanges aloud. Swap roles on the second reading.</p>
{book_link(track, page, 'This scenario in the book, page ' + str(page))}{reference}</details>''')
    return '<section class="work-section work-additional" id="additional-conversations"><p class="work-kicker">More situations, different skills</p><h2>Three additional workplace scenarios</h2>' + ''.join(scenes) + '</section>'
