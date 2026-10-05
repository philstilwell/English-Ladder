"""Publish authored English for Work lessons. Offline; no paid service calls.

Run generate_work_documents.py first after curriculum changes, then this file.
"""
import html
import json
from bs4 import BeautifulSoup
from editorial import document
from work_curriculum import ROOT, REVISION, RUBRIC, load_tracks, related_tracks, validate_tracks
from work_ai_prompts import web_section, url as ai_url
from work_ready_prompts import lesson_prompts, dialogue_prompts, write_prompt_packs
from work_icons import card_icon
from work_lesson_conversations import render_activities, load_course
from work_books import validate_publication


def e(value):
    return html.escape(str(value), quote=True)


def ul(items):
    return '<ul>' + ''.join(f'<li>{e(i)}</li>' for i in items) + '</ul>'


def all_tracks():
    return load_tracks()


def page(title, content, current):
    body_class = 'theme-efsp work-page' + (' work-directory-page' if current == 'efsp.html' else '')
    result = document(title, content, body_class=body_class, current=current)
    result = result.replace('Learn English with real stories. Read, practice, and discuss at your level.',
                            e(f'Practice {title} with realistic workplace conversations, guided language checks, clear vocabulary, and a complete printable learner book.'))
    return result.replace('</head>', '<link rel="stylesheet" href="work.css?v=20260905"><script defer src="work.js?v=20260905"></script><link rel="stylesheet" href="work-ai.css?v=20260930-prompt-spacing1"><script defer src="work-ai.js?v=20260906-ai1"></script><script defer src="work-ready.js?v=20260906-ready2"></script></head>')


def pdf_metadata(track):
    path = ROOT / 'content/work/documents.json'
    href = track['pdfs'][0][1]
    meta = json.loads(path.read_text())['documents'][href]
    return f"{href}?v={meta['sha256'][:12]}", meta


def pdf_links(track):
    href, meta = pdf_metadata(track)
    size = f"{meta['bytes'] / 1024:.0f} KB"
    return f'''<div class="work-book-download"><div><p class="work-kicker">PDF · {meta['pages']} pages · {size}</p><h3>{e(track['title'])}</h3><p id="learner-book-description">Follow the course's eight lessons with {meta['dialogue_count']} extended, 20-turn cloze conversations, {meta['vocabulary_entries']} vocabulary entries and collocations, and {meta['phrase_count']} reusable phrases. Includes word banks, structured practice, and complete answer keys with explanations and page references.</p></div><a class="work-button work-download" href="{e(href)}" aria-describedby="learner-book-description">Open learner book (PDF) <span aria-hidden="true">↗</span></a></div>'''


def render_quiz(m, q, number):
    name = f'{m["id"]}-q{number}'
    prompt = e(q['prompt']).replace('\n', '<br>')
    choices = ''.join(f'<label><input type="radio" name="{name}" value="{i}"><span>{e(option)}</span></label>' for i, option in enumerate(q['options']))
    reasons = ''.join(f'<li><strong>{chr(65+i)}. {e(option)}</strong> {e(q["feedback"][i])}</li>' for i, option in enumerate(q['options']))
    return f'''<div class="work-quiz" data-work-quiz data-correct="{q['correct_index']}">
<fieldset><legend>{number}. {prompt}</legend>{choices}</fieldset>
<button type="button" class="work-button work-check" data-check-answer hidden>Check answer</button>
<p class="work-feedback" data-quiz-feedback role="status" aria-live="polite"></p>
<details class="work-answer"><summary>Answer and explanations</summary><p><strong>Answer: {chr(65+q['correct_index'])}.</strong> {e(q['answer'])}</p><ol class="work-answer-reasons">{reasons}</ol></details></div>'''


