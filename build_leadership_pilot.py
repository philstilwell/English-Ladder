"""Build an isolated, book-oriented leadership edition for approval.

No website files or existing books are replaced. Run this, then
`node print_leadership_pilot.cjs`. The latter creates the tagged PDF.
"""
from __future__ import annotations

from collections import defaultdict
from html import escape
import hashlib
import json
from pathlib import Path
import random
import re
import sys
import zipfile
from xml.etree import ElementTree as ET

from books.leadership_pilot import (
    UNITS, SUPPLEMENTS, CHECKPOINTS, TITLE, SUBTITLE, AUTHOR, COPYRIGHT,
    NOTICE, EDITION, COURSE_URL, validate,
)

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'output/pdf'
STEM = 'cross-cultural-leadership-english-book-revised'
ART = ROOT / 'assets/work/leadership-book-cover-2026.png'
LOGO = ROOT / 'assets/brand/ladder-mark.png'
CSS = ROOT / 'books/leadership_pilot.css'
PAGES = []
LETTERS = 'ABCD'
BOOK = None
FOOTER_TITLE = 'Cross-Cultural Leadership'
KEYWORDS = 'English Ladder, international managers, workplace English, cross-cultural leadership'


def e(value):
    return escape(str(value), quote=True)


def para(text, cls=''):
    return f'<p class="{cls}">{e(text)}</p>'


def ref(target, label='Answers and explanations'):
    return (f'<a class="xref" href="#{target}">{e(label)}'
            f'<span class="print-reference">, page <span data-page-ref="{target}"></span></span></a>')


def unit_ref(number, label):
    return ref(f'u{number}-a', label)


def label(letter, title):
    return f'<h2><span class="section-letter">{letter}</span> {e(title)}</h2>'


def sheet(anchor, section, content, *, unit=None, kind='', flow=False):
    number = f'{unit:02d}' if unit else ''
    accent = ['blue', 'coral', 'gold', 'plum'][(unit - 1) % 4] if unit else 'blue'
    PAGES.append(dict(anchor=anchor, section=section, content=content, unit=unit,
                      kind=kind, flow=flow, accent=accent, number=number))


def render_sheet(page):
    return f'''<section id="{page['anchor']}" class="sheet {page['kind']} {page['accent']}"
        data-section="{e(page['section'])}" {'data-flow="true"' if page['flow'] else ''}>
      <header class="running-head" aria-hidden="true">
        <span class="brand"><img src="../../assets/brand/ladder-mark.png" alt=""/>English Ladder</span>
        <span>{e(page['section'])}</span>
      </header>
      <div class="page-body">{page['content']}</div>
      <footer aria-hidden="true"><span>{e(FOOTER_TITLE)}</span>
        <a href="https://englishladder.com/">ENGLISHLADDER.COM</a>
        <span>Phil Stilwell <span class="footer-divider">|</span> <span class="page-number"></span></span>
      </footer>
    </section>'''


def mcqs(items, prefix, key_prefix, start=1):
    blocks = []
    for n, item in enumerate(items, start):
        options = ''.join(f'<li><span class="option-letter">{LETTERS[i]}.</span> {e(text)}</li>'
                          for i, text in enumerate(item['options']))
        blocks.append(f'<article class="question" id="{prefix}{n}"><h3>{n}. {e(item["prompt"])}</h3>'
                      f'<ol class="options" type="A">{options}</ol></article>')
    return ''.join(blocks) + f'<p class="answer-link">{ref(key_prefix)}</p>'


def bank(scene, seed):
    values = [g['answer'] for g in scene['gaps']]
    random.Random(seed).shuffle(values)
    return '<aside class="word-bank"><h3>Word and phrase bank</h3><p>' + ' <span class="separator" aria-hidden="true">/</span> '.join(f'<span class="bank-entry">{e(s)}</span>' for s in values) + '</p></aside>'


def cloze(text):
    return re.sub(r'\{\{(\d+)\}\}',
                  lambda m: (f'<span class="cloze" role="img" aria-label="Blank {m[1]}">'
                             f'<sup>{m[1]}</sup><span class="blank" aria-hidden="true"></span></span>'), e(text))


def turns(scene, start, end):
    return '<ol class="dialogue" start="' + str(start + 1) + '">' + ''.join(
        f'<li><span class="turn-number" aria-hidden="true">{i + 1:02d}</span>'
        f'<p><strong>{e(speaker)}:</strong> {cloze(words)}</p></li>'
        for i, (speaker, words) in enumerate(scene['dialogue'][start:end], start)) + '</ol>'


def answer_strip(scene, target):
    return '<aside class="answer-strip"><h3>Check the gaps</h3><p>' + ' <span aria-hidden="true">/</span> '.join(
        f'<b>{n}.</b> {e(g["answer"])}' for n, g in enumerate(scene['gaps'], 1)) + '</p>' + ref(target, 'Why these answers fit') + '</aside>'


