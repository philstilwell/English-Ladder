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
    reasons = question.get('reasons')
    rationale = (f'<ol class="work-answer-reasons">' + ''.join(
        f'<li><strong>{chr(65 + i)}. {e(option)}</strong><span>{e(reason)}</span></li>'
        for i, (option, reason) in enumerate(zip(question['options'], reasons, strict=True))) + '</ol>'
        if reasons and len(set(reasons)) > 1 else f'<p>{e(question["reason"])}</p>')
    layout = ' work-quiz-extended' if len(question['prompt']) > 240 else ''
    return f'''<div class="work-quiz{layout}" data-work-quiz data-correct="{question['answer']}" data-explanation="{e(question['reason'])}">
<fieldset><legend>{number}. {e(question['prompt'])}</legend>{choices}</fieldset>
<button type="button" class="work-button work-check" data-check-answer hidden>Check answer</button>
<p class="work-feedback" data-quiz-feedback role="status" aria-live="polite"></p>
<details class="work-answer"><summary>Answer and explanation</summary><p><strong>Correct: {chr(65 + question['answer'])}. {e(answer)}</strong></p>{rationale}</details></div>'''


def shuffled_question(question, key):
    order = sorted(range(len(question['options'])), key=lambda i: hashlib.sha256(
        f'{key}:{question["prompt"]}:{question["options"][i]}'.encode()).digest())
    result = dict(question, options=[question['options'][i] for i in order], answer=order.index(question['answer']))
    if question.get('reasons'):
        result['reasons'] = [question['reasons'][i] for i in order]
    return result


def checks(items, prefix, shuffle=False):
    rendered = []
    for i, question in enumerate(items, 1):
        if shuffle:
            question = shuffled_question(question, f'{prefix}:{i}')
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
    script = scene.get('script')
    if not script:
        practice = checks(scene['lines'], key, shuffle=True)
    else:
        gaps = {gap['turn']: i for i, gap in enumerate(script['gaps'])}
        parts = []
        for turn, (speaker, words) in enumerate(script['dialogue'], 1):
            if turn in gaps:
                index = gaps[turn]
                question = shuffled_question(scene['lines'][index], f'{key}:{index + 1}')
                parts.append(quiz(question, f'{key}-{index + 1}', index + 1))
            else:
                parts.append(f'<p class="work-transfer-context"><strong>{e(speaker)}:</strong> {e(words)}</p>')
        complete = ''.join(f'<li><strong>{e(role)}:</strong> {e(completed_turn(words, script["gaps"]))}</li>'
                           for role, words in script['dialogue'])
        practice = ('<div class="work-transfer-questions">' + ''.join(parts) + '</div>'
                    '<details class="work-transfer-script"><summary>Read the complete follow-up exchange</summary>'
                    f'<ol class="work-conversation-lines">{complete}</ol></details>')
    return f'<h5>{e(scene["title"])}</h5><p>{e(scene["setup"])}</p><p>Choose one answer for each gap, then read the exchange in order. Check the explanation after each choice.</p>{practice}'


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
    repair_page = module['book_repair_key_page']
    return f'''<div class="work-practice"><section class="work-conversations">
{heading('E', 'Conversations')}<h4>{e(unit['scene'])}</h4>
<details class="work-extended-conversation" id="{module['id']}-conversation"><summary>Extended conversation · 20 turns · {len(unit['gaps'])} gaps</summary>
{cloze(unit, module['id'] + '-cloze')}
{book_link(track, module['book_dialogue_page'], 'Dialogue in the book, page ' + str(module['book_dialogue_page']))}</details>
<h5 class="work-short-heading">Three more conversations at work</h5><p>Each short conversation has its own fictional situation and facts.</p>{''.join(conversations)}</section>
<section class="work-speaking">{heading('F', 'Say it')}<h4>Two scenarios to practice</h4>
<div class="work-speaking-scenario"><h5>{e(unit['scene'])}</h5><ol>{rehearsal}</ol><p class="work-support">On your own: read both roles. With a partner: swap roles after the first reading. Use the completed conversation to check any line you need to repeat.</p></div>
<div class="work-speaking-scenario">{transfer(unit['transfer'], module['id'] + '-transfer')}<p>Read the completed exchange twice, switching roles. Keep the printed facts and professional responsibilities unchanged.</p></div>
<details class="work-accuracy"><summary>Check accuracy and scope · 2 questions</summary><h5>{e(unit.get('repair_title', unit['transfer_title']))}</h5>
<p class="work-review-facts">{e(unit.get('repair_facts', unit['transfer_facts']))}</p><p>Choose one answer using the supplied facts. Read the corrected message aloud.</p>
{checks(unit['repair'], module['id'] + '-repair')}{book_link(track, repair_page, 'Accuracy-check explanations in the book, page ' + str(repair_page))}</details>
<details class="work-second-take"><summary>{'Second take: change one fact' if track['slug'] == 'cultural-leadership-us-branches' else 'Rebuild the exchange'} · 1 question</summary>
<p>Choose the response that fits, then say the complete response aloud. Keep every supplied fact intact.</p>{checks([unit['second_take']], module['id'] + '-second-take')}
{book_link(track, track['book_page_map'][f'key-u{module["number"]}-second'], 'Second-take explanation in the book')}</details>
<p class="work-precision"><strong>Listen for the distinction.</strong> {e(unit['delivery'])}</p>
{book_link(track, module['book_conversation_key_page'], 'Speaking-exchange explanations in the book, page ' + str(module['book_conversation_key_page']))}</section></div>'''


