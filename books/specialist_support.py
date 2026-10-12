"""Compact authoring helpers for explicitly written specialist communication courses."""
from books.authoring import rows, unit
from books.medical_support import short_lesson

CORE_TERMS = '''clarification request | Question that resolves an unclear meaning or instruction. | make a targeted clarification request
source attribution | Identification of where information came from. | preserve source attribution
working assumption | Provisional premise used while information is incomplete. | challenge a working assumption
scope boundary | Limit of the work or authority being discussed. | state the scope boundary
action owner | Named person responsible for a specified next step. | confirm the action owner
check-back | Restatement used to verify that a message was understood. | complete a check-back'''

CORE_PHRASES = '''Clarify the question | Are you asking about the finding or the next step?
Invite correction | Please correct me if I have misunderstood that detail.
Attribute information | That is what the current record says; it has not been independently confirmed.
Separate possibility | That is a possibility, not an agreed outcome.
Check scope | That decision sits outside my authority.
Pin down responsibility | Who is responsible for that specific next step?
Repair misunderstanding | Let me restate the distinction more clearly.
Close an exchange | We agree on the action, the owner, and the point for review.'''

CORE_NOTES = '''Reported versus verified | Reported attributes information to a source; verified indicates it has been checked. Do not use the words interchangeably.
Could versus will | Could introduces a possibility. Will commits to an action or predicts an outcome; check whether that certainty is justified.
By versus at | By gives a latest time; at identifies a scheduled moment. State the time zone when people work across locations.'''


def specialist_unit(*, vocabulary, phrases, notes, rehearsal, **kwargs):
    rows(vocabulary, 18, 3)
    rows(phrases, 8, 2)
    rows(notes, 3, 2)
    assert len(rehearsal) == 2
    return unit(vocabulary=vocabulary + '\n' + CORE_TERMS,
                phrases=phrases + '\n' + CORE_PHRASES,
                notes=notes + '\n' + CORE_NOTES,
                rehearsal=rehearsal + ['Complete the four-line follow-up with the supplied choices. Check the explanations, then read the corrected exchange twice, changing roles.'],
                **kwargs)


def source(title, url, note):
    return dict(title=title, url=url, note=note, checked='11 October 2026')


FICTION = 'All people, organizations, cases, figures, and documents in the exercises are fictional. '
