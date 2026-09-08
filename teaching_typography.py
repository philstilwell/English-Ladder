"""Reviewed display corrections for archived language-teaching text.

Keep the evidence-bearing lesson records and translation keys intact. Match
complete authored strings, never guess which ordinary words should be quoted.
New lessons follow the same convention through the shared writing guidance.
"""
import json
from functools import lru_cache
from pathlib import Path

GUIDANCE = ('When discussing a word, phrase, or example sentence as language within '
            'an explanation, question, or answer feedback, enclose that wording in '
            'quotation marks. For example: What does “about” mean in “about twenty '
            'people”? Use “on” with a named day. Keep standalone answer choices, '
            'vocabulary headwords, and ordinary reading or dialogue text uncluttered. '
            'Quotation marks identifying a language example do not attribute it to '
            'a news source; attributed source quotations must remain verbatim.')


@lru_cache(maxsize=1)
def corrections():
    return json.loads((Path(__file__).resolve().parent / 'content/teaching-typography.json').read_text())


def teaching_text(value):
    """Format only a reviewed complete teaching string; otherwise retain it."""
    return corrections().get(value, value)
