"""Publish authored English for Work lessons. Offline; no paid service calls.

Run generate_work_documents.py first after curriculum changes, then this file.
"""
import html
import json
from editorial import document
from work_curriculum import ROOT, REVISION, RUBRIC, load_tracks, related_tracks, validate_tracks
from work_ai_prompts import web_section, url as ai_url
from work_ready_prompts import lesson_prompts, dialogue_prompts, write_prompt_packs
from work_icons import card_icon


def e(value):
    return html.escape(str(value), quote=True)


def ul(items):
    return '<ul>' + ''.join(f'<li>{e(i)}</li>' for i in items) + '</ul>'


def all_tracks():
    return load_tracks()


def page(title, content, current):
    result = document(title, content, body_class='theme-efsp work-page', current=current)
    result = result.replace('Learn English with real stories. Read, practice, and discuss at your level.',
                            e(f'Practice {title} with realistic workplace cases, speaking, writing, clear vocabulary, and printable teaching guides.'))
    return result.replace('</head>', '<link rel="stylesheet" href="work.css?v=20260905"><script defer src="work.js?v=20260905"></script><link rel="stylesheet" href="work-ai.css?v=20260906-ready2"><script defer src="work-ai.js?v=20260906-ai1"></script><script defer src="work-ready.js?v=20260906-ready2"></script></head>')


def pdf_links(track):
    path = ROOT / 'content/work/documents.json'
    manifest = json.loads(path.read_text()).get('documents', {}) if path.exists() else {}
    labels = ["Teacher's guide", 'Learner workbook', 'Conversation lab', 'Vocabulary & phrasebook']
    descriptions = ['Timed lesson plans, coaching notes, and assessment criteria.',
                    'Cases, practice, writing space, and a separate answer section.',
                    'Partner roles, follow-up questions, and repeat-practice challenges.',
                    'Clear definitions, reusable expressions, and model responses.']
    cards = []
    for i, (_old, href) in enumerate(track['pdfs']):
        meta = manifest.get(href, {})
        size = f" · {meta['pages']} pages" if meta.get('pages') else ''
        version = meta.get('sha256', REVISION)[:12]
        description = descriptions[i]
        if i == 2 and meta.get('dialogue_count'):
            description = f"{meta['dialogue_count']} complete workplace dialogues, professional vocabulary, and eight additional role-play cases."
        if meta.get('ai_prompt_count'):
            description += ' Includes two AI extension prompts.'
        cards.append(f'<a class="work-download" href="{e(href)}?v={e(version)}"><span class="work-kicker">PDF{size}</span><strong>{labels[i]}</strong><span>{description}</span><span class="work-download-action">Open document ↗</span></a>')
    return ''.join(cards)


def render_quiz(m, q, number):
    name = f'{m["id"]}-q{number}'
    choices = ''.join(f'<label><input type="radio" name="{name}" value="{i}"><span>{e(option)}</span></label>' for i, option in enumerate(q['options']))
    reasons = ''.join(f'<li><strong>{chr(65+i)}. {e(option)}</strong> {e(q["feedback"][i])}</li>' for i, option in enumerate(q['options']))
    return f'''<div class="work-quiz" data-work-quiz data-correct="{q['correct_index']}">
<fieldset><legend>{number}. {e(q['prompt'])}</legend>{choices}</fieldset>
<button type="button" class="work-button work-check" data-check-answer hidden>Check answer</button>
<p class="work-feedback" data-quiz-feedback role="status" aria-live="polite"></p>
<details class="work-answer"><summary>Answer and explanations</summary><p><strong>Answer: {chr(65+q['correct_index'])}.</strong> {e(q['answer'])}</p><ol class="work-answer-reasons">{reasons}</ol></details></div>'''