def front():
    if BOOK is not None:
        return industry_front()
    cover = (f'<p class="eyebrow">English for Work / International managers</p>'
             f'<h1>Cross-Cultural<br/>Leadership <span>English</span></h1>'
             '<p class="subtitle">Clear decisions. Constructive disagreement.<br/>Trusted teams.</p>'
             '<img class="cover-art" src="../../assets/work/leadership-book-cover-2026.png" '
             'alt="Four international managers discuss a project schedule at a shared table."/>'
             '<div class="cover-author"><p class="author">Phil Stilwell</p>'
             f'<p class="copyright">{e(COPYRIGHT)}<br/>{e(NOTICE)}</p></div>'
             '<p class="cover-description">Eight practical lessons. Eleven extended conversations.<br/>'
             'Vocabulary, phrase banks, guided speaking, and explained answers.</p>'
             f'<p class="edition">{EDITION} / Upper-intermediate to advanced</p>')
    sheet('cover', 'Learner book', cover, kind='cover')
    rows = ''.join(f'<li>{unit_ref(i, str(i).zfill(2) + "  " + u["title"])}<p>{e(u["skill"])}</p></li>'
                   for i, u in enumerate(UNITS, 1))
    content = '<h2>Your route through the book</h2><ol class="contents">' + rows + '</ol>'
    content += '<div class="contents-extra">' + ''.join(
        ref(target, title) for target, title in [
            ('culture', 'Directness, disagreement, and local norms'),
            ('additional-1', 'Three additional workplace cases'),
            ('key-u1-a', 'Answers and explanations'),
            ('phrase-finder', 'Phrase finder'), ('index', 'Vocabulary index'), ('sources', 'References and publication notes')]) + '</div>'
    content += para('Suggested study range: B2-C1. The core language is followed by more demanding precision and transfer work. This is an editorial study range, not a certified proficiency assessment.', 'small')
    sheet('contents', 'Book map', content, kind='contents-page')
    content = '<h2>Direct is not the same as hostile.</h2>'
    content += para('"I don\'t buy that estimate" can be an invitation to test a proposal, not a statement of personal dislike. But you cannot reliably infer intent from directness alone. Ask for the evidence, watch the response, and distinguish a sharp challenge from personal contempt.')
    content += '<dl class="field-notes">' + ''.join(
        f'<div><dt>{e(title)}</dt><dd>{e(text)}</dd></div>' for title, text in [
            ('Challenge the claim', '"Which assumption is wrong?" keeps the discussion on something that can be checked. Accepting one criticism does not require abandoning the whole proposal.'),
            ('Set a behavioral boundary', '"Keep the criticism on the estimate, not the people." A colleague\'s stated good intention does not erase an insult or repeated interruption.'),
            ('Check the local rule', 'First names, humor, and informal meetings do not tell you who can approve spending. Ask which decisions are yours and which need approval.'),
            ('Make room for a different pace', 'Some colleagues think aloud; others want time to read before speaking. Use a pre-read, a clear speaking order, and a later input route rather than equating speed with competence.'),
            ('Separate rapport from commitment', 'A friendly "sounds good" can support a direction without accepting a deadline. Confirm the deliverable, owner, condition, and time.'),
            ('Name what a deadline means', '"Friday" may refer to different time zones or different versions of a report. State the clock time, location, and whether the figures are provisional or verified.'),
        ]) + '</dl>'
    content += '<aside class="note"><h3>People vary within every workplace.</h3>' + para('Nationality is not a personality test. Role, power, language confidence, professional training, and company norms also shape an exchange. Do not normalize threats, discrimination, or intimidation as a cultural style; use appropriate workplace support and reporting routes.') + '</aside>'
    content += para('Research background: collaborative meaning-making [1], feedback about behavior and impact [2], and psychological safety in teams [3]. These are not rules predicting an individual\'s intent.', 'small')
    sheet('culture', 'Cultural field notes', content)


def industry_front():
    art = '../../' + ART.relative_to(ROOT).as_posix()
    cover = (f'<p class="eyebrow">English for Work / {e(BOOK["cover_label"])}</p>'
             f'<h1>{e(BOOK["cover_title"]).replace(chr(10), "<br/>")} <span>English</span></h1>'
             f'<p class="subtitle">{e(BOOK["tagline"])}</p>'
             f'<img class="cover-art" src="{art}" alt="{e(BOOK["art_alt"])}"/>'
             '<div class="cover-author"><p class="author">Phil Stilwell</p>'
             f'<p class="copyright">{e(COPYRIGHT)}<br/>{e(NOTICE)}</p></div>'
             '<p class="cover-description">Eight practical lessons. Eleven extended conversations.<br/>'
             'Vocabulary, phrase banks, guided speaking, and explained answers.</p>'
             f'<p class="edition">{e(EDITION)} / Upper-intermediate to advanced</p>')
    sheet('cover', 'Learner book', cover, kind='cover industry-cover')
    rows = ''.join(f'<li>{unit_ref(i, str(i).zfill(2) + "  " + u["title"])}<p>{e(u["skill"])}</p></li>'
                   for i, u in enumerate(UNITS, 1))
    content = '<h2>Your route through the book</h2><ol class="contents">' + rows + '</ol>'
    content += '<div class="contents-extra">' + ''.join(ref(target, title) for target, title in [
        ('culture', 'Professional communication notes'), ('additional-1', 'Three additional workplace cases'),
        ('key-u1-a', 'Answers and explanations'), ('phrase-finder', 'Phrase finder'),
        ('index', 'Vocabulary index'), ('sources', 'References and publication notes')]) + '</div>'
    content += para('Suggested study range: B2-C1. This is an editorial study range, not a certified proficiency assessment.', 'small')
    sheet('contents', 'Book map', content, kind='contents-page')
    content = f'<h2>{e(BOOK["notes_title"])}</h2>' + para(BOOK['notes_intro'])
    content += '<dl class="field-notes">' + ''.join(
        f'<div><dt>{e(title)}</dt><dd>{e(explanation)}{para(example)}</dd></div>'
        for title, explanation, example in BOOK['field_notes']) + '</dl>'
    content += '<aside class="note"><h3>Professional boundaries</h3>' + para(BOOK['scope_note']) + '</aside>'
    sheet('culture', 'Professional field notes', content)


