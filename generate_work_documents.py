"""Rebuild the 164 existing English for Work PDFs from one authored curriculum.

Usage: python3 generate_work_documents.py [--course manufacturing]
Dependencies: requirements-documents.txt. No network access or paid services.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import tempfile
from pathlib import Path

from PIL import Image
from pypdf import PdfReader
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, PageBreak,
                               KeepTogether, Table, TableStyle, Flowable)

from work_curriculum import ROOT, REVISION, RUBRIC, SCORE_DESCRIPTORS, load_tracks, validate_tracks, content_hash
from work_lesson_conversations import lesson_content, load_course, content_hash as conversation_content_hash, EDITION as ACTIVITY_EDITION
from work_icons import ICON_SLUGS, icon_right_trim

INK = colors.HexColor('#172c3d')
BLUE = colors.HexColor('#174c69')
MUTED = colors.HexColor('#4d606b')
LINE = colors.HexColor('#ccd6db')
PAPER = colors.HexColor('#eef3f3')
GREEN = colors.HexColor('#eaf0eb')
PAGE_W, PAGE_H = letter
MARGIN = 48
WIDTH = PAGE_W - MARGIN * 2 - 12  # ReportLab's frame has 6-point inner padding.

for name, filename in [('Work', 'Vera.ttf'), ('Work-Bold', 'VeraBd.ttf'), ('Work-Italic', 'VeraIt.ttf'), ('Work-BoldItalic', 'VeraBI.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(ROOT / 'assets/fonts' / filename)))
pdfmetrics.registerFontFamily('Work', normal='Work', bold='Work-Bold', italic='Work-Italic', boldItalic='Work-BoldItalic')

STYLES = {
    'body': ParagraphStyle('WorkBody', fontName='Work', fontSize=10.5, leading=15.2, textColor=INK, spaceAfter=8),
    'small': ParagraphStyle('WorkSmall', fontName='Work', fontSize=8.8, leading=12.5, textColor=MUTED, spaceAfter=7),
    'prompt': ParagraphStyle('WorkPrompt', fontName='Work', fontSize=9.3, leading=13.8, textColor=INK, spaceAfter=7),
    'title': ParagraphStyle('WorkTitle', fontName='Work-Bold', fontSize=30, leading=34, textColor=INK, spaceAfter=20),
    'h1': ParagraphStyle('WorkH1', fontName='Work-Bold', fontSize=20, leading=25, textColor=INK, spaceAfter=14, keepWithNext=True),
    'h2': ParagraphStyle('WorkH2', fontName='Work-Bold', fontSize=12.4, leading=16, textColor=BLUE, spaceBefore=12, spaceAfter=8, keepWithNext=True),
    'kicker': ParagraphStyle('WorkKicker', fontName='Work-Bold', fontSize=8, leading=11, textColor=BLUE, spaceAfter=12, tracking=1),
    'quote': ParagraphStyle('WorkQuote', fontName='Work', fontSize=11.3, leading=16.5, textColor=INK, spaceAfter=7),
    'term': ParagraphStyle('WorkTerm', fontName='Work-Bold', fontSize=10.5, leading=14, textColor=BLUE, spaceAfter=3, keepWithNext=True),
}


def clean(text):
    return str(text).translate(str.maketrans({'\u2011':'-', '\u2013':'-', '\u2014':' - ', '\u2018':"'", '\u2019':"'", '\u201c':'"', '\u201d':'"', '\u2022':'-', '\u00a0':' '}))


def p(text, style='body'):
    return Paragraph(html.escape(clean(text)), STYLES[style])


def heading(text, anchor=None):
    item = p(text, 'h1')
    if anchor:
        item.bookmark = anchor
        item.bookmark_title = clean(text)
    return item


def bullets(items):
    return [p('- ' + text) for text in items]


def box(label, text, fill=PAPER):
    table = Table([[p(label.upper(), 'kicker')], [p(text, 'quote')]], colWidths=[WIDTH])
    table.setStyle(TableStyle([('FONTNAME',(0,0),(-1,-1),'Work'),('BACKGROUND',(0,0),(-1,-1),fill),('LEFTPADDING',(0,0),(-1,-1),16),
                               ('RIGHTPADDING',(0,0),(-1,-1),16),('TOPPADDING',(0,0),(-1,0),14),
                               ('BOTTOMPADDING',(0,-1),(-1,-1),12)]))
    return KeepTogether([table, Spacer(1, 10)])


class WritingLines(Flowable):
    def __init__(self, count=4, spacing=23):
        Flowable.__init__(self)
        self.width, self.height = WIDTH, count * spacing
        self.count, self.spacing = count, spacing

    def draw(self):
        self.canv.setStrokeColor(LINE)
        self.canv.setLineWidth(.45)
        for i in range(self.count):
            self.canv.line(0, self.height - (i + 1) * self.spacing + 5, WIDTH, self.height - (i + 1) * self.spacing + 5)


class WorkCanvas(Canvas):
    def __init__(self, *args, **kwargs):
        # Avoid even an unused standard-font resource: all font programs embed.
        kwargs['initialFontName'] = 'Work'
        kwargs['invariant'] = 1
        super().__init__(*args, **kwargs)


class WorkDocument(SimpleDocTemplate):
    def afterFlowable(self, flowable):
        if hasattr(flowable, 'bookmark'):
            self.canv.bookmarkPage(flowable.bookmark)
            self.canv.addOutlineEntry(flowable.bookmark_title, flowable.bookmark, level=0)


def decorate(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(.6)
    canvas.line(MARGIN, PAGE_H - 39, PAGE_W - MARGIN, PAGE_H - 39)
    canvas.setFillColor(MUTED)
    canvas.setFont('Work', 7.5)
    label = doc.course_title
    while pdfmetrics.stringWidth(label, 'Work', 7.5) > WIDTH - 115:
        label = label[:-4] + '...'
    canvas.drawString(MARGIN, PAGE_H - 29, label)
    canvas.drawRightString(PAGE_W - MARGIN, PAGE_H - 29, doc.kind)
    canvas.line(MARGIN, 39, PAGE_W - MARGIN, 39)
    canvas.drawImage(str(ROOT / 'assets/brand/ladder-mark.png'), MARGIN, 16, width=16, height=16, mask='auto')
    canvas.drawString(MARGIN + 23, 21, 'English Ladder  |  English for Work')
    canvas.drawRightString(PAGE_W - MARGIN, 21, f'{getattr(doc, "revision", REVISION)}  |  {doc.page}')
    canvas.restoreState()


class ProfessionIllustration(Flowable):
    """Embed only the selected atlas cell so downloads do not carry all 41 icons."""
    def __init__(self, slug, size=72):
        super().__init__()
        self.slug = slug
        self.width = self.height = size

    def draw(self):
        index = ICON_SLUGS.index(self.slug)
        size = self.width
        canvas = self.canv
        fraction = 1 - icon_right_trim(self.slug) / 104
        with Image.open(ROOT / 'assets/work/professional-icons.png') as atlas:
            cell_w, cell_h = atlas.width / 7, atlas.height / 6
            left, top = (index % 7) * cell_w, (index // 7) * cell_h
            cell = atlas.crop((round(left), round(top), round(left + cell_w * fraction), round(top + cell_h)))
            canvas.drawImage(ImageReader(cell), 0, 0, width=size * fraction, height=size, mask='auto')


def cover(t, kind, purpose):
    title = Table([[p(t['title'], 'title'), ProfessionIllustration(t['slug'])]], colWidths=[WIDTH - 90, 90])
    title.setStyle(TableStyle([('FONTNAME', (0, 0), (-1, -1), 'Work'),
                               ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                               ('LEFTPADDING', (0, 0), (-1, -1), 0),
                               ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                               ('BOTTOMPADDING', (0, 0), (-1, -1), 12)]))
    return [Spacer(1, 27), p('ENGLISH FOR WORK / SEPTEMBER 2026', 'kicker'), title,
            p(kind, 'h1'), p(purpose, 'quote'), Spacer(1, 20),
            box('Practice that transfers to work', 'Read a realistic case. Study complete conversations. Find the right language, speak, get feedback, and try again.', GREEN),
            p('Eight lessons | Intermediate to advanced | Independent or classroom study', 'small'),
            p('For ' + t['roles'].rstrip('.') + '.'), Spacer(1, 20),
            p(t['scope_note'], 'small'),
            p('All scenarios, figures, and model responses are fictional teaching material. Use invented details in practice.', 'small'),
            Paragraph(f'<link href="https://englishladder.com/efsp-{t["slug"]}.html" color="#174c69">Open this course on English Ladder</link>', STYLES['body']),
            PageBreak()]


def course_map(t):
    from work_ai_prompts import pdf_link
    story = [heading('Your course at a glance', 'course-map'), p('Use the lesson numbers to match this document with the website and the other guides.')]
    for m in t['modules']:
        story += [p(f'{m["number"]:02d}  {m["title"]}', 'term'), p(m['workshop']['goal'], 'small')]
    story += [p('Choose your pace', 'h2'), p('Quick practice: spend 15 minutes reading one conversation and rehearsing one scenario. Full lesson: allow 45-60 minutes for language work, three conversations, two speaking scenarios, and feedback.'),
              p('Level support', 'h2'), p('B1 learners can use the frames and a partner. B2 learners can try a response before reading the model. C1 learners can add the harder follow-up and reduce preparation time. These are teaching suggestions, not certified CEFR level ratings.'),
              pdf_link(t, 'roleplay', 'module-1', 'After practicing: open the AI prompt workshop, or use the prompts at the end of this guide.'), PageBreak()]
    return story


def reference_page(t):
    story = [heading('Use the language responsibly', 'references'), p(t['scope_note']),
             p('Meaning before performance', 'h2'), p('Use specialist terms only when they help the listener. Explain unfamiliar words, preserve uncertainty, and ask when an instruction or responsibility is unclear. The model responses illustrate language; they do not authorize professional actions.'),
             p('Sources and further reading', 'h2'), p('The cases, workshops, and explanations are original teaching material. These references provide language frameworks and selected professional context. References were checked in September 2026; consult current local guidance for actual work.', 'small')]
    for source in t['sources']:
        story += [Paragraph(f'<link href="{html.escape(source["url"],quote=True)}" color="#174c69">{html.escape(source["title"])}</link>', STYLES['body']), p(source['url'], 'small')]
    story += [p('Your next step', 'h2'), p('Choose one expression you can use in a genuine work situation. Rehearse it with fictional details, then adapt the wording to your role and audience.')]
    return story


def assessment_page():
    story = [heading('Give feedback that helps', 'assessment'), p('Score each criterion 0, 1, or 2. This is a practice rubric, not a professional qualification or CEFR test. Do not award or remove points for a particular accent.')]
    for name, criterion in RUBRIC:
        story += [p(name, 'h2'), p(criterion)]
    story += [p('Use the same scale for each criterion', 'h2')]
    for score, label, description in SCORE_DESCRIPTORS:
        story += [p(f'{score} - {label}: {description}')]
    story += [p('Feedback sequence', 'h2'), p('First, identify a successful phrase. Next, identify one point where meaning or accuracy needs work. Offer one useful language correction, allow a repeat, and compare the two attempts. A total out of eight describes this performance only; do not translate it into a proficiency level.'),
              p('Final challenge', 'h2'), p('Choose a case not rehearsed today. The learner gives a one-minute response, answers two follow-up questions, and writes a 70-110 word message. Add the lesson\'s second-round challenge. Compare the result with an earlier attempt using the four criteria.')]
    return story


def teacher(t):
    from work_ai_prompts import pdf_link
    story = cover(t, "Teacher's guide", 'Teach practical workplace communication with specific cases, clear language targets, and a repeatable feedback process.')
    story += course_map(t)
    story += [heading('A 60-minute lesson that works', 'teaching-plan'), p('Prepare the case and the learner pages. Keep the model response hidden until learners have attempted their own. Choose two field terms that are important to understanding the case.')]
    steps = [('0-5 minutes', 'Activate experience', 'Ask learners to name a comparable situation without sharing confidential details. Introduce the communication goal.'),
             ('5-12 minutes', 'Read and sort facts', 'Read the case. Learners identify confirmed facts, unknowns, the audience, and the immediate communication need.'),
             ('12-22 minutes', 'Notice and practice language', 'Explain the workshop pattern. Work through the vocabulary and editing example, then discuss both language checks and the reasons behind the choices.'),
             ('22-35 minutes', '05 · Conversations', 'Read one ten-turn conversation aloud, notice a useful expression, then compare the other two. Identify each speaker\'s purpose and how the exchange ends.'),
             ('35-47 minutes', '06 · Say it', 'Rehearse both speaking scenarios from the workbook. Give two minutes of preparation, switch roles, and use the success checks. Add the complication only after a successful first round.'),
             ('47-55 minutes', 'Compare and revise', 'Reveal the model. Discuss alternative acceptable wording. Give one meaning correction and one language correction, then repeat.'),
             ('55-60 minutes', 'Retrieve and transfer', 'Close the materials. Learners recall two expressions and identify one communication habit to use in another situation.')]
    for time, title, instruction in steps:
        story += [p(f'{time} | {title}', 'term'), p(instruction, 'small')]
    story += [p('Adapt the session', 'h2'), p('For 45 minutes, study one complete conversation and rehearse one scenario; assign the others for oral follow-up. For 90 minutes, rehearse all three conversations and give both scenarios a second round. More time should produce more meaningful practice, not longer explanations.'), PageBreak()]
    for m in t['modules']:
        w = m['workshop']
        story += [p(f'LESSON {m["number"]:02d} / FACILITATOR NOTES', 'kicker'), heading(m['title'], m['id']),
                  p(w['goal']), box('Case', m['brief']), p('Teach this move', 'h2'), p(w['explanation']),
                  p('Vocabulary to check: ' + ', '.join(m['terms']) + '.', 'small'),
                  p('Model response', 'h2'), p(m['model'], 'quote'),
                  p('Listen for, then coach', 'h2'), p('Ask learners to point to the case fact behind each important statement. Accept different wording when it preserves meaning, fits the listener, and does not invent an outcome. ' + w['reason'], 'small'),
                  p('Second-round challenge', 'h2'), p(w['challenge'], 'small'),
                  p('Language-check answers', 'h2')]
        for i, q in enumerate(w['questions']):
            story += [p(f'{i+1}. {chr(65+q["correct_index"])} - {q["answer"]} ' + q['feedback'][q['correct_index']], 'small')]
        activities = lesson_content(t, m)
        story += [p('05 · Conversations', 'h2'), *[p(f'{i}. {d["title"]} - {d["setting"]}', 'small') for i, d in enumerate(activities['conversations'], 1)],
                  p('Use the complete ten-turn scripts in the learner workbook and conversation lab. Read with roles, identify the decision or open question, then replay without reading.', 'small')]
        story += additional_speaking_scenario(activities['additional_scenario'], '06 · Say it: second scenario')
        story += [pdf_link(t, 'teacher', m['id'], 'AI extension: adapt this lesson for your learners and available time.'), PageBreak()]
    story += assessment_page() + [PageBreak()] + reference_page(t)
    return story


def conversation_scripts(t, m):
    story = []
    for i, dialogue in enumerate(lesson_content(t, m)['conversations'], 1):
        story += [PageBreak(), p(f'LESSON {m["number"]:02d} / 05 · CONVERSATIONS / {i} OF 3', 'kicker'),
                  heading(dialogue['title'], f'{m["id"]}-conversation-{i}'), p(dialogue['setting'], 'small')]
        for n, (role, speech) in enumerate(dialogue['turns'], 1):
            story.append(Paragraph(f'<b>{n:02d} · {html.escape(clean(role))}:</b> {html.escape(clean(speech))}', STYLES['body']))
        story += [p('Notice, then rehearse', 'h2'), p('Name each speaker\'s purpose. Identify one useful expression and the next step or unresolved question. Read the roles aloud, then switch roles.', 'small')]
    return story


def additional_speaking_scenario(scenario, label='Scenario 2'):
    return [p(label + ' | ' + scenario['title'], 'h2'), p(scenario['brief']),
            p('Role A: ' + scenario['role_a'], 'small'), p('Role B: ' + scenario['role_b'], 'small'),
            p('Possible opening: ' + scenario['opening_line'], 'quote'),
            p('Success checks', 'term'), *bullets(scenario['success_checks']),
            p('Add a complication: ' + scenario['complication'], 'small')]


def speaking_scenarios(t, m):
    return [PageBreak(), p(f'LESSON {m["number"]:02d} / 06 · SAY IT', 'kicker'),
            heading('Two scenarios to practice', f'{m["id"]}-speaking'), p('Use only the supplied facts. Prepare for two minutes, speak for one minute, then respond to a follow-up. Switch roles and repeat. For solo study, speak both roles aloud.'),
            p('Scenario 1 | ' + m['title'], 'h2'), p(m['brief']), p(m['speaking_task'], 'small'),
            p('Partner: ' + m['workshop']['role_b'], 'small'),
            p('Second round: ' + m['workshop']['challenge'], 'small'),
            p('Model for scenario 1: ' + m['model'], 'quote'),
            *additional_speaking_scenario(lesson_content(t, m)['additional_scenario'])]


def workbook(t):
    from work_ai_prompts import pdf_link
    story = cover(t, 'Learner workbook', 'Work with realistic cases, develop your own response, and use the answer section after you have tried the tasks.') + course_map(t)
    for m in t['modules']:
        w = m['workshop']
        story += [p(f'LESSON {m["number"]:02d} / READ AND NOTICE', 'kicker'), heading(m['title'], m['id']),
                  p(w['goal']), box('Situation', m['brief']),
                  p('1. Understand the situation', 'h2'), p('Identify two confirmed facts, one missing detail, and the person who needs your response. Do not fill gaps with invented facts.'), WritingLines(2),
                  p('2. Find the words', 'h2')]
        for j in m['vocabulary']:
            story += [p(j['term'] + ' - ' + j['definition'], 'small')]
        story += [p('3. Notice the language', 'h2'), p(w['explanation']), *[p(frame, 'small') for frame in w['frames']],
                  p('Improve this sentence: ' + w['before'], 'small'), WritingLines(1), PageBreak(),
                  p(f'LESSON {m["number"]:02d} / PRACTICE AND PRODUCE', 'kicker'), heading(w['title']),
                  p('4. Check the language', 'h2')]
        for i, q in enumerate(w['questions']):
            story += [p(f'{i+1}. {q["prompt"]}', 'small')]
            story += [p(f'{chr(65+j)}. {option}', 'small') for j, option in enumerate(q['options'])]
        story += [p('05 · Conversations', 'h2'), p('The next three pages contain original fictional conversations for this lesson. Each numbered line is one speaking turn. Read the setting before assigning roles.', 'small')]
        story += conversation_scripts(t, m) + speaking_scenarios(t, m)
        story += [
                  p('Check: facts accurate | meaning clear | tone appropriate | next action or question explicit', 'small'),
                  pdf_link(t, 'roleplay', m['id'], 'Continue scenario 1 with an AI partner.'), PageBreak()]
    story += [heading('Answer workshop', 'answers'), p('Try the tasks first. The model is one acceptable response to scenario 1, not a script to memorize. Assess your spoken version using the four criteria at the end.')]
    for m in t['modules']:
        w = m['workshop']
        block = [p(f'{m["number"]:02d} | {m["title"]}', 'h2'), p('Editing example: ' + w['after']), p(w['reason'], 'small')]
        for i, q in enumerate(w['questions']):
            block += [p(f'Check {i+1}: {chr(65+q["correct_index"])} - {q["answer"]}', 'term')]
            block += [p(f'{chr(65+j)}: {feedback}', 'small') for j, feedback in enumerate(q['feedback'])]
        block += [p('Model response: ' + m['model']), p('Case check: underline the confirmed information and circle a limitation, question, or next step in the response.', 'small')]
        story += [KeepTogether(block)]
    story += [PageBreak()] + assessment_page() + [PageBreak()] + reference_page(t)
    return story


def conversation(t):
    from work_dialogues import gallery
    from work_ai_prompts import url as ai_url
    story = gallery(t)
    for m in t['modules']:
        w = m['workshop']
        story += [p(f'ROLE-PLAY CASE {m["number"]:02d}', 'kicker'), heading(m['title'], m['id']), box('Shared case', m['brief']),
                  p('Role A | Responding professional', 'h2'), p(w['goal'] + ' Use only the facts given. Choose two relevant terms and be ready to explain one of them in ordinary words.'),
                  p('Role B | Listener', 'h2'), p(w['role_b']),
                  p('Useful expressions', 'h2'), *[p(frame, 'small') for frame in w['frames']],
                  p('Cover this until after your first attempt', 'h2'), p(m['model'], 'quote'),
                  p('Second round', 'h2'), p(w['challenge']),
                  Paragraph(f'<link href="{html.escape(ai_url(t, "roleplay", m["id"], True), quote=True)}" color="#174c69">Debrief and extend with AI</link>', STYLES['h2']),
                  p('Which phrase helped the listener? Which case fact needed clarification? Write one better follow-up question, then repeat the exchange.', 'small'), WritingLines(1), PageBreak()]
    story += [heading('Lesson conversations and speaking practice', 'lesson-conversations'),
              p('The following sections match 05 and 06 on the industry webpage and in the learner workbook. Each lesson has three ten-turn conversations and two bounded speaking scenarios. These are original fictional teaching scripts, not transcripts of real people.')]
    for m in t['modules']:
        story += conversation_scripts(t, m) + speaking_scenarios(t, m)
    story += assessment_page() + [PageBreak()] + reference_page(t)
    return story


def phrasebook(t):
    from work_ai_prompts import pdf_link
    story = cover(t, 'Vocabulary & phrasebook', 'Keep precise meanings and useful expressions close. Retrieve the words, then use them in a complete message.')
    story += [heading('Make vocabulary usable', 'vocabulary-method'), p('Knowing a definition is a start. To use a term well, explain it in plain English, connect it to a case, and choose a natural sentence around it.'),
              *bullets(['Read five terms, cover their definitions, and recall the meanings.', 'Sort a pair you might confuse and explain the difference.', 'Use one term in a sentence about a fictional case.', 'Ask a partner to explain the sentence without repeating the specialist word.', 'Return to the same terms on another day and test recall again.']),
              p('Abbreviations need context', 'h2'), p('Expand an abbreviation on first use when the listener needs it. Some abbreviations have different meanings across professions: API can refer to an application programming interface or an active pharmaceutical ingredient. The course context determines the meaning.'),
              p('Definitions have limits', 'h2'), p('These are concise language-learning explanations, not complete legal, clinical, or technical specifications. Use the applicable authoritative definition for regulated or operational decisions.'), PageBreak(),
              heading('Field vocabulary A-Z', 'glossary')]
    for j in sorted(t['jargon'], key=lambda j:j['term'].casefold()):
        story += [KeepTogether([p(j['term'], 'term'), p(j['definition']), Spacer(1, 4)])]
    if t.get('nomenclature'):
        story += [PageBreak(), heading('Specialist terminology', 'specialist-terms'), p('Additional semiconductor terminology grouped by technical area.')]
        category = None
        for item in t['nomenclature']:
            if item['category'] != category:
                category = item['category']; story += [p(category, 'h2')]
            story += [KeepTogether([p(item['term'], 'term'), p(item['meaning']), Spacer(1, 4)])]
    story += [PageBreak(), heading('Expressions for this course', 'expressions'), p('Complete the frames with the facts of your case. A frame helps organize meaning; it should not replace an actual explanation.')]
    seen = set()
    for m in t['modules']:
        w = m['workshop']
        if m['function'] in seen:
            continue
        seen.add(m['function'])
        story += [KeepTogether([p(w['title'], 'h2'), *[p(frame) for frame in w['frames']], p(w['explanation'], 'small')])]
    story += [PageBreak(), heading('Model responses in context', 'model-responses'), p('Read the situation first. Cover the model, say your own response, and compare the two for meaning and tone.')]
    for m in t['modules']:
        story += [KeepTogether([p(f'{m["number"]:02d} | {m["title"]}', 'h2'), p(m['brief'], 'small'), p(m['model'], 'quote'), p('Try it again: ' + m['workshop']['challenge'], 'small'),
                                pdf_link(t, 'vocabulary', m['id'], 'AI extension: build and retrieve vocabulary from this case.')])]
    story += [PageBreak()] + reference_page(t)
    return story


BUILDERS = [teacher, workbook, conversation, phrasebook]
KINDS = ["Teacher's guide", 'Learner workbook', 'Conversation lab', 'Phrasebook']


def build_track(track, kinds=None):
    from work_ai_prompts import pdf_appendix, prompt_hash, EDITION as AI_EDITION
    result = {}
    for index, (_label, href) in enumerate(track['pdfs']):
        if kinds and index not in kinds:
            continue
        path = ROOT / href
        path.parent.mkdir(parents=True, exist_ok=True)
        handle, temp = tempfile.mkstemp(suffix='.pdf', dir=path.parent)
        os.close(handle)
        try:
            doc = WorkDocument(temp, pagesize=letter, leftMargin=MARGIN, rightMargin=MARGIN,
                               topMargin=56, bottomMargin=53, title=f'{track["title"]} | {KINDS[index]}',
                               author='English Ladder', subject=f'English for Work - activity edition {ACTIVITY_EDITION}',
                               initialFontName='Work', pageCompression=1)
            doc.course_title, doc.kind = track['title'], KINDS[index]
            doc.revision = ACTIVITY_EDITION
            doc.build(BUILDERS[index](track) + pdf_appendix(track, index), onFirstPage=decorate, onLaterPages=decorate, canvasmaker=WorkCanvas)
            reader = PdfReader(temp)
            assert len(reader.pages) > 3
            os.replace(temp, path)
            result[href] = dict(course=track['slug'], kind=KINDS[index], pages=len(reader.pages),
                                bytes=path.stat().st_size, sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                                content_hash=content_hash(), ai_prompt_hash=prompt_hash(), ai_prompt_count=2, ai_prompt_edition=AI_EDITION)
            result[href]['illustration_sha256'] = hashlib.sha256((ROOT / 'assets/work/professional-icons.png').read_bytes()).hexdigest()
            result[href]['activity_edition'] = ACTIVITY_EDITION
            if index in (0, 1, 2):
                result[href]['lesson_conversation_hash'] = conversation_content_hash()
                result[href]['lesson_conversation_count'] = 24
            if index == 2:
                from work_dialogues import dialogue_hash, load_dialogues, EDITION
                result[href].update(dialogue_hash=dialogue_hash(), dialogue_count=len(load_dialogues()[track['slug']]), dialogue_edition=EDITION)
        finally:
            if os.path.exists(temp):
                os.unlink(temp)
    return result


def main(slugs=None, kinds=None):
    tracks = load_tracks()
    validate_tracks(tracks)
    if slugs:
        unknown = set(slugs) - {t['slug'] for t in tracks}
        if unknown:
            raise ValueError(f'Unknown courses: {sorted(unknown)}')
        tracks = [t for t in tracks if t['slug'] in slugs]
    if kinds is None or any(kind in (0, 1, 2) for kind in kinds):
        for track in tracks:
            load_course(track['slug'])
    manifest_path = ROOT / 'content/work/documents.json'
    documents = json.loads(manifest_path.read_text()).get('documents', {}) if (slugs or kinds) and manifest_path.exists() else {}
    for t in tracks:
        result = build_track(t, kinds)
        documents.update(result)
        print(f'{t["slug"]}: ' + ', '.join(str(v['pages']) + ' pages' for v in result.values()), flush=True)
    manifest_path.write_text(json.dumps(dict(revision=REVISION, content_hash=content_hash(), documents=documents), indent=2) + '\n')
    print(f'Built {len(tracks) * (len(kinds) if kinds else 4)} PDFs.', flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--course', action='append', help='A course slug; repeat to build several courses.')
    parser.add_argument('--kind', choices=['conversation', 'activities'], help='Rebuild Conversation Labs or all three activity-bearing guides, preserving other PDF assets.')
    args = parser.parse_args()
    main(args.course, [2] if args.kind == 'conversation' else [0, 1, 2] if args.kind == 'activities' else None)
