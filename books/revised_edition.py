"""Prepare the book edition without changing the website's lesson data.

Cases, dialogue turns, terminology, and explanations come from each field's
authored source. New retrieval questions compare that book's actual definitions;
no profession names are substituted into a universal workplace conversation.
"""
from copy import deepcopy
import hashlib
import importlib
from pathlib import Path
import random
import re

from books.supplements import load_supplements

ROOT = Path(__file__).resolve().parents[1]


def inventory():
    result = []
    for path in sorted((ROOT / 'books').glob('*_content.py')):
        if ' ' in path.name or path.stem == 'cross_cultural_leadership_content':
            continue
        result.append(importlib.import_module('books.' + path.stem).BOOK['slug'])
    assert len(result) == 79, len(result)
    return result


def question(prompt, options, answer, reasons):
    order = list(range(4))
    random.Random(hashlib.sha256(prompt.encode()).hexdigest()).shuffle(order)
    return dict(prompt=prompt, options=[options[i] for i in order],
                answer=order.index(answer), reasons=[reasons[i] for i in order])


def vocabulary_question(unit, index, *, prompt=None):
    """All alternatives are real terms with their own explained meaning."""
    selected = [unit['vocabulary'][(index + offset) % 24] for offset in (0, 5, 11, 17)]
    term, definition, collocation = selected[0]
    prompt = prompt or f'A colleague needs the term for this meaning: {definition} Which term fits?'
    reasons = [f'{name}: {meaning} The usual combination is "{phrase}".'
               for name, meaning, phrase in selected]
    return question(prompt, [row[0] for row in selected], 0, reasons)


def source_question(item):
    """Retain the author's rationale, including questions asking for an error."""
    result = deepcopy(item)
    result['reasons'] = [item['reason']] * 4
    result['shared_explanation'] = item['reason']
    return result


def complete_turn(scene, index):
    speaker, line = scene['dialogue'][index]
    return speaker, re.sub(r'\{\{(\d+)\}\}',
                          lambda m: scene['gaps'][int(m[1]) - 1]['answer'], line)


def exchange_question(unit, gap_index):
    """Reconstruct a real exchange; explain alternatives through their contexts."""
    target = unit['gaps'][gap_index % len(unit['gaps'])]['turn'] - 1
    target = min(max(target, 1), len(unit['dialogue']) - 2)
    speaker, response = complete_turn(unit, target)
    previous_name, previous = complete_turn(unit, target - 1)
    next_name, following = complete_turn(unit, target + 1)
    candidates = [i for i, (name, _) in enumerate(unit['dialogue'])
                  if name == speaker and i not in (target - 1, target, target + 1) and i > 0]
    candidates.sort(key=lambda i: abs(len(complete_turn(unit, i)[1].split()) - len(response.split())))
    if len(candidates) < 3:
        raise ValueError('Not enough same-speaker alternatives: ' + unit['title'])
    indices = [target, *candidates[:3]]
    options = [complete_turn(unit, i)[1] for i in indices]
    reasons = []
    for i in indices:
        before_name, before = complete_turn(unit, i - 1)
        if i == target:
            reasons.append(f'This is {speaker}\'s response in turn {i + 1}. It connects '
                           f'{previous_name}\'s preceding point with {next_name}\'s follow-up. '
                           + next((g['reason'] for g in unit['gaps'] if g['turn'] == i + 1),
                                  'Read the three turns together to hear the question-and-response sequence.'))
        else:
            reasons.append(f'This line belongs to turn {i + 1}, after {before_name} says: "{before}" '
                           'It addresses that point, not the missing turn in the supplied exchange.')
    prompt = (f'Rebuild the exchange from "{unit["scene"]}". '
              f'{previous_name}: "{previous}" {speaker}: [missing response] '
              f'{next_name}: "{following}" Which response belongs in the gap?')
    return question(prompt, options, 0, reasons)


def transfer_scene(transfer):
    dialogue, gaps = [], []
    for i, item in enumerate(transfer['lines'], 1):
        prompt = item['prompt']
        speaker, separator, line = prompt.partition(':')
        if not separator:
            raise ValueError('A transfer line must identify its speaker: ' + prompt)
        line = line.strip().strip('"')
        answer = item['options'][item['answer']]
        dialogue.append((speaker.strip(), line.replace('___', '{{' + str(i) + '}}')))
        gaps.append(dict(answer=answer, turn=i, reason=item['reason']))
    return dict(dialogue=dialogue, gaps=gaps)


def revise_unit(original, number):
    u = deepcopy(original)
    u['number'] = number
    u['artifact_title'] = u['scene']
    u['artifact_headers'] = ['Case record', 'Information available']
    u['artifact_rows'] = [['Briefing', u['brief']]]
    u['checks'] = [source_question(q) for q in u['a']]
    u['choices'] = [source_question(q) for q in u['d'][:2]] + [vocabulary_question(u, 3)]
    u['focus_instruction'] = 'Stress the highlighted expression. Keep the surrounding words connected; pause at the end of the phrase.'
    u['focus'] = []
    for i in (0, 5, 11, 16):
        term, definition, collocation = u['vocabulary'][i]
        u['focus'].append((term, term.upper(), collocation,
                           f'Keep the meaning precise: {definition}'))
    u['register_heading'] = 'Precision in real exchanges'
    u['registers'] = [('Purpose', label, 'Useful wording', phrase)
                      for label, phrase in u['phrases'][3:5]]
    original_transfer = deepcopy(u['transfer'])
    u['transfer_title'] = original_transfer['title']
    u['transfer_facts'] = original_transfer['setup']
    u['transfer'] = transfer_scene(original_transfer)
    u['repair'] = [source_question(q) for q in u['d'][2:]]
    u['repair_title'] = u['scene']
    u['repair_facts'] = u['brief']
    u['delivery'] = u['rehearsal'][1]
    u['source_transfer'] = original_transfer
    return u


