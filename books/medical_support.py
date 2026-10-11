"""Shared communication language; specialty cases and clinical terms are authored separately."""
from books.authoring import rows, unit

CORE_TERMS = '''qualified interpreter | Trained language professional supporting accurate communication between speakers. | request a qualified interpreter
teach-back | Checking an explanation by inviting the listener to restate its meaning. | use teach-back without blame
patient preference | A person's stated wishes about care or communication. | elicit the patient preference
clinical handoff | Transfer of relevant care information and responsibility between professionals. | confirm the clinical handoff
documented plan | Agreed next steps recorded for the people involved. | review the documented plan
source attribution | Identification of who reported, observed, or established a fact. | preserve source attribution'''

CORE_PHRASES = '''Invite correction | Please stop me if I have misunderstood.
Explain a term | In everyday language, that means the following.
Separate uncertainty | That remains uncertain; it is not a confirmed finding.
Check your explanation | Let me explain that another way.
Make space | We can pause before moving to the next point.
Name responsibility | Let us confirm who will follow up.
Keep a record accurate | I will distinguish what was reported from what was observed.
Confirm an agreement | We have agreed on the next step, not on an outcome.'''

CORE_NOTES = '''Reported versus established | Attribute a person's account with reports or describes. Use confirms only when the relevant evidence supports confirmation.
Can versus will | Can describes an available possibility or ability; will makes a commitment. Do not turn a possible result into a promise.
Checking a message | A check-back confirms the meaning received. Correct the explanation calmly when the listener has understood something different.'''


def medical_unit(*, vocabulary, phrases, notes, rehearsal, **kwargs):
    """Keep six core terms available for retrieval alongside 18 specialty terms."""
    rows(vocabulary, 18, 3)
    rows(phrases, 8, 2)
    rows(notes, 3, 2)
    assert len(rehearsal) == 2
    return unit(vocabulary=vocabulary + '\n' + CORE_TERMS,
                phrases=phrases + '\n' + CORE_PHRASES,
                notes=notes + '\n' + CORE_NOTES,
                rehearsal=rehearsal + ['Complete the four-line follow-up with the supplied words. Check every explanation, then read the corrected exchange twice, changing roles.'],
                **kwargs)


def source(title, url, note):
    return dict(title=title, url=url, note=note, checked='10 October 2026')


TEACH_BACK = source('AHRQ. Use the Teach-Back Method: Tool 5.',
    'https://www.ahrq.gov/health-literacy/improve/precautions/tool5.html',
    'Supports checking the clarity of an explanation without treating the patient as the problem. The original conversations are language practice, not copied clinical scripts.')

SCOPE = ('All people, records, figures, and encounters are fictional. This is professional English practice, not medical advice, clinical training, a treatment protocol, or certification. '
         'Use current evidence, authorized supervision where required, local law, and your actual clinical and emergency procedures. Do not use an exercise to decide that symptoms can safely wait, select treatment, or calculate a dose. '
         'Communication about privacy, consent, and professional duties depends on jurisdiction and setting. Use qualified language support and protect real patient information.')


def short_lesson(unit, text):
    """Parse three explicitly authored ten-turn exchanges; reuse the bounded follow-up."""
    conversations = []
    for block in text.strip().split('\n\n'):
        lines = block.strip().splitlines()
        assert len(lines) == 11, (unit['title'], len(lines))
        title, setting, first, second = [value.strip() for value in lines[0].split('|')]
        turns = [(first if i % 2 == 0 else second, line.strip())
                 for i, line in enumerate(lines[1:])]
        assert len(' '.join(line for _, line in turns).split()) >= 100, title
        conversations.append(dict(title=title, setting=setting, turns=turns))
    assert len(conversations) == 3
    followup = unit['transfer']
    first = followup['lines'][0]
    return dict(conversations=conversations, additional_scenario=dict(
        title=followup['title'], brief=followup['setup'],
        role_a='Read the first and third lines using the supplied choices.',
        role_b='Read the second and fourth lines using the supplied choices.',
        opening_line=first['prompt'].replace('___', first['options'][first['answer']]),
        complication=unit['precision'],
        success_checks=['Use only the facts supplied in the follow-up.',
                        'Check each selected answer against its explanation.',
                        'Read the corrected exchange twice, changing roles.']))
