"""Offline publishing helpers for the shared design and guided reading experience.

Run `python3 editorial.py` after changing page templates or curated stories.
This command never calls a language model or paid service.
"""
import html
import json
import re
import struct
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
    if current.startswith("efsp-"):
        current = "efsp.html"
    elif current.startswith("concept-"):
        current = "grammar-concepts.html"
    elif current in {"intermediate.html", "advanced.html"}:
        current = "beginner.html"
    links = [("index.html", "Discover"), ("beginner.html", "Daily news"),
             ("grammar-concepts.html", "Grammar"), ("efsp.html", "English for Work")]
    nav = "".join(f'<a href="{prefix}{url}"' + (' aria-current="page"' if current == url else '') + f'>{label}</a>' for url, label in links)
    return f'<a class="skip-link" href="#main-content">Skip to content</a><div class="site-masthead"><header class="site-header"><a class="brand" href="{prefix}index.html" aria-label="English Ladder home"><img class="brand-mark" src="{prefix}assets/brand/ladder-mark.png" width="40" height="40" alt="">English Ladder</a><nav class="site-links" aria-label="Main navigation">{nav}</nav></header></div>'


def footer(prefix=""):
    return f'<footer class="site-footer"><span>English for a world worth exploring.</span><a href="{prefix}photo-credits.html">Photo credits</a><a href="https://englishroad.com" target="_blank" rel="noopener noreferrer">Check your English level ↗</a></footer>'


def phrase_preview(work=False):
    label = "In your next meeting" if work else "A little English goes a long way"
    quote = "Could you walk me through that?" if work else "Could you help me, please?"
    note = "Ask someone to explain, step by step." if work else "Start a conversation. Make a connection."
    return f'<aside class="phrase-preview{ " phrase-preview-work" if work else ""}"><p class="eyebrow">{label}</p><blockquote>“{quote}”</blockquote><p class="phrase-preview-note">{note}</p><span class="phrase-preview-caption">Useful words. Real situations.</span></aside>'


