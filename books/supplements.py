"""Load explicitly authored additional conversations; never synthesize dialogue."""
from __future__ import annotations

import importlib
import re

from books.authoring import rows


def scenario(*, title, skill, setup, cast, dialogue, transfer_title,
             transfer_setup, transfer, reference=None):
    script, gaps = [], []
    for turn, (speaker, speech) in enumerate(rows(dialogue, 20, 2), 1):
        def replace(match):
            answer, reason = match[1].split('::', 1)
            gaps.append(dict(turn=turn, answer=answer.strip(), reason=reason.strip()))
            return '{{' + str(len(gaps)) + '}}'
        script.append((speaker, re.sub(r'\[\[(.*?)\]\]', replace, speech)))
    items = rows(transfer, 4, 3)
    bank = [answer for _, answer, _ in items]
    result = dict(scene=title, skill=skill, brief=setup, cast=rows(cast, 2, 2),
                  dialogue=script, gaps=gaps,
                  transfer=dict(title=transfer_title, setup=transfer_setup,
                                lines=[dict(prompt=p, options=bank.copy(), answer=i, reason=r)
                                       for i, (p, _, r) in enumerate(items)]))
    if reference is not None:
        result['reference'] = reference
    validate_scenario(result)
    return result


def validate_scenario(item):
    assert item['scene'] and item['skill'] and item['brief']
    cast = {name for name, _ in item['cast']}
    assert len(cast) == 2 and len(item['dialogue']) == 20
    assert len(item['gaps']) == 6
    assert len({g['answer'].casefold() for g in item['gaps']}) == 6
    numbers = []
    for turn, (speaker, speech) in enumerate(item['dialogue'], 1):
        assert speaker in cast and speech
        for match in re.findall(r'\{\{(\d+)\}\}', speech):
            numbers.append(int(match))
            assert item['gaps'][int(match) - 1]['turn'] == turn
    assert numbers == list(range(1, 7))
    assert all(len(g['reason'].split()) >= 8 for g in item['gaps'])
    lines = item['transfer']['lines']
    assert len(lines) == 4
    assert len({q['options'][q['answer']] for q in lines}) == 4
    for question in lines:
        assert question['prompt'].count('___') == 1
        assert len(question['options']) == len(set(question['options'])) == 4
        assert len(question['reason'].split()) >= 8
    assert not re.search(r'\[\[|\]\]', str(item))
    if 'reference' in item:
        title, url = item['reference']
        assert title and url.startswith('https://')


def load_supplements(slug):
    module = importlib.import_module('books.additional.' + slug.replace('-', '_'))
    result = module.SCENARIOS
    assert len(result) == 3
    assert len({item['scene'].casefold() for item in result}) == 3
    for item in result:
        validate_scenario(item)
    return result
