"""Offline, reviewed grammar publishing. HTML and print share one curriculum."""
import html
import json
import hashlib
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent

# Keep the original graphics. Explain exceptions and limits alongside them.
GRAPHIC_CORRECTIONS = {
    'concept-07': 'In talk about and think about, about introduces the topic. It does not tell us how long the activity lasts. Keep these limits in mind when using the graphic:',
    'concept-16': 'Recently and lately refer to a recent time. They do not automatically require have/has been + a verb ending in -ing, or mean that an activity will continue. Notice these different patterns:',
    'concept-28': 'This, that, and it depend on what you are referring to and how you present it. This and that are not reserved for different speakers. Compare these examples:',
}
GRAPHIC_EXAMPLES = {
    'concept-07': [
        ('A short conversation.', 'We talked about the plan for thirty seconds.',
         'About introduces the plan as the topic, even though the conversation was short.'),
        ('A different meaning.', 'We walked about the town.',
         'Here, about means around.'),
        ('A different verb pattern.', 'We discussed the plan for an hour.',
         'Discuss normally takes its topic directly, without about. The length of the discussion does not change this pattern.'),
    ],
    'concept-16': [
        ('A single finished event.', 'I recently bought a bicycle.',
         'Recently works with a finished action. Lately is not normally used for a single event like this.'),
        ('A recent state.', 'I have been tired lately.',
         'This describes a state, not an activity in progress. Lately often goes with recent states or repeated activities.'),
        ('An activity that may have just stopped.', 'I have been running, so I need a rest.',
         'Have been running can explain a present result even after the running has stopped. It does not promise future activity.'),
    ],
    'concept-28': [
        ('Your own earlier idea.', 'I missed the train. That made me late.',
         'That can refer to something you have just said yourself.'),
        ('Another person’s idea.', 'A: We could meet online. B: This could work well.',
         'This can also refer to someone else’s suggestion; here it brings that suggestion into focus.'),
        ('An established reference.', 'I bought a bag. It is light.',
         'It refers back to the bag. It does not have to introduce an idea that comes later in the sentence.'),
    ],
}


def clarify_original_graphic(soup, key):
    for old in soup.select('[data-graphic-correction]'):
        old.decompose()
    text = GRAPHIC_CORRECTIONS.get(key)
    figure = soup.select_one('.concept-graphic')
    if not text or figure is None:
        return
    for target, identifier in [(figure, 'graphic-correction'), (soup.select_one('.image-lightbox-image'), 'lightbox-graphic-correction')]:
        if target is None:
            continue
        note = soup.new_tag('aside', attrs={'class': 'graphic-correction', 'id': identifier, 'data-graphic-correction': ''})
        label = soup.new_tag('strong'); label.string = 'Exceptions and useful limits'
        paragraph = soup.new_tag('p'); paragraph.string = text
        examples = soup.new_tag('ul')
        for heading, sentence, explanation in GRAPHIC_EXAMPLES[key]:
            item = soup.new_tag('li')
            title = soup.new_tag('strong'); title.string = heading
            item.extend([title, f' “{sentence}” {explanation}'])
            examples.append(item)
        note.extend([label, paragraph, examples]); target.insert_before(note)
        image = target.select_one('img') if target is figure else target
        if image is not None:
            image['aria-describedby'] = identifier


def load_curriculum():
    concepts = json.loads((ROOT / 'content/grammar-curriculum.json').read_text())['concepts']
    assert [c['number'] for c in concepts] == list(range(1, 45))
    for c in concepts:
        assert len(c['checks']) >= 3 and len(c['cards']) >= 2 and len(c['pdfs']) == 2
        for q in [*c['checks'], c['application']]:
            options = q.get('options', [])
            if not q.get('prompt') or len(options) != 3 or sum(o.get('correct') is True for o in options) != 1:
                raise ValueError(f'Concept {c["number"]}: each question needs three choices and exactly one correct answer')
            if len({o.get('text', '').strip().casefold() for o in options}) != len(options):
                raise ValueError(f'Concept {c["number"]}: duplicate choices')
            if any(not o.get('text', '').strip() or not o.get('feedback', '').strip() or type(o.get('correct')) is not bool for o in options):
                raise ValueError(f'Concept {c["number"]}: every choice needs text, correctness, and its own feedback')
    return concepts