def render_module(track, m):
    w = m['workshop']
    vocab = ''.join(f'<div><dt>{e(j["term"])}</dt><dd>{e(j["definition"])}</dd></div>' for j in m['vocabulary'])
    quiz = ''.join(render_quiz(m, q, i+1) for i, q in enumerate(w['questions']))
    checklist = ul([criterion for _name, criterion in RUBRIC])
    ai_links = ''.join(f'<a data-ai-preset href="{e(ai_url(track, mode, m["id"]))}">{label}</a>' for mode, label in [('vocabulary', 'Extend the vocabulary'), ('grammar', 'Practice the grammar'), ('roleplay', 'Rehearse with AI'), ('writing', 'Review your draft')])
    return f'''<details class="work-module" id="{m['id']}" {'open' if m['number']==1 else ''}>
<summary><span class="work-module-number">{m['number']:02d}</span><span><strong>{e(m['title'])}</strong><small>{e(w['title'])} · 45-60 minutes</small></span><span class="work-expand" aria-hidden="true">+</span></summary>
<div class="work-module-body"><div class="work-lesson-heading"><p class="work-kicker">Your goal</p><h3>{e(w['goal'])}</h3></div>
<div class="work-two-column"><section class="work-case"><p class="work-kicker">01 · Read the situation</p><h4>A moment at work</h4><p>{e(m['brief'])}</p><p class="work-prompt">Before you look at the model: what is confirmed, what is missing, and who needs a response?</p></section>
<section><p class="work-kicker">02 · Find the words</p><h4>Vocabulary for this lesson</h4><dl class="work-vocabulary compact">{vocab}</dl></section></div>
<section class="work-language"><p class="work-kicker">03 · Notice the language</p><h4>{e(w['title'])}</h4><p>{e(w['explanation'])}</p>{ul(w['frames'])}<div class="work-edit"><p><strong>Improve this:</strong> {e(w['before'])}</p><details><summary>See a clearer version</summary><p><strong>{e(w['after'])}</strong></p><p>{e(w['reason'])}</p></details></div></section>
<section class="work-checks"><p class="work-kicker">04 · Check your understanding</p><h4>Two short language checks</h4><p>These language patterns recur across courses so you can retrieve and reuse them.</p><div class="work-two-column">{quiz}</div></section>
<div class="work-two-column work-practice"><section><p class="work-kicker">05 · Say it</p><h4>Practice with a partner</h4><p>{e(m['speaking_task'])}</p><details><summary>Partner's role and follow-up</summary><p>{e(w['role_b'])}</p></details><details><summary>Try a harder second round</summary><p>{e(w['challenge'])}</p></details><p class="work-support"><strong>Studying alone?</strong> Give both sides of the conversation aloud. Pause before answering the follow-up, then repeat with fewer notes.</p></section>
<section><p class="work-kicker">06 · Write it</p><h4>A message someone can act on</h4><p>{e(m['writing_task'])}</p><label class="work-note-label" for="{m['id']}-note">Your draft</label><textarea id="{m['id']}-note" data-work-note="{m['id']}" rows="7" placeholder="Subject: ...&#10;Start with the purpose of your message."></textarea><p class="work-word-count" data-word-count>0 words · target 70-110</p></section></div>
<details class="work-model"><summary>Compare with a model response</summary><blockquote>{e(m['model'])}</blockquote><p>This is one possible spoken response, not the only acceptable wording. For your written version, add a subject line, opening, and relevant context without inventing facts.</p><p><strong>Notice:</strong> {e(w['goal'])} Underline the wording that does this. Then identify one detail from the case that the response preserves.</p></details>
<section class="work-case-transfer"><h4>Apply it to this case</h4><p>In “{e(m['title'])}”, choose one confirmed detail from the situation and one item that still needs clarification. Draft a two-sentence response using “{e(w['frames'][0])}”. Keep the known detail accurate and ask about the missing one.</p><details><summary>Check your reasoning</summary><p>Compare with the case above and the model response. Can you point to the words that support your factual statement? Is your question about something the case leaves open? If you introduce a possible outcome, clearly label it as a possibility.</p></details></section>
<section class="work-reflect"><h4>Review, then try again</h4>{checklist}<p>Revise one sentence and repeat the response. A useful response can be clear even with a few grammar errors; judge meaning and task completion, not accent.</p><label class="work-completion"><input type="checkbox" data-work-complete="{m['id']}"> I practiced, checked my response, and tried again.</label></section>
<aside class="work-ai-invitation"><h4>Ready for another round?</h4><p>Choose an AI extension using this lesson's actual case and language.</p><nav aria-label="AI extensions for lesson {m['number']}">{ai_links}</nav></aside>
{lesson_prompts(track, m)}
</div></details>'''


