"""Small parsers for compact, explicitly authored learner-book content."""
import hashlib
import re


def rows(text, count, columns):
    result = [tuple(value.strip() for value in line.split('|'))
              for line in text.strip().splitlines() if line.strip()]
    assert len(result) == count, (len(result), count)
    assert all(len(row) == columns and all(row) for row in result)
    return result


def questions(text, count):
    result = []
    for row in rows(text, count, 6):
        prompt, correct, b, c, d, reason = row
        options = [correct, b, c, d]
        shift = int(hashlib.sha256(prompt.encode()).hexdigest()[:8], 16) % 4
        options = options[shift:] + options[:shift]
        result.append(dict(prompt=prompt, options=options, answer=(4 - shift) % 4, reason=reason))
    return result


def unit(*, title, scene, skill, brief, cast, culture, a, vocabulary, precision,
         precision_extra, phrases, notes, d, dialogue, transfer_title,
         transfer_setup, transfer, rehearsal=None):
    script, gaps = [], []
    for turn, (speaker, speech) in enumerate(rows(dialogue, 20, 2), 1):
        def replace(match):
            answer, reason = match[1].split('::', 1)
            gaps.append(dict(turn=turn, answer=answer.strip(), reason=reason.strip()))
            return '{{' + str(len(gaps)) + '}}'
        script.append((speaker, re.sub(r'\[\[(.*?)\]\]', replace, speech)))
    items = rows(transfer, 4, 3)
    bank = [answer for _, answer, _ in items]
    return dict(title=title, scene=scene, skill=skill, brief=brief, cast=rows(cast, 2, 2),
                setting=scene, facts=[], culture=culture, a=questions(a, 3),
                vocabulary=rows(vocabulary, 24, 3), precision=precision,
                precision_extra=precision_extra, phrases=rows(phrases, 16, 2),
                language=rows(notes, 6, 2)[:3], language_extra=rows(notes, 6, 2)[3:],
                d=questions(d, 4), dialogue=script, gaps=gaps,
                transfer=dict(title=transfer_title, setup=transfer_setup,
                              lines=[dict(prompt=p, options=bank.copy(), answer=i, reason=r)
                                     for i, (p, _, r) in enumerate(items)]),
                rehearsal=rehearsal or [
                    'Check your answers, then read turns 1-10 with a partner using the corrected words.',
                    'Switch roles for turns 11-20. Stress words that distinguish facts from conditions or estimates.',
                    'Complete and check the four-line exchange. Read it twice, switching roles and keeping the printed facts.'])
