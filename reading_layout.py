"""Compact reading pages without changing their lessons or level destinations."""
from pathlib import Path

LEVELS = {'beginner': 'A1–A2', 'intermediate': 'B1–B2', 'advanced': 'C1+'}


def prepare_reading_layout(soup, path, root, prefix):
    relative = Path(path).relative_to(root)
    level = relative.stem
    if level not in LEVELS or (len(relative.parts) > 1 and relative.parts[0] not in {'news', 'stories'}):
        return
    from editorial import fragment, level_links
    feed = len(relative.parts) == 1
    classes = soup.body.get('class', [])
    soup.body['class'] = list(dict.fromkeys([*classes, 'reading-page', *(['daily-feed'] if feed else [])]))
    hero = soup.select_one('.page-hero')
    masthead = soup.select_one('.site-masthead')
    if hero is None or masthead is None:
        return
    # Recreate a single selector using sibling URLs. A dated lesson stays on its
    # own date when changing levels; the browser also preserves feed anchors.
    for old in soup.select('.story-levels, .level-toolbar'):
        if old.parent is not None:
            old.decompose()
    toolbar = soup.new_tag('div', attrs={'class': 'level-toolbar'})
    toolbar.append(fragment(level_links(level)).nav)
    masthead.append(toolbar)
    hero['class'] = list(dict.fromkeys([*hero.get('class', []), 'reading-heading']))
    for redundant in soup.select('main > .top-nav, .lesson-content > .header'):
        redundant.decompose()
    if feed:
        hero.clear()
        heading = soup.new_tag('h1')
        heading.string = f'Daily English · {level.title()}'
        hero.append(heading)
        from update_site import LESSON_LIMIT
        intro = soup.select_one('.index-container > p')
        if intro:
            intro.string = f'Your latest {LESSON_LIMIT} news lessons.'
    else:
        read = soup.select_one('.learning-panel[data-stage="read"]')
        for notice in hero.select('.archive-notice'):
            if read is not None:
                read.append(notice.extract())
        for redundant in hero.select(':scope > p:not(.eyebrow), :scope > .level-badge, :scope > a'):
            redundant.decompose()
        for duplicate in soup.select('.daily-lesson > .lesson-description'):
            duplicate.decompose()
        label = soup.new_tag('p', attrs={'class': 'reading-print-level'})
        label.string = f'{level.title()} · {LEVELS[level]}'
        for old in hero.select('.reading-print-level'):
            old.decompose()
        hero.append(label)
    archive = soup.new_tag('a', href=prefix + 'archive.html',
                           attrs={'class': 'text-link reading-archive-link', 'data-archive-link': ''})
    archive.string = 'News archive →'
    hero.append(archive)


def finish_reading_layout(soup):
    """Position support added by SEO after its metadata has been assembled."""
    if 'reading-page' not in soup.body.get('class', []):
        return
    prepare_reading_controls(soup)
    main = soup.main
    footer = main.select_one('.site-footer')
    for breadcrumbs in main.select(':scope > .seo-breadcrumbs'):
        breadcrumbs.extract()
        if footer is not None:
            footer.insert_before(breadcrumbs)
        else:
            main.append(breadcrumbs)
    read = soup.select_one('.learning-panel[data-stage="read"]')
    if read is None:
        return
    cover = soup.select_one('.lesson-cover')
    if cover is not None:
        # The SEO cover includes full attribution. Keep that one illustration
        # beside the lesson content instead of repeating it above the lesson.
        for duplicate in read.select('.reading-photo'):
            duplicate.decompose()
        first_section = read.select_one('.section')
        if first_section is not None:
            first_section.insert_after(cover.extract())