def render_module(track, module):
    from work_ai_prompts import url
    from work_ready_prompts import lesson_prompts
    track = web_track(track)
    module = track['modules'][module['number'] - 1]
    unit = module['book_unit']
    vocabulary = ''.join(f'<div><dt>{e(term)}</dt><dd>{e(meaning)}<span class="work-collocation">{e(phrase)}</span></dd></div>' for term, meaning, phrase in unit['vocabulary'])
    phrases = ''.join(f'<div><dt>{e(purpose)}</dt><dd>{e(phrase)}</dd></div>' for purpose, phrase in unit['phrases'])
    notes = ''.join(f'<div><dt>{e(title)}</dt><dd>{e(note)}</dd></div>' for title, note in unit['language'] + unit['language_extra'])
    focus = ''.join(f'<div><dt>{e(term)} <span class="work-stress">{e(stress)}</span></dt><dd>{e(example)}<p>{e(contrast)}</p></dd></div>'
                    for term, stress, example, contrast in unit['focus'])
    registers = ''.join(f'<div><p><strong>{e(a)}:</strong> {e(b)}</p><p><strong>{e(c)}:</strong> {e(d)}</p></div>'
                        for a, b, c, d in unit['registers'])
    artifact = ''
    if track['slug'] == 'cultural-leadership-us-branches':
        headers = ''.join(f'<th scope="col">{e(cell)}</th>' for cell in unit['artifact_headers'])
        rows = ''.join('<tr>' + ''.join(f'<td>{e(cell)}</td>' for cell in row) + '</tr>' for row in unit['artifact_rows'])
        artifact = f'<table class="work-case-record"><caption>{e(unit["artifact_title"])}</caption><thead><tr>{headers}</tr></thead><tbody>{rows}</tbody></table>'
    ai_links = ''.join(f'<a data-ai-preset href="{e(url(track, mode, module["id"]))}">{label}</a>' for mode, label in [('vocabulary', 'Extend the vocabulary'), ('grammar', 'Practice the grammar'), ('roleplay', 'Rehearse with AI')])
    return f'''<details class="work-module" id="{module['id']}" {'open' if module['number'] == 1 else ''}>
<summary><span class="work-module-number">{module['number']:02d}</span><span><strong>{e(module['title'])}</strong><small>{e(unit['scene'])}</small></span><span class="work-expand" aria-hidden="true">+</span></summary>
<div class="work-module-body"><div class="work-lesson-heading"><p class="work-kicker">Your goal</p><h3>{e(unit['skill'])}</h3><p>{book_link(track, module['book_page'], 'This lesson in the book, page ' + str(module['book_page']))}</p></div>
<section class="work-case">{heading('A', 'Read the situation')}<h4>{e(unit['scene'])}</h4><p>{e(unit['brief'])}</p>{artifact}<p class="work-cast">{e(' / '.join(f'{name}: {role}' for name, role in unit['cast']))}</p>
<details class="work-briefing-checks"><summary>Check the facts · 3 questions</summary><p>Choose the answer supported by the briefing. Do not assume that a proposed action has already happened.</p>{checks(unit['a'], module['id'] + '-briefing')}</details></section>
<section class="work-words">{heading('B', 'Find the words')}<h4>Vocabulary and collocations</h4><p>{e(unit['precision'])}</p>
<details class="work-language-bank"><summary>24 field terms and natural word combinations</summary><dl class="work-vocabulary work-lesson-vocabulary">{vocabulary}</dl><p class="work-precision">{e(unit['precision_extra'])}</p></details>
<details class="work-language-bank work-context-focus"><summary>Say it in context · 4 expressions</summary><p>{e(unit.get('focus_instruction', 'Capitals show the stressed syllable, not a full pronunciation spelling.'))}</p><dl class="work-language-notes work-focus-list">{focus}</dl></details></section>
<section class="work-language">{heading('C', 'Notice the language')}<h4>{e(unit['culture'][0])}</h4><p>{e(unit['culture'][1])}</p>
<details class="work-language-bank"><summary>16 useful phrases, grouped by purpose</summary><dl class="work-phrase-list">{phrases}</dl></details>
<details class="work-language-bank"><summary>6 language and precision notes</summary><dl class="work-language-notes">{notes}</dl></details>
<details class="work-language-bank work-register"><summary>{e(unit.get('register_heading', 'Same purpose, different register'))}</summary><div class="work-register-examples">{registers}</div></details></section>
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
        page = track['book_additional_pages'][index]
        reference = ''
        if scene.get('reference'):
            title, url = scene['reference']
            reference = f'<p class="work-small">Professional context: <a href="{e(url)}">{e(title)}</a></p>'
        language = ''
        if track['slug'] != 'cultural-leadership-us-branches':
            entries = []
            for gap in scene['gaps']:
                speaker, words = scene['dialogue'][gap['turn'] - 1]
                entries.append(f'<div><dt>{e(gap["answer"])}</dt><dd>{e(gap["reason"])}<span class="work-collocation">{e(speaker)}: {e(completed_turn(words, scene["gaps"]))}</span></dd></div>')
            language = '<details class="work-additional-language"><summary>Language for this case · 6 expressions</summary><dl class="work-vocabulary">' + ''.join(entries) + '</dl></details>'
        delivery = f'<p class="work-precision"><strong>Keep the distinction audible.</strong> {e(scene["delivery"])}</p>' if scene.get('delivery') else ''
        scenes.append(f'''<details class="work-additional-scene" id="{key}"><summary>{e(scene['scene'])}</summary>
