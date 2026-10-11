"""Web views of the reviewed learner-book content, without changing print sources."""
from copy import deepcopy
from functools import lru_cache
import importlib
import re

from books.supplements import load_supplements
from work_books import book_units

EDITION = '2026-10-10'


@lru_cache(maxsize=None)
def course_book(slug):
    if slug == 'cultural-leadership-us-branches':
        return dict(units=book_units(slug))
    return importlib.import_module('books.' + slug.replace('-', '_') + '_content').BOOK


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
    result['supplemental_scenarios'] = load_supplements(track['slug'])
    glossary = []
    for index, (module, unit) in enumerate(zip(result['modules'], book['units'])):
        module['book_unit'] = unit
        module['book_page'] = 4 + index * 9
        module['book_key_page'] = 85 + index * 2
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
