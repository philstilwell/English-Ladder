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


def generation_schema(base_schema, news):
    """Create a generation-only schema that binds each sentence to its source.

    The archive schema stays unchanged. A grammar reference is checked against
    the completed reading at resolution time, since its length is not yet known.
    """
    choices = evidence_choices(news)
    if not choices:
        raise ValueError('No source passages are available for lesson evidence.')
    schema = copy.deepcopy(base_schema)
    properties = schema['properties']
    reading = properties.pop('news_brief_sentences')
    properties.pop('sentence_evidence')
    reading['items'] = {
        'type': 'object', 'additionalProperties': False,
        'required': ['text', 'source_id'],
        'properties': {
            'text': reading['items'],
            'source_id': {'type': 'integer', 'minimum': 0, 'maximum': len(choices) - 1},
        },
    }
    properties['reading'] = reading
    schema['required'] = ['reading' if name == 'news_brief_sentences' else name
                          for name in schema['required'] if name != 'sentence_evidence']
    grammar = properties['grammar']
    grammar['properties'].pop('example_quote')
    grammar['properties']['example_sentence_index'] = {'type': 'integer', 'minimum': 0}
    grammar['required'] = ['example_sentence_index' if name == 'example_quote' else name
                           for name in grammar['required']]
    return schema


def _source_excerpt(reference, choices, field):
    if type(reference) is not int or not 0 <= reference < len(choices):
        raise ValueError(f'{field} must be an integer source index '
                         f'from 0 to {len(choices) - 1}.')
    return choices[reference]


def resolve_evidence_references(lesson, news):
    """Decode generation references into the canonical archive lesson shape.

    Literal strings remain available for older drafts. Exact-match and semantic
    evidence checks still run after this operation; selecting a menu entry does
    not establish that it supports the associated reading sentence.
    """
    if not isinstance(lesson, dict):
        raise ValueError('The lesson must be an object before resolving source evidence.')
    resolved = copy.deepcopy(lesson)
    choices = evidence_choices(news)
    paired_reading = 'reading' in resolved
    if paired_reading:
        if 'news_brief_sentences' in resolved or 'sentence_evidence' in resolved:
            raise ValueError('Do not mix reading entries with canonical news_brief_sentences or sentence_evidence.')
        entries = resolved.pop('reading')
        if not isinstance(entries, list):
            raise ValueError('reading must be a list of text and source_id entries.')
        sentences, references = [], []
        for position, entry in enumerate(entries, 1):
            if (not isinstance(entry, dict) or set(entry) != {'text', 'source_id'}
                    or not isinstance(entry['text'], str)):
                raise ValueError(f'reading entry {position} must contain exactly a text string and source_id.')
            references.append(_source_excerpt(entry['source_id'], choices,
                                               f'reading entry {position} source_id'))
            sentences.append(entry['text'])
        resolved['news_brief_sentences'] = sentences
        resolved['sentence_evidence'] = references
    else:
        references = resolved.get('sentence_evidence')
        if not isinstance(references, list):
            raise ValueError('sentence_evidence must be a list of source references or exact excerpts.')
        for position, reference in enumerate(references, 1):
            if not isinstance(reference, str):
                references[position - 1] = _source_excerpt(
                    reference, choices, f'sentence_evidence entry {position}')

    grammar = resolved.get('grammar')
    if paired_reading or (isinstance(grammar, dict) and 'example_sentence_index' in grammar):
        expected = {'concept', 'explanation', 'example_sentence_index'}
        if (not isinstance(grammar, dict) or set(grammar) != expected
                or not isinstance(grammar['concept'], str)
                or not isinstance(grammar['explanation'], str)):
            raise ValueError('Referenced grammar must contain concept and explanation strings plus '
                             'example_sentence_index; do not mix an index with example_quote.')
        sentences = resolved.get('news_brief_sentences')
        index = grammar['example_sentence_index']
        if (not isinstance(sentences, list) or type(index) is not int
                or not 0 <= index < len(sentences) or not isinstance(sentences[index], str)):
            raise ValueError('grammar.example_sentence_index must refer to an actual reading sentence.')
        grammar['example_quote'] = sentences[index]
        del grammar['example_sentence_index']
    return resolved
