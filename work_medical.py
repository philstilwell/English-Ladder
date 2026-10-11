"""Book-first course records for the six dedicated medical professions."""
import importlib
import re
from pathlib import Path

MEDICAL_SLUGS = ('general-practitioners', 'oncologists', 'cardiologists',
                 'x-ray-technicians', 'pediatricians', 'obstetricians')


def book(slug):
    if slug not in MEDICAL_SLUGS:
        raise ValueError('Unknown medical profession: ' + slug)
    return importlib.import_module('books.' + slug.replace('-', '_') + '_content').BOOK


def completed(unit):
    return [(name, re.sub(r'\{\{(\d+)\}\}', lambda m: unit['gaps'][int(m[1]) - 1]['answer'], line))
            for name, line in unit['dialogue']]


def medical_courses():
    courses = []
    functions = ('clarify', 'explain', 'qualify', 'compare', 'update', 'request', 'pushback', 'handoff')
    # These compatibility records let the established generators consume one authored source.
    for slug in MEDICAL_SLUGS:
        data = book(slug)
        glossary, modules = {}, []
        for index, u in enumerate(data['units']):
            for term, meaning, phrase in u['vocabulary']:
                glossary.setdefault(term.casefold(), dict(term=term, definition=meaning,
                                                          collocation=phrase, group=u['title']))
            questions = [dict(prompt=q['prompt'], options=q['options'].copy(), correct_index=q['answer'],
                              feedback=[q['reason']] * 4) for q in u['d'][:2]]
            modules.append(dict(title=u['title'], focus=u['skill'], terms=[v[0] for v in u['vocabulary'][:4]],
                collocations=[v[2] for v in u['vocabulary'][:4]], outputs=['Guided clinical dialogue'],
                case=dict(function=functions[index], brief=u['brief'], model=' '.join(line for _, line in completed(u)[-4:])),
                workshop=dict(title=u['scene'], goal=u['skill'], explanation=u['precision'],
                    frames=[phrase for _, phrase in u['phrases'][:3]], questions=questions,
                    role_b=u['cast'][1][1], challenge=u['transfer']['setup'])))
        courses.append(dict(slug=slug, title=data['title'], summary=data['summary'], roles=data['roles'],
            category='Health & life sciences', revision='2026-10-10', scope_note=data['scope_note'],
            sources=data['sources'], jargon=list(glossary.values()), modules=modules,
            pdfs=[['Learner book', f'pdf/efsp/{slug}-english-book.pdf']]))
    return courses


def medical_dialogues():
    return {slug: [dict(title=u['scene'], setting=u['brief'], dialogue=completed(u),
                       notes=[u['precision'], u['precision_extra']]) for u in book(slug)['units']]
            for slug in MEDICAL_SLUGS}


def short_lessons(slug):
    return importlib.import_module('books.' + slug.replace('-', '_') + '_short').LESSONS


def source_paths():
    root = Path(__file__).resolve().parent
    return [Path(__file__), root / 'books/medical_support.py',
            *[root / 'books' / (slug.replace('-', '_') + '_content.py') for slug in MEDICAL_SLUGS]]
