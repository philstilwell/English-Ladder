"""Resolve source menu references without asking a model to recopy quotations."""
import copy
import re


MAX_EXCERPT_CHARS = 1200


def _paragraph_excerpts(text):
    """Keep paragraphs intact where practical and split long ones at sentence ends."""
    while len(text) > MAX_EXCERPT_CHARS:
        # Include closing quotation marks in the sentence they belong to.
        ends = [match.end() for match in re.finditer(
            r'''[.!?]["'”’\)\]]*(?=\s|$)''', text[:MAX_EXCERPT_CHARS + 1])
                if 8 <= match.end() <= MAX_EXCERPT_CHARS]
        end = ends[-1] if ends else text.rfind(' ', 8, MAX_EXCERPT_CHARS + 1)
        if end < 8:
            end = MAX_EXCERPT_CHARS
        remainder = text[end:].strip()
        if 0 < len(remainder) < 8:
            # Keep a short final word with its context instead of losing it.
            yield text
            return
        # A very long individual sentence may need a continuous partial span.
        # It remains verbatim; the semantic review must still establish support.
        yield text[:end].strip()
        text = remainder
    if len(text) >= 8:
        yield text


def evidence_choices(news):
    """Return stable, distinct source excerpts; normalize whitespace only."""
    choices = {}
    for field in ('title', 'summary', 'evidence_text'):
        value = news.get(field)
        if not value:
            continue
        for paragraph in re.split(r'\r?\n\s*\r?\n', str(value)):
            normalized = ' '.join(paragraph.split())
            for excerpt in _paragraph_excerpts(normalized):
                choices.setdefault(excerpt, None)
    return list(choices)


def resolve_evidence_references(lesson, news):
    """Copy a draft and replace integer evidence references with exact excerpts.

    Literal strings remain available for older drafts. Exact-match and semantic
    evidence checks still run after this operation; selecting a menu entry does
    not establish that it supports the associated reading sentence.
    """
    if not isinstance(lesson, dict):
        raise ValueError('The lesson must be an object before resolving source evidence.')
    resolved = copy.deepcopy(lesson)
    references = resolved.get('sentence_evidence')
    if not isinstance(references, list):
        raise ValueError('sentence_evidence must be a list of source references or exact excerpts.')
    choices = evidence_choices(news)
    for position, reference in enumerate(references):
        if isinstance(reference, str):
            continue
        if type(reference) is not int or not 0 <= reference < len(choices):
            raise ValueError(f'sentence_evidence entry {position + 1} must be an integer source index '
                             f'from 0 to {len(choices) - 1}, or an exact source excerpt.')
        references[position] = choices[reference]
    return resolved
