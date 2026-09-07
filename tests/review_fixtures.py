"""Explicitly synthetic reviewer responses for tests; never call a paid model."""
from lesson_levels import LEVEL_CHECKS


def approved_review():
    return {
        'approved': True,
        'issues': [],
        'level_checks': {name: {'passed': True, 'reason': 'Synthetic approval for a structurally valid test fixture.'}
                         for name in LEVEL_CHECKS},
    }


def draft_response(lesson, request, previous=None, level=None, news=None):
    """Encode fixture sections in the format actually requested by the generator."""
    import copy
    import update_site
    schema = request['config']['response_json_schema']
    result = copy.deepcopy(lesson)
    if 'reading' in schema['properties']:
        if news is None:
            # Canonical fixtures remain useful for deliberately malformed drafts.
            # Pass news to exercise the actual paired generation format.
            return result
        from lesson_evidence import evidence_choices
        choices = evidence_choices(news)
        reading = result.pop('news_brief_sentences')
        excerpts = result.pop('sentence_evidence')
        if len(reading) != len(excerpts):
            raise ValueError('A paired fixture needs one source excerpt per reading sentence.')
        result['reading'] = [
            {'text': sentence,
             'source_id': next(index for index, text in enumerate(choices)
                               if ' '.join(excerpt.split()) in text)}
            for sentence, excerpt in zip(reading, excerpts)
        ]
        result['grammar']['example_sentence_index'] = reading.index(
            result['grammar'].pop('example_quote'))
        return {name: result[name] for name in schema['required']}
    if 'news_brief_sentences' in schema['properties']:
        return result
    result = {name:result[name] for name in schema['required']}
    if 'vocabulary' in result:
        choices = update_site.reading_vocabulary_choices(previous or lesson, level)
        for item in result['vocabulary']:
            term = item.pop('term')
            item['term_id'] = next(i for i,value in enumerate(choices) if update_site.vocabulary_term_key(value) == update_site.vocabulary_term_key(term))
    if 'grammar' in result:
        reading = (previous or lesson)['news_brief_sentences']
        result['grammar']['example_sentence_index'] = reading.index(result['grammar'].pop('example_quote'))
    return result