def case_page(u):
    n = u['number']
    rows = ''.join('<tr>' + ''.join(f'<td>{e(c)}</td>' for c in row) + '</tr>' for row in u['artifact_rows'])
    table = (f'<table class="artifact"><caption>{e(u["artifact_title"])}</caption><thead><tr>'
             + ''.join(f'<th scope="col">{e(c)}</th>' for c in u['artifact_headers']) + '</tr></thead><tbody>' + rows + '</tbody></table>')
    if BOOK:
        table = '<aside class="case-facts"><h3>' + e(u['scene']) + '</h3>' + para(u['brief']) + '</aside>'
    content = f'<p class="eyebrow">Lesson {n:02d} / {e(u["title"])}</p>' + label('A', 'Read the situation')
    content += para(u['skill'], 'lead') + table
    content += para('People: ' + '; '.join(f'{name}, {role}' for name, role in u['cast']) + '.', 'small')
    content += '<h3>Read the record</h3>' + para('Choose one answer per question using the facts above.', 'instruction')
    content += mcqs(u['checks'], f'u{n}-a-q', f'key-u{n}-a')
    sheet(f'u{n}-a', f'Lesson {n:02d} / Situation', content, unit=n, kind='case-page')


def vocabulary_pages(u):
    n = u['number']
    for part in range(2):
        terms = u['vocabulary'][part * 12:(part + 1) * 12]
        content = label('B', 'Vocabulary in use' if not part else 'Precision and professional shorthand')
        content += para('Core terms' if not part else 'Extend your range', 'eyebrow')
        content += '<dl class="vocabulary">' + ''.join(
            f'<div id="term-u{n}-{part * 12 + i}"><dt>{e(term)}</dt><dd>{e(definition)}'
            f'<span class="collocation">{e(collocation)}</span></dd></div>'
            for i, (term, definition, collocation) in enumerate(terms)) + '</dl>'
        content += '<section class="stress"><h3>Say it in context</h3>'
        content += para(u.get('focus_instruction', 'Capitals show the stressed syllable, not a full pronunciation spelling.'), 'small')
        for term, stress, example, contrast in u['focus'][part * 2:(part + 1) * 2]:
            content += f'<div><h4>{e(term)} <span>{e(stress)}</span></h4>{para(example)}{para(contrast, "small")}</div>'
        content += '</section>'
        sheet(f'u{n}-b{part + 1}', f'Lesson {n:02d} / Vocabulary', content, unit=n, kind='vocab-page')


def phrase_page(u):
    n = u['number']
    content = label('C', 'Phrases that move the work forward')
    content += '<dl class="phrases">' + ''.join(
        f'<div><dt>{e(function)}</dt><dd>{e(phrase)}</dd></div>' for function, phrase in u['phrases']) + '</dl>'
    content += '<section class="register"><h3>' + e(u.get('register_heading', 'Same purpose, different register')) + '</h3>'
    for a, b, c, d in u['registers']:
        content += f'<p><b>{e(a)}:</b> {e(b)}<br/><b>{e(c)}:</b> {e(d)}</p>'
    content += '</section>'
    sheet(f'u{n}-c', f'Lesson {n:02d} / Phrase bank', content, unit=n, kind='phrase-page')


def choice_page(u):
    n = u['number']
    content = label('D', 'Choose the response that fits')
    content += para('Choose one response for each situation. Preserve the facts, the decision boundary, and the purpose of the exchange.', 'instruction')
    content += mcqs(u['choices'], f'u{n}-d-q', f'key-u{n}-d')
    content += '<aside class="note"><h3>One useful distinction</h3>' + para(u['precision']) + '</aside>'
    sheet(f'u{n}-d', f'Lesson {n:02d} / Response choices', content, unit=n, kind='choices-page')


def dialogue_pages(scene, anchor, section, title, setup, key, unit=None):
    content = label('E', 'Conversation') if unit else '<h2>Conversation</h2>'
    content += f'<h3 class="scene-title">{e(title)}</h3>' + para(setup, 'scene-setup')
    content += para('Complete the numbered gaps. Use each bank entry once; some entries contain several words.', 'instruction')
    content += bank(scene, anchor) + turns(scene, 0, 10)
    content += para('Conversation continues on the next page.', 'small continuation')
    sheet(anchor, section, content, unit=unit, kind='conversation-page')
    content = f'<h2>{e(title)}</h2>' + para('Conversation / continued', 'eyebrow') + turns(scene, 10, 20)
    content += answer_strip(scene, key)
    sheet(anchor + '-continued', section, content, unit=unit, kind='conversation-page')


