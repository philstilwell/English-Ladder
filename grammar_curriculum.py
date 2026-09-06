"""Offline, reviewed grammar publishing. HTML and print share one curriculum."""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def load_curriculum():
    concepts = json.loads((ROOT / 'content/grammar-curriculum.json').read_text())['concepts']
    assert [c['number'] for c in concepts] == list(range(1, 45))
    for c in concepts:
        assert len(c['checks']) >= 3 and len(c['cards']) >= 2 and len(c['pdfs']) == 2
    return concepts

def e(value):
    return html.escape(str(value), quote=True)

def slug(c):
    return f'concept-{c["number"]:02}.html'

def build_pages():
    from editorial import document, decorate_page
    concepts = load_curriculum()
    cards = []
    for i,c in enumerate(concepts):
        comparisons = ''.join(f'<article class="concept-comparison"><p class="eyebrow">{e(v["label"])}</p><p class="concept-example">{e(v["example"])}</p><p>{e(v["note"])}</p></article>' for v in c['cards'])
        checks = ''.join(f'''<article class="grammar-response"><h3>{j}. {e(q['prompt'])}</h3><label>Your answer<textarea rows="2" data-study-draft="grammar-{c['number']}-{j}"></textarea></label><details><summary>Compare your answer</summary><p><strong>{e(q['answer'])}</strong></p><p>{e(q['explanation'])}</p></details></article>''' for j,q in enumerate(c['checks'],1))
        neighbors = []
        if i: neighbors.append(f'<a class="secondary-button" href="{slug(concepts[i-1])}">← {e(concepts[i-1]["title"])}</a>')
        if i+1<len(concepts): neighbors.append(f'<a class="primary-button" href="{slug(concepts[i+1])}">{e(concepts[i+1]["title"])} →</a>')
        content = f'''<nav class="breadcrumb" aria-label="Breadcrumb"><a href="../grammar-concepts.html">All grammar lessons</a><span>Concept {c['number']:02}</span></nav>
<section class="page-hero"><p class="eyebrow">{e(c['category'])} · {e(c['level'])} · 10–15 minutes</p><h1>{e(c['title'])}</h1><p>{e(c['goal'])}</p><p class="muted">Level ranges are study guidance. Start with the examples and choose your own pace.</p><div class="stage-actions"><a class="primary-button" href="#practice-check">Try the practice →</a><a class="secondary-button" href="../pdf/students/{e(c['pdfs'][0])}">Learner workbook PDF</a><a class="secondary-button" href="../pdf/teachers/{e(c['pdfs'][1])}">Teaching guide PDF</a></div></section>
<section class="concept-comparisons" aria-label="Compare the patterns">{comparisons}</section>
<section class="reading-width concept-explanation" id="core-idea"><p class="eyebrow">Understand</p><h2>The useful distinction</h2>{''.join(f'<p>{e(r)}</p>' for r in c['rules'])}</section>
<section class="reading-width" id="practice-check"><p class="eyebrow">Try it</p><h2>Check your understanding</h2><p>Write an answer, then compare it with the explanation. Other wording may also be correct. These responses are for self-checking and are not automatically graded.</p>{checks}</section>
<section class="reading-width transfer-task"><p class="eyebrow">Use it</p><h2>Make it your own</h2><p>{e(c['transfer'])}</p><label>Your example<textarea rows="4" data-study-draft="grammar-{c['number']}-transfer"></textarea></label><details><summary>See one possible response</summary><p>{e(c['model'])}</p></details><p><strong>Self-check:</strong> Does your sentence express your intended meaning? Does its form follow the relevant pattern? Can a reader understand the context?</p><button class="primary-button" type="button" data-complete-study>Mark this lesson practiced</button><p data-study-status role="status"></p></section>
<section class="reading-width"><h2>Continue learning</h2><div class="stage-actions">{''.join(neighbors)}</div><p><a href="../grammar-concepts.html">Choose a different topic</a> · <a href="../about.html#corrections">Report a correction</a></p><p class="muted">Revised {c['reviewed']}. Web and PDF editions share the same teaching text.</p></section>'''
        path=ROOT/'grammar-concepts'/slug(c)
        path.write_text(document(c['title'],content,'theme-grammar-detail curriculum-page','../','grammar-concepts.html'))
        decorate_page(path)
        cards.append(f'''<article class="library-card" data-library-item data-category="{e(c['category'])}" data-level="{e(c['level'])}" data-search="{e(c['title']+' '+c['goal']+' '+c['category'])}"><p class="eyebrow">{c['number']:02} · {e(c['level'])} · 10–15 min</p><h2><a href="grammar-concepts/{slug(c)}">{e(c['title'])}</a></h2><p>{e(c['goal'])}</p><span class="library-category">{e(c['category'])}</span></article>''')
    categories=''.join(f'<option>{e(cat)}</option>' for cat in sorted({c['category'] for c in concepts}))
    content=f'''<section class="page-hero"><p class="eyebrow">Understand it. Use it.</p><h1>Grammar for real conversations</h1><p>Choose a useful distinction, compare natural examples, then write something of your own.</p><p>New to the library? Start with <a href="grammar-concepts/concept-01.html">in, on, and at</a>, <a href="grammar-concepts/concept-20.html">asking about prices</a>, or <a href="grammar-concepts/concept-44.html">asking for advice</a>.</p></section><section data-library><div class="library-filters"><label>Find a topic<input type="search" data-library-search placeholder="Try dates, advice, or questions"></label><label>Topic<select data-library-category><option value="">All topics</option>{categories}</select></label><label>Level<select data-library-level><option value="">All levels</option><option value="A1">A1</option><option value="A2">A2</option><option value="B1">B1</option><option value="B2">B2</option></select></label></div><p data-library-count role="status">44 lessons</p><p data-library-empty hidden>No lessons match. Try a shorter search or another level.</p><div class="library-grid">{''.join(cards)}</div></section>'''
    path=ROOT/'grammar-concepts.html';path.write_text(document('Grammar lessons',content,'theme-grammar-index',current='grammar-concepts.html'));decorate_page(path)

if __name__ == '__main__':
    build_pages()