def load_edition(slug):
    module = importlib.import_module('books.' + slug.replace('-', '_') + '_content')
    book = deepcopy(module.BOOK)
    book['art_alt'] = book['cover_title'].replace('\n', ' ') + ': professionals communicating in their workplace.'
    book['units'] = [revise_unit(u, i) for i, u in enumerate(book['units'], 1)]
    book['supplements'] = deepcopy(load_supplements(slug))
    for s in book['supplements']:
        s.update(title=s['scene'], setup=s['brief'], pilot_transfer=transfer_scene(s['transfer']),
                 delivery=s['skill'])
    from books.revisions.editorial import revise
    revise(book)
    override = ROOT / 'books/revisions' / (slug.replace('-', '_') + '.py')
    if override.exists():
        importlib.import_module('books.revisions.' + slug.replace('-', '_')).revise(book)
    for u in book['units']:
        u['choices'].append(exchange_question(u, 2))
        u['second_take'] = exchange_question(u, 6)
    book['checkpoints'] = []
    for i in range(4):
        left, right = book['units'][i * 2:i * 2 + 2]
        earlier = book['units'][max(0, i * 2 - 1)]
        items = [vocabulary_question(left, 2), vocabulary_question(right, 7),
                 exchange_question(earlier, 4), exchange_question(right, 8)]
        book['checkpoints'].append(dict(after=(i + 1) * 2, title=f'Review {i + 1} / Meaning and context',
            facts=f'Revisit "{left["title"]}" and "{right["title"]}". '
                  'Choose precise terminology, then reconstruct the missing responses using both neighboring turns. '
                  'The final two questions also revisit earlier conversations.', questions=items))
    distinguish_phrase_banks(book)
    validate(book)
    return book


def distinguish_phrase_banks(book):
    """Replace repeated generic lines with intact wording from that lesson."""
    seen = set()
    for u in book['units']:
        phrases = []
        candidates = []
        for speaker, line in u['dialogue']:
            complete = re.sub(r'\{\{(\d+)\}\}', lambda m: u['gaps'][int(m[1]) - 1]['answer'], line)
            for sentence in re.split(r'(?<=[.!?])\s+', complete):
                if 7 <= len(sentence.split()) <= 25 and not re.search(r'fictional|exercise|supplied', sentence, re.I):
                    candidates.append((speaker + ' / in the conversation', sentence))
        for label, phrase in u['phrases']:
            if phrase in seen:
                replacement = next((p for p in candidates if p[1] not in seen and p[1] not in {x[1] for x in u['phrases']}), None)
                if replacement is None:
                    raise ValueError('Not enough distinct phrase examples: ' + book['slug'] + ' / ' + u['title'])
                label, phrase = replacement
            phrases.append((label, phrase))
            seen.add(phrase)
        u['phrases'] = phrases


def validate(book):
    assert len(book['units']) == 8 and len(book['supplements']) == 3
    assert len(book['checkpoints']) == 4
    for u in book['units']:
        seen_prompts = set()
        assert len(u['vocabulary']) == 24 and len(u['phrases']) == 16
        assert len(u['dialogue']) == 20 and len(u['gaps']) == 10
        assert len(u['checks']) == 3 and len(u['choices']) == 4 and len(u['repair']) == 2
        assert len(u['focus']) == 4
        for q in [*u['checks'], *u['choices'], *u['repair'], u['second_take']]:
            validate_question(q)
            assert q['prompt'] not in seen_prompts, (book['slug'], q['prompt'])
            seen_prompts.add(q['prompt'])
    for c in book['checkpoints']:
        for q in c['questions']:
            validate_question(q)
    for scene in [*book['units'], *book['supplements']]:
        validate_dialogue(scene)
        validate_dialogue(scene.get('pilot_transfer') or scene['transfer'])


def validate_question(q):
    assert q['prompt'] and len(q['options']) == len(set(q['options'])) == len(q['reasons']) == 4
    assert 0 <= q['answer'] < 4 and all(q['reasons'])


def validate_dialogue(scene):
    numbers = []
    for turn, (speaker, line) in enumerate(scene['dialogue'], 1):
        assert speaker and line
        for n in re.findall(r'\{\{(\d+)\}\}', line):
            numbers.append(int(n))
            assert scene['gaps'][int(n) - 1]['turn'] == turn
    assert numbers == list(range(1, len(scene['gaps']) + 1))
    assert len({g['answer'].casefold() for g in scene['gaps']}) == len(scene['gaps'])
    assert all(g['reason'] for g in scene['gaps'])
