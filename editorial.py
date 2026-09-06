"""Offline publishing helpers for the shared design and guided reading experience.

Run `python3 editorial.py` after changing page templates or curated stories.
This command never calls a language model or paid service.
"""
import html
import json
import re
from pathlib import Path
from urllib.parse import urlparse

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent


def fragment(markup):
    return BeautifulSoup(markup, "html.parser")


def safe_url(value):
    parsed = urlparse(str(value))
    return str(value) if parsed.scheme == "https" and parsed.netloc else ""


def site_header(prefix="", current=""):
    links = [("index.html", "Discover"), ("beginner.html", "Daily news"),
             ("grammar-concepts.html", "Grammar"), ("efsp.html", "English for Work")]
    nav = "".join(f'<a href="{prefix}{url}"' + (' aria-current="page"' if current == url else '') + f'>{label}</a>' for url, label in links)
    return f'<a class="skip-link" href="#main-content">Skip to content</a><header class="site-header"><a class="brand" href="{prefix}index.html" aria-label="English Ladder home"><span class="brand-mark" aria-hidden="true"></span>English Ladder</a><nav class="site-links" aria-label="Main navigation">{nav}</nav></header>'


def footer(prefix=""):
    return f'<footer class="site-footer"><span>English for a world worth exploring.</span><a href="{prefix}photo-credits.html">Photo credits</a><a href="https://englishroad.com" target="_blank" rel="noopener noreferrer">Check your English level ↗</a></footer>'