def document(title, content, body_class="theme-hub", prefix="", current=""):
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} | English Ladder</title><meta name="description" content="Learn English with real stories. Read, practice, and discuss at your level.">
<link rel="icon" href="{prefix}assets/brand/favicon.png"><link rel="stylesheet" href="{prefix}styles.css"><link rel="stylesheet" href="{prefix}editorial.css">
<script defer src="{prefix}app.js"></script><script defer src="{prefix}learning.js"></script>
</head><body class="{body_class}">{site_header(prefix, current)}<main id="main-content" class="page-shell">{content}{footer(prefix)}</main></body></html>'''


def locate_title_instruction(text):
    """Keep instructions explicit about the title's position without repeating 'above'."""
    return re.sub(r'\b(Read|Look at) the (title|headline)(?=[.!?])', r'\1 the \2 above', text, flags=re.IGNORECASE)


def enhance_lesson(lesson, lesson_data=None, source=None):
    """Enhance generated and older markup once; retain all content without JavaScript."""
    key = lesson.get("data-lesson-key", "lesson")
    lesson["id"] = "lesson-" + key
    for prompt in lesson.select('.prediction p'):
        prompt.string = locate_title_instruction(prompt.get_text())
    if lesson.select_one(".learning-panel"):
        return
    content = lesson.select_one(".lesson-content")
    if not content:
        return
    sections = content.select(":scope > .section")
    if len(sections) < 3:
        return
    data = lesson_data or {}
    prediction = locate_title_instruction(data.get("prediction") or "Read the title above. What do you think you will learn?")
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
    if source:
        topic_text = " ".join(str(source.get(k,"")) for k in ("title","summary")).lower()
        sensitive = any(word in topic_text for word in ("murder", "deaths", "killed", "death toll", "deport", "attack"))
        if sensitive:
            read.insert(0, fragment('<aside class="archive-notice"><strong>Choose what you read.</strong> This report includes distressing events. You can choose an everyday story on Discover instead.</aside>').aside)
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
    prefix = "/" if path.name == "404.html" else "../" * len(path.relative_to(ROOT).parent.parts)
    if not soup.find("link", href=re.compile(r"(^|/)editorial\.css(?:\?|$)")):
        soup.head.append(fragment(f'<link rel="stylesheet" href="{prefix}editorial.css">').link)
    for element in soup.select(".site-masthead, .skip-link"):
        element.decompose()
    for element in soup.select(".site-header"):
        element.decompose()
    for element in reversed(list(fragment(site_header(prefix, path.name)).contents)):
        soup.body.insert(0, element)
    for icon in soup.select('link[rel="icon"]'):
        icon["href"] = prefix + "assets/brand/favicon.png"
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
    for image in soup.select(".efsp-industry-logo"):
        image.decompose()
    # Use useful course language instead of an unrelated location photograph.
    for visual in soup.select(".efsp-hero-visual, .us-life-hero-visual"):
        visual.clear()
        is_work = "efsp-hero-visual" in visual.get("class", [])
        visual.append(fragment(phrase_preview(is_work)).aside)
    for paragraph in soup.select(".grammar-detail-hero .grammar-hero-copy > p:not(.eyebrow)"):
        paragraph.string = "See the pattern, explore the examples, and put it into practice."
    for image in soup.select(".grammar-thumb img, .grammar-hero-image"):
        image["loading"] = "eager" if "grammar-hero-image" in image.get("class", []) else "lazy"
        # Intrinsic dimensions prevent the artwork from shifting the surrounding text.
        image_path = (path.parent / image["src"]).resolve()
        if image_path.is_file():
            with image_path.open("rb") as original:
                header = original.read(24)
            if header.startswith(b"\x89PNG\r\n\x1a\n"):
                image["width"], image["height"] = map(str, struct.unpack(">II", header[16:24]))
    for hint in soup.select(".grammar-image-hint"):
        hint.string = "View full-size guide ↗"
    directory_header = soup.select_one(".efsp-directory-header")
    if directory_header and not directory_header.select_one(".directory-search-field"):
        search_field = soup.new_tag("div", attrs={"class": "directory-search-field"})
        for element in directory_header.select(".efsp-search-label, .efsp-directory-search"):
            search_field.append(element.extract())
        directory_header.append(search_field)
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
        from update_site import LESSON_LIMIT
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
            intro.string = f"Your latest {LESSON_LIMIT} news lessons. Open a headline to begin."
        for lesson in soup.select("details.daily-lesson"):
            key = lesson.get("data-lesson-key", "")
            archive = ROOT / "archive" / "lessons" / f"{key}.json"
            data = json.loads(archive.read_text()) if archive.is_file() else {}
            enhance_lesson(lesson, data.get("levels", {}).get(level, {}).get("lesson"), data.get("source"))
        if not soup.select_one('script[src*="learning.js"]'):
            soup.head.append(fragment(f'<script defer src="{prefix}learning.js"></script>').script)
    if soup.title:
        for old, new in LABELS.items():
            if old in soup.title.get_text():
                soup.title.string = soup.title.get_text().replace(old, new)
    from site_quality import enhance_page
    enhance_page(soup, path, prefix)
    path.write_text(str(soup), encoding="utf-8")


def level_links(current, story=None):
    levels = [("beginner", "Beginner", "A1–A2"), ("intermediate", "Intermediate", "B1–B2"), ("advanced", "Advanced", "C1+")]
    return '<nav class="story-levels" aria-label="Choose your English level">' + "".join(
        f'<a href="{key}.html" data-level-choice="{key}" aria-label="{name} · {cefr}"' + (' aria-current="page"' if current == key else '') + f'><span class="level-name">{name}</span> <span class="level-range">{cefr}</span></a>' for key, name, cefr in levels) + '</nav>'


def build_homepage():
    from daily_images import latest_lesson, image_for_lesson
    _, latest = latest_lesson(ROOT)
    title = "Can trees cool a city?"
    overview = "A little shade can make a big difference. Explore how trees change the places we live."
    eyebrow = "Nature &amp; city life · 5-minute lesson"
    urls = {level: f"stories/city-trees/{level}.html" for level in ("beginner", "intermediate", "advanced")}
    visual = '<figure class="feature-photo"><img src="assets/editorial/city-trees.webp" width="1600" height="1199" alt="A tree-filled urban park surrounded by city buildings." fetchpriority="high"><figcaption>Green space in the city. Photograph by <a href="https://unsplash.com/photos/an-aerial-view-of-a-park-with-trees-and-buildings-in-the-background-_YEJI5nZBPk">Leo_Visions / Unsplash</a>.</figcaption></figure>'
    daily_class = ""
    if latest:
        brief = latest["levels"]["beginner"]["lesson"]
        title, overview = brief["title"], brief["overview"]
        date = latest["release_date"]
        from datetime import date as calendar_date
        date_label = calendar_date.fromisoformat(date).strftime("%B %d, %Y").replace(" 0", " ")
        eyebrow = f'Latest news lesson · <time datetime="{date}">{date_label}</time>'
        urls = {level: f'{level}.html#lesson-{date}' for level in urls}
        daily_class = " feature-story--daily"
        picture = image_for_lesson(latest, ROOT)
        if picture:
            visual = f'<figure class="feature-photo"><img src="{picture["path"]}" width="{picture["width"]}" height="{picture["height"]}" alt="{html.escape(picture["alt"], quote=True)}" fetchpriority="high"><figcaption>AI-generated illustration · Inspired by this lesson; not a news photograph.</figcaption></figure>'
        else:
            words = "".join(f'<li>{html.escape(str(item["term"]))}</li>' for item in brief.get("vocabulary", [])[:5] if "term" in item)
            question = html.escape(locate_title_instruction(brief.get("prediction") or "Read the title above. What do you think you will learn?"))
            visual = f'<aside class="feature-preview" aria-label="Inside this lesson"><p class="eyebrow">Before you read</p><h2>{question}</h2><p>Read a real story. Learn useful words. Share your ideas.</p><ul aria-label="Words to explore">{words}</ul><span class="feature-preview-steps">Read / Practice / Discuss</span></aside>'
    title, overview = html.escape(title), html.escape(overview)
    content = f'''<section class="home-intro"><h1>Free English lessons for real life.</h1><p>Build your English with <a href="beginner.html">daily reading</a>, <a href="grammar-concepts.html">grammar practice</a>, and <a href="efsp.html">workplace conversations</a>. Study at your level, with printable guides and ready-to-copy AI prompts.</p></section>
