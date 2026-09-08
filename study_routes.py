"""Small, optional sequences through existing lessons. No generation or tracking."""
import html
import json
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LEVELS = ('beginner', 'intermediate', 'advanced')


@lru_cache(maxsize=1)
def routes():
    from daily_images import latest_lesson
    _, latest = latest_lesson(ROOT)
    reading_end = {
        'title': 'Try a news story',
        'description': 'Read, check your understanding, and discuss the latest story.',
        'path': 'news/{date}/{level}.html' if latest else '{level}.html',
        'href': f'news/{latest["release_date"]}/{{level}}.html' if latest else '{level}.html',
    }
    return {
        'everyday': {
            'title': 'My first week in the US',
            'goal': 'Practice asking for help, shopping, and getting around.',
            'level': 'Beginner · A1–A2',
            'time': 'About 10–15 minutes per activity',
            'guidance': 'Read the useful phrases, learn the words, and try the dialogue. Language help is available in each unit.',
            'steps': [
                {'title': 'Arrival and first week', 'description': 'Ask someone to speak slowly and help you find your ride.', 'path': 'us-life.html#arrival'},
                {'title': 'Shopping and returns', 'description': 'Find an item and ask about returning it.', 'path': 'us-life.html#shopping'},
                {'title': 'Getting around', 'description': 'Ask which bus to take and how much the fare costs.', 'path': 'us-life.html#transportation'},
            ],
        },
        'reading': {
            'title': 'Build a reading habit',
            'goal': 'Start with everyday topics, then try a news story.',
            'level': 'All three levels',
            'time': 'About 10–20 minutes per activity',
            'guidance': 'Use Read, Practice, and Discuss in each lesson. Choose a level below; you can change it inside any story.',
            'steps': [
                {'title': 'A conversation at the market', 'description': 'Read about a small question that starts a conversation.', 'path': 'stories/food-market/{level}.html'},
                {'title': 'Trees in the city', 'description': 'Explore how shade can make a city more comfortable.', 'path': 'stories/city-trees/{level}.html'},
                reading_end,
            ],
        },
        'work': {
            'title': 'Speak more clearly at work',
            'goal': 'Ask precise questions, explain progress, and make a clear request.',
            'level': 'Upper intermediate–advanced · B2–C1',
            'time': 'About 45–60 minutes per activity',
            'guidance': 'These three lessons use project-team situations. Follow the numbered activities inside each lesson; no other course lessons are required first.',
            'steps': [
                {'title': 'Ask a precise question', 'description': 'Clarify a project brief: Project Charter and Scope Definition.', 'path': 'efsp-project-management.html#module-1'},
                {'title': 'Give a useful progress update', 'description': 'Explain a delay: Schedule, Critical Path, and Dependencies.', 'path': 'efsp-project-management.html#module-2'},
                {'title': 'Ask for an actionable next step', 'description': 'Request missing information: Vendor and Cross-Functional Delivery.', 'path': 'efsp-project-management.html#module-7'},
            ],
        },
    }


def step_href(route, step, level='beginner'):
    path = step.get('href', step['path']).replace('{level}', level)
    page, _, anchor = path.partition('#')
    return f'{page}?route={route}' + (f'#{anchor}' if anchor else '')


def build_page():
    from editorial import document, decorate_page
    cards = []
    for key, route in routes().items():
        selector = ''
        if key == 'reading':
            choices = ''.join(
                f'<label class="level-option"><input type="radio" name="feature-level" value="{level}"'
                + (' checked' if level == 'beginner' else '') + f'><span>{label}</span></label>'
                for level, label in [('beginner', 'Beginner · A1–A2'), ('intermediate', 'Intermediate · B1–B2'), ('advanced', 'Advanced · C1+')])
            selector = f'<fieldset class="route-level-choice"><legend>Reading level</legend><div class="level-options">{choices}</div></fieldset>'
            selector += '<noscript><p>These links start at Beginner. Use the level buttons inside any story to change level.</p></noscript>'
        steps = ''.join(
            f'<li><a href="{html.escape(step_href(key, step), quote=True)}"'
            + (' data-level-link' if key == 'reading' else '')
            + f'>{"Start: " if index == 0 else ""}{html.escape(step["title"])}</a>'
            + f'<p>{html.escape(step["description"])}</p></li>'
            for index, step in enumerate(route['steps']))
        cards.append(f'<article class="study-route-card" id="{key}" aria-labelledby="route-{key}">'
                     f'<h2 id="route-{key}">{route["title"]}</h2><p>{route["goal"]}</p>'
                     f'<p class="route-meta">{route["level"]} · {route["time"]}</p>'
                     f'<p>{route["guidance"]}</p>{selector}<ol class="study-route-steps">{steps}</ol></article>')
    body = ('<section class="route-intro"><h1>Choose a study route</h1>'
            '<p>Pick one goal. Start with activity 1, then use the next-activity link inside the lesson. '
            'Do one activity today and return when you are ready.</p>'
            '<p>Each route has just three activities. Times are a guide; take the time you need.</p>'
            '<noscript><p>Use the numbered lists below to open each activity. Return to this page for the next one.</p></noscript>'
            '<nav class="route-goals" aria-label="Choose a study goal"><a href="#everyday">Everyday life ↓</a>'
            '<a href="#reading">Reading ↓</a><a href="#work">Work ↓</a></nav></section>'
            + '<div class="study-route-list">' + ''.join(cards) + '</div>'
            '<p class="route-browse">Prefer to choose your own lessons? <a href="sitemap.html">Browse all lessons →</a></p>')
    path = ROOT / 'study-routes.html'
    path.write_text(document('Choose a Study Route: Everyday Life, Reading or Work', body), encoding='utf-8')
    decorate_page(path)


def enhance_page(soup, relative, prefix):
    """Load route navigation only on the guide and lessons it can accompany."""
    eligible = relative in {'study-routes.html', 'us-life.html', 'efsp-project-management.html'}
    eligible |= relative in {level+'.html' for level in LEVELS}
    eligible |= relative.startswith(('stories/food-market/', 'stories/city-trees/', 'news/'))
    if not eligible:
        return
    for old in soup.select('[data-study-routes], script[src*="study-routes.js"], link[href*="study-routes.css"]'):
        old.decompose()
    soup.head.append(soup.new_tag('link', rel='stylesheet', href=prefix+'study-routes.css?v=20260908-routes1'))
    if relative == 'study-routes.html':
        return
    data = soup.new_tag('script', type='application/json', attrs={'data-study-routes': '', 'data-site-root': prefix or './'})
    data.string = json.dumps(routes(), ensure_ascii=False).replace('<', '\\u003c')
    soup.head.append(data)
    soup.head.append(soup.new_tag('script', src=prefix+'study-routes.js?v=20260908-routes1', defer=True))
