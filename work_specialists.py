"""Book-first specialist courses added to the English for Work collection."""
import importlib
from pathlib import Path

from work_medical import completed

SPECIALIST_SLUGS = ('nutrition-dietetics', 'sports-medicine', 'international-law',
                    'patent-law', 'university-professors', 'investment-management-banking',
                    'cross-border-ma-integration', 'localization-qa')


def book(slug):
    if slug not in SPECIALIST_SLUGS:
        raise ValueError('Unknown specialist course: ' + slug)
    return importlib.import_module('books.' + slug.replace('-', '_') + '_content').BOOK


def specialist_courses():
    courses = []
    functions = ('clarify', 'explain', 'qualify', 'compare', 'update', 'request', 'pushback', 'handoff')
    for slug in SPECIALIST_SLUGS:
        data = book(slug)
        glossary, modules = {}, []
        for index, u in enumerate(data['units']):
            for term, meaning, phrase in u['vocabulary']:
                glossary.setdefault(term.casefold(), dict(term=term, definition=meaning,
                                                          collocation=phrase, group=u['title']))
            questions = [dict(prompt=q['prompt'], options=q['options'].copy(), correct_index=q['answer'],
                              feedback=[q['reason']] * 4) for q in u['d'][:2]]
            modules.append(dict(title=u['title'], focus=u['skill'], terms=[v[0] for v in u['vocabulary'][:4]],
                collocations=[v[2] for v in u['vocabulary'][:4]], outputs=['Guided professional dialogue'],
                case=dict(function=functions[index], brief=u['brief'], model=' '.join(line for _, line in completed(u)[-4:])),
                workshop=dict(title=u['scene'], goal=u['skill'], explanation=u['precision'],
                    frames=[phrase for _, phrase in u['phrases'][:3]], questions=questions,
                    role_b=u['cast'][1][1], challenge=u['transfer']['setup'])))
        courses.append(dict(slug=slug, title=data['title'], summary=data['summary'], roles=data['roles'],
            category=data['category'], revision='2026-10-11', scope_note=data['scope_note'],
            sources=data['sources'], jargon=list(glossary.values()), modules=modules,
            pdfs=[['Learner book', f'pdf/efsp/{slug}-english-book.pdf']]))
    return courses


def specialist_dialogues():
    return {slug: [dict(title=u['scene'], setting=u['brief'], dialogue=completed(u),
                       notes=[u['precision'], u['precision_extra']]) for u in book(slug)['units']]
            for slug in SPECIALIST_SLUGS}


def short_lessons(slug):
    return importlib.import_module('books.' + slug.replace('-', '_') + '_short').LESSONS


def source_paths():
    root = Path(__file__).resolve().parent
    return [Path(__file__), root / 'books/specialist_support.py',
            *[root / 'books' / (slug.replace('-', '_') + '_content.py') for slug in SPECIALIST_SLUGS]]