def document(title, content, body_class="theme-hub", prefix="", current=""):
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} | English Ladder</title><meta name="description" content="Learn English with real stories. Read, practice, and discuss at your level.">
<link rel="icon" href="{prefix}favicon.png"><link rel="stylesheet" href="{prefix}styles.css"><link rel="stylesheet" href="{prefix}editorial.css">
<script defer src="{prefix}app.js"></script><script defer src="{prefix}learning.js"></script>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon='{{"token":"c9c5fc6fc0f947efb5b32e0139ad4459"}}'></script>
</head><body class="{body_class}">{site_header(prefix, current)}<main id="main-content" class="page-shell">{content}{footer(prefix)}</main></body></html>'''


def enhance_lesson(lesson, lesson_data=None, source=None):
    """Enhance generated and older markup once; retain all content without JavaScript."""
    key = lesson.get("data-lesson-key", "lesson")
    lesson["id"] = "lesson-" + key
    if lesson.select_one(".learning-panel"):
        return
    content = lesson.select_one(".lesson-content")
    if not content:
        return
    sections = content.select(":scope > .section")
    if len(sections) < 3:
        return
    data = lesson_data or {}
    prediction = data.get("prediction") or "Look at the title. What do you think you will learn?"
    prompts = data.get("discussion") or ["Explain this story to a friend in two sentences.", "Which detail interests you most? Say why."]
    read = fragment('<div class="learning-panel" data-stage="read"></div>').div
    practice = fragment('<div class="learning-panel" data-stage="practice"></div>').div
    discuss = fragment('<div class="learning-panel" data-stage="discuss"></div>').div
    read.append(fragment(f'<aside class="prediction"><h3>Before you read</h3><p>{html.escape(prediction)}</p></aside>').aside)
    for index, section in enumerate(sections[:3]):
        heading = section.find("h2")
        if heading:
            heading.string = ["Read the story", "Words and grammar", "Check your understanding"][index]
        (read if index < 2 else practice).append(section.extract())
    # Preserve any additional original sections rather than silently dropping them.
    for section in sections[3:]:
        practice.append(section.extract())
    read.append(fragment('<p class="reading-hint" data-word-hint hidden>Tap an underlined word in the story to see its meaning.</p>').p)
    quiz_count = len(practice.select(".quiz-question"))
    practice.insert(0, fragment(f'<p class="practice-progress" role="status" aria-live="polite">0 of {quiz_count} questions answered</p>').p)
    questions = "".join(f'<li>{html.escape(str(prompt))}</li>' for prompt in prompts)
    discuss.append(fragment(f'<section class="discussion"><h2>Share your ideas</h2><ol>{questions}</ol><p>Try using two words from the story. You can speak to a partner or practice on your own.</p><label for="notes-{key}">Your ideas (optional)</label><textarea id="notes-{key}" placeholder="I think… / One thing I learned is…"></textarea><p class="note-hint">These notes stay on this page. They are not sent or saved.</p><p class="completion-message" role="status" hidden>Lesson complete. You have read the story, practiced, and shared your ideas.</p></section>').section)
    if source and safe_url(source.get("link", "")):
        read.append(fragment(f'<p class="lesson-source">Source: <a href="{html.escape(safe_url(source["link"]), quote=True)}" target="_blank" rel="noopener noreferrer">{html.escape(source.get("name") or "Original report")} ↗</a></p>').p)
    content.extend([read, practice, discuss])


LABELS = {
    "Back to Level Hub": "Back to Discover", "Back to EFSP Directory": "Back to English for Work",
    "English for Special Purposes curricula": "English for Work", "Professional Curricula": "English for Work",
    "Industry-specific English practice labs": "English for Work", "ESL Study Tools": "Practice your English",
    "US Life Starter": "Everyday English in the US", "English Grammar Concepts": "Grammar you can use",
    "I. The News Brief": "Read the story", "II. Vocabulary & Grammar Focus": "Words and grammar",
    "III. Comprehension & Mastery Quiz": "Check your understanding",
    "Low-Level ESL": "Everyday conversations", "English for Special Purposes": "English for Work",
    "Diagnostic": "Check your grammar", "Shadowing": "Listen and repeat", "Register": "Formal or casual?",
    "Grammar Diagnostic Map": "Find grammar to practice", "Sentence Repair Lab": "Improve a sentence",
    "Pronunciation Shadowing Studio": "Listen and repeat", "Register Transformer": "Make it formal or casual",
    "Curriculum Directory": "Find your field", "Open an industry page": "Choose your area of work",
    "Web practice plus printable depth": "Practice online or use a workbook",
    "Local image assets": "Visual explanations", "Map my study path": "Show what to practice",
    "Make it your own": "Share your ideas",
}


def decorate_page(path):
    path = Path(path)
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
    if not soup.head or not soup.body or not soup.find("main"):
        return
    prefix = "../" * len(path.relative_to(ROOT).parent.parts)
    if not soup.select_one('link[href$="editorial.css"]'):
        soup.head.append(fragment(f'<link rel="stylesheet" href="{prefix}editorial.css">').link)
    if not soup.select_one(".site-header"):
        for element in reversed(list(fragment(site_header(prefix, path.name)).contents)):
            soup.body.insert(0, element)
    main = soup.find("main")
    main["id"] = "main-content"
    if not soup.select_one(".site-footer"):
        main.append(fragment(footer(prefix)).footer)
    for node in list(soup.find_all(string=True)):
        if node.parent.name in {"script", "style"}:
            continue
        stripped = str(node).strip()
        if stripped in LABELS:
            node.replace_with(str(node).replace(stripped, LABELS[stripped]))
    for image in soup.select('img[src$="English-Ladder.png"]'):
        if "efsp-industry-logo" in image.get("class", []):
            image.decompose()
        else:
            image["src"] = prefix + "assets/editorial/everyday-travel.webp"
            image["alt"] = "Passengers waiting on a subway platform in Japan."
            image["width"], image["height"] = "1000", "667"
    for image in soup.select('.efsp-hero-image, .us-life-hero-image'):
        if image.get("src", "").endswith("everyday-travel.webp") and not image.parent.select_one(".photo-context"):
            image.parent.append(fragment('<p class="photo-context">Everyday journeys: a subway platform in Japan. Photo by john Applese / Unsplash.</p>').p)
    intro_copy = {
        "tools.html": (".tools-hero-copy > p:not(.eyebrow)", "Choose a quick activity. Improve a sentence, practice pronunciation, or find words for a conversation."),
        "efsp.html": (".efsp-hero-copy > p:not(.eyebrow)", "Find your field and practice the conversations you have at work. Explore useful phrases, real situations, and printable workbooks."),
        "grammar-concepts.html": (".grammar-hero-copy > p:not(.eyebrow)", "Explore 44 visual guides to English grammar. Choose a topic, see how it works, and try a short exercise."),
    }
    if path.parent == ROOT and path.name in intro_copy:
        selector, copy = intro_copy[path.name]
        paragraph = soup.select_one(selector)
        if paragraph:
            paragraph.string = copy
    if path.name in {"beginner.html", "intermediate.html", "advanced.html"} and path.parent == ROOT:
        level = path.stem
        hero = soup.select_one(".page-hero")
        if hero:
            hero.h1.string = f"The world, in {level} English."
            paragraphs = hero.find_all("p")
            if paragraphs:
                paragraphs[-1].string = "Choose a story. Read it, practice useful words, then share your ideas."
            if not hero.select_one(".story-levels"):
                hero.append(fragment(level_links(level)).nav)
        badge = soup.select_one(".top-nav > span")
        if badge:
            badge["class"] = "level-badge"
            badge.string = {"beginner": "Beginner · A1–A2", "intermediate": "Intermediate · B1–B2", "advanced": "Advanced · C1+"}[level]
        intro = soup.select_one(".index-container > p")
        if intro:
            intro.string = "Your latest seven news lessons. Open a headline to begin."
        for lesson in soup.select("details.daily-lesson"):
            key = lesson.get("data-lesson-key", "")
            archive = ROOT / "archive" / "lessons" / f"{key}.json"
            data = json.loads(archive.read_text()) if archive.is_file() else {}
            enhance_lesson(lesson, data.get("levels", {}).get(level, {}).get("lesson"), data.get("source"))
        if not soup.select_one('script[src$="learning.js"]'):
            soup.head.append(fragment(f'<script defer src="{prefix}learning.js"></script>').script)
    if soup.title:
        for old, new in LABELS.items():
            if old in soup.title.get_text():
                soup.title.string = soup.title.get_text().replace(old, new)
    path.write_text(str(soup), encoding="utf-8")


def level_links(current, story=None):
    levels = [("beginner", "Beginner · A1–A2"), ("intermediate", "Intermediate · B1–B2"), ("advanced", "Advanced · C1+")]
    return '<nav class="story-levels" aria-label="Choose your English level">' + "".join(
        f'<a href="{key}.html"' + (' aria-current="page"' if current == key else '') + f'>{name}</a>' for key, name in levels) + '</nav>'


def build_homepage():
    archives = sorted((ROOT / "archive/lessons").glob("*.json"), reverse=True)
    latest = json.loads(archives[0].read_text()) if archives else None
    news = ""
    if latest:
        brief = latest["levels"]["beginner"]["lesson"]
        date = latest["release_date"]
        links = "".join(f'<a href="{level}.html#lesson-{date}">{level.title()} →</a>' for level in ["beginner", "intermediate", "advanced"])
        news = f'<section aria-labelledby="latest-heading"><div class="section-heading"><h2 id="latest-heading">In the news</h2><span class="text-link">{date}</span></div><article class="news-strip"><p class="eyebrow">Latest story</p><div><h3>{html.escape(brief["title"])}</h3><p>{html.escape(brief["overview"])}</p><div class="news-levels">{links}</div></div><a class="text-link" href="beginner.html">More news →</a></article></section>'
    content = f'''<div class="issue-line"><span>Stay curious. Keep learning.</span><span>Real stories · Three English levels</span></div>