def transfer_pages(u):
    n = u['number']
    content = label('F', 'Check accuracy and scope' if BOOK else 'Repair the message') + f'<h3 class="scene-title">{e(u.get("repair_title", u["transfer_title"]))}</h3>'
    content += '<aside class="case-facts"><h3>' + ('Return to the case' if BOOK else 'New case / facts you can use') + '</h3>' + para(u.get('repair_facts', u['transfer_facts'])) + '</aside>'
    content += para('Choose one answer per question. Use the case facts and keep any uncertainty or limits intact.' if BOOK else 'Choose the correction that preserves the supplied facts. Say the complete corrected message aloud.', 'instruction')
    content += mcqs(u['repair'], f'u{n}-f-q', f'key-u{n}-f')
    content += '<aside class="note"><h3>Listen for the distinction</h3>' + para(u['delivery']) + '</aside>'
    content += f'<aside class="note"><h3>{e(u["culture"][0])}</h3>{para(u["culture"][1])}</aside>'
    sheet(f'u{n}-f', f'Lesson {n:02d} / Repair', content, unit=n, kind='repair-page')
    content = label('F', 'Say it / transfer to a new case' if BOOK else 'Say it / then change one fact')
    content += para(u['transfer_title'], 'scene-title') + para(u['transfer_facts'], 'scene-setup')
    content += para('Complete the four gaps. With a partner, read alternate roles, then switch. Studying alone, read both roles and pause before each response.', 'instruction')
    content += bank(u['transfer'], f'u{n}-transfer') + turns(u['transfer'], 0, 6)
    content += answer_strip(u['transfer'], f'key-u{n}-transfer')
    content += '<h3 class="second-take">' + ('Rebuild the exchange' if BOOK else 'Second take') + '</h3>'
    content += para('Choose the missing response. Read the completed three-turn exchange aloud, changing roles on the second reading.' if BOOK else 'Choose the updated response, then say it without looking at the options. Retain every fact in the correct response.', 'instruction')
    content += mcqs([u['second_take']], f'u{n}-second-q', f'key-u{n}-second')
    sheet(f'u{n}-transfer', f'Lesson {n:02d} / Guided speaking', content, unit=n, kind='transfer-page')


def checkpoint(c, idx):
    content = f'<h2>{e(c["title"])}</h2>' + para('Use language from the lessons you have completed. Choose one answer per question.', 'instruction')
    content += '<aside class="case-facts"><h3>Case file</h3>' + para(c['facts']) + '</aside>'
    content += mcqs(c['questions'], f'review-{idx}-q', f'key-review-{idx}')
    sheet(f'review-{idx}', f'Cumulative review / Lessons 1-{c["after"]}', content, kind='review-page')


def additional_pages():
    for i, s in enumerate(SUPPLEMENTS, 1):
        if BOOK is not None:
            content = '<h2>Language for the next case</h2>' + para(s['title'], 'scene-title')
            content += '<dl class="vocabulary case-vocabulary">'
            for j, gap in enumerate(s['gaps']):
                speaker, line = s['dialogue'][gap['turn'] - 1]
                complete = re.sub(r'\{\{(\d+)\}\}', lambda m: s['gaps'][int(m[1]) - 1]['answer'], line)
                content += (f'<div id="term-additional-{i}-{j}"><dt>{e(gap["answer"])}</dt>'
                            f'<dd>{e(gap["reason"])}<span class="collocation">{e(speaker)}: {e(complete)}</span></dd></div>')
            content += '</dl>' + para('Read the phrases aloud. Then complete the conversation on the following pages using the word bank.', 'instruction')
            sheet(f'additional-language-{i}', f'Additional case {i} / Language', content, kind='vocab-page')
        dialogue_pages(s, f'additional-{i}', f'Additional case {i}', s['title'], s['setup'], f'key-additional-{i}')
        content = f'<h2>{e(s["transfer"]["title"])}</h2>' + para(s['transfer']['setup'], 'scene-setup')
        content += para('Complete the exchange using each phrase once. Read both roles, then switch roles and repeat with the bank covered.', 'instruction')
        content += bank(s['pilot_transfer'], f'additional-transfer-{i}') + turns(s['pilot_transfer'], 0, 6)
        content += answer_strip(s['pilot_transfer'], f'key-additional-transfer-{i}')
        content += '<aside class="note"><h3>Keep the distinction audible</h3>' + para(s.get('delivery') or [
            'Contrast adding a group with replacing one. Name the reduced Friday deliverable separately from the full analysis. Tuesday is a scheduling update, not a promised completion date.',
            'Separate accurate results from incomplete credit. Name each person\'s contribution. Do not make public praise a condition of receiving proper attribution.',
            'Contrast paused with canceled. Keep the new date open until the evidence and release criteria support a decision. Do not imply that all completed work is invalid.',
        ][i - 1]) + '</aside>'
        sheet(f'additional-transfer-{i}', f'Additional case {i} / Transfer', content, kind='transfer-page')


def key_questions(items, keyprefix, returnto, group, heading=''):
    blocks = []
    for i, item in enumerate(items, 1):
        correct = item['answer']
        rows = ''.join(f'<li><b>{LETTERS[j]} {"Correct" if j == correct else "Not here"}.</b> {e(reason)}</li>'
                       for j, reason in enumerate(item['reasons']))
        explanation = ('<ul class="rationales">' + rows + '</ul>' if not item.get('shared_explanation')
                       else para(item['shared_explanation']))
        intro = f'<h3 class="key-group" id="{keyprefix}">{e(heading)}</h3>' if i == 1 else ''
        blocks.append(f'<article class="key-entry flow-block" id="{keyprefix}-q{i}">{intro}'
                      f'<h3>{e(group)}{i}. {e(item["prompt"])}</h3>'
                      f'<p class="correct-response">{LETTERS[correct]}. {e(item["options"][correct])}</p>'
                      f'{explanation}'
                      f'<p class="back-link">{ref(returnto, "Return to the exercise")}</p></article>')
    return ''.join(blocks)


