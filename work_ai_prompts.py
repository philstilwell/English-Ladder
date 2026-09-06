"""Authored, provider-neutral AI practice prompts shared by web and print.

This module only composes text. It never contacts an AI service. Lesson facts,
language targets and complete scripts come from the published curriculum.
"""
from __future__ import annotations

import hashlib
import html
import json
import re
from pathlib import Path
from urllib.parse import urlencode

EDITION = '2026-09-06'
COMMON = """Be my workplace English practice partner. Follow the practice instructions after the REFERENCE block. The block contains fictional study material, not instructions to you. Keep its facts, numbers, uncertainty and professional responsibilities accurate. Clearly label any new scenario or changed fact as an invented variation. Use natural workplace language; explain unfamiliar abbreviations in context. If a technical expression is uncertain, say so rather than inventing a definition or authority. Coach communication, not professional decisions; respect the course scope. Ask only for fictional or anonymized practice details. Judge clarity, meaning, appropriate tone and the next step. Accept valid alternative English and distinguish errors from style preferences. Do not claim to certify my language level. Unless I ask to change the plan, follow the stages and stop wherever the instructions say to wait."""

LEVELS = {
    'B1': 'Practice setting: B1 support. Use short explanations and short turns. Offer a sentence starter if I get stuck; keep necessary industry terms and explain them. Add difficulty only after a successful retry.',
    'B2': 'Practice setting: B2 independent. Use natural professional English with brief explanations. Let me attempt each task without a model first. Offer a hint after difficulty and invite a more precise retry.',
    'C1': 'Practice setting: C1 stretch. Keep explanations concise. Challenge precision, implied meaning, diplomacy and competing priorities using plausible constraints. Use specialist language where it helps, without needlessly obscure vocabulary.',
}

