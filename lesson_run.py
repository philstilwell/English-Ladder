"""Resume a daily edition while retaining all publication requirements."""
import copy
import hashlib
import os
from pathlib import Path

from lesson_checkpoint import CheckpointStore

ROOT = Path(__file__).resolve().parent
MAX_SOURCE_ARTICLES_PER_RUN = 4
SOURCE_FAILURES_BEFORE_WORLD_FALLBACK = 1


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


def source_link(source):
    if isinstance(source, dict) and isinstance(source.get('link'), str):
        return source['link'].strip()
    return ''


def saved_source_is_complete(source):
    return isinstance(source, dict) and all(
        isinstance(source.get(k), str) and source[k].strip()
        for k in ('title', 'summary', 'link', 'evidence_text')
    )


def exhausted_draft_keys(drafts, max_attempts):
    """Draft-limit checkpoints need a new article, but review checkpoints can resume."""
    if not isinstance(drafts, dict):
        return []
    exhausted = []
    for key, state in drafts.items():
        if not isinstance(key, str) or not isinstance(state, dict):
            continue
        if state.get('phase') == 'review':
            continue
        attempts = state.get('attempts')
        if type(attempts) is int and attempts >= max_attempts:
            exhausted.append(key)
    return sorted(exhausted)


def source_can_be_retried_with_another_article(error):
    message = str(error)
    return (message.startswith('Could not generate a valid ')
            or ' reached its daily limit of ' in message)


def generate_daily_lessons(release_dt):
    """Save source, successful levels and each unfinished attempt outside the site."""
    import update_site as u
    store = CheckpointStore(os.environ.get('LESSON_STATE_DIR') or None,
                            u.lesson_key_from_release_dt(release_dt), generation_policy_fingerprint())
    saved = store.load() or {}
    source = saved.get('source')
    excluded_links = set()
    failed_source_count = 0

    def fetch_news():
        print('Fetching news for the new daily edition...')
        preferred_categories = (('world',)
                                if failed_source_count >= SOURCE_FAILURES_BEFORE_WORLD_FALLBACK
                                else None)
        if excluded_links:
            if preferred_categories:
                return u.get_daily_news(release_dt, excluded_links=excluded_links,
                                        preferred_categories=preferred_categories)
            return u.get_daily_news(release_dt, excluded_links=excluded_links)
        if preferred_categories:
            return u.get_daily_news(release_dt, preferred_categories=preferred_categories)
        return u.get_daily_news(release_dt)

    if saved_source_is_complete(source):
        exhausted = exhausted_draft_keys(saved.get('drafts', {}), u.MAX_DAILY_GENERATION_ATTEMPTS)
        if exhausted:
            link = source_link(source)
            if link:
                excluded_links.add(link)
            print(f"Saved {', '.join(exhausted)} draft reached the daily retry limit; "
                  "choosing a fresh source article.")
            failed_source_count = 1
            source = fetch_news()
            saved = {}
        elif saved:
            print('Resuming the saved source and checked progress for this date.')
    else:
        source = fetch_news()
        saved = {}

    attempted_sources = 1

    while True:
        previous = saved.get('levels', {})
        drafts = copy.deepcopy(saved.get('drafts', {}))
        completed = {}
        reserved = []
        client = None

        def persist():
            # Keep later completed levels until they have also been revalidated in order.
            store.save(source, {**previous, **completed}, drafts)

        try:
            persist()  # Keep the source before any paid generation request.
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
        except RuntimeError as error:
            if not source_can_be_retried_with_another_article(error):
                raise
            link = source_link(source)
            if link:
                excluded_links.add(link)
            failed_source_count += 1
            if attempted_sources >= MAX_SOURCE_ARTICLES_PER_RUN:
                raise RuntimeError(
                    f"Could not complete the daily edition after trying {attempted_sources} "
                    f"source articles. Last error: {error}"
                ) from error
            print('This source article could not produce a valid full edition; trying another article.')
            source = fetch_news()
            saved = {}
            attempted_sources += 1
        finally:
            if client is not None and hasattr(client, 'close'):
                client.close()
