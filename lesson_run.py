"""Resume a daily edition while retaining all publication requirements."""
import copy
import hashlib
import os
from pathlib import Path

from lesson_checkpoint import CheckpointStore

ROOT = Path(__file__).resolve().parent


def generation_policy_fingerprint():
    digest = hashlib.sha256()
    for name in ('update_site.py', 'news_quality.py', 'lesson_levels.py',
                 'lesson_evidence.py', 'lesson_run.py'):
        digest.update(name.encode())
        digest.update((ROOT / name).read_bytes())
    return digest.hexdigest()


def reusable_lesson(lesson, source, level):
    """Approval must match this content, source, level and current generation policy."""
    import update_site as u
    from news_quality import validate_evidence, validate_editorial_review
    from lesson_levels import LANGUAGE_POLICY_VERSION
    if not isinstance(lesson, dict):
        return False
    check = lesson.get('editorial_check')
    if not isinstance(check, dict) or check.get('status') != 'passed':
        return False
    if (check.get('target_level') != level['cefr']
            or check.get('language_policy_version') != LANGUAGE_POLICY_VERSION
            or check.get('content_digest') != u.lesson_approval_digest(lesson, source, level)):
        return False
    try:
        issues = (u.validate_lesson_data(lesson, level) + validate_evidence(lesson, source)
                  + validate_editorial_review({'approved': True, 'issues': [],
                                                'level_checks': check.get('level_checks')}))
        return not issues
    except (ValueError, TypeError, KeyError):
        return False


def generate_daily_lessons(release_dt):
    """Save source, successful levels and each unfinished attempt outside the site."""
    import update_site as u
    store = CheckpointStore(os.environ.get('LESSON_STATE_DIR') or None,
                            u.lesson_key_from_release_dt(release_dt), generation_policy_fingerprint())
    saved = store.load() or {}
    source = saved.get('source')
    if not isinstance(source, dict) or not all(isinstance(source.get(k), str) and source[k].strip()
                                              for k in ('title', 'summary', 'link', 'evidence_text')):
        print('Fetching news for the new daily edition...')
        source = u.get_daily_news(release_dt)
        saved = {}
    elif saved:
        print('Resuming the saved source and checked progress for this date.')
    previous = saved.get('levels', {})
    drafts = copy.deepcopy(saved.get('drafts', {}))
    completed = {}
    reserved = []
    client = None

    def persist():
        # Keep later completed levels until they have also been revalidated in order.
        store.save(source, {**previous, **completed}, drafts)

    persist()  # Keep the source before any paid generation request.
    try:
        for base in u.LEVELS:
            key = base['name'].lower()
            level = dict(base, reserved_vocabulary=list(reserved))
            candidate = previous.get(key)
            if reusable_lesson(candidate, source, level):
                lesson = copy.deepcopy(candidate)
                print(f'Reused the approved {key} lesson after checking its content and vocabulary reservations.')
            else:
                if key in previous:
                    del previous[key]
                    drafts.pop(key, None)
                if client is None:
                    client = u.configure_gemini()

                def checkpoint(state, key=key):
                    drafts[key] = copy.deepcopy(state)
                    persist()

                print(f'Generating or repairing the {key} lesson...')
                lesson, _ = u.generate_lesson(client, source, level, release_dt,
                                               initial_state=drafts.get(key), checkpoint=checkpoint)
            completed[key] = lesson
            drafts.pop(key, None)
            reserved.extend({'term': item['term'], 'level': base['name']} for item in lesson['vocabulary'])
            persist()
        issues = u.validate_edition_vocabulary(completed)
        if issues:
            raise ValueError('Daily vocabulary lists overlap: ' + '; '.join(issues))
        return source, completed
    finally:
        if client is not None and hasattr(client, 'close'):
            client.close()
