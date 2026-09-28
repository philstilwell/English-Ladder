"""Occupation-specific source files shared by the web and print courses."""
from pathlib import Path
from functools import lru_cache
import copy
import json

SOURCE = Path(__file__).resolve().parent / 'content/work/occupations'
EDITION = '2026-09-28'
OCCUPATION_SLUGS = (
    'home-care-caregivers', 'dental-assistants', 'pharmacy-technicians',
    'medical-assistants', 'childcare-early-education', 'restaurant-servers',
    'cooks-kitchen-staff', 'baristas-cafe-staff', 'housekeeping-commercial-cleaning',
    'hairdressers-barbers', 'nail-technicians', 'retail-associates-cashiers',
    'truck-delivery-drivers', 'warehouse-distribution', 'landscaping-grounds',
    'carpentry-remodeling', 'electricians', 'plumbers', 'hvac-refrigeration',
    'automotive-service', 'office-administrative-assistants', 'bookkeeping-payroll',
    'software-developers', 'software-quality-assurance', 'medical-laboratory-technicians',
)


def load_occupation(slug):
    if slug not in OCCUPATION_SLUGS:
        raise ValueError('Unknown occupation: ' + slug)
    path = SOURCE / (slug + '.json')
    return copy.deepcopy(_read_occupation(slug, path.stat().st_mtime_ns))


@lru_cache(maxsize=128)
def _read_occupation(slug, modified):
    data = json.loads((SOURCE / (slug + '.json')).read_text())
    course = data['course']
    if course['slug'] != slug or len(course['modules']) != 8:
        raise ValueError('Expected eight lessons for ' + slug)
    if len(data['dialogues']) != 8:
        raise ValueError('Expected eight extended dialogues for ' + slug)
    validate_occupation(data)
    return data


def validate_occupation(data):
    course = data['course']
    slug = course['slug']
    assert slug in OCCUPATION_SLUGS
    assert len(course['modules']) == 8
    assert len(course['sources']) >= 2
    assert len(course['jargon']) >= 32
    terms = {j['term'] for j in course['jargon']}
    assert len(terms) == len(course['jargon']), slug
    assert set(data['lesson_conversations']) == {f'module-{n}' for n in range(1, 9)}, slug
    assert len(data['dialogues']) == 8
    scripts, titles = set(), set()

    def script_check(dialogue, turn_key, count, minimum):
        turns = dialogue[turn_key]
        assert len(turns) == count, (slug, dialogue['title'], len(turns))
        assert dialogue['title'].strip() and dialogue['setting'].strip()
        assert all(len(turn) == 2 and all(isinstance(v, str) and v.strip() for v in turn) for turn in turns)
        assert all(a[0] != b[0] for a, b in zip(turns, turns[1:])), (slug, dialogue['title'])
        assert len(' '.join(speech for _, speech in turns).split()) >= minimum, (slug, dialogue['title'])
        signature = json.dumps(turns)
        assert signature not in scripts and dialogue['title'] not in titles, (slug, dialogue['title'])
        scripts.add(signature)
        titles.add(dialogue['title'])

    for i, module in enumerate(course['modules'], 1):
        assert len(module['terms']) == 4 and set(module['terms']) <= terms, (slug, i)
        assert len(module['collocations']) == 4 and all(module['collocations'])
        assert len(module['case']['model'].split()) >= 20
        workshop = module['workshop']
        assert len(workshop['frames']) == 3 and len(workshop['questions']) == 2
        for q in workshop['questions']:
            assert q['prompt'].count('____') == 1, (slug, i, q['prompt'])
            assert len(q['options']) == len(set(q['options'])) == len(q['feedback']) == 4, (slug, i)
            assert 0 <= q['correct_index'] < 4 and all(q['feedback']), (slug, i)
        lesson = data['lesson_conversations'][f'module-{i}']
        assert len(lesson['conversations']) == 3
        for dialogue in lesson['conversations']:
            script_check(dialogue, 'turns', 10, 100)
        scenario = lesson['additional_scenario']
        assert all(scenario[k].strip() for k in ('title', 'brief', 'role_a', 'role_b', 'opening_line', 'complication'))
        assert len(scenario['success_checks']) == 3 and all(scenario['success_checks'])
    for dialogue in data['dialogues']:
        script_check(dialogue, 'dialogue', 12, 140)
        assert len(dialogue['notes']) >= 2
    return {'course': slug, 'lessons': 8, 'conversations': 24, 'extended_dialogues': 8, 'terms': len(terms)}


def occupation_courses():
    courses = []
    for slug in OCCUPATION_SLUGS:
        course = load_occupation(slug)['course']
        course['is_occupation'] = True
        course['revision'] = EDITION
        course['pdfs'] = [
            ["Teacher's guide", f'pdf/efsp/efsp-{slug}-english-instructor-guide.pdf'],
            ['Learner workbook', f'pdf/efsp/efsp-{slug}-english-participant-workbook.pdf'],
            ['Conversation lab', f'pdf/efsp/efsp-{slug}-dialogue-lab.pdf'],
            ['Vocabulary & phrasebook', f'pdf/efsp/efsp-{slug}-jargon-quick-reference.pdf'],
        ]
        courses.append(course)
    return courses


def source_paths():
    return [SOURCE / (slug + '.json') for slug in OCCUPATION_SLUGS]