<section class="feature-story" aria-labelledby="feature-title"><div class="feature-copy"><p class="eyebrow">Nature &amp; city life · 5-minute lesson</p><h1 id="feature-title">Can trees cool a city?</h1><p>A little shade can make a big difference. Explore how trees change the places we live.</p>
<div class="level-form"><fieldset><legend>Choose your English level</legend><div class="level-options">
<label class="level-option"><input type="radio" name="feature-level" value="beginner" checked><span>Beginner</span></label>
<label class="level-option"><input type="radio" name="feature-level" value="intermediate"><span>Intermediate</span></label>
<label class="level-option"><input type="radio" name="feature-level" value="advanced"><span>Advanced</span></label></div></fieldset>
<a class="primary-link" id="feature-start" href="stories/city-trees/beginner.html">Start lesson <span aria-hidden="true">→</span></a><a class="level-help" href="https://englishroad.com" target="_blank" rel="noopener noreferrer">Not sure of your level? ↗</a>
<noscript><p>Also available in <a href="stories/city-trees/intermediate.html">Intermediate</a> and <a href="stories/city-trees/advanced.html">Advanced</a> English.</p></noscript></div></div>
<figure class="feature-photo"><img src="assets/editorial/city-trees.webp" width="1600" height="1199" alt="A tree-filled urban park surrounded by city buildings." fetchpriority="high"><figcaption>Green space in the city. Photograph by <a href="https://unsplash.com/photos/an-aerial-view-of-a-park-with-trees-and-buildings-in-the-background-_YEJI5nZBPk">Leo_Visions / Unsplash</a>.</figcaption></figure></section>
{news}
<section aria-labelledby="explore-heading"><div class="section-heading"><h2 id="explore-heading">English beyond the headlines</h2><span class="text-link">Everyday situations. Useful words.</span></div><div class="explore-grid">
<a class="explore-story" href="stories/food-market/beginner.html"><img src="assets/editorial/food-market.webp" width="1000" height="692" alt="Shoppers and colorful fruit stalls at an indoor market." loading="lazy"><div><span class="eyebrow">Food &amp; conversation</span><h3>A small question. A new conversation.</h3><p>Visit a market and practice asking for what you need.</p><span class="text-link">Try the lesson →</span></div></a>
<a class="explore-story" href="us-life.html"><img src="assets/editorial/everyday-travel.webp" width="1000" height="667" alt="Passengers waiting on a subway platform in Japan." loading="lazy"><div><span class="eyebrow">Everyday English</span><h3>Find your words in a new place.</h3><p>Practice the conversations that help you settle into life in the US.</p><span class="text-link">Explore everyday English →</span></div></a></div></section>
<section class="study-paths" aria-labelledby="paths-heading"><div class="section-heading"><h2 id="paths-heading">What would you like to practice?</h2></div><div class="path-grid">
<a class="path-link" href="tools.html"><span class="path-number">01 / Practice</span><h3>Build your confidence →</h3><p>Improve sentences, pronunciation, and conversation.</p></a>
<a class="path-link" href="grammar-concepts.html"><span class="path-number">02 / Grammar</span><h3>Understand grammar →</h3><p>44 visual guides to how English works.</p></a>
<a class="path-link" href="efsp.html"><span class="path-number">03 / Work</span><h3>Speak up at work →</h3><p>Practice meetings and conversations for your job.</p></a>
<a class="path-link" href="us-life.html"><span class="path-number">04 / Daily life</span><h3>Feel more at home →</h3><p>Useful English for getting settled in the US.</p></a></div></section>'''
    (ROOT / "index.html").write_text(document("Discover a world of English", content, current="index.html"), encoding="utf-8")


def build_credits():
    credits = json.loads((ROOT / "assets/editorial/credits.json").read_text())
    items = "".join(f'<li><a href="{item["source_page"]}">{html.escape(item["alt"])}</a> — {html.escape(item["creator"])}. <a href="{item["license_url"]}">{item["license"]}</a>. Resized and compressed for this site.</li>' for item in credits)
    (ROOT / "photo-credits.html").write_text(document("Photo credits", f'<section class="page-hero"><p class="eyebrow">Behind the photographs</p><h1>Photo credits</h1><p>Real places, photographed by real people.</p></section><ul>{items}</ul>'), encoding="utf-8")


def build_stories():
    from datetime import datetime, timezone
    from story_lessons import STORIES
    from update_site import LEVELS, render_lesson_html, validate_lesson_data
    credits = {item["key"]: item for item in json.loads((ROOT / "assets/editorial/credits.json").read_text())}
    for story in STORIES:
        for level in LEVELS:
            name = level["name"].lower()
            data = story["levels"][name]
            config = dict(level, sentence_count=6, vocabulary_count=3, quiz_count=5)
            issues = validate_lesson_data(data, config)
            if issues:
                raise ValueError(f'{story["slug"]}/{name}: {issues}')
            lesson = fragment(render_lesson_html(data, config, datetime(2026, 9, 5, tzinfo=timezone.utc), story.get("source"))).details
            lesson["data-lesson-key"] = story["slug"]
            lesson["open"] = ""
            enhance_lesson(lesson, data, story.get("source"))
            photo = credits[story["slug"]]
            figure = fragment(f'<figure class="reading-photo"><img src="../../assets/editorial/{story["slug"]}.webp" width="{photo["width"]}" height="{photo["height"]}" alt="{html.escape(photo["alt"], quote=True)}"><figcaption>{html.escape(story["photo_note"])} Photo: <a href="{photo["source_page"]}">{html.escape(photo["creator"])} / Unsplash</a>.</figcaption></figure>').figure
            lesson.select_one('[data-stage="read"]').insert(1, figure)
            if story.get("scenario_note"):
                lesson.select_one('[data-stage="read"]').append(fragment(f'<p class="lesson-source">{html.escape(story["scenario_note"])}</p>').p)
            for source_url in story.get("supporting_sources", []):
                title = "Benefits of trees" if "benefits" in source_url else "Caring for new trees"
                lesson.select_one('[data-stage="read"]').append(fragment(f'<p class="lesson-source">Read more: <a href="{source_url}" target="_blank" rel="noopener noreferrer">{title} — US Environmental Protection Agency ↗</a></p>').p)
            badge = {"beginner": "Beginner · A1–A2", "intermediate": "Intermediate · B1–B2", "advanced": "Advanced · C1+"}[name]
            content = f'<section class="page-hero"><p class="eyebrow">{story["category"]} · 5-minute lesson</p><h1>{html.escape(data["title"])}</h1><p>{html.escape(data["overview"])}</p><span class="level-badge">{badge}</span>{level_links(name, story["slug"])}</section>{lesson}'
            path = ROOT / "stories" / story["slug"] / f"{name}.html"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(document(data["title"], content, f'theme-{name} story-page', "../../"), encoding="utf-8")


def publish_editorial_pages():
    build_homepage()
    build_stories()
    build_credits()
    for path in [*ROOT.glob("*.html"), *ROOT.glob("grammar-concepts/*.html")]:
        decorate_page(path)


if __name__ == "__main__":
    publish_editorial_pages()