def key_gaps(scene, keyprefix, returnto, group='', heading='', complete_lines=False):
    blocks = []
    for i, gap in enumerate(scene['gaps'], 1):
        speaker, line = scene['dialogue'][gap['turn'] - 1]
        complete = re.sub(r'\{\{(\d+)\}\}', lambda m: scene['gaps'][int(m[1]) - 1]['answer'], line)
        intro = f'<h3 class="key-group" id="{keyprefix}">{e(heading)}</h3>' if i == 1 else ''
        excerpt = f'<p class="complete-line"><b>{e(speaker)}:</b> {e(complete)}</p>' if complete_lines else ''
        back = f'<p class="back-link">{ref(returnto, "Return to the conversation")}</p>' if i == len(scene['gaps']) else ''
        blocks.append(f'<article class="key-entry gap-key flow-block" id="{keyprefix}-{i}">{intro}'
                      f'<h3>{e(group)}{i}. {e(gap["answer"])}</h3>'
                      f'{excerpt}<p><b>Turn {gap["turn"]}.</b> {e(gap["reason"])}</p>{back}</article>')
    return ''.join(blocks)


def flowing_page(anchor, title, items, *, unit=None, kind='key-page', section='Answers and explanations'):
    sheet(anchor, section, f'<h2 class="flow-heading">{e(title)}</h2><div class="flow-items">{items}</div>',
          unit=unit, kind=kind, flow=True)


def answers():
    for u in UNITS:
        n = u['number']
        items = ''
        for group, key, heading in [('a', 'checks', 'A / Read the situation'), ('d', 'choices', 'D / Response choices')]:
            target = f'key-u{n}-{group}'
            items += key_questions(u[key], target, f'u{n}-{group}', group.upper(), heading)
        items += key_gaps(u, f'key-u{n}-e', f'u{n}-e', heading='E / Conversation')
        items += key_questions(u['repair'], f'key-u{n}-f', f'u{n}-f', 'F', 'F / Accuracy and scope' if BOOK else 'F / Repair the message')
        target = f'key-u{n}-transfer'
        items += key_gaps(u['transfer'], target, f'u{n}-transfer', heading='F / Guided speaking', complete_lines=BOOK is not None)
        items += key_questions([u['second_take']], f'key-u{n}-second', f'u{n}-transfer', '', 'F / Rebuild the exchange' if BOOK else 'F / Second take')
        flowing_page(f'key-u{n}', f'{n:02d} / Answers and explanations', items, unit=n)
    for i, c in enumerate(CHECKPOINTS, 1):
        flowing_page(f'key-review-section-{i}', f'Review {i} / Explanations',
                     key_questions(c['questions'], f'key-review-{i}', f'review-{i}', '', 'Cumulative review'))
    for i, s in enumerate(SUPPLEMENTS, 1):
        items = key_gaps(s, f'key-additional-{i}', f'additional-{i}', heading='Extended conversation')
        items += key_gaps(s['pilot_transfer'], f'key-additional-transfer-{i}', f'additional-transfer-{i}', heading='Transfer exchange', complete_lines=BOOK is not None)
        flowing_page(f'key-additional-section-{i}', f'Additional case {i} / Explanations', items)


