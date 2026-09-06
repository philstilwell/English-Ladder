"""Offline, reviewed grammar publishing. HTML and print share one curriculum."""
import html
import json
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent

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
        comparisons = ''.join(f'<article class="concept-comparison"><p class="eyebrow">{e(v["label"])}</p><p class="concept-example">{e(v["example"])}</p><p>{e(v["note"])}</p></article>' for v in c['cards'])
        checks = ''.join(question_html(c,q,j) for j,q in enumerate(c['checks'],1))
        application=question_html(c,c['application'],len(c['checks'])+1)
        answer_key=''.join(f'<li><strong>{e(next(o["text"] for o in q["options"] if o["correct"]))}</strong> — {e(next(o["feedback"] for o in q["options"] if o["correct"]))}</li>' for q in [*c['checks'],c['application']])
        neighbors = []
        if i: neighbors.append(f'<a class="secondary-button" href="{slug(concepts[i-1])}">← {e(concepts[i-1]["title"])}</a>')
        if i+1<len(concepts): neighbors.append(f'<a class="primary-button" href="{slug(concepts[i+1])}">{e(concepts[i+1]["title"])} →</a>')
        content = f'''<nav class="breadcrumb" aria-label="Breadcrumb"><a href="../grammar-concepts.html">All grammar lessons</a><span>Concept {c['number']:02}</span></nav>
<section class="page-hero"><p class="eyebrow">{e(c['category'])} · {e(c['level'])} · 10–15 minutes</p><h1>{e(c['title'])}</h1><p>{e(c['goal'])}</p><p class="muted">Level ranges are study guidance. Start with the examples and choose your own pace.</p><div class="stage-actions"><a class="primary-button" href="#practice-check">Try the practice →</a><a class="secondary-button" href="../pdf/students/{e(c['pdfs'][0])}">Learner workbook PDF</a><a class="secondary-button" href="../pdf/teachers/{e(c['pdfs'][1])}">Teaching guide PDF</a></div></section>
<section class="concept-comparisons" aria-label="Compare the patterns">{comparisons}</section>
<section class="reading-width concept-explanation" id="core-idea"><p class="eyebrow">Understand</p><h2>The useful distinction</h2>{''.join(f'<p>{e(r)}</p>' for r in c['rules'])}</section>
<section class="reading-width" id="practice-check"><p class="eyebrow">Try it</p><h2>Check your understanding</h2><p>Choose one answer for each question. The feedback explains your selected answer. You can change your choice and try again.</p><p class="choice-progress" data-choice-progress role="status">0 of {len(c['checks'])+1} correct</p>{checks}</section>
<section class="reading-width transfer-task"><p class="eyebrow">Use it</p><h2>Choose the best response</h2>{application}<button class="primary-button" type="button" data-complete-study disabled>Mark this lesson practiced</button><p data-study-status role="status">Answer all {len(c['checks'])+1} questions correctly to complete this activity.</p></section>
<noscript><section class="reading-width"><p>Choose an option for each question. Turn on JavaScript for feedback on your selection, or check the answer key below.</p><details><summary>Multiple-choice answer key</summary><ol>{answer_key}</ol></details></section></noscript>
<section class="reading-width"><h2>Continue learning</h2><div class="stage-actions">{''.join(neighbors)}</div><p><a href="../grammar-concepts.html">Choose a different topic</a> · <a href="../about.html#corrections">Report a correction</a></p><p class="muted">Revised {c['reviewed']}. Web and PDF editions share the same teaching text.</p></section>'''
        path=ROOT/'grammar-concepts'/slug(c)
        path.write_text(document(c['title'],content,'theme-grammar-detail curriculum-page','../','grammar-concepts.html'))
        decorate_page(path)
        cards.append(f'''<article class="library-card" data-library-item data-category="{e(c['category'])}" data-level="{e(c['level'])}" data-search="{e(c['title']+' '+c['goal']+' '+c['category'])}"><p class="eyebrow">{c['number']:02} · {e(c['level'])} · 10–15 min</p><h2><a href="grammar-concepts/{slug(c)}">{e(c['title'])}</a></h2><p>{e(c['goal'])}</p><span class="library-category">{e(c['category'])}</span></article>''')
    categories=''.join(f'<option>{e(cat)}</option>' for cat in sorted({c['category'] for c in concepts}))
    content=f'''<section class="page-hero"><p class="eyebrow">Understand it. Use it.</p><h1>Grammar for real conversations</h1><p>Compare natural examples, then check your understanding with multiple-choice practice.</p><p>New to the library? Start with <a href="grammar-concepts/concept-01.html">in, on, and at</a>, <a href="grammar-concepts/concept-20.html">asking about prices</a>, or <a href="grammar-concepts/concept-44.html">asking for advice</a>.</p></section><section data-library><div class="library-filters"><label>Find a topic<input type="search" data-library-search placeholder="Try dates, advice, or questions"></label><label>Topic<select data-library-category><option value="">All topics</option>{categories}</select></label><label>Level<select data-library-level><option value="">All levels</option><option value="A1">A1</option><option value="A2">A2</option><option value="B1">B1</option><option value="B2">B2</option></select></label></div><p data-library-count role="status">44 lessons</p><p data-library-empty hidden>No lessons match. Try a shorter search or another level.</p><div class="library-grid">{''.join(cards)}</div></section>'''
    path=ROOT/'grammar-concepts.html';path.write_text(document('Grammar lessons',content,'theme-grammar-index',current='grammar-concepts.html'));decorate_page(path)

if __name__ == '__main__':
    build_pages()