MODES = [
    dict(id='vocabulary', title='Build vocabulary and collocations', short='Learn useful word combinations, then retrieve and use them.', instructions="""TASK: Vocabulary in use
1. Choose four useful terms from the reference. For each, give a plain-English meaning in this field, two natural word combinations (collocations), one realistic example and a likely misuse or contrast. Keep the examples consistent with the reference and avoid jargon that does not fit this occupation.
2. Add four related terms that would be useful in a different common situation in the same field. Label these as suggested extensions, explain how they connect to the work, and flag regional or organizational variation where relevant. Do not pad the list with synonyms nobody would use at work.
3. Start a retrieval round: give one short workplace sentence with a gap and a clear clue. Ask me to supply the best term and explain my choice. Stop and wait; do not reveal the answer or a completed sentence yet. Accept another term if its meaning and collocation work.
4. After my attempt, explain one useful distinction and ask me to write my own sentence. Wait, correct a genuine meaning or usage problem, then give the next retrieval question. Work through four questions one at a time.
5. Finish with a short handoff or message task using three terms, followed by two recall questions I can save for another day. Do not pretend to schedule a reminder."""),
    dict(id='grammar', title='Practice grammar in context', short='Use the lesson’s language pattern to communicate more precisely.', instructions="""TASK: Grammar that changes the meaning
1. For a lesson, use its language workshop as the focus. For a dialogue, quote one actual sentence and select one useful grammar feature from it, such as question word order, tense, modality, conditionals or clause linking. Explain in no more than 90 words how this feature helps the speakers do their work. Keep the grammar target narrow.
2. Give two short contrasting sentences using this workplace context. Explain the difference in time, certainty, condition or politeness. Label invented examples and preserve the distinction between possible, planned and confirmed events. Describe context-dependent choices as choices, not universal rules.
3. Give me one editing or sentence-building task using a known case fact. Do not copy the supplied editing example or reveal its answer. Ask me to explain my intended meaning. Stop and wait.
4. After I answer, quote my wording, identify at most two issues, and give a brief explanation and one hint. Ask me to revise before offering a full corrected version. Then accept any accurate, natural alternative that serves the purpose.
5. Continue with two new tasks, one at a time: first guided, then an original response without a sentence frame. End with a two-sentence workplace message using the target feature and a compact self-check. Do not replace this sequence with a worksheet and answer key."""),
    dict(id='roleplay', title='Rehearse with an AI colleague', short='You take one role. The AI answers as the other professional.', instructions="""TASK: Interactive workplace role-play
1. Use the supplied case or dialogue as the starting situation. Give a two-sentence briefing and offer two relevant professional roles for me to choose from. For a supplied dialogue, use its actual roles. Ask which role I want, then stop and wait. Do not write my replies.
2. After I choose, identify who you will play and the immediate communication goal. Play the other professional; where a meeting requires a third person, label each of your speakers clearly. Start with one natural workplace turn and wait for my reply. Keep most turns to one to three sentences and ask no more than one question at a time.
3. Let the exchange develop across six to ten learner turns, or end earlier if I type "feedback". Respond to what I actually say. Include a plausible clarification, disagreement or tradeoff without silently changing the starting facts. Mark any added constraint as a fictional second-round variation. Do not resolve approvals, evidence or commitments that remain uncertain.
4. Stay in role during the exchange. If my meaning is unclear, ask for clarification naturally. Give a hint only if I ask or cannot proceed. Do not deliver a model conversation in advance.
5. At the debrief, quote two of my phrases: one successful choice and one worth improving. Check factual accuracy, language, register and whether the next step was clear. Give up to three focused suggestions. Ask me to retry the weakest turn; wait. Only then offer an alternative wording and a harder replay."""),
    dict(id='dialogues', title='Create more scenario dialogues', short='Extend the lab with substantial, realistic professional exchanges.', instructions="""TASK: Extend the conversation library
1. Propose six distinct, common scenarios in this field beyond the supplied case or script. For each, name the setting, two or more professional roles, the communication problem and one useful terminology focus. Include routine coordination, clarification, a complication, disagreement, handoff and follow-up where relevant. Choose scenarios that fit this profession, rather than forcing unsuitable situations into it.
2. Ask me to choose one scenario, or request all six in sequence. Stop and wait. Do not write all the scripts before I choose.
3. For the selected scenario, write an original fictional dialogue of 12-18 substantial speaking turns between two or three professionals. Name each role, establish an actual work problem, and let the exchange progress through questions, clarification, competing constraints and a credible next step or explicitly unresolved issue. Use the occupation's natural nomenclature and register. Avoid an interview between a teacher and a learner, generic small talk, and inserting a glossary definition into every reply. Explain specialist terms outside the dialogue instead.
4. After the script, explain five useful expressions in context, identify two grammar or register choices and ask three questions about the speakers' reasoning. Withhold the answers until I attempt them. Add one role-switch challenge.
5. Before presenting a script, check names, numbers, chronology, roles and terminology for consistency. Label invented facts and acknowledge uncertain specialist usage. If I requested all six, deliver one complete script at a time and wait for "next". Make each scenario materially different."""),
    dict(id='writing', title='Get feedback on a draft', short='Improve your own message while preserving its intended meaning.', instructions="""TASK: Coach my workplace writing
1. Ask me to paste my own fictional or anonymized draft and identify its reader and purpose. If the reference gives a writing task, mention that task as the default. If it is a dialogue, suggest a brief follow-up message that records its outcome and open questions. Stop and wait. Do not write the message for me first.
2. Once I supply the draft, check it against the reference. If an ambiguity changes the meaning, ask one focused question before rewriting. Do not assume that the draft is correct evidence for a new deadline, approval, diagnosis, cost or commitment.
3. Give feedback in three parts: one effective phrase with a reason; up to three priority improvements, quoting my words; and one short revision task for me. Prioritize incorrect facts or unclear action before minor grammar. For each language correction, explain why it matters to this reader. Label optional stylistic alternatives separately and preserve my level of certainty and intended politeness.
4. Stop and wait for my revision. Then compare the two attempts, identify an improvement and offer one edited version that preserves my voice and purpose. Keep the requested length; if none is specified, use 70-110 words. Explain any meaningful change rather than silently making the message stronger or more certain.
5. Close with one phrase worth reusing and a short transfer task for a different fictional reader. Wait for my attempt before providing another model."""),
    dict(id='register', title='Adjust tone and register', short='Adapt the same meaning for a colleague, manager or outside reader.', instructions="""TASK: Match the language to the listener
1. Choose a short message or utterance from the reference and quote it exactly. Identify its purpose and likely audience. Ask me to choose a new audience: a close colleague, a decision-maker, or an external reader who may not know the jargon. Stop and wait.
2. Ask me to adapt that message for the chosen reader, keeping its facts and degree of certainty unchanged. Offer a short frame only if I request help. Wait for my attempt before showing alternatives.
3. Discuss at most three choices in my version: directness, specialist vocabulary and interpersonal tone. Explain when a direct request is clearer than extra politeness, and when an unfamiliar abbreviation needs expansion. Avoid cultural stereotypes or claims that one nationality always communicates a certain way.
4. Show two natural alternatives, such as a concise spoken version and a more explicit written version. Explain the tradeoff in each. Do not turn a request into an order, a possibility into a promise, or a pending decision into approval.
5. Ask me to respond to one realistic follow-up from the new reader, then wait. Finish by asking me to adapt the message for a second audience without losing its core meaning. Give feedback only after the attempt."""),
    dict(id='review', title='Test recall and transfer', short='Retrieve vocabulary, interpret meaning and respond without a model.', instructions="""TASK: A short retrieval session
1. Tell me to close my notes. Plan six questions: two vocabulary-in-context items, one grammar or meaning contrast, one question about a confirmed versus unknown detail, one short spoken-style response and one new-situation transfer task. Use the supplied material as the answer reference, but do not repeat its existing checks word for word.
2. Ask only the first question, then stop and wait. Prefer a short answer over a multiple-choice question. Do not display the remaining questions, model answers or a word bank in advance.
3. After each answer, say what it gets right and explain a meaningful error if there is one. Accept alternative wording when it preserves the facts and does the communication job. If I struggle, give one clue and invite a retry before revealing a model. Only then move to the next question.
4. Keep a simple record of which items I answered independently, with a hint, or after seeing a model. This records today's practice, not a certified proficiency score. Do not judge pronunciation from typed text.
5. At the end, summarize two strengths and two useful next steps with examples from my answers. Give me a small review card containing three prompts and a separate answer section. Suggest that I revisit it tomorrow and a week later; do not claim you will remember this session or send reminders. Label the final transfer scenario as fictional."""),
    dict(id='teacher', title='Adapt a partner or class activity', short='Prepare differentiated practice with separate learner and teacher material.', instructions="""TASK: Adapt this material for a teaching session
1. Ask me one brief planning question covering learner support needs, group size and available time. Offer a default of two B2 learners and 20 minutes. Stop and wait; use the default only if I choose it.
2. Create a timed plan using the supplied case or dialogue, its actual terminology and one narrow language goal. Include an individual first attempt, partner exchange, focused feedback and a retry. Keep the total within the time I choose. State what the learner should be able to communicate at the end.
3. Provide separate role cards for two or three professional speakers. Each card needs an objective, known information and one question to resolve. Label any invented private information as a variation; do not contradict shared facts. Do not place the model answer on the learner cards.
4. Add a B1 support option with useful frames, a B2 independent task and a C1 extension involving a plausible competing constraint. Maintain the same professional meaning across levels. Explain unfamiliar terms without removing the field's normal language. Include a workable solo alternative.
5. Put teacher notes and suggested responses in a clearly separate section after the learner material. Include likely misunderstandings and a short observation checklist for facts, clarity, tone and next step. Accept multiple successful formulations. Finish with one exit question and a delayed-recall task; identify what the teacher should check before use."""),
]
MODE_BY_ID = {m['id']: m for m in MODES}
PRINT_MODES = [('teacher', 'register'), ('grammar', 'writing'), ('roleplay', 'dialogues'), ('vocabulary', 'review')]