def reference_pages():
    blocks = []
    for u in UNITS:
        # Select existing phrases, with their specific job, rather than duplicate
        # a generic full phrase page throughout the course.
        phrases = ''.join(f'<p><b>{e(f)}:</b> {e(p)}</p>' for f, p in u['phrases'][:3])
        blocks.append(f'<section class="flow-block finder-entry"><h3>{e(u["title"])}</h3>'
                      + phrases + ref(f'u{u["number"]}-c', 'Full phrase bank') + '</section>')
    flowing_page('phrase-finder', 'Find a phrase by purpose', ''.join(blocks), kind='finder-page', section='Phrase finder')
    entries = defaultdict(list)
    for u in UNITS:
        for i, (term, definition, collocation) in enumerate(u['vocabulary']):
            entries[term.casefold()].append((term, f'term-u{u["number"]}-{i}', u['number']))
    if BOOK is not None:
        for i, s in enumerate(SUPPLEMENTS, 1):
            for j, gap in enumerate(s['gaps']):
                term = gap['answer']
                entries[term.casefold()].append((term, f'term-additional-{i}-{j}', f'Case {i}'))
    items = []
    for key in sorted(entries):
        term = entries[key][0][0]
        refs = ', '.join(f'<a href="#{anchor}">{("Lesson " + str(n).zfill(2)) if isinstance(n, int) else n}<span class="print-reference">, p. <span data-page-ref="{anchor}"></span></span></a>'
                         for _, anchor, n in entries[key])
        items.append(f'<p class="index-entry flow-block"><b>{e(term)}</b><span>{refs}</span></p>')
    flowing_page('index', 'Vocabulary index', ''.join(items), kind='index-page', section='Vocabulary index')
    references = [
        ('1', 'Council of Europe. Common European Framework of Reference for Languages: Mediation.',
         'https://www.coe.int/en/web/common-european-framework-reference-languages/mediation',
         'Background for collaborative meaning-making and communication across linguistic or cultural barriers. The lesson cases and the B2-C1 study range are editorial choices, not Council of Europe endorsements.'),
        ('2', 'Center for Creative Leadership. Use SBI (Situation-Behavior-Impact) to Inquire About Intent.',
         'https://www.ccl.org/articles/leading-effectively-articles/closing-the-gap-between-intent-vs-impact-sbii/',
         'The Situation-Behavior-Impact framework is attributed to the Center for Creative Leadership. Lesson 6 practices a related distinction between observed behavior, effect, and unverified assumptions about motive; its dialogue is original.'),
        ('3', 'Edmondson, Amy. 1999. Psychological Safety and Learning Behavior in Work Teams. Administrative Science Quarterly 44(2): 350-383. DOI: 10.2307/2666999.',
         'https://dash.harvard.edu/entities/publication/13a7b031-0fdd-45ec-a7e0-2b80e2bc679f',
         'Background on interpersonal risk and team learning. This study does not establish national personality types or imply that effective teams never disagree.'),
    ]
    if BOOK is not None:
        references = [(str(i), s['title'], s['url'], s['note'] + ' Source checked ' + s['checked'] + '.')
                      for i, s in enumerate(BOOK['sources'], 1)]
    content = '<h2>References and publication notes</h2>'
    content += para('All cases, organizations, figures, and conversations are fictional teaching material, not transcripts. Communication practice does not replace qualified advice or current workplace procedures.' + ('' if BOOK else ' References checked 14 October 2026.'))
    for number, title, url, note in references:
        content += f'<section class="source"><h3>[{number}] {e(title)}</h3>{para(note)}<p><a href="{url}">{e(url)}</a></p></section>'
    content += '<aside class="note"><h3>Companion course</h3>' + para('The website offers the eight-lesson course and related practice. This book can be used independently. No audio access or external account is needed for its exercises.') + f'<p><a href="{COURSE_URL}">{COURSE_URL}</a></p></aside>'
    sheet('sources', 'References', content, kind='sources-page')
    content = '<h2>' + e(BOOK['tagline'] if BOOK else 'Speak clearly. Keep the relationship.') + '</h2>'
    content += para(BOOK['map_intro'] if BOOK else 'A strong leader can question an estimate, correct a record, refuse an unsupported promise, and still leave room for the other person to contribute. The language in this book makes those choices explicit.', 'lead')
    closing_points = [(u['title'], u['precision']) for u in UNITS[:4]] if BOOK else [
        ('Name the claim', 'Ask which assumption or piece of evidence is being challenged.'),
        ('Keep the distinction', 'Separate understanding from approval, a target from a commitment, and a concern from a confirmed fault.'),
        ('Close the loop', 'Name the action, the owner, the deadline, and the next decision.'),
        ('Repair the record', 'Correct the same audience that received the mistake; do not require immediate reassurance.'),
    ]
    content += '<div class="closing-grid">' + ''.join(f'<section><h3>{e(title)}</h3>{para(text)}</section>' for title, text in closing_points) + '</div>'
    content += '<div class="publication"><p class="author">Phil Stilwell</p>' + para(COPYRIGHT) + para(NOTICE)
    content += para('English Ladder / English for Work / ' + EDITION)
    content += para('This publication includes AI-generated text and cover illustration, revised and checked during production. Brand artwork remains the English Ladder mark. This edition makes no claim of independent professional certification.')
    content += para('Typeface: Bitstream Vera, embedded under its accompanying license. Illustration created with OpenAI\'s native image generator for this edition. The copyright notice is not a claim to ownership of third-party frameworks or references.', 'small') + '</div>'
    sheet('publication', 'English Ladder', content, kind='closing-page')