def prepare_reading_controls(soup):
    """Publish the initial geometry; deferred JavaScript only enables controls.

    The small inline scripts run during parsing, before a linked lesson can be
    painted closed. Without JavaScript, the native disclosures and all three
    panels remain readable and the inactive controls stay hidden.
    """
    from editorial import fragment
    for old in soup.select('script[data-reading-start], script[data-reading-open]'):
        old.decompose()
    start = soup.new_tag('script', attrs={'data-reading-start': ''})
    start.string = 'document.documentElement.classList.add("reading-js");'
    soup.head.append(start)
    learning_script = soup.select_one('script[src*="learning.js"]')
    if learning_script:
        learning_script['onerror'] = 'document.documentElement.classList.remove("reading-js")'
    languages = [('en', 'English'), ('ja', 'Japanese'), ('ko', 'Korean'),
                 ('zh-Hans', 'Chinese'), ('es', 'Spanish'), ('pt-BR', 'Portuguese')]
    for index, lesson in enumerate(soup.select('.daily-lesson')):
        opener = soup.new_tag('script', attrs={'data-reading-open': ''})
        opener.string = ('try{if(decodeURIComponent(location.hash.slice(1))==='
                         'document.currentScript.parentElement.id)'
                         'document.currentScript.parentElement.open=true}catch(e){}')
        lesson.insert(0, opener)
        content = lesson.select_one('.lesson-content')
        if content is None:
            continue
        for old in content.select('.learning-flow, .stage-actions, .vocabulary-languages, .vocabulary-language-status'):
            old.decompose()
        nav = soup.new_tag('nav', attrs={'class': 'learning-flow', 'aria-label': 'Lesson steps', 'hidden': ''})
        for stage_index, stage in enumerate(('read', 'practice', 'discuss')):
            panel = content.select_one(f'[data-stage="{stage}"]')
            if panel is None:
                continue
            panel['id'] = f'learning-{index}-{stage}'
            button = soup.new_tag('button', type='button', disabled='',
                                  attrs={'aria-controls': panel['id']})
            button.string = f'{stage_index + 1}. {stage.title()}'
            if stage_index == 0:
                button['aria-current'] = 'step'
            nav.append(button)
            actions = soup.new_tag('div', attrs={'class': 'stage-actions', 'hidden': ''})
            if stage_index:
                back = soup.new_tag('button', type='button', disabled='', attrs={'class': 'secondary-button'})
                back.string = '← ' + ('Read again' if stage_index == 1 else 'Back to practice')
                actions.append(back)
            next_button = soup.new_tag('button', type='button', disabled='', attrs={'class': 'primary-button'})
            next_button.string = ["Check your understanding in the 'Practice' section.", 'Discuss the story →', 'Finish lesson ✓'][stage_index]
            if stage_index == 2:
                next_button['data-finish-lesson'] = ''
                next_button['aria-pressed'] = 'false'
            actions.append(next_button)
            if stage_index == 2:
                help_id = f'learning-{index}-completion-help'
                next_button['aria-describedby'] = help_id
                help_note = soup.new_tag('p', id=help_id, attrs={'class': 'lesson-completion-help'})
                help_note.string = ('Click to mark complete; click again to undo. Checkmarks across the site '
                                    'track your completed lessons in this browser.')
                actions.append(help_note)
            panel.append(actions)
        content.insert(0, nav)
        read = content.select_one('[data-stage="read"]')
        reading = read.select_one('.section') if read else None
        hint = content.select_one('[data-word-hint]')
        if reading:
            for word in reading.select('p strong'):
                word['class'] = list(dict.fromkeys([*word.get('class', []), 'word-seed']))
            if hint:
                reading.insert_before(hint.extract())
        vocabulary = content.select_one('.vocab-box')
        if vocabulary is None or not vocabulary.select_one('.vocab-definition'):
            continue
        vocabulary['id'] = f'vocabulary-{index}'
        controls = soup.new_tag('div', attrs={'class': 'vocabulary-languages', 'role': 'group',
                                             'aria-label': 'Definition language', 'hidden': ''})
        for language, label in languages:
            button = soup.new_tag('button', type='button', disabled='',
                                  attrs={'class': 'vocabulary-language', 'data-definition-language': language,
                                         'aria-controls': vocabulary['id'], 'aria-pressed': str(language == 'en').lower()})
            button.string = label
            if language in ('zh-Hans', 'pt-BR'):
                button['title'] = button['aria-label'] = label
            controls.append(button)
        status = fragment('<p class="vocabulary-language-status" role="status" aria-live="polite" '
                          'aria-atomic="true" hidden>Definitions in English.</p>').p
        vocabulary.insert_before(controls)
        vocabulary.insert_before(status)