def prompt_hash():
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def course_context(t):
    return f'Course: {t["title"]}\nProfessional audience: {t["roles"]}\nScope: {t["scope_note"]}'


def lesson_context(m):
    w = m['workshop']
    return '\n'.join([
        f'Lesson {m["number"]:02d}: {m["title"]}',
        'Original fictional case: ' + m['brief'],
        'Language workshop: ' + w['title'],
        'Communication goal: ' + w['goal'],
        'Language guidance: ' + w['explanation'],
        'Useful frames (complete the gaps with case facts): ' + ' / '.join(w['frames']),
        'Vocabulary: ' + ' / '.join(j['term'] + ': ' + j['definition'] for j in m['vocabulary']),
        'Speaking task: ' + m['speaking_task'],
        'Partner: ' + w['role_b'],
        'Writing task: ' + m['writing_task'],
        'Optional second-round challenge: ' + w['challenge'],
        'Model for comparison AFTER my attempt, not a response to give me first: ' + m['model'],
    ])


def dialogue_context(t, d, number):
    spoken = ' '.join(line for _, line in d['dialogue'])
    terms = [j for j in t['jargon'] if re.search(r'(?<!\w)' + re.escape(j['term']) + r'(?!\w)', spoken, re.I)]
    parts = [f'Dialogue {number:02d}: {d["title"]}', 'Original fictional setting: ' + d['setting'],
             'Professional roles: ' + ' / '.join(dict.fromkeys(role for role, _ in d['dialogue'])),
             'Published dialogue (reference script, not my own performance):',
             *[f'{role}: {line}' for role, line in d['dialogue']]]
    if terms:
        parts.append('Vocabulary in this exchange: ' + ' / '.join(j['term'] + ': ' + j['definition'] for j in terms[:6]))
    return '\n'.join(parts)