def render_module(track, m):
    w = m['workshop']
    vocab = ''.join(f'<div><dt>{e(j["term"])}</dt><dd>{e(j["definition"])}</dd></div>' for j in m['vocabulary'])
    collocations = ('<h4>Useful word combinations</h4>' + ul(m['collocations'])) if m.get('collocations') else ''
    transfer_verb = 'Say' if track.get('is_occupation') else 'Draft'
    quiz = ''.join(render_quiz(m, q, i+1) for i, q in enumerate(w['questions']))
    checklist = ul([criterion for _name, criterion in RUBRIC])
    ai_links = ''.join(f'<a data-ai-preset href="{e(ai_url(track, mode, m["id"]))}">{label}</a>' for mode, label in [('vocabulary', 'Extend the vocabulary'), ('grammar', 'Practice the grammar'), ('roleplay', 'Rehearse with AI')])
    return f'''<details class="work-module" id="{m['id']}" {'open' if m['number']==1 else ''}>
<summary><span class="work-module-number">{m['number']:02d}</span><span><strong>{e(m['title'])}</strong><small>{e(w['title'])} · 45-60 minutes</small></span><span class="work-expand" aria-hidden="true">+</span></summary>
<div class="work-module-body"><div class="work-lesson-heading"><p class="work-kicker">Your goal</p><h3>{e(w['goal'])}</h3></div>
<div class="work-two-column"><section class="work-case"><p class="work-kicker work-activity-heading"><span class="work-activity-letter">A</span> <span>Read the situation</span></p><h4>A moment at work</h4><p>{e(m['brief'])}</p><p class="work-prompt">Before you look at the model: what is confirmed, what is missing, and who needs a response?</p></section>
<section><p class="work-kicker work-activity-heading"><span class="work-activity-letter">B</span> <span>Find the words</span></p><h4>Vocabulary for this lesson</h4><dl class="work-vocabulary compact">{vocab}</dl>{collocations}</section></div>
<section class="work-language"><p class="work-kicker work-activity-heading"><span class="work-activity-letter">C</span> <span>Notice the language</span></p><h4>{e(w['title'])}</h4><p>{e(w['explanation'])}</p>{ul(w['frames'])}<div class="work-edit"><p><strong>Improve this:</strong> &quot;{e(w['before'])}&quot;</p><details><summary>See a clearer version</summary><p><strong>{e(w['after'])}</strong></p><p>{e(w['reason'])}</p></details></div></section>
<section class="work-checks"><p class="work-kicker work-activity-heading"><span class="work-activity-letter">D</span> <span>Check your understanding</span></p><h4>Two short language checks</h4><p>These language patterns recur across courses so you can retrieve and reuse them.</p><div class="work-two-column">{quiz}</div></section>
{render_activities(track, m)}
<details class="work-model"><summary>Compare scenario 1 with a model response</summary><blockquote>{e(m['model'])}</blockquote><p>This is one possible spoken response, not the only acceptable wording. Preserve the case facts when you try your own version.</p><p><strong>Notice:</strong> {e(w['goal'])} Identify the wording that does this, then name one detail from the case that the response preserves.</p></details>
<section class="work-case-transfer"><h4>Apply it to this case</h4><p>In “{e(m['title'])}”, choose one confirmed detail from the situation and one item that still needs clarification. {transfer_verb} a two-sentence response using “{e(w['frames'][0])}”. Keep the known detail accurate and ask about the missing one.</p><details><summary>Check your reasoning</summary><p>Compare with the case above and the model response. Can you point to the words that support your factual statement? Is your question about something the case leaves open? If you introduce a possible outcome, clearly label it as a possibility.</p></details></section>
<section class="work-reflect"><h4>Review, then try again</h4>{checklist}<p>Revise one sentence and repeat the response. A useful response can be clear even with a few grammar errors; judge meaning and task completion, not accent.</p></section>
<aside class="work-ai-invitation"><h4>Ready for another round?</h4><p>Choose an AI extension using this lesson's actual case and language.</p><nav aria-label="AI extensions for lesson {m['number']}">{ai_links}</nav></aside>
{lesson_prompts(track, m)}
</div></details>'''


