"""Topic-specific presentation and speaking practice for the two evergreen stories.

Applied after the shared reading/SEO decorators, which intentionally compact news
pages. No learner data, network calls, or JavaScript are needed by this layer.
"""
from html import escape as e
from pathlib import Path

from bs4 import BeautifulSoup
from story_lessons import STORIES

VERSION = "20261118-evergreen1"
LEVELS = ("beginner", "intermediate", "advanced")
STORY_DATA = {story["slug"]: story for story in STORIES}
TOPICS = {
    "food-market": {
        "label": "Food & conversation", "color": "market", "other": "city-trees",
        "promise": "Ask the price. Find the words. Keep the conversation going.",
        "preview": "“Could I have half a kilo, please?”",
        "action": "Step into the market",
        "return": "Without looking, ask a price, make a polite request, and ask someone to explain an amount.",
    },
    "city-trees": {
        "label": "Nature & city life", "color": "trees", "other": "food-market",
        "promise": "Discover how trees help a city, then make the case for a greener street.",
        "preview": "A little shade. A better place to live.",
        "action": "Explore a greener city",
        "return": "Without looking, explain how trees cool a place and why they need care after planting.",
    },
}

# Activities progress from a supported sentence to a conversation to independent
# use. Examples are optional, illustrative answers, never automatic grading.
PRACTICE = {
    ("food-market", "beginner"): {
        "goal": "Ask a price and buy the amount you need, politely.",
        "focus": "Notice the two questions Mina uses: one asks the price; the other asks for food.",
        "phrase": "Could I have …, please?",
        "phrase_note": "Use this to ask for something politely.",
        "activities": [
            ("Make one useful request", "Choose apples, bread, or tomatoes. Ask for an amount. Say your sentence aloud.", "Could I have ___, please?", "Could I have two apples, please?"),
            ("Play both parts", "One person sells apples for two dollars each. The other buys two apples. Ask the price, make a request, and say thank you. Then swap roles.", "How much are these apples? / Could I have two, please?", None),
            ("Make it your own", "Choose a food you like. Say what you want to buy and how much you need. Then ask for it without reading the example.", "I want ___. I need ___. Could I have ___, please?", None),
        ],
    },
    ("food-market", "intermediate"): {
        "goal": "Ask for clarification and keep a shopping conversation moving.",
        "focus": "Notice what Mina does when she understands the words but cannot picture the amount.",
        "phrase": "Could you show me what that looks like?",
        "phrase_note": "Ask for a demonstration when an amount is hard to imagine.",
        "activities": [
            ("Make the purpose clear", "Explain why Mina asks for help. Use so that to connect the action and its purpose.", "She asks ___ so that ___.", "She asks the vendor to show her the tomatoes so that she can understand the quantity."),
            ("Keep the conversation going", "You need fruit for a picnic for four people. Your partner suggests an amount you cannot picture. Ask for clarification, agree on an amount, and swap roles.", "Could you show me…? / Do you mean…? / That looks about right.", None),
            ("Use it somewhere else", "Imagine you do not understand a recipe instruction. Ask a useful follow-up question and explain why you need the answer.", "Could you explain ___ so that I can ___?", "Could you explain how small to cut the pieces so that I can prepare them correctly?"),
        ],
    },
    ("food-market", "advanced"): {
        "goal": "Clarify uncertainty tactfully and adapt your wording to the situation.",
        "focus": "Look for the difference between repeating a measurement and making its meaning clear.",
        "phrase": "Could you give me a concrete example?",
        "phrase_note": "Turn an abstract explanation into something you can picture.",
        "activities": [
            ("Explain the method", "Explain how the vendor makes an abstract quantity tangible. Use by + -ing, then paraphrase your sentence for a less fluent listener.", "By ___, the vendor ___.", "By demonstrating the quantity on the scale, the vendor makes the measurement tangible. More simply: he shows Mina the amount so she can picture it."),
            ("Change the setting", "First, ask a vendor to clarify an amount. Then ask a colleague to clarify an unfamiliar project estimate. Keep both requests respectful; explain how the wording changes.", "At the stall: “Could you show me…?” / At work: “Could you walk me through…?”", None),
            ("Test the conclusion", "A friend says, “Polite questions always prevent misunderstandings.” Use this scenario to give a more careful claim, then suggest a situation in which clarification might still be needed.", "This exchange suggests…; it does not establish that…", "This exchange suggests that a polite request can support mutual understanding; it does not establish that every request will succeed."),
        ],
    },
    ("city-trees", "beginner"): {
        "goal": "Explain how trees help and suggest a place that needs shade.",
        "focus": "Find two ways trees help cool a place. Then notice what young trees need.",
        "phrase": "Trees can help …",
        "phrase_note": "Use can + a verb to say what is possible.",
        "activities": [
            ("Say what a tree can do", "Use can to say two things trees do. Check your ideas against the story.", "Trees can ___. They can also ___.", "Trees can give people shade. They can also help cool the air."),
            ("Choose a shady place", "Imagine a school playground and a bus stop with no shade. Choose one place for more trees. Tell a partner why. Your partner chooses a place too.", "I choose ___. People can ___ there.", None),
            ("Remember the care", "Your friend wants to plant a tree. Tell your friend two things from the story to remember.", "Choose a tree that ___. Young trees need ___.", "Choose a tree that suits the local climate. Young trees need care."),
        ],
    },
    ("city-trees", "intermediate"): {
        "goal": "Explain the benefits of trees and recommend a practical planting plan.",
        "focus": "Separate the benefits of planting trees from the work needed to keep them healthy.",
        "phrase": "Trees provide shade, while …",
        "phrase_note": "Use while to connect two different actions in the same situation.",
        "activities": [
            ("Connect the benefits", "Explain the two cooling effects in one sentence using while. Then explain why a nearby building might need less air conditioning.", "Trees provide shade, while ___.", "Trees provide shade, while water released through their leaves helps cool the air."),
            ("Make a neighborhood choice", "Your neighborhood can improve either an exposed bus stop or a busy walking route. Recommend one. Give a reason, name one thing to check before planting, and describe the follow-up care.", "I recommend… because… / We should check… / After planting…", None),
            ("Respond to a shortcut", "A neighbor says, “Let’s buy the cheapest trees and leave them to grow.” Reply politely, using maintenance and one other word from the lesson.", "That could help, but we also need to consider…", "That could help, but we also need to consider whether the trees suit the climate and who will provide maintenance."),
        ],
    },
    ("city-trees", "advanced"): {
        "goal": "Evaluate a planting proposal and distinguish an attractive claim from lasting success.",
        "focus": "Track the writer’s shift from immediate benefits to the responsibility of long-term care.",
        "phrase": "A project evaluated solely by … may …",
        "phrase_note": "Use a shortened passive clause to specify how a project is judged.",
        "activities": [
            ("Question the measure", "Complete the sentence with an appropriate measure and limitation. Expand evaluated into a full relative clause, keeping the meaning.", "A project evaluated solely by ___ may ___.", "A project evaluated solely by planting numbers may overlook survival. Expanded: a project that is evaluated solely by planting numbers…"),
            ("Make the five-year case", "In a fictional council meeting, a colleague wants a large planting announcement. Propose two measures to check five years later and explain why each matters. Use stewardship and sustained.", "Planting numbers tell us…; to assess lasting success, we would also need…", None),
            ("Qualify the promise", "Respond to “Plant more trees and every street will be cooler.” State what the passage supports, what depends on local conditions, and one piece of evidence you would seek.", "The passage supports…; the outcome may depend on…; I would investigate…", "The passage supports cooling through shade and water release. Local results may depend on suitable trees and ongoing care; I would investigate tree survival and local temperature changes."),
        ],
    },
}