<div class="issue-line"><span>Stay curious. Keep learning.</span><span>Real stories · Three English levels</span></div>
<section class="feature-story{daily_class}" aria-labelledby="feature-title"><div class="feature-copy"><p class="eyebrow">{eyebrow}</p><h2 id="feature-title"><span class="lesson-title-label">Title: </span><span class="lesson-title-text">{title}</span></h2><p>{overview}</p>
<div class="level-form"><fieldset><legend>Choose your English level</legend><div class="level-options">
<label class="level-option"><input type="radio" name="feature-level" value="beginner" data-lesson-href="{urls['beginner']}" checked><span>Beginner</span></label>
<label class="level-option"><input type="radio" name="feature-level" value="intermediate" data-lesson-href="{urls['intermediate']}"><span>Intermediate</span></label>
<label class="level-option"><input type="radio" name="feature-level" value="advanced" data-lesson-href="{urls['advanced']}"><span>Advanced</span></label></div></fieldset>
<a class="primary-link" id="feature-start" href="{urls['beginner']}">Start lesson <span aria-hidden="true">→</span></a><a class="level-help" href="https://englishroad.com" target="_blank" rel="noopener noreferrer">Not sure of your level? ↗</a>
<noscript><p>Also available in <a href="{urls['intermediate']}">Intermediate</a> and <a href="{urls['advanced']}">Advanced</a> English.</p></noscript></div></div>
{visual}</section>
<section aria-labelledby="explore-heading"><div class="section-heading"><h2 id="explore-heading">English beyond the headlines</h2><span class="text-link">Everyday situations. Useful words.</span></div><div class="explore-grid">
<a class="explore-story" href="stories/food-market/beginner.html"><img src="assets/editorial/food-market.webp" width="1000" height="692" alt="Shoppers and colorful fruit stalls at an indoor market." loading="lazy"><div><span class="eyebrow">Food &amp; conversation</span><h3>A small question. A new conversation.</h3><p>Visit a market and practice asking for what you need.</p><span class="text-link">Try the lesson →</span></div></a>
<a class="explore-story" href="stories/city-trees/beginner.html"><img src="assets/editorial/city-trees.webp" width="1600" height="1199" alt="Trees surround a green urban park." loading="lazy"><div><span class="eyebrow">Nature &amp; city life</span><h3>Can trees cool a city?</h3><p>Explore how a little shade changes the places we live.</p><span class="text-link">Try the lesson →</span></div></a></div></section>
<section class="study-paths" aria-labelledby="paths-heading"><div class="section-heading"><h2 id="paths-heading">What would you like to practice?</h2></div><div class="path-grid">
<a class="path-link" href="tools.html"><span class="path-number">01 / Practice</span><h3>Build your confidence →</h3><p>Improve sentences, pronunciation, and conversation.</p></a>
<a class="path-link" href="grammar-concepts.html"><span class="path-number">02 / Grammar</span><h3>Understand grammar →</h3><p>44 lessons with examples, exercises, and free PDFs.</p></a>
<a class="path-link" href="efsp.html"><span class="path-number">03 / Work</span><h3>Speak up at work →</h3><p>Practice meetings and conversations for your job.</p></a>
<a class="path-link" href="us-life.html"><span class="path-number">04 / Daily life</span><h3>Feel more at home →</h3><p>Useful English for getting settled in the US.</p></a></div></section>'''
    page = document("Discover a world of English", content, current="index.html")
    # A returning visitor must not run the old selector that always opened the tree story.
    page = page.replace('src="learning.js"', 'src="learning.js?v=20260906"')
    page = page.replace('href="editorial.css"', 'href="editorial.css?v=20260906"')
    (ROOT / "index.html").write_text(page, encoding="utf-8")



def build_credits():
    credits = json.loads((ROOT / "assets/editorial/credits.json").read_text())
    items = "".join(f'<li><a href="{item["source_page"]}">{html.escape(item["alt"])}</a> — {html.escape(item["creator"])}. <a href="{item["license_url"]}">{item["license"]}</a>. Resized and compressed for this site.</li>' for item in credits)
    (ROOT / "photo-credits.html").write_text(document("Photo credits", f'<section class="page-hero"><p class="eyebrow">Behind the photographs</p><h1>Photo credits</h1><p>Photographs and illustrations used in our lessons.</p></section><section><h2>Daily news illustrations</h2><p>The featured daily image is generated with Google Gemini for that lesson and labeled as an AI-generated illustration. It illustrates the topic and does not document the reported event. Each image is saved with its generation details.</p></section><section><h2>Evergreen story photographs</h2><ul>{items}</ul></section>'), encoding="utf-8")


def build_stories():
    from datetime import datetime, timezone
    from story_lessons import STORIES
    from update_site import LEVELS, render_lesson_html, render_lesson_title, validate_lesson_data
    credits = {item["key"]: item for item in json.loads((ROOT / "assets/editorial/credits.json").read_text())}
    for story in STORIES:
        for level in LEVELS:
            name = level["name"].lower()
            data = story["levels"][name]
            config = dict(level, min_sentence_count=6, min_vocabulary_count=3, min_quiz_count=5)
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
            content = f'<section class="page-hero"><p class="eyebrow">{story["category"]} · 5-minute lesson</p><h1>{render_lesson_title(data["title"])}</h1><p>{html.escape(data["overview"])}</p><span class="level-badge">{badge}</span>{level_links(name, story["slug"])}</section>{lesson}'
            path = ROOT / "stories" / story["slug"] / f"{name}.html"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(document(data["title"], content, f'theme-{name} story-page', "../../"), encoding="utf-8")


def publish_editorial_pages():
    build_homepage()
    build_stories()
    build_credits()
    from site_quality import publish_quality_pages
    publish_quality_pages()
    from seo import build_category_pages, build_html_sitemap, write_sitemaps
    build_category_pages();build_html_sitemap()
    for path in [*ROOT.glob("*.html"), *ROOT.glob("grammar-concepts/*.html"), *ROOT.glob("stories/*/*.html")]:
        decorate_page(path)
    write_sitemaps()


if __name__ == "__main__":
    publish_editorial_pages()