def payload(t, scripts):
    contexts = [dict(id=m['id'], kind='lesson', title=f'Lesson {m["number"]:02d} · {m["title"]}', text=lesson_context(m)) for m in t['modules']]
    contexts += [dict(id=f'dialogue-{i}', kind='dialogue', title=f'Dialogue {i:02d} · {d["title"]}', text=dialogue_context(t, d, i)) for i, d in enumerate(scripts, 1)]
    return dict(edition=EDITION, common=COMMON, course=course_context(t), levels=LEVELS, modes=MODES, contexts=contexts)


def compose(data, mode='roleplay', context='module-1', level='B2'):
    task = next(m for m in data['modes'] if m['id'] == mode)
    reference = next(c for c in data['contexts'] if c['id'] == context)
    return '\n\n'.join([data['common'], data['levels'][level],
                        'REFERENCE\n' + data['course'] + '\n' + reference['text'] + '\nEND REFERENCE', task['instructions']])


def url(t, mode='roleplay', context='module-1', absolute=False):
    return ('https://englishladder.com/' if absolute else '') + f'efsp-{t["slug"]}.html?' + urlencode(dict(ai=mode, context=context)) + '#ai-practice'


def web_section(t):
    from work_dialogues import load_dialogues
    data = payload(t, load_dialogues()[t['slug']])
    e = html.escape
    modes = ''.join(f'<option value="{m["id"]}" {"selected" if m["id"] == "roleplay" else ""}>{e(m["title"])}</option>' for m in MODES)
    contexts = ''.join('<optgroup label="' + label + '">' + ''.join(f'<option value="{c["id"]}">{e(c["title"])}</option>' for c in data['contexts'] if c['kind'] == kind) + '</optgroup>' for kind, label in [('lesson', 'Eight lessons'), ('dialogue', 'Conversation Lab dialogues')])
    serialized = json.dumps(data, ensure_ascii=True).replace('<', '\\u003c')
    return f'''<section class="work-section work-ai" id="ai-practice" data-ai-workshop>
<div class="work-section-heading"><div><p class="work-kicker">Extend your practice</p><h2>Bring your own AI study partner.</h2></div><span>8 ways to practice</span></div>
<p>Try the lesson or rehearse the dialogue first. Then choose a goal and copy a carefully scripted prompt into your preferred AI. The prompt includes the actual case, language and professional context.</p>
<div class="work-ai-controls" data-ai-controls hidden>
<label for="ai-goal">What would you like to practice?<select id="ai-goal" data-ai-mode>{modes}</select></label>
<label for="ai-context">Which lesson or dialogue?<select id="ai-context" data-ai-context>{contexts}</select></label>
<label for="ai-level">How much support?<select id="ai-level" data-ai-level><option value="B1">B1 · With support</option><option value="B2" selected>B2 · Independent</option><option value="C1">C1 · Stretch</option></select></label></div>
<p class="work-ai-description" data-ai-description>{e(MODE_BY_ID['roleplay']['short'])}</p>
<p class="work-small">These settings adjust the practice; they are not an assessment of your level.</p>
<div class="work-ai-actions" data-ai-actions hidden><button class="work-button" type="button" data-ai-copy>Copy prompt</button><a class="work-text-button" data-ai-download download="{t['slug']}-ai-practice.txt">Save prompt as text</a><a class="work-text-button" data-ai-link href="{e(url(t))}">Link to this prompt</a></div>
<p class="work-ai-status" data-ai-status role="status" aria-live="polite"></p>
<details class="work-ai-preview" open><summary>Read your ready-to-use prompt</summary>
<label class="sr-only" for="ai-prompt">Prompt to copy into your preferred AI</label>
<textarea id="ai-prompt" data-ai-prompt readonly rows="15" spellcheck="false" maxlength="30000">{e(compose(data))}</textarea>
<pre class="work-ai-print" data-ai-print aria-hidden="true">{e(compose(data))}</pre></details>
<noscript><p>You can select and copy the prompt above for Lesson 01. Enable JavaScript to choose another task, lesson or dialogue.</p></noscript>
<p class="work-small">Paste into a new chat, then follow the exercise one step at a time. For writing feedback, the AI will ask for your draft; use fictional or anonymized details. Your drafts are not added to these prompts. English Ladder does not send anything to an AI service. Your chosen service's terms and any usage charges apply.</p>
<p class="work-small">AI responses can contain mistakes. Compare feedback with the lesson and check specialist claims against the course references. Use these exercises for language practice; follow qualified guidance for actual professional decisions.</p>
<script type="application/json" data-ai-data>{serialized}</script></section>'''