def render_industry_page(t, tracks):
    book_url, _ = pdf_metadata(t)
    modules = ''.join(render_module(t, m) for m in t['modules'])
    jump = ''.join(f'<a href="#{m["id"]}" title="{e(m["title"])}">{m["number"]:02d}<span class="sr-only"> {e(m["title"])}</span></a>' for m in t['modules'])
    glossary = ''.join(f'<div data-work-term><dt>{e(j["term"])}</dt><dd>{e(j["definition"])}</dd></div>' for j in sorted(t['jargon'], key=lambda j:j['term'].casefold()))
    related = ''.join(f'<a href="efsp-{r["slug"]}.html">{e(r["title"])} <span aria-hidden="true">↗</span></a>' for r in related_tracks(t, tracks))
    extra = ''
    if t.get('nomenclature'):
        terms = ''.join(f'<div><dt>{e(n["term"])} <small>({e(n["category"])})</small></dt><dd>{e(n["meaning"])}</dd></div>' for n in t['nomenclature'])
        extra = f'<section class="work-section"><h2>More specialist terminology</h2><dl class="work-vocabulary work-glossary">{terms}</dl></section>'
    sources = ''.join(f'<li><a href="{e(s["url"])}">{e(s["title"])}</a></li>' for s in t['sources'])
    final_response = ('repeat the conversation with your partner taking the other role' if t.get('is_occupation')
                      else 'write a 70-110 word message')
    first_attempt = 'first attempt' if t.get('is_occupation') else 'first draft'
    content = f'''<div data-work-course="{e(t['slug'])}">
<nav class="work-breadcrumb" aria-label="Breadcrumb"><a href="efsp.html">English for Work</a><span aria-hidden="true">/</span><span>{e(t['category'])}</span></nav>
<section class="work-hero"><div>{card_icon(t)}<p class="work-kicker">English for Work · {e(t['category'])}</p><h1>{e(t['title'])}</h1><p class="work-intro">{e(t['summary'])}</p><div class="work-meta"><span>8 practical lessons</span><span>Intermediate to advanced</span><span>1 complete learner book</span></div><a class="work-button" href="#lessons">Start practicing <span aria-hidden="true">→</span></a></div>
<aside class="work-study-card"><p class="work-kicker">Words into action</p><p class="work-study-phrase">Read the situation.<br>Find your words.<br>Make yourself clear.</p><p>For {e(t['roles']).rstrip('.')}.</p><a href="{e(book_url)}">Open learner book (PDF) ↗</a><p><a href="#finished-dialogue-prompts">Copy complete AI prompts ↓</a></p></aside></section>
<details class="work-orientation"><summary>What you will practice · Choose your pace</summary><div class="work-two-column"><div><h2>What you will practice</h2>{ul(t['outcomes'][:5])}</div><div><h2>Choose your pace</h2><p><strong>Quick practice · 15 minutes:</strong> read one conversation, study its useful expressions, and rehearse one scenario aloud.</p><p><strong>Full lesson · 45-60 minutes:</strong> complete the language checks, compare three conversations, and practice both speaking scenarios with feedback.</p><p><strong>Level guide:</strong> designed for intermediate to advanced learners. B1 learners can use the sentence frames; B2 learners can work independently; C1 learners can try the harder second round. These are teaching suggestions, not a certified level assessment.</p></div></div></details>
<section id="downloads" class="work-section"><div class="work-section-heading"><div><p class="work-kicker">Take the lesson with you</p><h2>Your complete learner book</h2></div><span>October 2026 edition</span></div><div class="work-downloads">{pdf_links(t)}</div></section>
<div id="lessons" class="work-section"><div class="work-section-heading"><div><p class="work-kicker">Practice, reflect, repeat</p><h2>Your eight lessons</h2></div><a class="work-book-inline" href="{e(book_url)}">Open the learner book (PDF) ↗</a></div></div><div class="work-lesson-tools"><span class="work-lesson-icon" aria-hidden="true">{card_icon(t)}</span><nav class="work-jump" aria-label="Jump to lesson or prompts"><div class="work-lesson-links">{jump}</div><a class="work-prompts-link" href="#finished-dialogue-prompts">Prompts</a></nav></div><button type="button" class="work-text-button" data-expand-lessons hidden>Open all lessons</button><p class="work-scope">{e(t['scope_note'])}</p>
{modules}
<section class="work-section work-capstone"><p class="work-kicker">Put it together</p><h2>Your final workplace challenge</h2><p>Choose a case you have not rehearsed today. Give a one-minute response, answer two follow-up questions, then {final_response}. Have your partner introduce the harder second-round challenge. Review the four criteria used in the lessons and repeat the part that needs improvement.</p><p><strong>Compare your progress:</strong> return to your {first_attempt}. Identify one improvement in clarity, one in accuracy, and one in how you ask for or explain the next step.</p></section>
<details id="vocabulary" class="work-section work-glossary-disclosure"><summary>Explore your field vocabulary</summary><div class="work-section-heading"><div><p class="work-kicker">Keep the meaning close</p><h2>Your field vocabulary</h2></div><label data-vocabulary-filter hidden>Find a term<input type="search" data-vocabulary-search placeholder="Search words and meanings"></label></div><p data-vocabulary-count role="status">{len(t['jargon'])} terms</p><dl class="work-vocabulary work-glossary">{glossary}</dl></details>
{extra}{dialogue_prompts(t)}{web_section(t)}<section class="work-section work-two-column"><div><h2>For teachers and study partners</h2><p>Ask learners to respond before revealing the model. Give feedback on one meaning issue and one language pattern, then let them repeat. For mixed levels, offer the frames first and remove them in the second round.</p><p>Use the learner book for extended dialogue practice, vocabulary and collocations, reusable phrases, and explained answer keys.</p></div><div><h2>Language notes and further reading</h2><p>The cases and explanations are original teaching material. The references provide language frameworks and selected professional context; use current local guidance for actual work.</p><ul class="work-sources">{sources}</ul><p class="work-small">Course edition: {t['revision']}.</p></div></section>
<section class="work-section"><p class="work-kicker">Continue in your field</p><h2>Related courses</h2><div class="work-related">{related}</div></section></div>'''
    soup = BeautifulSoup(page(t['title'], content, f'efsp-{t["slug"]}.html'), 'html.parser')
    course = soup.select_one('[data-work-course]')
    # The main element includes the prompts and footer, keeping the menu sticky to the end.
    soup.main['data-work-course'] = course['data-work-course']
    course.unwrap()
    return str(soup)