def render_industry_page(t, tracks):
    modules = ''.join(render_module(t, m) for m in t['modules'])
    jump = ''.join(f'<a href="#{m["id"]}" title="{e(m["title"])}">{m["number"]:02d}<span class="sr-only"> {e(m["title"])}</span></a>' for m in t['modules'])
    glossary = ''.join(f'<div data-work-term><dt>{e(j["term"])}</dt><dd>{e(j["definition"])}</dd></div>' for j in sorted(t['jargon'], key=lambda j:j['term'].casefold()))
    related = ''.join(f'<a href="efsp-{r["slug"]}.html">{e(r["title"])} <span aria-hidden="true">↗</span></a>' for r in related_tracks(t, tracks))
    extra = ''
    if t.get('nomenclature'):
        terms = ''.join(f'<div><dt>{e(n["term"])} <small>({e(n["category"])})</small></dt><dd>{e(n["meaning"])}</dd></div>' for n in t['nomenclature'])
        extra = f'<section class="work-section"><h2>More specialist terminology</h2><dl class="work-vocabulary work-glossary">{terms}</dl></section>'
    sources = ''.join(f'<li><a href="{e(s["url"])}">{e(s["title"])}</a></li>' for s in t['sources'])
    content = f'''<div data-work-course="{e(t['slug'])}">
<nav class="work-breadcrumb" aria-label="Breadcrumb"><a href="efsp.html">English for Work</a><span aria-hidden="true">/</span><span>{e(t['category'])}</span></nav>
<section class="work-hero"><div><p class="work-kicker">English for Work · {e(t['category'])}</p><h1>{e(t['title'])}</h1><p class="work-intro">{e(t['summary'])}</p><div class="work-meta"><span>8 practical lessons</span><span>Intermediate to advanced</span><span>4 printable guides</span></div><a class="work-button" href="#lessons">Start practicing <span aria-hidden="true">→</span></a></div>
<aside class="work-study-card"><p class="work-kicker">Words into action</p><p class="work-study-phrase">Read the situation.<br>Find your words.<br>Make yourself clear.</p><p>For {e(t['roles']).rstrip('.')}.</p><a href="#downloads">Choose your materials ↓</a><p><a href="#finished-dialogue-prompts">Copy complete AI prompts ↓</a></p></aside></section>
<section class="work-orientation work-two-column"><div><h2>What you will practice</h2>{ul(t['outcomes'][:5])}</div><div><h2>Choose your pace</h2><p><strong>Quick practice · 15 minutes:</strong> read a case, study the useful expressions, and say your response aloud.</p><p><strong>Full lesson · 45-60 minutes:</strong> add the language checks, partner exchange, writing, and revision.</p><p><strong>Level guide:</strong> designed for intermediate to advanced learners. B1 learners can use the sentence frames; B2 learners can work independently; C1 learners can try the harder second round. These are teaching suggestions, not a certified level assessment.</p></div></section>
<section id="downloads" class="work-section"><div class="work-section-heading"><div><p class="work-kicker">Take the lesson with you</p><h2>Four guides. Four useful jobs.</h2></div><span>Revised September 2026</span></div><div class="work-downloads">{pdf_links(t)}</div></section>
<section id="lessons" class="work-section"><div class="work-section-heading"><div><p class="work-kicker">Practice, reflect, repeat</p><h2>Your eight lessons</h2></div><p class="work-progress" data-work-progress role="status">0 of 8 practiced</p></div><div class="work-lesson-tools"><nav class="work-jump" aria-label="Jump to lesson">{jump}</nav><button type="button" class="work-text-button" data-expand-lessons hidden>Open all lessons</button></div><p class="work-scope">{e(t['scope_note'])}</p>
<div class="work-save-controls" hidden data-storage-controls><label><input type="checkbox" data-save-notes> Save my drafts and progress in this browser</label><button type="button" class="work-text-button" data-clear-work>Clear saved practice</button><p data-storage-status role="status">Saving is off. Use fictional details; practice is not submitted or automatically graded.</p></div>{modules}</section>
<section class="work-section work-capstone"><p class="work-kicker">Put it together</p><h2>Your final workplace challenge</h2><p>Choose a case you have not rehearsed today. Give a one-minute response, answer two follow-up questions, then write a 70-110 word message. Have your partner introduce the harder second-round challenge. Review the four criteria used in the lessons and repeat the part that needs improvement.</p><p><strong>Compare your progress:</strong> return to your first draft. Identify one improvement in clarity, one in accuracy, and one in how you ask for or explain the next step.</p></section>
<details id="vocabulary" class="work-section work-glossary-disclosure"><summary>Explore your field vocabulary</summary><div class="work-section-heading"><div><p class="work-kicker">Keep the meaning close</p><h2>Your field vocabulary</h2></div><label>Find a term<input type="search" data-vocabulary-search placeholder="Search words and meanings"></label></div><p data-vocabulary-count role="status">{len(t['jargon'])} terms</p><dl class="work-vocabulary work-glossary">{glossary}</dl></details>
{extra}{dialogue_prompts(t)}{web_section(t)}<section class="work-section work-two-column"><div><h2>For teachers and study partners</h2><p>Ask learners to respond before revealing the model. Give feedback on one meaning issue and one language pattern, then let them repeat. For mixed levels, offer the frames first and remove them in the second round.</p><p>Use the teacher's guide for a 60-minute plan, performance criteria, model answers, and extension tasks. A recorded practice completion is not a proficiency score.</p><p><a data-ai-preset href="{e(ai_url(t, 'teacher'))}">Adapt an activity with a scripted AI prompt →</a></p></div><div><h2>Language notes and further reading</h2><p>The cases and explanations are original teaching material. The references provide language frameworks and selected professional context; use current local guidance for actual work.</p><ul class="work-sources">{sources}</ul><p class="work-small">Course edition: {REVISION}.</p></div></section>
<section class="work-section"><p class="work-kicker">Continue in your field</p><h2>Related courses</h2><div class="work-related">{related}</div></section></div>'''
    return page(t['title'], content, f'efsp-{t["slug"]}.html')


