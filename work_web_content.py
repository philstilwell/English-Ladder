"""Web views of the reviewed learner-book content, without changing print sources."""
from copy import deepcopy
from functools import lru_cache
import json
import re

EDITION = '2026-10-14'


@lru_cache(maxsize=None)
def course_book(slug):
    from books.revised_edition import load_edition
    if slug == 'cultural-leadership-us-branches':
        from books.leadership_pilot import UNITS, SUPPLEMENTS
        book = dict(units=deepcopy(UNITS), supplements=deepcopy(SUPPLEMENTS))
    else:
        book = load_edition(slug)
    for unit in book['units']:
        unit['a'] = [web_question(q) for q in unit['checks']]
        unit['d'] = [web_question(q) for q in unit['choices']]
        if 'source_transfer' in unit:
            unit['transfer'] = unit['source_transfer']
        else:
            unit['transfer'] = web_transfer(unit['transfer'], unit['transfer_title'], unit['transfer_facts'])
    for scene in book['supplements']:
        scene['transfer'] = web_transfer(scene['pilot_transfer'], scene['transfer']['title'], scene['transfer']['setup'])
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
def publication_pages():
    from work_books import ROOT
    manifest = json.loads((ROOT / 'content/work/documents.json').read_text())
    return {m['course']: m['page_map'] for m in manifest['documents'].values()}


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
    result['revision'] = EDITION
    result['scope_note'] = book.get('scope_note', track['scope_note'])
    result['sources'] = book.get('sources', track['sources'])
    result['supplemental_scenarios'] = book['supplements']
    pages = publication_pages()[track['slug']]
    result['book_additional_pages'] = [pages[f'additional-{i}'] for i in range(1, 4)]
    glossary = []
    for index, (module, unit) in enumerate(zip(result['modules'], book['units'])):
        module['book_unit'] = unit
        module['book_page'] = pages[f'u{index + 1}-a']
        module['book_key_page'] = pages[f'key-u{index + 1}-d']
        module['book_dialogue_page'] = pages[f'u{index + 1}-e']
        module['book_conversation_key_page'] = pages[f'key-u{index + 1}-transfer']
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