def render_directory(tracks):
    options = ''.join(f'<option>{e(g)}</option>' for g in sorted({t['category'] for t in tracks}))
    cards = ''.join(f'''<a class="work-course-card" href="efsp-{e(t['slug'])}.html" data-work-course-link data-category="{e(t['category'])}" data-search="{e(t['title']+' '+t['summary']+' '+t['roles']+' '+' '.join(m['title'] for m in t['modules']))}">{card_icon(t)}<span class="work-kicker">{e(t['category'])}</span><h3>{e(t['title'])}</h3><p>{e(t['summary'])}</p><span class="work-card-footer">8 lessons · 1 learner book <span aria-hidden="true">↗</span></span></a>''' for t in tracks)
    content = f'''<section class="page-hero work-directory-hero"><div class="work-directory-copy"><p class="work-kicker">English for Work</p><h1>Good work.<br>Clearly expressed.</h1><p class="work-intro">Find the words for the work you do. Practice real conversations, choose clear messages, and build confidence one situation at a time.</p><div class="work-meta"><span>{len(tracks)} fields and occupations</span><span>{sum(len(t['modules']) for t in tracks)} practical lessons</span><span>{len(tracks)} complete learner books</span></div><a class="work-button" href="#courses">Browse all {len(tracks)} courses <span aria-hidden="true">↓</span></a></div><img class="work-directory-collage" src="assets/work/industry-collage-66.webp" width="1196" height="1315" alt="Illustrated tools and people representing all 66 professional fields and occupations." fetchpriority="high" decoding="async"></section>
<section class="work-start-paths"><article><span class="work-kicker">On your own</span><h2>Make fifteen minutes count.</h2><p>Choose a case, try a spoken response, and compare it with the model. Add another conversation and a second attempt when you have more time.</p></article><article><span class="work-kicker">With a class or partner</span><h2>Turn practice into a conversation.</h2><p>Read the web conversations together and switch roles. Use the learner book for extended conversations and word-bank gaps. Every course includes one complete learner book with explained answers.</p></article></section>
<section id="courses" class="work-section" data-work-directory><div class="work-section-heading"><div><p class="work-kicker">Find your field</p><h2>What do you do?</h2></div><p data-course-count role="status">{len(tracks)} courses</p></div><div class="work-directory-filters" hidden><label>Search by role, topic, or industry<input type="search" data-course-search placeholder="Try nursing, carpentry, or customer support"></label><label>Browse a field<select data-course-category><option value="">All fields</option>{options}</select></label></div><button type="button" class="work-text-button work-filter-reset" data-course-reset hidden>Clear filters</button><p class="work-empty" data-course-empty hidden>No courses match. Try a broader word or choose all fields.</p><div class="work-course-grid">{cards}</div></section>
<section class="work-section work-two-column"><div><h2>Know what you are practicing.</h2><p>Every lesson combines an original case, relevant vocabulary, a language workshop, short checks with explanations, conversations, and supported speaking. Repeated language patterns help you recall useful expressions in a new context.</p><p><strong>Keep practicing with your preferred AI.</strong> Every course includes ready-to-copy prompts for vocabulary, grammar, role-play, and new dialogues. The complete text appears beneath each lesson and in the dialogue prompt library. Copy it as written, or download the full course prompt collection. No prompt-writing is required. The printable learner books provide extended conversations, vocabulary, phrases, and explained practice; the complete AI prompts remain available here on the website.</p></div><div><h2>Choose the right starting point.</h2><p>These courses suit intermediate to advanced learners. Use the sentence frames for support or add the harder follow-up challenge. For foundational practice, start with <a href="grammar-concepts.html">the grammar guides</a> and <a href="beginner.html">daily reading</a>.</p></div></section>'''
    from seo_content import CATEGORIES
    fields = '<nav class="seo-category-links" aria-label="Professional English fields">' + ''.join(f'<a href="english-for-work/{c["slug"]}.html">{e(c["title"])}</a>' for c in CATEGORIES.values()) + '</nav>'
    content = content.replace('<section id="courses" class="work-section" data-work-directory>', '<section class="work-section"><h2>Explore your professional field</h2>' + fields + '</section><section id="courses" class="work-section" data-work-directory>')
    return page('English for Work', content, 'efsp.html')


def main():
    tracks = all_tracks()
    print(validate_tracks(tracks))
    for track in tracks:
        load_course(track['slug'])
    validate_publication(tracks)
    print('Published complete prompts:', write_prompt_packs(tracks))
    (ROOT / 'efsp.html').write_text(render_directory(tracks))
    for t in tracks:
        (ROOT / f'efsp-{t["slug"]}.html').write_text(render_industry_page(t, tracks))
    # Keep the shared navigation, metadata and asset versions
    # when this generator is run independently of the full editorial build.
    from editorial import decorate_page
    for path in [ROOT / 'efsp.html', *[ROOT / f'efsp-{t["slug"]}.html' for t in tracks]]:
        decorate_page(path)
    from seo import build_category_pages, build_html_sitemap, write_sitemaps
    build_category_pages();build_html_sitemap();write_sitemaps()
    print(f'Generated {len(tracks)} course pages and the directory.')


if __name__ == '__main__':
    main()
