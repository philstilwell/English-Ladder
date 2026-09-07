"""Explicitly synthetic reviewer responses for tests; never call a paid model."""
from lesson_levels import LEVEL_CHECKS


def approved_review():
    return {
        'approved': True,
        'issues': [],
        'level_checks': {name: {'passed': True, 'reason': 'Synthetic approval for a structurally valid test fixture.'}
                         for name in LEVEL_CHECKS},
    }