<p><strong>{e(scene['skill'])}</strong></p><p>{e(scene['brief'])}</p>{language}{cloze(scene, key + '-cloze')}
<div class="work-follow-up">{transfer(scene['transfer'], key + '-transfer')}</div>
<p>Check the answers, then read both exchanges aloud. Swap roles on the second reading.</p>{delivery}
{book_link(track, page, 'This scenario in the book, page ' + str(page))}{reference}</details>''')
    return '<section class="work-section work-additional" id="additional-conversations"><p class="work-kicker">More situations, different skills</p><h2>Three additional workplace scenarios</h2>' + ''.join(scenes) + '</section>'


def render_checkpoint(track, checkpoint, index):
    page = track['book_page_map'][f'review-{index}']
    key_page = track['book_page_map'][f'key-review-{index}']
    return f'''<details class="work-review" id="review-{index}"><summary><span>Cumulative review · Lessons 1–{checkpoint['after']}</span><strong>{e(checkpoint['title'])}</strong></summary>
<p class="work-review-facts">{e(checkpoint['facts'])}</p><p>Use the case facts and language from the completed lessons. Choose one answer per question.</p>
{checks(checkpoint['questions'], f'review-{index}')}
<p>{book_link(track, page, 'Review in the book, page ' + str(page))} · {book_link(track, key_page, 'Explanations, page ' + str(key_page))}</p></details>'''


def render_field_notes(track):
    notes = track['book_field_notes']
    if not notes:
        notes = dict(notes_title='Directness, disagreement, and local norms',
            notes_intro='Do not infer intent from volume or speed alone. Test the claim, watch the response, and distinguish a sharp challenge from personal contempt.',
            field_notes=[
                ('Challenge the claim', '"Which assumption is wrong?" keeps the discussion on something that can be checked. Accepting one criticism does not require abandoning the whole proposal.', ''),
                ('Set a behavioral boundary', '"Keep the criticism on the estimate, not the people." A colleague\'s stated good intention does not erase an insult or repeated interruption.', ''),
                ('Check the local rule', 'First names, humor, and informal meetings do not tell you who can approve spending. Ask which decisions are yours and which need approval.', ''),
                ('Make room for a different pace', 'Some colleagues think aloud; others want time to read before speaking. Use a pre-read, a clear speaking order, and a later input route rather than equating speed with competence.', ''),
                ('Separate rapport from commitment', 'A friendly "sounds good" can support a direction without accepting a deadline. Confirm the deliverable, owner, condition, and time.', ''),
                ('Name what a deadline means', '"Friday" may refer to different time zones or different versions of a report. State the clock time, location, and whether the figures are provisional or verified.', ''),
            ])
    entries = ''.join(f'<div><dt>{e(title)}</dt><dd>{e(explanation)}' + (f'<p class="work-collocation">{e(example)}</p>' if example else '') + '</dd></div>'
                      for title, explanation, example in notes['field_notes'])
    boundary = track['scope_note'] if track['book_field_notes'] else ('Nationality is not a personality test. Role, power, language confidence, professional training, and company norms also shape an exchange. Do not normalize threats, discrimination, or intimidation as a cultural style; use appropriate workplace support and reporting routes.')
    page = track['book_page_map']['culture']
    return f'<details class="work-field-notes" id="professional-notes"><summary>Professional communication notes</summary><h2>{e(notes["notes_title"])}</h2><p>{e(notes["notes_intro"])}</p><dl class="work-language-notes">{entries}</dl><p class="work-precision">{e(boundary)}</p>{book_link(track, page, "Communication notes in the book, page " + str(page))}</details>'
