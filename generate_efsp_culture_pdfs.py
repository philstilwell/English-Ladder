from __future__ import annotations

import html
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    HRFlowable,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = ROOT / "pdf" / "efsp"
BRAND_LOGO_PATH = ROOT / "assets" / "english-ladder-pdf-logo.png"

PAGE_WIDTH, PAGE_HEIGHT = letter
MARGIN_X = 0.68 * inch
MARGIN_TOP = 0.72 * inch
MARGIN_BOTTOM = 0.58 * inch
CONTENT_WIDTH = PAGE_WIDTH - (2 * MARGIN_X)
BRAND_LOGO_WIDTH = 0.14 * inch
BRAND_LOGO_HEIGHT = 0.2 * inch

PALETTE = {
    "paper": colors.HexColor("#FBFAF7"),
    "ink": colors.HexColor("#232523"),
    "muted": colors.HexColor("#5F6761"),
    "line": colors.HexColor("#C9D2CB"),
    "teal": colors.HexColor("#1F6F66"),
    "teal_dark": colors.HexColor("#154E49"),
    "blue": colors.HexColor("#255C99"),
    "amber": colors.HexColor("#C8842E"),
    "rose": colors.HexColor("#A94C55"),
    "green_light": colors.HexColor("#E6F1EC"),
    "blue_light": colors.HexColor("#E8F0F9"),
    "amber_light": colors.HexColor("#F7EAD8"),
    "rose_light": colors.HexColor("#F5E6E8"),
    "white": colors.HexColor("#FFFFFF"),
}


def esc(text: str) -> str:
    return html.escape(text, quote=False)


def styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    body = ParagraphStyle(
        "Body",
        parent=base["BodyText"],
        fontName="Helvetica",
        fontSize=9.4,
        leading=12.4,
        textColor=PALETTE["ink"],
        spaceAfter=6,
    )
    return {
        "CoverKicker": ParagraphStyle(
            "CoverKicker",
            parent=body,
            fontName="Helvetica-Bold",
            fontSize=10,
            leading=13,
            textColor=PALETTE["teal_dark"],
            alignment=TA_CENTER,
            spaceAfter=14,
        ),
        "CoverTitle": ParagraphStyle(
            "CoverTitle",
            parent=body,
            fontName="Helvetica-Bold",
            fontSize=25,
            leading=29,
            textColor=PALETTE["ink"],
            alignment=TA_CENTER,
            spaceAfter=12,
        ),
        "CoverSub": ParagraphStyle(
            "CoverSub",
            parent=body,
            fontSize=12.2,
            leading=16,
            textColor=PALETTE["muted"],
            alignment=TA_CENTER,
            spaceAfter=20,
        ),
        "Title": ParagraphStyle(
            "Title",
            parent=body,
            fontName="Helvetica-Bold",
            fontSize=18,
            leading=22,
            textColor=PALETTE["teal_dark"],
            spaceBefore=8,
            spaceAfter=8,
        ),
        "H1": ParagraphStyle(
            "H1",
            parent=body,
            fontName="Helvetica-Bold",
            fontSize=15.5,
            leading=19,
            textColor=PALETTE["teal_dark"],
            spaceBefore=10,
            spaceAfter=7,
        ),
        "H2": ParagraphStyle(
            "H2",
            parent=body,
            fontName="Helvetica-Bold",
            fontSize=12.5,
            leading=15.5,
            textColor=PALETTE["blue"],
            spaceBefore=8,
            spaceAfter=4,
        ),
        "H3": ParagraphStyle(
            "H3",
            parent=body,
            fontName="Helvetica-Bold",
            fontSize=10.7,
            leading=13.5,
            textColor=PALETTE["ink"],
            spaceBefore=6,
            spaceAfter=3,
        ),
        "Body": body,
        "Small": ParagraphStyle(
            "Small",
            parent=body,
            fontSize=8.3,
            leading=10.4,
            textColor=PALETTE["muted"],
            spaceAfter=4,
        ),
        "Bullet": ParagraphStyle(
            "Bullet",
            parent=body,
            leftIndent=0,
            firstLineIndent=0,
            spaceAfter=3,
        ),
        "BoxTitle": ParagraphStyle(
            "BoxTitle",
            parent=body,
            fontName="Helvetica-Bold",
            fontSize=10.5,
            leading=13,
            textColor=PALETTE["ink"],
            spaceAfter=4,
        ),
        "BoxBody": ParagraphStyle(
            "BoxBody",
            parent=body,
            fontSize=8.9,
            leading=11.5,
            spaceAfter=4,
        ),
        "TableHead": ParagraphStyle(
            "TableHead",
            parent=body,
            fontName="Helvetica-Bold",
            fontSize=8.6,
            leading=10.2,
            textColor=PALETTE["white"],
            alignment=TA_LEFT,
        ),
        "TableCell": ParagraphStyle(
            "TableCell",
            parent=body,
            fontSize=8.2,
            leading=10.1,
            spaceAfter=0,
        ),
        "CardTitle": ParagraphStyle(
            "CardTitle",
            parent=body,
            fontName="Helvetica-Bold",
            fontSize=13,
            leading=16,
            textColor=PALETTE["teal_dark"],
            spaceAfter=6,
        ),
    }


S = styles()


def p(text: str, style: str = "Body") -> Paragraph:
    return Paragraph(esc(text), S[style])


def h1(text: str) -> list:
    return [Paragraph(esc(text), S["H1"]), rule()]


def h2(text: str) -> Paragraph:
    return Paragraph(esc(text), S["H2"])


def h3(text: str) -> Paragraph:
    return Paragraph(esc(text), S["H3"])


def rule() -> HRFlowable:
    return HRFlowable(width="100%", thickness=0.8, color=PALETTE["line"], spaceBefore=2, spaceAfter=8)


def bullets(items: list[str], numbered: bool = False) -> Table:
    rows = []
    for index, item in enumerate(items, start=1):
        marker = f"{index}." if numbered else "-"
        rows.append([p(marker, "Bullet"), p(item, "Bullet")])
    out = Table(rows, colWidths=[0.28 * inch, CONTENT_WIDTH - 0.28 * inch], hAlign="LEFT")
    out.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TEXTCOLOR", (0, 0), (0, -1), PALETTE["teal"]),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 1),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
            ]
        )
    )
    return out


def box(title: str, body: list[str], tone: str = "green") -> Table:
    background = {
        "green": PALETTE["green_light"],
        "blue": PALETTE["blue_light"],
        "amber": PALETTE["amber_light"],
        "rose": PALETTE["rose_light"],
    }.get(tone, PALETTE["green_light"])
    content = [p(title, "BoxTitle")]
    content.extend(p(paragraph, "BoxBody") for paragraph in body)
    table = Table([[content]], colWidths=[CONTENT_WIDTH])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), background),
                ("BOX", (0, 0), (-1, -1), 0.7, PALETTE["line"]),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ]
        )
    )
    return table


