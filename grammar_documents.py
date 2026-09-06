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
def question(q,number):
    items=[p(f'{number}. {q["prompt"]}')]
    items.extend(p(f'{chr(65+i)}. {o["text"]}','small') for i,o in enumerate(q['options']))
    items.append(Spacer(1,14))
    return KeepTogether(items)
def build(c,teacher=False):
    story=[p(f'CONCEPT {c["number"]:02} / {c["level"]} / 10-15 MINUTES','label'),p(c['title'],'title'),p('Teaching guide' if teacher else 'Learner workbook','label'),p(c['goal']),h('Understand the distinction','understand')]
    story.extend(p(r) for r in c['rules'])
    story.append(PageBreak());story.append(h('Compare the patterns','compare'));story.extend(box(v) for v in c['cards'])
    story.append(p('Read each example and notice how its form changes the meaning. Use these distinctions to choose your answers on the following pages.'))
    story.append(PageBreak());story.append(h('Check your understanding','practice'));story.append(p('Circle one answer for each question. There is one correct choice among the options shown. Check the answer key after choosing.'))
    for i,q in enumerate(c['checks'],1):story.append(question(q,i))
    story.extend([PageBreak(),h('Choose the best response','transfer'),p('Choose the response that fits the situation. Check both its meaning and its grammar.'),question(c['application'],len(c['checks'])+1),p('Review your choices','label'),p('Use the answer explanations on the next page. If you chose a different answer, find the detail that makes it unsuitable and try the question again.'),p('Practice online','label'),p('The web lesson gives feedback for the option you select and lets you try again. No written response is required.')])
    story.extend([PageBreak(),h('Answers and explanation','answers')])
    for i,q in enumerate([*c['checks'],c['application']],1):
        answer_index=next(j for j,o in enumerate(q['options']) if o['correct']);answer=q['options'][answer_index]
        story.append(KeepTogether([p(f'{i}. {chr(65+answer_index)}. {answer["text"]}','label'),p(answer['feedback'])]))
        if teacher:
            story.extend(p(f'{chr(65+j)}: {o["feedback"]}','small') for j,o in enumerate(q['options']) if not o['correct'])
    story.extend([p('Continue learning','label'),p(f'Web lesson and related topics: englishladder.com/grammar-concepts/concept-{c["number"]:02}.html')])
    if teacher:
        story.extend([PageBreak(),h('A practical teaching sequence','teaching'),p('1. Notice (2 minutes)','label'),p('Read the comparison examples with the learners. Point out the meaning and form that distinguish each pattern.'),p('2. Choose (4 minutes)','label'),p('Learners select one option for each of the three checks. Keep the answer key covered. Use the selected option’s explanation rather than presenting a generic model as feedback.'),p('3. Apply (5 minutes)','label'),p(c['application']['prompt']),p('Learners choose the response that fits this situation. All responses in this activity are multiple choice; do not replace the choices with a written-answer task.'),p('4. Review (3 minutes)','label'),p('Compare selected options with the key. Use the option-specific notes to explain why a distractor does not fit. Let learners change their selection and try again.'),p('Scope of the answer key','label'),p('Each question has one correct option among the choices shown. This does not mean that every other way to express the idea is wrong. Preserve the qualifications in the teaching notes.'),p('Feedback criteria','label'),p('Check both grammatical form and the stated situation. A correct option answers this question; four correct choices do not certify a learner’s overall proficiency.')])
    from ai_extensions import grammar_prompts, prompt as ai_prompt
    extension=grammar_prompts(c)[0]
    if teacher:
        extension=ai_prompt('teacher',{'lesson':c['title'],'study_level':c['level'],'goal':c['goal'],'grammar_focus':c['rules'],'examples':c['cards']})
    story.extend([PageBreak(),h('Extend this lesson with AI','ai-practice'),p('Optional: copy the complete prompt below into the AI you prefer. All learner answers remain multiple choice. AI explanations can be wrong; compare them with this lesson. Your chosen service may have its own fees and privacy rules.','small'),p('This lesson also has online prompts for fresh examples, branching dialogue, and retrieval practice.','small')])
    url=f'https://englishladder.com/grammar-concepts/concept-{c["number"]:02}.html#ai-grammar'
    story.append(Paragraph(f'<link href="{url}" color="#2445eb">Open this lesson\'s AI extensions</link>',styles['body']))
    story.append(p('Copy from the next paragraph through the study material.','label'))
    instructions,material=extension['text'].split('\n\nLESSON MATERIAL\n',1)
    prompt_paragraph=lambda part: Paragraph(html.escape(clean(part)).replace('\n','<br/>'),styles['small'])
    story.extend(prompt_paragraph(part) for part in instructions.split('\n\n'))
    story.append(KeepTogether([p('LESSON MATERIAL','label'),*[prompt_paragraph(part) for part in material.split('\n\n')]]))
    folder='teachers' if teacher else 'students';name=c['pdfs'][1 if teacher else 0];path=ROOT/'pdf'/folder/name;path.parent.mkdir(parents=True,exist_ok=True)
    doc=Doc(str(path),pagesize=letter,leftMargin=54,rightMargin=54,topMargin=54,bottomMargin=54,title=c['title']+(' - Teaching guide' if teacher else ' - Learner workbook'),author='English Ladder',subject=c['goal'],initialFontName='Ladder')
    doc.build(story,onFirstPage=page,onLaterPages=page,canvasmaker=partial(Canvas,initialFontName='Ladder'))
    return path

def build_all():
    paths=[str(build(c,t).relative_to(ROOT)) for c in load_curriculum() for t in (False,True)]
    print(f'Rebuilt {len(paths)} grammar PDFs with embedded fonts and bookmarks.')
    return paths

if __name__=='__main__':build_all()
