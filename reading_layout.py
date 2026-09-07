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
