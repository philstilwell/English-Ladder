"""Explicitly synthetic reviewer responses for tests; never call a paid model."""
from lesson_levels import LEVEL_CHECKS


def approved_review():
    return {
        'approved': True,
        'issues': [],
        'level_checks': {name: {'passed': True, 'reason': 'Synthetic approval for a structurally valid test fixture.'}
                         for name in LEVEL_CHECKS},
    }


def draft_response(lesson, request, previous=None, level=None):
    """Encode fixture sections in the format actually requested by the generator."""
    import copy
    import update_site
    schema = request['config']['response_json_schema']
    result = copy.deepcopy(lesson)
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