def table(rows: list[list[str]], widths: list[float], header: bool = True) -> Table:
    converted = []
    for row_index, row in enumerate(rows):
        style_name = "TableHead" if header and row_index == 0 else "TableCell"
        converted.append([p(cell, style_name) for cell in row])
    out = Table(converted, colWidths=widths, repeatRows=1 if header else 0, hAlign="LEFT")
    commands = [
        ("BOX", (0, 0), (-1, -1), 0.6, PALETTE["line"]),
        ("INNERGRID", (0, 0), (-1, -1), 0.35, PALETTE["line"]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]
    if header:
        commands.extend(
            [
                ("BACKGROUND", (0, 0), (-1, 0), PALETTE["teal"]),
                ("TEXTCOLOR", (0, 0), (-1, 0), PALETTE["white"]),
            ]
        )
    out.setStyle(TableStyle(commands))
    return out


def lines(count: int = 4) -> Table:
    rows = [[""] for _ in range(count)]
    out = Table(rows, colWidths=[CONTENT_WIDTH], rowHeights=[0.28 * inch] * count)
    out.setStyle(
        TableStyle(
            [
                ("LINEBELOW", (0, 0), (-1, -1), 0.35, PALETTE["line"]),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    return out


def draw_page(canvas, doc, title: str, first: bool = False) -> None:
    canvas.saveState()
    if first:
        canvas.setFillColor(PALETTE["paper"])
        canvas.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, stroke=0, fill=1)
        canvas.setFillColor(PALETTE["teal"])
        canvas.rect(0, PAGE_HEIGHT - 0.45 * inch, PAGE_WIDTH, 0.45 * inch, stroke=0, fill=1)
        canvas.setFillColor(PALETTE["amber"])
        canvas.rect(0, PAGE_HEIGHT - 0.52 * inch, PAGE_WIDTH, 0.07 * inch, stroke=0, fill=1)
    else:
        canvas.setStrokeColor(PALETTE["line"])
        canvas.setLineWidth(0.5)
        canvas.line(MARGIN_X, PAGE_HEIGHT - 0.48 * inch, PAGE_WIDTH - MARGIN_X, PAGE_HEIGHT - 0.48 * inch)
        canvas.setFont("Helvetica", 7.5)
        canvas.setFillColor(PALETTE["muted"])
        canvas.drawString(MARGIN_X, PAGE_HEIGHT - 0.38 * inch, title[:82])
    if BRAND_LOGO_PATH.exists():
        canvas.drawImage(
            str(BRAND_LOGO_PATH),
            MARGIN_X,
            0.22 * inch,
            width=BRAND_LOGO_WIDTH,
            height=BRAND_LOGO_HEIGHT,
            preserveAspectRatio=True,
            mask="auto",
        )
        brand_x = MARGIN_X + BRAND_LOGO_WIDTH + 0.08 * inch
    else:
        brand_x = MARGIN_X
    canvas.setFont("Helvetica-Bold", 7.5)
    canvas.setFillColor(PALETTE["muted"])
    canvas.drawString(brand_x, 0.34 * inch, "English Ladder")
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(PALETTE["muted"])
    canvas.drawRightString(PAGE_WIDTH - MARGIN_X, 0.34 * inch, f"Page {doc.page}")
    canvas.restoreState()


def build_pdf(filename: str, title: str, story: list) -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUTPUT_DIR / filename
    doc = SimpleDocTemplate(
        str(path),
        pagesize=letter,
        rightMargin=MARGIN_X,
        leftMargin=MARGIN_X,
        topMargin=MARGIN_TOP,
        bottomMargin=MARGIN_BOTTOM,
        title=title,
        author="English Ladder EFSP",
    )
    doc.build(
        story,
        onFirstPage=lambda canvas, doc: draw_page(canvas, doc, title, first=True),
        onLaterPages=lambda canvas, doc: draw_page(canvas, doc, title, first=False),
    )
    return path


def cover(title: str, subtitle: str, audience: str) -> list:
    return [
        Spacer(1, 1.05 * inch),
        p("EFSP Auxiliary ESL Curriculum", "CoverKicker"),
        Paragraph(esc(title), S["CoverTitle"]),
        Paragraph(esc(subtitle), S["CoverSub"]),
        Spacer(1, 0.28 * inch),
        box(
            audience,
            [
                "Focus: cultural leadership, pragmatic communication, meeting behavior, conflict repair, and confident pushback in US branch environments.",
                "Designed for advanced Japanese and Chinese managers who already have functional English and need a clearer map of American workplace expectations.",
            ],
            "blue",
        ),
        Spacer(1, 0.25 * inch),
        p(
            "Teaching stance: culture is a pattern, not a prison. The materials describe common workplace expectations and perception gaps, then ask learners to observe the actual company, team, role, and person in front of them.",
            "Small",
        ),
        PageBreak(),
    ]


COURSE_OBJECTIVES = [
    "Recognize when American directness is a challenge to an idea rather than a rejection of the person.",
    "Respond to fast, blunt, public disagreement without freezing, over-apologizing, or escalating unnecessarily.",
    "Lead meetings with clear decision rights, visible confidence, and enough openness for American staff to trust the process.",
    "Use pushback that is firm, evidence-based, and relationship-safe.",
    "Handle performance issues, deadlines, ownership gaps, and cross-border tension in a US branch setting.",
    "Repair conflict after a difficult exchange and distinguish normal debate from unacceptable disrespect.",
]


MODULES = [
    {
        "title": "Module 1. Reading the US Branch Room",
        "time": "90 minutes",
        "big_idea": "American workplaces often reward visible participation, concise opinions, and quick objection. Silence may be misread as weak agreement, lack of expertise, or disengagement.",
        "objectives": [
            "Separate personal identity from workplace role behavior.",
            "Name three US branch signals that can feel aggressive but may be intended as participation.",
            "Identify personal triggers that make pushback harder to answer.",
        ],
        "concepts": [
            "Low-context communication: the speaker is expected to put more meaning into words, not leave it in shared background.",
            "Equality theater: even with hierarchy, employees may speak as if ideas compete on the same table.",
            "Task trust: some Americans build trust by testing plans and finding defects early.",
        ],
        "activities": [
            "Perception split: learners label ten workplace comments as hostile, neutral, or unclear; then compare possible US interpretations.",
            "Room scan: learners map where authority, expertise, emotion, and decision rights appear in a meeting.",
            "Trigger journal: learners write what behaviors make them feel disrespected, then convert each one into a question to test intent.",
        ],
        "outputs": [
            "Personal observation checklist for the learner's own branch.",
            "A one-sentence self-grounding response for surprise pushback.",
        ],
    },
    {
        "title": "Module 2. The American Idea-Combat Style",
        "time": "90 minutes",
        "big_idea": "Some Americans verbally attack an opinion with intensity while feeling no personal hostility. They may believe they are improving the plan, respecting the seriousness of the work, or proving engagement.",
        "objectives": [
            "Describe the difference between idea attack, relationship attack, and status attack.",
            "Practice staying present when language sounds stronger than the speaker's intent.",
            "Set boundaries when the attack becomes personal or disrespectful.",
        ],
        "concepts": [
            "Adversarial collaboration: two people pressure-test the same problem from different sides.",
            "Blunt cognitive shorthand: comments like 'That won't work' may mean 'I see a risk we need to solve,' not 'You are incompetent.'",
            "After-conflict reset: many Americans expect the relationship to continue normally after a heated exchange if the conflict stayed task-focused.",
        ],
        "activities": [
            "Decode the line: learners rewrite harsh-sounding comments into likely business concerns.",
            "Heat meter: learners place comments on a scale from normal debate to manager intervention required.",
            "Boundary drill: learners practice 'Challenge the plan, not the person' and 'Let's keep this about the data.'",
        ],
        "outputs": [
            "Idea-combat decoder card.",
            "Boundary phrase bank.",
        ],
    },
    {
        "title": "Module 3. Confident Leadership Without Overcorrecting",
        "time": "90 minutes",
        "big_idea": "Managers who are used to indirect authority may overcorrect in the US by becoming either too soft and invisible or too hard and controlling. The target is calm clarity plus credible openness.",
        "objectives": [
            "Use leader language that shows ownership without shutting down input.",
            "Make a decision after disagreement and preserve commitment.",
            "Explain the reason behind a decision without sounding defensive.",
        ],
        "concepts": [
            "Authority as service to clarity: the manager reduces ambiguity about goal, constraints, process, and decision.",
            "Confidence markers: clear verbs, direct ownership, time boundaries, and explicit next steps.",
            "Openness markers: invitation to risks, evidence requests, and visible revision when the facts change.",
        ],
        "activities": [
            "Weak/strong/overstrong sorting: learners compare manager statements and identify the leadership signal.",
            "Decision close practice: learners decide after three objections and state what will happen next.",
            "Two-minute rationale: learners explain a decision using goal, evidence, tradeoff, and commitment.",
        ],
        "outputs": [
            "Decision close template.",
            "Personal leadership sentence patterns.",
        ],
    },
    {
        "title": "Module 4. The Pushback Ladder",
        "time": "90 minutes",
        "big_idea": "Effective US branch pushback usually moves from curiosity to evidence to consequence to decision. Jumping straight to authority can look defensive; staying only curious can look weak.",
        "objectives": [
            "Use four levels of pushback based on the risk and the relationship.",
            "Push back upward, sideways, and downward.",
            "Avoid common traps: apology loops, vague disagreement, status arguments, and hidden no.",
        ],
        "concepts": [
            "Level 1: clarify the assumption.",
            "Level 2: add data or operational detail.",
            "Level 3: name the business consequence.",
            "Level 4: make or request a decision.",
        ],
        "activities": [
            "Ladder building: learners turn one disagreement into four stronger versions.",
            "Peer challenge: one learner pushes; the other asks what evidence would change the decision.",
            "Upward pushback: learners practice disagreeing with headquarters or a senior US executive.",
        ],
        "outputs": [
            "Pushback ladder worksheet.",
            "Three polished pushback scripts for the learner's real branch context.",
        ],
    },
    {
        "title": "Module 5. Meetings, Interruptions, and Decision Rights",
        "time": "90 minutes",
        "big_idea": "US meetings often mix discussion, debate, decision, and performance display. Managers need to name the meeting mode and control the process without suppressing useful challenge.",
        "objectives": [
            "Distinguish brainstorm, debate, alignment, decision, and execution meetings.",
            "Interrupt constructively and reclaim the floor.",
            "Convert noisy discussion into action owners, deadlines, and decision records.",
        ],
        "concepts": [
            "Interruption may signal energy or urgency; repeated interruption can still require process control.",
            "Decision rights must be visible: recommend, consult, decide, veto, execute.",
            "Meeting closure is a leadership act, not an administrative detail.",
        ],
        "activities": [
            "Meeting mode cards: learners announce the mode and rules for five meeting types.",
            "Floor control drill: learners interrupt politely but firmly in three levels of intensity.",
            "Decision record: learners convert a messy transcript into decisions, risks, owners, and next steps.",
        ],
        "outputs": [
            "Meeting opening script.",
            "Decision record template.",
        ],
    },
    {
        "title": "Module 6. Feedback, Accountability, and Face",
        "time": "90 minutes",
        "big_idea": "American employees may expect direct feedback, but they also expect fairness, specificity, documentation, and respect. Public embarrassment, vague criticism, or surprise consequences can create serious trust problems.",
        "objectives": [
            "Give direct feedback without humiliation.",
            "Name performance gaps in observable terms.",
            "Understand why documentation and HR partnership matter in US branches.",
        ],
        "concepts": [
            "Behavior, impact, expectation, support, consequence.",
            "Private dignity: direct does not mean public shaming.",
            "Process fairness: US employees often evaluate discipline by whether expectations were explicit and consistently applied.",
        ],
        "activities": [
            "Feedback rewrite: learners convert vague criticism into behavior-based feedback.",
            "Face-safe directness: learners practice direct messages that preserve dignity.",
            "Escalation map: learners identify when to involve HR, legal, or senior leadership.",
        ],
        "outputs": [
            "Feedback conversation planner.",
            "Accountability email template.",
        ],
    },
    {
        "title": "Module 7. Cross-Border Tension: Headquarters, Local Staff, and the Manager in Between",
        "time": "90 minutes",
        "big_idea": "Foreign managers in US branches often translate between headquarters expectations and local American expectations. The manager must protect strategic intent while making local reality speak clearly.",
        "objectives": [
            "Explain headquarters constraints without blaming headquarters.",
            "Represent US branch realities upward with evidence and options.",
            "Prevent employees from feeling that decisions are mysterious, delayed, or already made elsewhere.",
        ],
        "concepts": [
            "Two-way translation: headquarters needs local evidence; local staff need business context.",
            "Local autonomy expectations: many US employees expect influence over execution details.",
            "Credibility under constraint: a manager can be honest about limits and still lead with authority.",
        ],
        "activities": [
            "Constraint translation: learners turn 'Japan/China said no' into a business explanation.",
            "Options memo: learners prepare three options for headquarters with tradeoffs and a recommendation.",
            "Employee trust role-play: learners answer 'Do we actually have any say in this?'",
        ],
        "outputs": [
            "Headquarters update format.",
            "Local autonomy explanation script.",
        ],
    },
    {
        "title": "Module 8. Repair, Escalation, and Long-Term Trust",
        "time": "90 minutes",
        "big_idea": "A tense exchange does not have to damage the relationship if the manager can repair quickly, clarify intent, set norms, and follow through. Some behavior, however, must be escalated.",
        "objectives": [
            "Use a repair conversation after a difficult meeting.",
            "Separate normal disagreement from bullying, harassment, discrimination, or retaliation risk.",
            "Build a team norm that allows challenge without personal attack.",
        ],
        "concepts": [
            "Repair sequence: name, own, clarify, reset, invite.",
            "Norm setting: teams debate better when the manager defines what good challenge looks like.",
            "Escalation is not failure; it is part of protecting people and the business.",
        ],
        "activities": [
            "Repair script rehearsal: learners practice after three types of conflict.",
            "Norm charter: teams draft debate rules for a US branch meeting.",
            "Capstone simulation: learners lead a 20-minute meeting with objections, interruptions, and a final decision.",
        ],
        "outputs": [
            "Personal repair script.",
            "Team debate norm charter.",
            "Capstone rubric score and coaching notes.",
        ],
    },
]


WORKBOOK_TASKS = [
    {
        "scenario": "A US employee says very little in a one-on-one but strongly challenges the plan in a larger meeting.",
        "practice": [
            "Write two possible interpretations that do not assume disrespect.",
            "Write one question that tests intent without sounding defensive.",
            "Write one meeting norm that would make earlier disagreement easier next time.",
        ],
        "reflection": "Which behavior do you usually trust more: private harmony or public challenge? How might that preference affect your reading of US staff?",
    },
    {
        "scenario": "A colleague says, 'That proposal ignores the customer reality.' The sentence feels like an attack.",
        "practice": [
            "Underline the business issue hidden inside the sharp wording.",
            "Ask for the strongest evidence behind the objection.",
            "Set a boundary only if the person moves from the proposal to your competence or identity.",
        ],
        "reflection": "What physical signal tells you that you are reacting to tone more than content?",
    },
    {
        "scenario": "The room disagrees with your preferred plan, and you are tempted either to withdraw or to force the decision.",
        "practice": [
            "State the goal in one sentence.",
            "Invite one more objection with a time limit.",
            "Close the decision using reason, tradeoff, owner, and review date.",
        ],
        "reflection": "What does confidence sound like when it is calm, not loud?",
    },
    {
        "scenario": "A US director asks for a shortcut. You believe the shortcut will create quality risk.",
        "practice": [
            "Write Level 1: a clarifying question.",
            "Write Level 2: a data-based objection.",
            "Write Level 3: the business consequence.",
            "Write Level 4: your decision or escalation request.",
        ],
        "reflection": "Which ladder level do you overuse? Which level do you avoid?",
    },
    {
        "scenario": "Two people dominate the meeting while a technical expert stays quiet.",
        "practice": [
            "Interrupt the dominator without humiliating them.",
            "Invite the quiet expert by function, not personality.",
            "Summarize the decision and assign owners before the meeting ends.",
        ],
        "reflection": "What meeting mode do you need to announce more clearly: brainstorm, debate, decision, or execution?",
    },
    {
        "scenario": "An employee missed a deadline twice but says the expectations were never clear.",
        "practice": [
            "Describe the missed behavior in observable terms.",
            "Name the business impact without judging character.",
            "Set the future expectation, support, follow-up date, and consequence.",
        ],
        "reflection": "Where might indirect feedback have protected comfort but weakened fairness?",
    },
    {
        "scenario": "Headquarters rejects a local adaptation that the US team believes is necessary.",
        "practice": [
            "Explain the fixed constraint without blaming headquarters.",
            "Name what is still open for local decision.",
            "Prepare one upward message to headquarters using local evidence and options.",
        ],
        "reflection": "Do your employees know which decisions are fixed, consultative, or locally owned?",
    },
    {
        "scenario": "A debate became too personal, and one employee has stopped contributing.",
        "practice": [
            "Write a repair opening that owns the process without surrendering the business decision.",
            "Clarify what kind of challenge is welcome next time.",
            "Name the boundary that protects dignity.",
        ],
        "reflection": "What relationship repair do you tend to delay because the task seems more urgent?",
    },
]


DIFFERENCES = [
    [
        "Visible disagreement",
        "Many US employees see disagreement as contribution. A quiet meeting may look unproductive or politically controlled.",
        "Invite objections early, set time limits, and close with a clear decision.",
    ],
    [
        "Speed and provisional decisions",
        "Teams may prefer a decision that can be revised over a perfect decision that arrives late.",
        "Use pilot language: 'We will test this for two weeks and review the data.'",
    ],
    [
        "Self-promotion",
        "Employees may describe their own achievements directly. This can sound boastful to managers from more modesty-oriented contexts.",
        "Ask for evidence and impact; do not punish appropriate visibility.",
    ],
    [
        "Hierarchy",
        "US staff may challenge a boss in public and still accept the boss's authority after the decision.",
        "Do not read challenge automatically as rebellion. Name the decision point.",
    ],
    [
        "Written accountability",
        "Emails, meeting notes, goals, and performance records carry heavy weight.",
        "Document expectations, decisions, and follow-up in neutral language.",
    ],
    [
        "HR and legal sensitivity",
        "Rules around harassment, discrimination, retaliation, wage/time, disability, and protected leave are serious.",
        "Partner with HR early. This curriculum is not legal advice.",
    ],
    [
        "Work-life boundaries",
        "Some American employees protect evenings, weekends, vacation, and family obligations strongly.",
        "Clarify urgency standards and avoid implying loyalty requires constant availability.",
    ],
    [
        "Psychological safety",
        "Employees may expect the right to raise risks without punishment.",
        "Thank people for surfacing risk, then evaluate the risk rigorously.",
    ],
    [
        "Friendliness vs friendship",
        "Warm small talk may not mean deep personal relationship; direct debate may not mean personal dislike.",
        "Track behavior over time rather than one emotional signal.",
    ],
    [
        "Indirect no",
        "Phrases like 'we will consider it' may be read as genuine possibility in the US.",
        "When the answer is no, say no with a reason, an alternative, or a next condition.",
    ],
]


HEAT_SCALE = [
    ["1. Normal debate", "No, I disagree. The timeline is unrealistic.", "Answer with evidence; invite alternatives."],
    ["2. Strong but task-focused", "That assumption is wrong, and here is why.", "Slow the pace; restate the business issue."],
    ["3. Process problem", "Repeated interruption, sarcasm, eye-rolling, or dominating.", "Intervene: set meeting rules and protect the floor."],
    ["4. Personal attack", "You clearly do not understand this business.", "Stop and redirect: behavior is not acceptable."],
    ["5. Escalation issue", "Threats, slurs, harassment, discrimination, retaliation, or safety risk.", "Pause the exchange and involve HR or appropriate leadership."],
]


PHRASE_BANK = {
    "Ground yourself": [
        "Let me separate the tone from the business concern.",
        "I want to understand the risk you are seeing.",
        "Give me the strongest version of your objection.",
    ],
    "Clarify": [
        "Which assumption are you challenging?",
        "Are you concerned about cost, timing, quality, or customer impact?",
        "What evidence would make you more comfortable with this direction?",
    ],
    "Push back": [
        "I see the concern. I disagree on the conclusion because the current data points another way.",
        "That solves one problem but creates a larger operational risk.",
        "I cannot support that timeline unless we remove scope or add resources.",
    ],
    "Lead the room": [
        "We are in debate mode for ten more minutes; after that I will make the call.",
        "I want one objection from each function before we decide.",
        "We have heard the risk. Now we need options.",
    ],
    "Set boundaries": [
        "Challenge the plan, not the person.",
        "The interruption is making it hard to evaluate the idea. Let her finish, then I will come back to you.",
        "That wording is too personal. Restate the concern as a business risk.",
    ],
    "Close decisions": [
        "I am deciding to proceed with option B. The reason is speed to customer impact.",
        "This is not unanimous, but it is clear enough to move. We will review results on Friday.",
        "The decision is made. I expect full support in execution, and I will own the tradeoff.",
    ],
    "Repair": [
        "The discussion became sharper than useful. I want to reset the working relationship.",
        "My intent was to test the plan, not dismiss your expertise.",
        "Next time I will name debate mode earlier and protect time for each function.",
    ],
}


SCENARIOS = [
    {
        "title": "1. The Blunt Engineer",
        "context": "A senior engineer says, 'No, that architecture is a bad idea,' during your project review.",
        "manager": "You are the branch manager. You feel publicly embarrassed, but the engineer may have a real technical concern. Keep authority, extract the risk, and close the discussion.",
        "colleague": "You are the engineer. You are not trying to insult the manager; you believe the proposal could fail under load. You speak quickly and directly.",
        "observer": "Watch whether the manager separates tone from content, asks for evidence, and sets a process boundary if needed.",
    },
    {
        "title": "2. Headquarters Already Decided",
        "context": "US staff suspect the meeting is fake because headquarters has already chosen the plan.",
        "manager": "Explain what is fixed, what is open, and where local input can still shape execution.",
        "colleague": "Push hard: 'Do we actually have any say, or is this just theater?'",
        "observer": "Listen for honesty about constraints and a credible invitation for input.",
    },
    {
        "title": "3. The Deadline Refusal",
        "context": "A team lead says a headquarters deadline is impossible and refuses to commit.",
        "manager": "Push for ownership without ignoring reality. Ask for options and tradeoffs.",
        "colleague": "Do not accept vague optimism. You need scope removed or more people.",
        "observer": "Track whether the conversation reaches an action plan rather than a status argument.",
    },
    {
        "title": "4. Silence After the Question",
        "context": "You ask for objections. The room is quiet. Two days later, an employee says everyone knew the plan had problems.",
        "manager": "Reset the norm. Make silence less comfortable than useful dissent.",
        "colleague": "You stayed quiet because you did not want to embarrass the manager.",
        "observer": "Notice whether the manager creates a specific structure for dissent.",
    },
    {
        "title": "5. Public Performance Challenge",
        "context": "An employee challenges your data in front of a visiting executive.",
        "manager": "Respond without defensiveness. Decide whether to answer now, park it, or follow up.",
        "colleague": "You believe the data is wrong and the executive needs to know before approving budget.",
        "observer": "Watch for face-saving, factual clarity, and executive confidence.",
    },
    {
        "title": "6. The Overly Friendly Employee",
        "context": "An employee uses first names, jokes in meetings, and challenges your priorities casually.",
        "manager": "Decide what is cultural style and what is a performance issue. Set expectations only where necessary.",
        "colleague": "You think informality builds trust and speed.",
        "observer": "Check whether the manager avoids turning style discomfort into discipline.",
    },
    {
        "title": "7. The Hidden No",
        "context": "You told a US partner, 'We will consider it,' meaning no. They announced the idea as likely approved.",
        "manager": "Repair the misunderstanding and replace indirect refusal with clear conditions.",
        "colleague": "You believed 'consider' meant there was a real chance.",
        "observer": "Listen for a clear no, reason, and possible alternative.",
    },
    {
        "title": "8. Interrupted Three Times",
        "context": "A strong talker interrupts a quieter analyst three times.",
        "manager": "Protect the analyst's floor without shaming the interrupter.",
        "colleague": "You are excited and believe your points are urgent.",
        "observer": "Watch for process control and dignity for both people.",
    },
    {
        "title": "9. The Escalating Tone",
        "context": "Debate moves from 'The plan has a gap' to 'You do not understand the customer.'",
        "manager": "Stop the personal attack and redirect to business evidence.",
        "colleague": "You are frustrated because the same issue has appeared before.",
        "observer": "Mark the exact moment when manager intervention is required.",
    },
    {
        "title": "10. Quality vs Speed",
        "context": "Headquarters wants quality review; local sales wants launch speed.",
        "manager": "Translate both values into business risk and make a temporary decision.",
        "colleague": "Push for launch: 'The market will not wait for perfect.'",
        "observer": "Look for pilot thinking, risk ownership, and review date.",
    },
    {
        "title": "11. Performance Feedback Surprise",
        "context": "An employee is shocked by negative feedback in the annual review.",
        "manager": "Explain the issue directly, but acknowledge if expectations were not made clear earlier.",
        "colleague": "You feel blindsided and unfairly judged.",
        "observer": "Check for observable examples, fairness, and next steps.",
    },
    {
        "title": "12. The Seniority Mismatch",
        "context": "A younger US specialist contradicts an older visiting executive from Asia.",
        "manager": "Protect the executive's dignity while preserving the specialist's useful information.",
        "colleague": "You are the specialist. You believe the executive is missing a local regulatory detail.",
        "observer": "Notice whether expertise and hierarchy both receive respect.",
    },
    {
        "title": "13. Email That Sounds Angry",
        "context": "You receive a short email: 'This does not address my concern. Fix by EOD.'",
        "manager": "Decide whether to answer by email, call, or clarify. Do not assume hostility too quickly.",
        "colleague": "You are under customer pressure and think your email is efficient, not rude.",
        "observer": "Evaluate whether the manager chooses the right channel.",
    },
    {
        "title": "14. Local Autonomy",
        "context": "US employees want to adapt a process that headquarters standardized globally.",
        "manager": "Define what can be localized and what cannot.",
        "colleague": "You think the global process ignores US customers.",
        "observer": "Listen for fixed/open categories and escalation path.",
    },
    {
        "title": "15. The After-Hours Request",
        "context": "A manager from headquarters expects weekend responses; US staff object.",
        "manager": "Set urgency standards and protect critical work without creating constant availability.",
        "colleague": "You need predictable personal time and dislike vague urgency.",
        "observer": "Check whether the policy is clear, fair, and business-realistic.",
    },
    {
        "title": "16. The Strong Candidate",
        "context": "A candidate in an interview speaks confidently and asks pointed questions.",
        "manager": "Distinguish confidence from arrogance and evaluate job-relevant evidence.",
        "colleague": "You are the candidate. You expect the interview to be a two-way evaluation.",
        "observer": "Look for bias control and evidence-based evaluation.",
    },
    {
        "title": "17. Repair After a Bad Meeting",
        "context": "You shut down debate too quickly yesterday. A key employee is now quiet.",
        "manager": "Repair without surrendering authority.",
        "colleague": "You felt dismissed and are not sure it is worth speaking up again.",
        "observer": "Listen for ownership, invitation, and specific future process.",
    },
    {
        "title": "18. Capstone: The Product Launch Decision",
        "context": "Engineering, sales, headquarters, and finance disagree about launch timing.",
        "manager": "Lead a 20-minute meeting. Surface objections, control interruptions, decide next action, and assign owners.",
        "colleague": "Choose a function and push strongly for your priority.",
        "observer": "Score leadership clarity, pushback handling, decision close, and relationship safety.",
    },
]


def add_course_opening(story: list) -> None:
    story += h1("Purpose and Teaching Position")
    story.append(
        p(
            "This auxiliary EFSP curriculum is for advanced adult managers who do not primarily need grammar correction. They need cultural maps, leadership practice, and pragmatic language for situations where American workplace behavior feels confrontational, assertive, or personally aggressive."
        )
    )
    story.append(
        p(
            "The course does not teach learners to imitate a stereotype of American aggressiveness. It teaches them to recognize the local meaning of direct challenge, respond with calm authority, and decide when the behavior has crossed from normal debate into disrespect or risk."
        )
    )
    story.append(box("Core caution", [
        "Use national culture as a starting hypothesis, never as a diagnosis. Japanese, Chinese, and American employees vary by company, region, generation, gender, role, personality, industry, and international experience.",
        "The best learner outcome is not 'act American.' It is 'read the room accurately, lead clearly, and protect both results and dignity.'",
    ], "amber"))
    story.append(h2("Course objectives"))
    story.append(bullets(COURSE_OBJECTIVES))


def add_american_idea_combat(story: list) -> None:
    story += h1("The American Idea-Combat Personality")
    story.append(
        p(
            "Many US branches include at least one high-energy professional who treats ideas as objects to be stress-tested in public. This person may interrupt, speak quickly, use blunt negatives, challenge senior people, and sound as if they are verbally assaulting an opinion. Their intent may be completely non-hostile. In their mind, they are doing the work: finding the weak point before the customer, market, auditor, or competitor finds it."
        )
    )
    story.append(
        p(
            "A useful label is the adversarial collaborator. This person attacks the proposal so the team can make it stronger. They may say, 'That will never work,' then happily eat lunch with the person who proposed it. They often separate person and idea more sharply than managers from more face-sensitive or harmony-oriented environments expect."
        )
    )
    story.append(h2("Common signals"))
    story.append(
        bullets(
            [
                "Blunt challenge: 'No,' 'I disagree,' 'That is not realistic,' or 'The assumption is wrong.'",
                "Fast turn-taking: they may enter before a pause feels complete to a Japanese or Chinese listener.",
                "Public testing: they challenge in the meeting because the meeting is where the work is happening.",
                "Low ritual repair: they may not apologize because they do not think damage occurred.",
                "Quick emotional reset: five minutes after debate, they may act relaxed and friendly.",
            ]
        )
    )
    story.append(h2("What it may mean"))
    story.append(
        bullets(
            [
                "I am engaged enough to test this seriously.",
                "I respect you enough to be direct.",
                "I believe the best idea should survive challenge.",
                "I expect you, as the leader, to answer objections with evidence and then decide.",
                "I am not attacking your status unless I move from the work to your character, intelligence, accent, nationality, or dignity.",
            ]
        )
    )
    story.append(h2("What it does not excuse"))
    story.append(
        p(
            "Non-hostile intent does not erase impact. Managers should not allow personal insults, ridicule, discriminatory comments, harassment, threats, repeated domination, or retaliation. A healthy American debate style is direct about work and respectful toward people. The manager's job is to protect both."
        )
    )
    story.append(table([["Type", "Example", "Manager response"]] + HEAT_SCALE, [1.35 * inch, 3.0 * inch, 2.75 * inch]))


def add_culture_maps(story: list) -> None:
    story += h1("Culture Maps for US Branch Managers")
    story.append(
        p(
            "The following patterns explain why a meeting can feel rude to one manager and normal to another participant. They are not moral rankings. They are operating systems. A leader becomes effective by seeing which operating system is active and making expectations explicit."
        )
    )
    story.append(h2("Patterns that often surprise Japanese managers"))
    story.append(
        bullets(
            [
                "Consensus before meeting vs debate inside meeting: US employees may expect the meeting itself to change the idea, not merely confirm prior alignment.",
                "Respect through challenge: a younger specialist may disagree publicly because they believe expertise matters more than seniority in that moment.",
                "Quality and preparation vs speed and iteration: US teams may accept a provisional answer if it lets work move now.",
                "Silence as ambiguity: quiet listening may be read as agreement, lack of confidence, or lack of opinion.",
                "Apology patterns: repeated apology can reduce authority if the issue requires ownership and corrective action instead.",
            ]
        )
    )
    story.append(h2("Patterns that often surprise Chinese managers"))
    story.append(
        bullets(
            [
                "Face and public disagreement: US employees may challenge in public without intending to reduce a leader's face.",
                "Hierarchy vs delegated ownership: employees may expect a manager to define the goal, then let local owners shape execution.",
                "Relationship trust vs process trust: US staff may trust clear rules, documented decisions, and fair process even when personal relationship is limited.",
                "Indirect refusal: softened no can be mistaken for maybe, creating later frustration.",
                "Central approval: employees may lose confidence if every meaningful answer appears to require distant permission.",
            ]
        )
    )
    story.append(h2("Other differences foreign managers may encounter"))
    story.append(table([["Difference", "Possible US interpretation", "Manager move"]] + DIFFERENCES, [1.35 * inch, 3.05 * inch, 2.7 * inch]))


def add_course_map(story: list) -> None:
    story += h1("Curriculum Map")
    story.append(
        p(
            "The full course is eight 90-minute modules plus optional coaching. It can also be taught as a two-day intensive or as eight short workshops over a quarter. Each module includes cultural interpretation, leadership behavior, controlled language practice, role-play, and transfer to the learner's actual workplace."
        )
    )
    story.append(h2("Full course sequence"))
    rows = [["Module", "Core question", "Main performance outcome"]]
    for module in MODULES:
        rows.append([module["title"].replace("Module ", ""), module["big_idea"], "; ".join(module["outputs"])])
    story.append(table(rows, [1.25 * inch, 3.25 * inch, 2.55 * inch]))
    story.append(Spacer(1, 8))
    story.append(h2("Fast-track version"))
    story.append(
        bullets(
            [
                "Hour 1: orientation, culture maps, and the idea-combat decoder.",
                "Hour 2: pushback ladder and confidence markers.",
                "Hour 3: meeting control, interruption management, and decision close.",
                "Hour 4: feedback and accountability conversations.",
                "Hour 5: headquarters/local translation role-plays.",
                "Hour 6: capstone simulation, peer feedback, and personal action plan.",
            ],
            numbered=True,
        )
    )


def add_module_details(story: list) -> None:
    story += h1("Instructor Module Plans")
    for module in MODULES:
        story.append(h2(f"{module['title']} ({module['time']})"))
        story.append(p(module["big_idea"]))
        story.append(h3("Learning objectives"))
        story.append(bullets(module["objectives"]))
        story.append(h3("Core concepts"))
        story.append(bullets(module["concepts"]))
        story.append(h3("Activities"))
        story.append(bullets(module["activities"], numbered=True))
        story.append(h3("Learner outputs"))
        story.append(bullets(module["outputs"]))
        story.append(
            box(
                "Facilitator note",
                [
                    "Keep the discussion concrete. Ask learners to describe actual words, timing, channel, role, and business stakes. Avoid debates about which national culture is better. The question is: what will this behavior mean in this branch, and what leadership move will work here?"
                ],
                "blue",
            )
        )


def add_assessment(story: list) -> None:
    story += h1("Assessment and Coaching")
    story.append(h2("Pre-course diagnostic"))
    story.append(
        bullets(
            [
                "Learner describes a recent US branch conflict and identifies what was said, what they felt, what they did, and what happened next.",
                "Learner rates confidence from 1 to 5 in meetings, pushback, feedback, interruption control, and repair.",
                "Instructor conducts a five-minute role-play with blunt disagreement and notes default response patterns.",
            ]
        )
    )
    story.append(h2("Performance rubric"))
    story.append(
        table(
            [
                ["Skill", "Developing", "Proficient", "Strong"],
                ["Decode intent", "Treats most bluntness as personal disrespect.", "Separates tone, content, and possible intent.", "Tests intent quickly and stays focused on business stakes."],
                ["Push back", "Uses vague disagreement or retreats.", "Uses evidence and consequences clearly.", "Adapts intensity to risk, role, and relationship."],
                ["Lead meetings", "Lets debate sprawl or shuts it down early.", "Names mode, controls floor, closes decisions.", "Creates useful dissent and strong commitment after decision."],
                ["Boundary setting", "Ignores disrespect or overreacts.", "Redirects personal comments to work issues.", "Sets norms early and escalates serious behavior appropriately."],
                ["Repair", "Avoids follow-up after tension.", "Clarifies intent and resets expectations.", "Turns conflict into a team norm and stronger trust."],
            ],
            [1.35 * inch, 1.9 * inch, 1.9 * inch, 1.9 * inch],
        )
    )
    story.append(h2("Capstone simulation"))
    story.append(
        p(
            "Learners lead a meeting about a delayed product launch. The instructor assigns roles: sales wants speed, engineering wants quality, headquarters wants global consistency, finance wants cost control, and HR watches team behavior. The manager must surface objections, use the pushback ladder, protect the floor, make a decision or define the next decision gate, and repair any tense moment."
        )
    )
    story.append(h2("Suggested further reading"))
    story.append(
        bullets(
            [
                "Edward T. Hall, Beyond Culture.",
                "Geert Hofstede, Gert Jan Hofstede, and Michael Minkov, Cultures and Organizations.",
                "Erin Meyer, The Culture Map.",
                "Stella Ting-Toomey and John Oetzel, Managing Intercultural Conflict Effectively.",
                "Robert House and colleagues, Culture, Leadership, and Organizations: The GLOBE Study.",
                "Amy Edmondson, The Fearless Organization.",
            ]
        )
    )


def add_workbook_module_pages(story: list) -> None:
    story += h1("Module Practice Pages")
    story.append(
        p(
            "Use these pages during class, coaching, or self-study. The goal is not to memorize perfect sentences. The goal is to build a repeatable leadership move: read the situation, name the business issue, choose the right level of directness, and preserve dignity."
        )
    )
    for module, task in zip(MODULES, WORKBOOK_TASKS):
        story.append(PageBreak())
        story.append(h2(module["title"]))
        story.append(p(module["big_idea"]))
        story.append(h3("What you should be able to do"))
        story.append(bullets(module["objectives"]))
        story.append(h3("Practice situation"))
        story.append(box("Scenario", [task["scenario"]], "blue"))
        story.append(h3("Your leadership moves"))
        story.append(bullets(task["practice"], numbered=True))
        story.append(lines(7))
        story.append(h3("Reflection"))
        story.append(p(task["reflection"]))
        story.append(lines(4))
        story.append(h3("Transfer to your branch"))
        story.append(p("Where will you use this skill in the next two weeks?"))
        story.append(lines(3))


def instructor_guide() -> Path:
    story = cover(
        "Leading in the American Branch",
        "Instructor guide for Japanese and Chinese managers navigating directness, pushback, and conflict in US teams",
        "Audience: instructors, coaches, HR learning partners, and senior facilitators",
    )
    add_course_opening(story)
    add_american_idea_combat(story)
    add_culture_maps(story)
    add_course_map(story)
    add_module_details(story)
    add_assessment(story)
    return build_pdf(
        "efsp-cultural-leadership-in-us-branches-instructor-guide.pdf",
        "EFSP Cultural Leadership in US Branches - Instructor Guide",
        story,
    )


def participant_workbook() -> Path:
    story = cover(
        "Leading in the American Branch",
        "Participant workbook: cultural leadership, confident pushback, and relationship-safe directness",
        "Audience: Japanese and Chinese managers working with US branch teams",
    )
    story += h1("How to Use This Workbook")
    story.append(
        p(
            "This workbook is not mainly an English grammar course. It is practice for moments when you already know the words but the workplace meaning is unclear. You will learn to read American directness, lead through disagreement, and push back without becoming either passive or harsh."
        )
    )
    story.append(h2("Your starting point"))
    story.append(bullets([
        "A US colleague challenges your plan in public. What do you normally feel first?",
        "When you disagree with a US employee, do you become indirect, silent, detailed, humorous, strict, or overly apologetic?",
        "What behavior from American employees feels most disrespectful to you?",
        "What behavior from you might American employees misunderstand?",
    ]))
    story.append(lines(5))
    story += h1("The Main Cultural Reframe")
    story.append(
        p(
            "In many US workplaces, an opinion can be attacked very strongly while the person remains accepted. The proposal is treated like a draft, prototype, or stress-test object. This is not always pleasant, and it is not always skillful. But it often has a different meaning from personal hostility."
        )
    )
    story.append(box("Remember", [
        "Do not ask only, 'Was the tone polite?' Also ask, 'Was the speaker attacking the work, the process, my status, or my dignity?' Your response should match the real level of the problem."
    ], "amber"))
    story.append(h2("Idea attack vs personal attack"))
    story.append(table([["Type", "What you may hear", "Useful response"]] + HEAT_SCALE, [1.35 * inch, 3.0 * inch, 2.75 * inch]))
    story += h1("Pushback Ladder")
    story.append(
        p(
            "Use the ladder when you need to push back. Start low when the risk is low or the relationship is new. Move up when the business risk is high, the decision is near, or people are avoiding the real issue."
        )
    )
    story.append(
        table(
            [
                ["Level", "Purpose", "Example"],
                ["1. Clarify", "Find the assumption.", "Which part of the forecast are you most concerned about?"],
                ["2. Add evidence", "Bring data or operational facts.", "The last two launches needed six weeks of QA, so four weeks is a real risk."],
                ["3. Name consequence", "Show business impact.", "If we keep the date without reducing scope, customer defects will likely increase."],
                ["4. Decide", "Create commitment or escalate.", "I am deciding to move the launch by two weeks. I will explain the tradeoff to headquarters."],
            ],
            [1.1 * inch, 2.15 * inch, 3.8 * inch],
        )
    )
    story.append(h2("Practice: build your ladder"))
    story.append(p("Situation: A US colleague says your team's plan is too slow and asks you to skip a review step."))
    story.append(p("Level 1 - clarify:"))
    story.append(lines(2))
    story.append(p("Level 2 - evidence:"))
    story.append(lines(2))
    story.append(p("Level 3 - consequence:"))
    story.append(lines(2))
    story.append(p("Level 4 - decision:"))
    story.append(lines(2))
    story += h1("Meeting Leadership Moves")
    story.append(h2("Open the meeting mode"))
    story.append(
        bullets(
            [
                "Brainstorm mode: 'We are generating options. No decision for the first twenty minutes.'",
                "Debate mode: 'I want the strongest risks on the table. Challenge the plan, not the person.'",
                "Decision mode: 'We will hear final objections, then I will make the call.'",
                "Execution mode: 'The decision is made. Today is about owners, dates, and blockers.'",
            ]
        )
    )
    story.append(h2("Control interruptions"))
    story.append(
        bullets(
            [
                "Light: 'Hold that thought. I want to let Mei finish.'",
                "Firm: 'I am going to stop the interruption. You are next.'",
                "Boundary: 'We are losing the process. One speaker at a time.'",
            ]
        )
    )
    story.append(h2("Close a decision"))
    story.append(
        bullets(
            [
                "Decision: 'We will proceed with option B.'",
                "Reason: 'It gives us the fastest customer learning with acceptable risk.'",
                "Tradeoff: 'We are accepting a temporary manual workaround.'",
                "Owner/date: 'Alex owns the customer pilot by Friday.'",
                "Review: 'We will review defects and customer feedback next Wednesday.'",
            ]
        )
    )
    story += h1("Feedback and Accountability")
    story.append(
        p(
            "Direct feedback in the US should still protect dignity. The safest structure is behavior, impact, expectation, support, and consequence. Avoid vague labels such as careless, lazy, not serious, immature, or not loyal. Use observable behavior."
        )
    )
    story.append(table([
        ["Less effective", "More effective"],
        ["You are not careful enough.", "The last two reports included pricing errors. The impact is that sales cannot quote confidently."],
        ["You need to be more proactive.", "When the customer changed the deadline, I needed you to alert the team the same day."],
        ["Your attitude is bad.", "In today's meeting you interrupted twice and said the plan was stupid. Challenge is welcome; personal wording is not."],
    ], [3.25 * inch, 3.75 * inch]))
    story.append(h2("Planner"))
    story.append(p("Behavior I observed:"))
    story.append(lines(2))
    story.append(p("Business impact:"))
    story.append(lines(2))
    story.append(p("Expectation from now on:"))
    story.append(lines(2))
    story.append(p("Support or resources I can provide:"))
    story.append(lines(2))
    story.append(p("Follow-up date or consequence:"))
    story.append(lines(2))
    story += h1("Cross-Border Translation")
    story.append(
        p(
            "A US branch manager often translates in two directions. Headquarters needs local facts without emotional noise. Local employees need business context without feeling that all decisions are mysterious or predetermined."
        )
    )
    story.append(h2("Instead of blaming headquarters"))
    story.append(table([
        ["Avoid", "Use"],
        ["Japan will not allow it.", "The global standard is fixed because it protects product consistency. The open question is how we implement it for US customers."],
        ["China already decided.", "The investment level is already approved. We can still influence timeline, staffing, and launch sequence."],
        ["I cannot say anything.", "I cannot share the confidential detail yet. I can tell you the decision criteria and when we will know more."],
    ], [2.6 * inch, 4.4 * inch]))
    story += h1("Repair After Conflict")
    story.append(p("Use this sequence after a meeting that became too tense or when someone may feel dismissed."))
    story.append(bullets([
        "Name: 'Yesterday's discussion became sharper than useful.'",
        "Own: 'I moved to decision too quickly and did not make enough room for the risk you were raising.'",
        "Clarify: 'My intent was to protect the launch date, not dismiss your expertise.'",
        "Reset: 'In the next review, I will open with risks before we discuss dates.'",
        "Invite: 'What do you need from me so you can raise concerns early?'",
    ], numbered=True))
    story.append(h2("My repair script"))
    story.append(lines(8))
    story += h1("Personal Action Plan")
    story.append(p("Choose three behaviors to practice in the next 30 days. Make them visible and measurable."))
    story.append(table([
        ["Behavior", "Situation where I will use it", "How I will know it worked"],
        ["", "", ""],
        ["", "", ""],
        ["", "", ""],
    ], [2.1 * inch, 2.45 * inch, 2.45 * inch]))
    add_workbook_module_pages(story)
    story.append(h2("Phrase bank"))
    for title, phrases in PHRASE_BANK.items():
        story.append(h3(title))
        story.append(bullets(phrases))
    return build_pdf(
        "efsp-cultural-leadership-in-us-branches-participant-workbook.pdf",
        "EFSP Cultural Leadership in US Branches - Participant Workbook",
        story,
    )


def scenario_cards() -> Path:
    story = cover(
        "US Branch Cultural Leadership Scenario Cards",
        "Role-play packet for directness, pushback, meeting control, feedback, and repair",
        "Audience: instructors, coaches, peer practice groups, and advanced manager cohorts",
    )
    story += h1("How to Run the Scenario Cards")
    story.append(
        bullets(
            [
                "Use groups of three: manager, US colleague, observer.",
                "Give the manager 90 seconds to prepare and four minutes to act.",
                "The US colleague should be direct and realistic, not cartoonishly rude.",
                "The observer scores: business clarity, pushback handling, process control, dignity, and decision close.",
                "After the role-play, replay the hardest 30 seconds with a stronger manager response.",
            ],
            numbered=True,
        )
    )
    story.append(box("Facilitator guardrail", [
        "Do not reward aggression for its own sake. The target is calm authority, useful challenge, and relationship-safe directness."
    ], "amber"))
    for scenario in SCENARIOS:
        story.append(PageBreak())
        story.append(Paragraph(esc(scenario["title"]), S["CardTitle"]))
        story.append(rule())
        story.append(box("Context", [scenario["context"]], "blue"))
        story.append(Spacer(1, 6))
        story.append(table([
            ["Manager card", "US colleague card"],
            [scenario["manager"], scenario["colleague"]],
        ], [3.45 * inch, 3.45 * inch]))
        story.append(Spacer(1, 8))
        story.append(box("Observer focus", [scenario["observer"]], "green"))
        story.append(h3("Debrief questions"))
        story.append(bullets([
            "What did the manager correctly decode?",
            "Where did the manager need more confidence or more restraint?",
            "What phrase changed the emotional direction of the exchange?",
            "What should be documented or followed up after this situation?",
        ]))
        story.append(h3("Replay line"))
        story.append(lines(3))
    return build_pdf(
        "efsp-cultural-leadership-scenario-cards.pdf",
        "EFSP Cultural Leadership Scenario Cards",
        story,
    )


def quick_reference() -> Path:
    story = cover(
        "American Pushback Field Guide",
        "Quick reference for managers who need to respond in the moment",
        "Audience: Japanese and Chinese managers in US branch settings",
    )
    story += h1("When an American Colleague Attacks an Idea")
    story.append(table([
        ["What happens", "First interpretation to test", "Useful first response"],
        ["They say, 'No, that will not work.'", "They may see a risk, not an insult opportunity.", "Tell me the failure point you are seeing."],
        ["They interrupt.", "They may be excited, rushed, or used to faster turn-taking.", "Hold that thought. I want to finish this point, then I will come to you."],
        ["They challenge you publicly.", "They may believe public challenge improves the decision.", "Good. Put the strongest objection on the table."],
        ["They sound fine afterward.", "They may believe the conflict was only about the task.", "Before we move on, I want to confirm our working agreement."],
    ], [1.65 * inch, 2.65 * inch, 2.7 * inch]))
    story.append(box("Mental reset", [
        "Do not decide too quickly that the speaker is hostile. Also do not tolerate disrespect. Decode first, then lead."
    ], "amber"))
    story += h1("Decision Tree")
    story.append(bullets([
        "Is the comment about the work? Answer with curiosity, evidence, or decision.",
        "Is the comment about process? Set meeting rules: time, turn-taking, decision mode, next step.",
        "Is the comment about a person's character, identity, accent, nationality, or dignity? Stop it and redirect.",
        "Does the behavior involve threats, harassment, discrimination, retaliation, or safety risk? Pause and involve HR or appropriate leadership.",
    ], numbered=True))
    story += h1("Confident Leadership Markers")
    story.append(table([
        ["Instead of", "Use"],
        ["Maybe we can think about it.", "I will review two options and decide by Thursday."],
        ["I am sorry, but I think maybe no.", "I cannot approve this version because the risk is too high."],
        ["Please understand headquarters.", "Here is the business constraint. Here is where we still have room to adapt."],
        ["Let's avoid conflict.", "I want direct challenge on the plan and respect for the people in the room."],
    ], [2.65 * inch, 4.35 * inch]))
    story += h1("Pushback Phrases by Strength")
    for title, phrases in PHRASE_BANK.items():
        story.append(h2(title))
        story.append(bullets(phrases))
    story += h1("Meeting Control Mini-Scripts")
    story.append(h2("Opening"))
    story.append(
        p(
            "We are in debate mode for the first 20 minutes. I want risks, not politeness. Challenge the plan, not the person. At 2:30 I will decide the next step."
        )
    )
    story.append(h2("Interruption"))
    story.append(
        p(
            "I am going to stop the interruption. You are next, but I want Priya to finish the customer impact first."
        )
    )
    story.append(h2("Decision"))
    story.append(
        p(
            "I have heard the objections. We will proceed with the pilot, reduce scope to two customers, and review results next Friday. I own the tradeoff."
        )
    )
    story.append(h2("Boundary"))
    story.append(
        p(
            "That wording is too personal. Restate it as a business concern, and we will address it."
        )
    )
    story += h1("Email Templates")
    story.append(h2("After a heated meeting"))
    story.append(
        box(
            "Subject: Follow-up on today's launch discussion",
            [
                "Thank you for the direct discussion today. The key risk raised was customer impact if QA time is reduced. The decision is to keep the launch date but reduce scope to two pilot customers. Alex owns the revised QA checklist by Tuesday. We will review defect data Friday at 10:00. Please send any additional risk in writing by tomorrow noon.",
            ],
            "blue",
        )
    )
    story.append(h2("Pushing back to headquarters"))
    story.append(
        box(
            "Subject: US branch risk and recommended option",
            [
                "The US team can meet the requested date only if we remove two launch features or add temporary QA support. My recommendation is option 2: keep the customer-facing date, remove feature C, and add a two-week post-launch review. The main risk is customer confusion if feature C remains partially supported.",
            ],
            "green",
        )
    )
    story.append(h2("Performance expectation"))
    story.append(
        box(
            "Subject: Follow-up on reporting expectations",
            [
                "In today's discussion, we agreed that pricing reports must be checked against the master sheet before they go to sales. The last two reports had errors that delayed customer quotes. Starting this week, please send the checked report by Wednesday 3:00 PM and copy me for the next three cycles. We will review progress on June 21.",
            ],
            "amber",
        )
    )
    story += h1("Red Lines")
    story.append(
        bullets(
            [
                "Direct challenge to an idea is acceptable when it remains about the work.",
                "Mocking a person's accent, nationality, age, gender, race, disability, religion, or other protected identity is not normal debate.",
                "Threats, intimidation, retaliation, and repeated personal attacks require intervention.",
                "When unsure, pause the situation, document objective facts, and consult HR or appropriate leadership.",
            ]
        )
    )
    return build_pdf(
        "efsp-american-pushback-quick-reference.pdf",
        "EFSP American Pushback Field Guide",
        story,
    )


def main() -> None:
    paths = [
        instructor_guide(),
        participant_workbook(),
        scenario_cards(),
        quick_reference(),
    ]
    for path in paths:
        print(path)


if __name__ == "__main__":
    main()
