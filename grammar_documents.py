"""Rebuild stable grammar download URLs from the reviewed local curriculum."""
import html
import json
from functools import partial
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether, Table, TableStyle
from grammar_curriculum import ROOT, load_curriculum

for name,file in [('Ladder','Vera.ttf'),('Ladder-Bold','VeraBd.ttf'),('Ladder-Italic','VeraIt.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(ROOT/'assets/fonts'/file)))
pdfmetrics.registerFontFamily('Ladder',normal='Ladder',bold='Ladder-Bold',italic='Ladder-Italic',boldItalic='Ladder-Bold')
BLUE=colors.HexColor('#2445eb'); INK=colors.HexColor('#172432'); MUTED=colors.HexColor('#526273'); LINE=colors.HexColor('#d4dce5')
styles={key:ParagraphStyle(key,fontName='Ladder-Bold' if key in ['title','heading','label'] else 'Ladder',fontSize=size,leading=leading,textColor=BLUE if key=='label' else INK,spaceAfter=10,keepWithNext=key=='heading') for key,size,leading in [('title',28,34),('heading',17,22),('body',10.5,15.5),('label',9,13),('small',9,13)]}
def clean(s):return s.translate(str.maketrans({'–':'-','—':' - ','’':"'",'‘':"'",'“':'"','”':'"','→':'to'}))
def p(s,style='body'):return Paragraph(html.escape(clean(s)),styles[style])
def h(s,key):
    item=p(s,'heading');item.bookmark=key;return item
class Doc(SimpleDocTemplate):
    def afterFlowable(self,item):
        if hasattr(item,'bookmark'):
            self.canv.bookmarkPage(item.bookmark)
            self.canv.addOutlineEntry(item.getPlainText(),item.bookmark,level=0)
def page(canvas,doc):
    canvas.saveState();canvas.setFont('Ladder-Bold',9);canvas.setFillColor(BLUE)
    canvas.drawString(54,letter[1]-30,'ENGLISH LADDER');canvas.setStrokeColor(LINE);canvas.line(54,43,558,43)
    canvas.setFont('Ladder',8);canvas.setFillColor(MUTED);canvas.drawString(54,29,'englishladder.com | Grammar | Revised September 2026');canvas.drawRightString(558,29,str(doc.page));canvas.restoreState()
def box(card):
    table=Table([[p(card['label'],'label')],[p(card['example'])],[p(card['note'],'small')]],colWidths=[492])
    table.setStyle(TableStyle([('FONTNAME',(0,0),(-1,-1),'Ladder'),('BACKGROUND',(0,0),(-1,-1),colors.HexColor('#f0f3ff')),('LEFTPADDING',(0,0),(-1,-1),14),('RIGHTPADDING',(0,0),(-1,-1),14),('TOPPADDING',(0,0),(-1,0),12),('BOTTOMPADDING',(0,-1),(-1,-1),10)]))
    return KeepTogether([table,Spacer(1,10)])
def lines(count):
    t=Table([[''] for _ in range(count)],colWidths=[492],rowHeights=25)
    t.setStyle(TableStyle([('FONTNAME',(0,0),(-1,-1),'Ladder'),('LINEBELOW',(0,0),(-1,-1),.4,LINE)]));return t
def build(c,teacher=False):
    story=[p(f'CONCEPT {c["number"]:02} / {c["level"]} / 10-15 MINUTES','label'),p(c['title'],'title'),p('Teaching guide' if teacher else 'Learner workbook','label'),p(c['goal']),h('Understand the distinction','understand')]
    story.extend(p(r) for r in c['rules'])
    story.append(PageBreak());story.append(h('Compare the patterns','compare'));story.extend(box(v) for v in c['cards'])
    story.append(p('Read each example. Explain what the highlighted choice means in context. Then cover the example and say a similar sentence.'))
    story.append(PageBreak());story.append(h('Check your understanding','practice'));story.append(p('Write before looking at the answers. The guide gives a model answer and explains the choice. Other wording can be correct.'))
    for i,q in enumerate(c['checks'],1):
        story.extend([p(f'{i}. {q["prompt"]}'),lines(2),Spacer(1,12)])
    story.extend([PageBreak(),h('Use it in your own life','transfer'),p(c['transfer']),lines(5),Spacer(1,16),p('Self-check','label'),p('Does your sentence express your intended meaning? Does its form follow the relevant pattern? Can a reader understand the context?'),p('Try again','label'),p('After checking the explanation, revise your sentence. Say it aloud or use it in a short conversation.'),lines(3)])
    story.extend([PageBreak(),h('Answers and explanation','answers')])
    for i,q in enumerate(c['checks'],1):story.extend([p(f'{i}. {q["answer"]}','label'),p(q['explanation'])])
    story.extend([p('One possible response','label'),p(c['model']),p('This is a model, not the only acceptable answer. Assess meaning, grammar, and context together.'),p('Continue learning','label'),p(f'Web lesson and related topics: englishladder.com/grammar-concepts/concept-{c["number"]:02}.html')])
    if teacher:
        story.extend([PageBreak(),h('A practical teaching sequence','teaching'),p('1. Notice (2 minutes)','label'),p('Ask learners to explain the differences between the comparison examples before reading the rules. Use their answers to identify the point that needs attention.'),p('2. Explain and check (4 minutes)','label'),p('Read the short explanation together. Keep its qualifications: a common pattern is not necessarily a rule for every context. Ask learners to give a counterexample where the lesson mentions an exception.'),p('3. Apply (5 minutes)','label'),p(c['transfer']),p('Have learners work alone, then compare with a partner. Ask the partner to restate the intended meaning before suggesting a correction.'),p('4. Review (3 minutes)','label'),p('Use the answer explanations to review the three checks. Accept natural alternatives that preserve the intended meaning. Ask each learner to revise one sentence and identify the change.'),p('Extension','label'),p('Change the person, time, place, or purpose in a comparison example. Ask whether the original pattern still fits and why. Revisit one example in the next lesson.'),p('Feedback criteria','label'),p('Meaning: the message is understandable. Form: the target pattern fits the context. Transfer: the learner can use it in a fresh example. This short activity is not a proficiency certification.')])
    folder='teachers' if teacher else 'students';name=c['pdfs'][1 if teacher else 0];path=ROOT/'pdf'/folder/name;path.parent.mkdir(parents=True,exist_ok=True)
    doc=Doc(str(path),pagesize=letter,leftMargin=54,rightMargin=54,topMargin=54,bottomMargin=54,title=c['title']+(' - Teaching guide' if teacher else ' - Learner workbook'),author='English Ladder',subject=c['goal'],initialFontName='Ladder')
    doc.build(story,onFirstPage=page,onLaterPages=page,canvasmaker=partial(Canvas,initialFontName='Ladder'))
    return path

def build_all():
    paths=[str(build(c,t).relative_to(ROOT)) for c in load_curriculum() for t in (False,True)]
    print(f'Rebuilt {len(paths)} grammar PDFs with embedded fonts and bookmarks.')
    return paths

if __name__=='__main__':build_all()