def render_directory(tracks):
    options = ''.join(f'<option>{e(g)}</option>' for g in sorted({t['category'] for t in tracks}))
    cards = ''.join(f'''<a class="work-course-card" href="efsp-{e(t['slug'])}.html" data-work-course-link data-category="{e(t['category'])}" data-search="{e(t['title']+' '+t['summary']+' '+t['roles']+' '+' '.join(m['title'] for m in t['modules']))}">{card_icon(t)}<span class="work-kicker">{e(t['category'])}</span><h3>{e(t['title'])}</h3><p>{e(t['summary'])}</p><span class="work-card-footer">8 lessons · 4 guides <span aria-hidden="true">↗</span></span></a>''' for t in tracks)
    content = f'''<section class="work-directory-hero"><p class="work-kicker">English for Work</p><h1>Good work.<br>Clearly expressed.</h1><p class="work-intro">Find the words for the work you do. Practice real conversations, write useful messages, and build confidence one situation at a time.</p><div class="work-meta"><span>41 professional fields</span><span>328 practical lessons</span><span>164 printable guides</span></div></section>
<section class="work-start-paths"><article><span class="work-kicker">On your own</span><h2>Make fifteen minutes count.</h2><p>Choose a case, try a response, and compare it with the model. Add writing and revision when you have more time.</p></article><article><span class="work-kicker">With a class or partner</span><h2>Turn practice into a conversation.</h2><p>Use partner roles, follow-up questions, timed lesson plans, and clear feedback criteria. Every course includes a teacher's guide.</p></article></section>
<section class="work-section" data-work-directory><div class="work-section-heading"><div><p class="work-kicker">Find your field</p><h2>What do you do?</h2></div><p data-course-count role="status">41 courses</p></div><div class="work-directory-filters"><label>Search by role, topic, or industry<input type="search" data-course-search placeholder="Try nursing, presentations, or customer support"></label><label>Browse a field<select data-course-category><option value="">All fields</option>{options}</select></label></div><p class="work-empty" data-course-empty hidden>No courses match. Try a broader word or choose all fields.</p><div class="work-course-grid">{cards}</div></section>
<section class="work-section work-two-column"><div><h2>Know what you are practicing.</h2><p>Every lesson combines an original case, relevant vocabulary, a language workshop, short checks with explanations, speaking, writing, and revision. Repeated language patterns help you recall useful expressions in a new context.</p><p><strong>Keep practicing with your preferred AI.</strong> Every course includes ready-to-copy prompts for vocabulary, grammar, role-play, new dialogues, writing feedback, tone, review and teaching. The complete text appears beneath each lesson and in the dialogue prompt library. Copy it as written, or download the full course prompt collection. No prompt-writing is required. Two printable prompts are also included in every guide.</p></div><div><h2>Choose the right starting point.</h2><p>These courses suit intermediate to advanced learners. Use the sentence frames for support or add the harder follow-up challenge. For foundational practice, start with <a href="grammar-concepts.html">the grammar guides</a> and <a href="beginner.html">daily reading</a>.</p></div></section>'''
    from seo_content import CATEGORIES
    fields = '<nav class="seo-category-links" aria-label="Professional English fields">' + ''.join(f'<a href="english-for-work/{c["slug"]}.html">{e(c["title"])}</a>' for c in CATEGORIES.values()) + '</nav>'
    content = content.replace('<section class="work-section" data-work-directory>', '<section class="work-section"><h2>Explore your professional field</h2>' + fields + '</section><section class="work-section" data-work-directory>')
    return page('English for Work', content, 'efsp.html')


def main():
    tracks = all_tracks()
    print(validate_tracks(tracks))
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