def e(value):
    return html.escape(str(value), quote=True)

def slug(c):
    return f'concept-{c["number"]:02}.html'

def question_html(c, q, number):
    key=f'grammar-{c["number"]}-{number}'
    revision=hashlib.sha256(json.dumps(q,sort_keys=True).encode()).hexdigest()[:12]
    options=''.join(f'''<label class="grammar-choice" for="{key}-{i}"><input id="{key}-{i}" type="radio" name="{key}" value="{i}" data-choice-correct="{str(o['correct']).lower()}" data-choice-feedback="{e(o['feedback'])}"><span>{e(o['text'])}</span></label>''' for i,o in enumerate(q['options']))
    return f'''<fieldset class="grammar-response" data-choice-question data-study-choice="{key}-{revision}"><legend>{number}. {e(q['prompt'])}</legend><div class="grammar-choices">{options}</div><p class="choice-feedback" id="{key}-feedback" role="status" aria-live="polite" hidden></p></fieldset>'''

def build_pages():
    from editorial import document, decorate_page
    concepts = load_curriculum()
    cards = []
    for i,c in enumerate(concepts):
        image_path=f'assets/grammar-concepts/concept-{c["number"]:02}.png'
        with Image.open(ROOT/image_path) as original:
            image_width,image_height=original.size
        image_alt=f'Original concept {c["number"]:02} graphic: {c["title"]}.'
        comparisons = ''.join(f'<article class="concept-comparison"><p class="eyebrow">{e(v["label"])}</p><p class="concept-example">{e(v["example"])}</p><p>{e(v["note"])}</p></article>' for v in c['cards'])
        checks = ''.join(question_html(c,q,j) for j,q in enumerate(c['checks'],1))
        application=question_html(c,c['application'],len(c['checks'])+1)
        answer_key=''.join(f'<li><strong>{e(next(o["text"] for o in q["options"] if o["correct"]))}</strong> — {e(next(o["feedback"] for o in q["options"] if o["correct"]))}</li>' for q in [*c['checks'],c['application']])
        neighbors = []
        if i: neighbors.append(f'<a class="secondary-button" href="{slug(concepts[i-1])}">← {e(concepts[i-1]["title"])}</a>')
        if i+1<len(concepts): neighbors.append(f'<a class="primary-button" href="{slug(concepts[i+1])}">{e(concepts[i+1]["title"])} →</a>')
        content = f'''<nav class="breadcrumb" aria-label="Breadcrumb"><a href="../grammar-concepts.html">All grammar lessons</a><span>Concept {c['number']:02}</span></nav>
<section class="page-hero"><p class="eyebrow">{e(c['category'])} · {e(c['level'])} · 10–15 minutes</p><h1>{e(c['title'])}</h1><p>{e(c['goal'])}</p><p class="muted">Level ranges are study guidance. Start with the examples and choose your own pace.</p><div class="stage-actions"><a class="primary-button" href="#practice-check">Try the practice →</a><a class="secondary-button" href="../pdf/students/{e(c['pdfs'][0])}">Learner workbook PDF</a><a class="secondary-button" href="../pdf/teachers/{e(c['pdfs'][1])}">Teaching guide PDF</a></div></section>
<figure class="concept-graphic"><a class="grammar-image-trigger" href="../{image_path}" target="_blank" rel="noopener" aria-label="Enlarge the graphic for {e(c['title'])}" aria-haspopup="dialog" data-lightbox-src="../{image_path}" data-lightbox-alt="{e(image_alt)}"><img class="grammar-hero-image" src="../{image_path}" width="{image_width}" height="{image_height}" alt="{e(image_alt)}" decoding="async"><span class="grammar-image-hint">View full-size guide ↗</span></a><figcaption>Original concept graphic · <a href="../{image_path}" target="_blank" rel="noopener">Open the full-resolution image in a new tab</a></figcaption></figure>
<section class="concept-comparisons" aria-label="Compare the patterns">{comparisons}</section>
<section class="reading-width concept-explanation" id="core-idea"><p class="eyebrow">Understand</p><h2>The useful distinction</h2>{''.join(f'<p>{e(r)}</p>' for r in c['rules'])}</section>
<section class="reading-width" id="practice-check"><p class="eyebrow">Try it</p><h2>Check your understanding</h2><p>Choose one answer for each question. The feedback explains your selected answer. You can change your choice and try again.</p><p class="choice-progress" data-choice-progress role="status">0 of {len(c['checks'])+1} correct</p>{checks}</section>
<section class="reading-width transfer-task"><p class="eyebrow">Use it</p><h2>Choose the best response</h2>{application}<button class="primary-button" type="button" data-complete-study disabled>Mark this lesson practiced</button><p data-study-status role="status">Answer all {len(c['checks'])+1} questions correctly to complete this activity.</p></section>
<noscript><section class="reading-width"><p>Choose an option for each question. Turn on JavaScript for feedback on your selection, or check the answer key below.</p><details><summary>Multiple-choice answer key</summary><ol>{answer_key}</ol></details></section></noscript>
<section class="reading-width"><h2>Continue learning</h2><div class="stage-actions">{''.join(neighbors)}</div><p><a href="../grammar-concepts.html">Choose a different topic</a> · <a href="../about.html#corrections">Report a correction</a></p><p class="muted">Revised {c['reviewed']}. Web and PDF editions share the same teaching text.</p></section>
<div class="image-lightbox" hidden><button aria-label="Close enlarged image" class="image-lightbox-backdrop" data-lightbox-close type="button"></button><div class="image-lightbox-dialog" role="dialog" aria-modal="true" aria-label="{e(c['title'])}: enlarged concept graphic"><button class="image-lightbox-close" data-lightbox-close type="button">Close</button><img class="image-lightbox-image" alt=""><a class="text-link" href="../{image_path}" target="_blank" rel="noopener">Open the full-resolution image in a new tab</a></div></div>'''
        path=ROOT/'grammar-concepts'/slug(c)
        path.write_text(document(c['title'],content,'theme-grammar-detail curriculum-page','../','grammar-concepts.html'))
        decorate_page(path)
        cards.append(f'''<article class="library-card" data-library-item data-category="{e(c['category'])}" data-level="{e(c['level'])}" data-search="{e(c['title']+' '+c['goal']+' '+c['category'])}"><a class="grammar-thumb" href="grammar-concepts/{slug(c)}" aria-label="Open {e(c['title'])}"><img src="{image_path}" width="{image_width}" height="{image_height}" alt="" loading="lazy" decoding="async"></a><p class="eyebrow">{c['number']:02} · {e(c['level'])} · 10–15 min</p><h2><a href="grammar-concepts/{slug(c)}">{e(c['title'])}</a></h2><p>{e(c['goal'])}</p><span class="library-category">{e(c['category'])}</span></article>''')
    categories=''.join(f'<option>{e(cat)}</option>' for cat in sorted({c['category'] for c in concepts}))
    content=f'''<section class="page-hero"><p class="eyebrow">Understand it. Use it.</p><h1>Grammar for real conversations</h1><p>Compare natural examples, then check your understanding with multiple-choice practice.</p><p>New to the library? Start with <a href="grammar-concepts/concept-01.html">in, on, and at</a>, <a href="grammar-concepts/concept-20.html">asking about prices</a>, or <a href="grammar-concepts/concept-44.html">asking for advice</a>.</p></section><section data-library><div class="library-filters"><label>Find a topic<input type="search" data-library-search placeholder="Try dates, advice, or questions"></label><label>Topic<select data-library-category><option value="">All topics</option>{categories}</select></label><label>Level<select data-library-level><option value="">All levels</option><option value="A1">A1</option><option value="A2">A2</option><option value="B1">B1</option><option value="B2">B2</option></select></label></div><p data-library-count role="status">44 lessons</p><p data-library-empty hidden>No lessons match. Try a shorter search or another level.</p><div class="library-grid">{''.join(cards)}</div></section>'''
    path=ROOT/'grammar-concepts.html';path.write_text(document('Grammar lessons',content,'theme-grammar-index',current='grammar-concepts.html'));decorate_page(path)
    from seo import build_html_sitemap, write_sitemaps
    build_html_sitemap();write_sitemaps()

if __name__ == '__main__':
    build_pages()