def fragment(markup):
    return BeautifulSoup(markup, "html.parser")


def explore_section():
    cards = []
    for slug in ("food-market", "city-trees"):
        topic = TOPICS[slug]
        title = STORY_DATA[slug]["levels"]["beginner"]["title"]
        alt = ("Shoppers and colorful fruit stalls at an indoor market." if slug == "food-market"
               else "A tree-filled urban park surrounded by city buildings.")
        width, height = (1000, 692) if slug == "food-market" else (1600, 1199)
        cards.append(f'''<a class="explore-story evergreen-card evergreen-{topic['color']}" data-level-link data-completion-story="stories/{slug}" href="stories/{slug}/beginner.html">
<div class="evergreen-card-image"><img src="assets/editorial/{slug}.webp" width="{width}" height="{height}" alt="{alt}" loading="lazy" decoding="async"></div>
<div class="evergreen-card-copy"><span class="eyebrow">{e(topic['label'])}</span><h3><span class="lesson-title-text">{e(title)}</span></h3><p>{e(topic['promise'])}</p><p class="evergreen-card-preview">{e(topic['preview'])}</p><div class="evergreen-card-footer"><span>3 levels · About 10–15 min</span><span class="text-link">{e(topic['action'])} <span aria-hidden="true">→</span></span></div></div></a>''')
    return ('<section class="evergreen-explore" aria-labelledby="explore-heading">'
            '<div class="section-heading"><div><p class="eyebrow">Small lessons. Everyday confidence.</p>'
            '<h2 id="explore-heading">English beyond the headlines</h2></div>'
            '<p>Read a little. Say something new.</p></div><div class="explore-grid">'
            + ''.join(cards) + '</div></section>')


