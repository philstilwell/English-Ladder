"""Web views of the reviewed learner-book content, without changing print sources."""
from copy import deepcopy
from functools import lru_cache
import json
import re

EDITION = '2026-10-14-web2'


@lru_cache(maxsize=None)
def course_book(slug):
    from books.revised_edition import load_edition
    if slug == 'cultural-leadership-us-branches':
        from books.leadership_pilot import UNITS, SUPPLEMENTS, CHECKPOINTS
        book = dict(units=deepcopy(UNITS), supplements=deepcopy(SUPPLEMENTS), checkpoints=deepcopy(CHECKPOINTS))
    else:
        book = load_edition(slug)
    for unit in book['units']:
        unit['a'] = [web_question(q) for q in unit['checks']]
        unit['d'] = [web_question(q) for q in unit['choices']]
        unit['repair'] = [web_question(q) for q in unit['repair']]
        unit['second_take'] = web_question(unit['second_take'])
        script = deepcopy(unit['transfer'])
        if 'source_transfer' in unit:
            unit['transfer'] = deepcopy(unit['source_transfer'])
        else:
            unit['transfer'] = web_transfer(unit['transfer'], unit['transfer_title'], unit['transfer_facts'])
        unit['transfer']['script'] = script
    for scene in book['supplements']:
        scene['scene'] = scene['title']
        scene['brief'] = scene['setup']
        scene['transfer'] = web_transfer(scene['pilot_transfer'], scene['transfer']['title'], scene['transfer']['setup'])
        scene['transfer']['script'] = deepcopy(scene['pilot_transfer'])
    if slug == 'cultural-leadership-us-branches':
        for scene, delivery in zip(book['supplements'], [
            'Contrast adding a group with replacing one. Name the reduced Friday deliverable separately from the full analysis. Tuesday is a scheduling update, not a promised completion date.',
            'Separate accurate results from incomplete credit. Name each person\'s contribution. Do not make public praise a condition of receiving proper attribution.',
            'Contrast paused with canceled. Keep the new date open until the evidence and release criteria support a decision. Do not imply that all completed work is invalid.',
        ], strict=True):
            scene['delivery'] = delivery
    for checkpoint in book['checkpoints']:
        checkpoint['questions'] = [web_question(q) for q in checkpoint['questions']]
    return book


def web_question(question):
    return dict(question, reason=question.get('shared_explanation') or question['reasons'][question['answer']])


def web_transfer(scene, title, setup):
    answers = [g['answer'] for g in scene['gaps']]
    lines = []
    for i, gap in enumerate(scene['gaps']):
        speaker, line = scene['dialogue'][gap['turn'] - 1]
        line = re.sub(r'\{\{(\d+)\}\}', lambda m: '___' if int(m[1]) == i + 1 else answers[int(m[1]) - 1], line)
        lines.append(dict(prompt=f'{speaker}: "{line}"', options=answers.copy(), answer=i, reason=gap['reason']))
    return dict(title=title, setup=setup, lines=lines)


@lru_cache(maxsize=1)
def publication_documents():
    from work_books import ROOT
    manifest = json.loads((ROOT / 'content/work/documents.json').read_text())
    return {m['course']: m for m in manifest['documents'].values()}


def publication_pages():
    return {slug: m['page_map'] for slug, m in publication_documents().items()}


def completed_turn(speech, gaps):
    return re.sub(r'\{\{(\d+)\}\}', lambda m: gaps[int(m[1]) - 1]['answer'], speech)


def web_track(track):
    """Keep cases, prompt references and printed conversations on the same facts."""
    if track.get('web_book_edition') == EDITION:
        return track
    result = deepcopy(track)
    book = course_book(track['slug'])
    if [m['title'] for m in result['modules']] != [u['title'] for u in book['units']]:
        raise ValueError('Web lesson order differs from the learner book: ' + track['slug'])
    result['web_book_edition'] = EDITION
    result['revision'] = '2026-10-14'
    result['scope_note'] = book.get('scope_note', track['scope_note'])
    result['sources'] = book.get('sources', track['sources'])
    result['supplemental_scenarios'] = book['supplements']
    pages = publication_pages()[track['slug']]
    result['book_page_map'] = pages
    result['book_checkpoints'] = book['checkpoints']
    result['book_field_notes'] = {key: book[key] for key in ('notes_title', 'notes_intro', 'field_notes') if key in book}
    result['book_additional_pages'] = [pages[f'additional-{i}'] for i in range(1, 4)]
    glossary = []
    for index, (module, unit) in enumerate(zip(result['modules'], book['units'])):
        module['book_unit'] = unit
        module['book_page'] = pages[f'u{index + 1}-a']
        module['book_key_page'] = pages[f'key-u{index + 1}-d']
        module['book_dialogue_page'] = pages[f'u{index + 1}-e']
        module['book_conversation_key_page'] = pages[f'key-u{index + 1}-transfer']
        module['book_repair_page'] = pages[f'u{index + 1}-f']
        module['book_repair_key_page'] = pages[f'key-u{index + 1}-f']
        module['brief'] = unit['brief']
        module['vocabulary'] = [dict(term=term, definition=meaning, collocation=phrase)
                                for term, meaning, phrase in unit['vocabulary']]
        module['collocations'] = [phrase for _, _, phrase in unit['vocabulary']]
        module['model'] = '\n'.join(f'{role}: {completed_turn(line, unit["gaps"])}'
                                    for role, line in unit['dialogue'][-4:])
        module['speaking_task'] = ' '.join(unit['rehearsal'])
        module['guided_response'] = True
        module['writing_task'] = ('Select supplied answers for the dialogue gaps. Check the explanations, '
                                  'then read the completed exchange aloud; no original writing is required.')
        module['workshop'].update(
            title=unit['scene'], goal=unit['skill'], explanation=unit['precision'],
            frames=[phrase for _, phrase in unit['phrases']],
            role_b=' / '.join(f'{name}: {role}' for name, role in unit['cast']),
            challenge=unit['transfer']['setup'])
        module['goals'] = [unit['skill']]
        glossary.extend(dict(term=term, definition=meaning, collocation=phrase,
                             lesson=module['number'], lesson_id=module['id'])
                        for term, meaning, phrase in unit['vocabulary'])
    result['web_glossary'] = glossary
    result['outcomes'] = [m['book_unit']['skill'] for m in result['modules']]
    return result