def pdf_link(t, mode, context, label):
    from reportlab.platypus import Paragraph
    from generate_work_documents import STYLES
    return Paragraph(f'<link href="{html.escape(url(t, mode, context, True), quote=True)}" color="#174c69">{html.escape(label)}</link>', STYLES['small'])


def pdf_appendix(t, kind):
    """Two fully copyable starter prompts; every context remains available online."""
    from reportlab.platypus import PageBreak
    from generate_work_documents import p, heading
    from work_dialogues import load_dialogues
    data = payload(t, load_dialogues()[t['slug']])
    context = 'dialogue-1' if kind == 2 else 'module-1'
    story = [PageBreak(), heading('Extend your practice with AI', 'ai-practice'),
             p('Use the next two prompts after your own first attempt. Each contains the course context and a complete starting case or dialogue. Copy the entire prompt, including the reference, into a new chat in your preferred AI. You can also use the links to copy it from the website.'),
             p('Choose the right kind of help', 'h2'),
             p('A role-play prompt makes the AI wait for your replies. A new-dialogue prompt asks for a complete professional script. Writing feedback begins with your draft. Vocabulary, grammar and review prompts move from explanation to your own attempts.'),
             p('Choose any lesson or dialogue online', 'h2'),
             p('The course prompt workshop has eight practice goals and B1 support, B2 independent and C1 stretch settings. These are practice choices, not assessed proficiency levels. Select the same lesson number or dialogue title you used in this guide.'),
             pdf_link(t, PRINT_MODES[kind][0], context, 'Open this course\'s AI prompt workshop'),
             p('Keep practice useful', 'h2'),
             p('Use fictional or anonymized details. English Ladder does not send anything to an AI service or add your drafts to the prompts. Your chosen service\'s terms and any usage charges apply. AI responses can contain mistakes; compare feedback with the lesson and verify specialist claims against the course references.'),
             p('The two starter prompts use B2 practice. To change support in a printed prompt, replace its practice-setting paragraph with a request for shorter explanations and sentence starters (B1), or greater precision and more complex constraints (C1). Keep the professional facts unchanged.'),
             p('Changing the example', 'h2'),
             p('For another case on paper, replace the text between REFERENCE and END REFERENCE with that case, its course context, relevant terms and language target. Include the full exchange if practicing a dialogue. Do not assume your AI can access this PDF or a link. The website makes this substitution for you.'),
             p('Prompt edition: ' + EDITION + '. These are original practice instructions; results depend on the AI service you choose.', 'small')]
    for mode in PRINT_MODES[kind]:
        story += [PageBreak(), heading(MODE_BY_ID[mode]['title'], 'ai-' + mode),
                  p('START PROMPT / COPY THROUGH END PROMPT', 'kicker')]
        # Paragraphs, rather than a single oversized block, keep long references
        # readable and allow natural page breaks without shrinking the type.
        prompt = compose(data, mode, context)
        for paragraph in prompt.split('\n\n'):
            for line in paragraph.splitlines():
                story.append(p(line, 'prompt'))
        story += [p('END PROMPT', 'kicker'), pdf_link(t, mode, context, 'Copy this prompt online or choose another lesson and support level')]
    return story