def build_epub():
    """A reflowable companion uses the same semantic content, without print furniture."""
    sections = []
    for p in PAGES:
        body = ET.fromstring('<section>' + p['content'] + '</section>')
        body.set('id', p['anchor'])
        for parent in body.iter():
            for child in list(parent):
                if 'print-reference' in child.get('class', '').split():
                    parent.remove(child)
        for img in body.iter('img'):
            img.set('src', 'images/' + Path(img.get('src')).name)
        for node in body.iter():
            if isinstance(node.tag, str):
                node.attrib.pop('role', None)
        sections.append(ET.tostring(body, encoding='unicode', method='xml'))
    xhtml = ('<?xml version="1.0" encoding="utf-8"?>'
             '<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en-US" lang="en-US">'
             f'<head><title>{TITLE}</title><link rel="stylesheet" href="style.css"/></head><body>'
             + ''.join(sections) + '</body></html>')
    nav_items = [('contents', 'Contents')] + [(f'u{u["number"]}-a', u['title']) for u in UNITS] + [
        ('additional-1', 'Additional conversations'), ('key-u1-a', 'Answers and explanations'),
        ('phrase-finder', 'Phrase finder'), ('index', 'Vocabulary index'), ('sources', 'References')]
    nav = ('<?xml version="1.0" encoding="utf-8"?>'
           '<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en-US">'
           '<head><title>Contents</title></head><body><nav epub:type="toc"><h1>Contents</h1><ol>'
           + ''.join(f'<li><a href="book.xhtml#{anchor}">{e(title)}</a></li>' for anchor, title in nav_items)
           + '</ol></nav></body></html>')
    import uuid
    uid = 'urn:uuid:' + str(uuid.uuid5(uuid.NAMESPACE_URL, COURSE_URL + '/2026-book'))
    opf = f'''<?xml version="1.0" encoding="utf-8"?>
    <package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="book-id">
    <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
      <dc:identifier id="book-id">{uid}</dc:identifier><dc:title>{e(TITLE)}</dc:title>
      <dc:creator>{AUTHOR}</dc:creator><dc:language>en-US</dc:language>
      <dc:publisher>English Ladder</dc:publisher><dc:rights>{e(COPYRIGHT + ' ' + NOTICE)}</dc:rights>
      <meta property="dcterms:modified">2026-10-14T00:00:00Z</meta>
      <meta property="rendition:layout">reflowable</meta>
    </metadata><manifest>
      <item id="book" href="book.xhtml" media-type="application/xhtml+xml"/>
      <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
      <item id="css" href="style.css" media-type="text/css"/>
      <item id="cover-art" href="images/{ART.name}" media-type="image/png" properties="cover-image"/>
    </manifest><spine><itemref idref="book"/></spine></package>'''
    epub_css = '''body{font-family:serif;line-height:1.5;margin:1em;color:#202733}section{margin-bottom:2em}
    h1,h2,h3,h4,dt{font-family:sans-serif;line-height:1.25}h2{border-bottom:2px solid #245abe;padding-bottom:.3em}
    p{margin:.6em 0}img{max-width:100%;height:auto}.cover-art{width:100%}dd{margin:.3em 0 1em}
    dt{font-weight:bold}.collocation{display:block;font-style:italic}.word-bank,.case-facts,.note{border-left:3px solid #245abe;padding:.5em 1em;margin:1em 0}
    .blank{display:inline-block;min-width:7em;border-bottom:1px solid}sup{font-size:.75em}.cloze{white-space:nowrap}
    .option-letter,.turn-number{display:none}table{border-collapse:collapse;width:100%}td,th{border:1px solid #888;padding:.4em}
    .rationales{list-style:none;padding-left:0}.index-entry span{display:block}.publication{margin-top:3em}'''
    path = OUT / (STEM + '.epub')
    with zipfile.ZipFile(path, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        z.writestr('mimetype', 'application/epub+zip', compress_type=zipfile.ZIP_STORED)
        z.writestr('META-INF/container.xml', '<?xml version="1.0"?><container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="EPUB/package.opf" media-type="application/oebps-package+xml"/></rootfiles></container>')
        for name, data in [('book.xhtml', xhtml), ('nav.xhtml', nav), ('package.opf', opf), ('style.css', epub_css)]:
            z.writestr('EPUB/' + name, data)
        z.write(ART, 'EPUB/images/' + ART.name)
    return path


def build():
    validate()
    PAGES.clear()
    front()
    for u in UNITS:
        case_page(u)
        vocabulary_pages(u)
        phrase_page(u)
        choice_page(u)
        dialogue_pages(u, f'u{u["number"]}-e', f'Lesson {u["number"]:02d} / Conversation',
                       u['scene'], u['setting'], f'key-u{u["number"]}-e', unit=u['number'])
        transfer_pages(u)
        for i, c in enumerate(CHECKPOINTS, 1):
            if c['after'] == u['number']:
                checkpoint(c, i)
    additional_pages()
    answers()
    reference_pages()
    if BOOK is not None:
        flow_industry_pages()
    OUT.mkdir(parents=True, exist_ok=True)
    html = (f'<!DOCTYPE html><html lang="en-US"><head><meta charset="utf-8"/>'
            f'<title>{TITLE} | {EDITION}</title><meta name="author" content="{AUTHOR}"/>'
            f'<meta name="description" content="{e(SUBTITLE)}"/>'
            f'<link rel="stylesheet" href="../../books/leadership_pilot.css"/></head><body><main>'
            + ''.join(render_sheet(p) for p in PAGES) + '</main></body></html>')
    (OUT / (STEM + '.html')).write_text(html)
    manifest = dict(title=TITLE, edition=EDITION, source_hash=source_hash(),
                    source_pages=len(PAGES), vocabulary_entries=sum(len(u['vocabulary']) for u in UNITS),
                    distinct_terms=len({v[0].casefold() for u in UNITS for v in u['vocabulary']}),
                    distinct_phrases=len({p[1] for u in UNITS for p in u['phrases']}),
                    additional_language_entries=sum(len(s['gaps']) for s in SUPPLEMENTS) if BOOK else 0,
                    illustration_asset=ART.relative_to(ROOT).as_posix(),
                    illustration_sha256=hashlib.sha256(ART.read_bytes()).hexdigest(),
                    extended_dialogues=11, short_transfers=11, core_questions=80, cumulative_questions=16,
                    external_expert_review=False, learner_pilot=False, physical_proof=False)
    (OUT / (STEM + '-manifest.json')).write_text(json.dumps(manifest, indent=2) + '\n')
    if BOOK is None:
        build_epub()
    print(f'Built {len(PAGES)} source sections; print step will paginate answer keys and index.')


def source_hash():
    return hashlib.sha256(Path(__file__).read_bytes() + CSS.read_bytes() +
                          (ROOT / 'print_leadership_pilot.cjs').read_bytes() + ART.read_bytes() +
                          json.dumps([UNITS, SUPPLEMENTS, CHECKPOINTS, BOOK], sort_keys=True).encode()).hexdigest()


def flow_industry_pages():
    """Longer field-specific language earns space instead of smaller type."""
    def markup(node):
        text = ET.tostring(node, encoding='unicode', method='xml', short_empty_elements=False)
        return re.sub(r'<(br|img)([^>]*)></\1>', r'<\1\2/>', text)

    for page in PAGES:
        if page['flow'] or page['anchor'] == 'cover':
            continue
        tree = ET.fromstring('<div>' + page['content'] + '</div>')
        blocks = []
        heading = None
        for node in list(tree):
            if heading is None and node.tag == 'h2':
                node.set('class', (node.get('class', '') + ' flow-heading').strip())
                heading = markup(node)
            elif node.tag == 'ol' and node.get('class') == 'dialogue':
                for turn in list(node):
                    wrapper = ET.Element('ol', {'class': 'dialogue'})
                    wrapper.append(turn)
                    blocks.append(markup(wrapper))
            elif node.tag == 'dl' and any(c in node.get('class', '').split() for c in ('vocabulary', 'phrases')):
                children = list(node)
                for offset in range(0, len(children), 2):
                    wrapper = ET.Element('dl', node.attrib)
                    wrapper.extend(children[offset:offset + 2])
                    blocks.append(markup(wrapper))
            elif node.tag == 'ol' and node.get('class') == 'contents':
                for item in list(node):
                    wrapper = ET.Element('ol', {'class': 'contents'})
                    wrapper.append(item)
                    blocks.append(markup(wrapper))
            else:
                blocks.append(markup(node))
        if heading is None:
            raise ValueError('No heading for flowing section: ' + page['anchor'])
        grouped, pending = [], []
        for block in blocks:
            pending.append(block)
            if re.match(r'<h[34]\b', block) or 'class="instruction"' in block or 'class="word-bank"' in block:
                continue
            grouped.append('<div class="flow-block">' + ''.join(pending) + '</div>')
            pending = []
        if pending:
            grouped.append('<div class="flow-block">' + ''.join(pending) + '</div>')
        page['content'] = heading + '<div class="flow-items">' + ''.join(grouped) + '</div>'
        page['flow'] = True


def finalize():
    from PIL import Image
    from pypdf import PdfReader, PdfWriter
    from pypdf.generic import NameObject, BooleanObject, DictionaryObject, TextStringObject
    pdf = OUT / (STEM + '.pdf')
    layout = json.loads((OUT / (STEM + '-layout.json')).read_text())
    manifest_path = OUT / (STEM + '-manifest.json')
    manifest = json.loads(manifest_path.read_text())
    reader = PdfReader(pdf)
    assert len(reader.pages) == layout['pages']
    assert reader.trailer['/Root'].get('/StructTreeRoot')
    writer = PdfWriter(clone_from=reader)
    writer.add_metadata({'/Title': TITLE + ' | ' + EDITION, '/Author': AUTHOR,
                         '/Creator': 'English Ladder', '/Subject': SUBTITLE,
                         '/Keywords': KEYWORDS})
    writer._root_object[NameObject('/Lang')] = TextStringObject('en-US')
    writer._root_object[NameObject('/ViewerPreferences')] = DictionaryObject({NameObject('/DisplayDocTitle'): BooleanObject(True)})
    writer._root_object.pop(NameObject('/Outlines'), None)
    page_map = {p['id']: p['page'] - 1 for p in layout['pageStats']}
    for title, anchor in [('Cover', 'cover'), ('Contents', 'contents'), ('Cultural field notes', 'culture')]:
        writer.add_outline_item(title, page_map[anchor])
    for u in UNITS:
        n = u['number']
        parent = writer.add_outline_item(f'{n:02d} {u["title"]}', page_map[f'u{n}-a'])
        for title, suffix in [('A Situation', 'a'), ('B Vocabulary', 'b1'), ('C Phrase bank', 'c'),
                              ('D Response choices', 'd'), ('E Conversation', 'e'), ('F Repair and speaking', 'f')]:
            writer.add_outline_item(title, page_map[f'u{n}-{suffix}'], parent=parent)
        if n % 2 == 0:
            writer.add_outline_item(f'Cumulative review {n // 2}', page_map[f'review-{n // 2}'])
    parent = writer.add_outline_item('Additional workplace cases', page_map['additional-1'])
    for i, s in enumerate(SUPPLEMENTS, 1):
        writer.add_outline_item(s['title'], page_map[f'additional-{i}'], parent=parent)
    parent = writer.add_outline_item('Answers and explanations', page_map['key-u1'])
    for n in range(1, 9):
        writer.add_outline_item(f'Lesson {n:02d}', page_map[f'key-u{n}'], parent=parent)
    for i in range(1, 5):
        writer.add_outline_item(f'Review {i}', page_map[f'key-review-section-{i}'], parent=parent)
    writer.add_outline_item('Additional-case answers', page_map['key-additional-section-1'], parent=parent)
    for title, anchor in [('Phrase finder', 'phrase-finder'), ('Vocabulary index', 'index'), ('References', 'sources')]:
        writer.add_outline_item(title, page_map[anchor])
    temporary = pdf.with_suffix('.finalizing.pdf')
    writer.write(temporary)
    temporary.replace(pdf)
    with Image.open(ART) as image:
        resolution = round(max(image.width / 4.65, image.height / 3.1), 1)
    manifest.update(pdf_pages=len(reader.pages), tagged_pdf=True, document_language='en-US',
                    cover_resolution_dpi=resolution, uniform_blank_width_points=100,
                    sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(), page_map=layout['anchors'])
    manifest_path.write_text(json.dumps(manifest, indent=2) + '\n')
    print(f'Finalized {len(reader.pages)} pages with author metadata and chapter bookmarks.')


if __name__ == '__main__':
    finalize() if '--finalize' in sys.argv else build()