def enhance_page(soup, relative, prefix=""):
    """Idempotent final pass; preserve quizzes, translations, metadata and controls."""
    relative = Path(relative)
    if relative.as_posix() == "index.html":
        heading = soup.find(id="explore-heading")
        if not heading:
            return
        heading.find_parent("section").replace_with(fragment(explore_section()).section)
    elif len(relative.parts) == 3 and relative.parts[0] == "stories" and (relative.parts[1], relative.stem) in PRACTICE:
        enhance_story(soup, relative.parts[1], relative.stem, prefix)
    else:
        return
    for old in soup.select('link[href*="evergreen.css"]'):
        old.decompose()
    soup.head.append(soup.new_tag("link", rel="stylesheet", href=f"{prefix}evergreen.css?v={VERSION}"))


def enhance_story(soup, slug, level, prefix):
    topic, practice = TOPICS[slug], PRACTICE[slug, level]
    lesson_data = STORY_DATA[slug]["levels"][level]
    hero, lesson = soup.select_one(".page-hero"), soup.select_one(".daily-lesson")
    if hero is None or lesson is None:
        return
    soup.body["class"] = list(dict.fromkeys([*soup.body.get("class", []), "evergreen-page", f"evergreen-{topic['color']}"]))
    photo = soup.select_one(".lesson-cover, .reading-photo, .evergreen-photo")
    if photo:
        photo.extract()
        photo["class"] = ["evergreen-photo"]
        photo.img["loading"] = "eager"
        photo.img["fetchpriority"] = "high"
    hero.clear()
    hero["class"] = ["page-hero", "reading-heading", "evergreen-hero"]
    badge = {"beginner": "A1–A2", "intermediate": "B1–B2", "advanced": "C1+"}[level]
    hero.append(fragment(f'''<div class="evergreen-hero-copy"><a class="evergreen-back" href="{prefix}index.html#explore-heading">← English beyond the headlines</a>
<p class="eyebrow">{e(topic['label'])}</p><h1><span class="lesson-title-text">{e(lesson_data['title'])}</span></h1>
<p class="evergreen-goal">{e(practice['goal'])}</p><p class="evergreen-meta">{level.title()} · {badge} <span aria-hidden="true">/</span> About 10–15 min</p>
<a class="evergreen-start" href="#lesson-{slug}">Read the story <span aria-hidden="true">↓</span></a>
<p class="evergreen-steps">3 useful words · 5 questions · Your turn to speak</p></div>''').div)
    if photo:
        hero.append(photo)
    read = lesson.select_one('[data-stage="read"]')
    for old in lesson.select(".evergreen-focus, .evergreen-phrase, .evergreen-practice-intro"):
        old.decompose()
    story_section = read.select_one(".section")
    story_section.h2.insert_after(fragment(f'<aside class="evergreen-focus" aria-label="As you read">{e(practice["focus"])}</aside>').aside)
    phrase = fragment(f'<aside class="evergreen-phrase" aria-label="A phrase to take with you"><p class="eyebrow">A phrase to take with you</p><blockquote>{e(practice["phrase"])}</blockquote><p>{e(practice["phrase_note"])}</p></aside>').aside
    words = read.select(".section")[-1]
    words.insert_after(phrase)
    quiz_panel = lesson.select_one('[data-stage="practice"]')
    quiz_panel.select_one("h2").insert_after(fragment('<p class="evergreen-practice-intro">Try all five questions. Read the feedback, then try again if you need to. Your score is practice, not a test result.</p>').p)
    activities = []
    for title, instruction, support, example in practice["activities"]:
        model = (f'<details class="evergreen-example"><summary>See an example</summary><p>{e(example)}</p></details>' if example else '')
        activities.append(f'<li><h3>{e(title)}</h3><p>{e(instruction)}</p><p class="discussion-support">{e(support)}</p>{model}</li>')
    discussion = lesson.select_one(".discussion")
    discussion.replace_with(fragment('<section class="discussion evergreen-discussion"><p class="eyebrow">Make the English yours</p><h2>Your turn to speak</h2><p>Try these three short activities with a partner, or say both parts aloud on your own. Start with the sentence help; then try without it.</p><ol class="discussion-activities">' + ''.join(activities) + '<li class="evergreen-recall"><h3>One last try, from memory</h3><p>' + e(practice['goal']) + ' Close the examples and say your answer aloud.</p></li></ol><p class="completion-message" role="status" hidden>Lesson complete. You have read, practiced, and spoken.</p></section>').section)
    # Keep recommendations visible without requiring a completion click. Link to
    # the companion story at the current level, and offer a clear next challenge.
    other = topic["other"]
    other_title = STORY_DATA[other]["levels"][level]["title"]
    if level != "advanced":
        next_level = LEVELS[LEVELS.index(level) + 1]
        next_url, next_label = f"{next_level}.html", f"Try the {next_level.title()} version"
        next_note = PRACTICE[slug, next_level]["goal"]
    else:
        next_url, next_label = f"{prefix}advanced.html", "Use your English with today’s news"
        next_note = "Meet a new topic and put the same reading and speaking skills to work."
    for old in soup.select("[data-seo-related], .evergreen-next"):
        old.decompose()
    followup = fragment(f'''<section class="evergreen-next" aria-labelledby="evergreen-next-heading"><p class="eyebrow">Keep your English moving</p><h2 id="evergreen-next-heading">What will you try next?</h2><div class="evergreen-next-grid">
<a href="../{other}/{level}.html"><span>Another everyday topic · {level.title()}</span><h3>{e(other_title)} <span aria-hidden="true">→</span></h3><p>{e(PRACTICE[other, level]['goal'])}</p></a>
<a href="{next_url}"><span>A new challenge</span><h3>{e(next_label)} <span aria-hidden="true">→</span></h3><p>{e(next_note)}</p></a></div><p class="evergreen-return"><strong>Next time, start from memory.</strong> {e(topic['return'])} Then come back and check.</p></section>''').section
    lesson.insert_after(followup)
