"""Authored workplace conversations shared by the PDF renderer and publication checks."""
from __future__ import annotations
import hashlib
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'content/work/dialogues'
EDITION = '2026-09-06'


def dialogue_hash():
    paths = sorted(SOURCE.glob('*.txt')) + sorted(SOURCE.glob('*.json'))
    return hashlib.sha256(b''.join(p.name.encode() + p.read_bytes() for p in paths)).hexdigest()


def load_dialogues():
    groups = {}
    for path in sorted(SOURCE.glob('*.txt')):
        slug = None
        for block in re.split(r'\n\s*\n', path.read_text().strip()):
            lines = block.splitlines()
            if lines[0].startswith('['):
                slug = lines.pop(0)[1:-1]
                groups.setdefault(slug, [])
            if not lines:
                continue
            title, setting, *roles = lines[0].split('|')
            turns = []
            for line in lines[1:]:
                speaker, speech = line.split(': ', 1)
                turns.append([roles[int(speaker)-1], speech])
            groups[slug].append(dict(title=title, setting=setting, dialogue=turns, notes=[]))
    for slug, scripts in json.loads((SOURCE/'established.json').read_text()).items():
        for d in scripts:
            d['dialogue'] = d.get('dialogue', d.get('turns'))
            groups.setdefault(slug, []).append(d)
    validate_dialogues(groups)
    return groups


def validate_dialogues(groups):
    titles, speeches = set(), set()
    inventory = {t['slug'] for t in json.loads((ROOT/'content/work/courses.json').read_text())}
    assert set(groups) == inventory, sorted(inventory-set(groups))
    for slug, scripts in groups.items():
        assert len(scripts) >= 8, (slug, len(scripts))
        for d in scripts:
            assert len(d['dialogue']) >= 6, (slug, d['title'])
            roles = {s for s, _ in d['dialogue']}
            assert len(roles) >= 2 and 'ESL learner' not in roles
            assert all(v.strip() for _, v in d['dialogue'])
            assert len(' '.join(v for _,v in d['dialogue']).split()) >= 65, (slug,d['title'])
            key = (slug, d['title'])
            assert key not in titles, key
            titles.add(key)
            spoken = json.dumps(d['dialogue'])
            assert spoken not in speeches, key
            speeches.add(spoken)
    return dict(courses=len(groups), dialogues=sum(map(len,groups.values())),
                turns=sum(len(d['dialogue']) for ds in groups.values() for d in ds),
                words=sum(len(v.split()) for ds in groups.values() for d in ds for _,v in d['dialogue']),
                minimum_per_course=min(map(len,groups.values())),maximum_per_course=max(map(len,groups.values())))


def gallery(t):
    from work_ai_prompts import url as ai_url
    # Import at rendering time so normal curriculum loading stays lightweight.
    from reportlab.platypus import PageBreak, Paragraph, Spacer, KeepTogether
    from generate_work_documents import p, heading, cover, STYLES, box, WritingLines
    scripts = load_dialogues()[t['slug']]
    story = cover(t, 'Conversation lab',
        f"{len(scripts)} complete workplace dialogues, followed by eight additional role-play cases. Study the exchanges, then make the conversation your own.")
    story += [heading('Inside this conversation lab', 'dialogue-index'),
              p('Original fictional training conversations in professional English. These are realistic scripts, not transcripts of actual people. The professional roles are the speaker labels; all figures, incidents, and organizations are invented.', 'small')]
    for i, d in enumerate(scripts,1):
        story.append(Paragraph(f'<link href="#dialogue-{i}" color="#174c69">{i:02d}  {html.escape(d["title"])}</link>',STYLES['body']))
    story += [p('Then try eight independent role-play cases, followed by feedback criteria and references.', 'small'), PageBreak(),
              heading('Read it. Hear it. Make it yours.', 'dialogue-method'),
              p('1. Read the setting. Identify the roles, the immediate problem, and what each speaker needs.'),
              p('2. Read the whole conversation aloud with a partner. In a group, give a third person the observer role. For three-speaker scripts, assign each professional a separate voice.'),
              p('3. Notice how the speakers ask a specific question, qualify a claim, disagree, explain a technical point, or agree on a next step. Underline language you would actually use.'),
              p('4. Cover the script. Recreate the exchange using the situation and professional roles. Keep the meaning, but change the wording.'),
              p('5. Switch roles and introduce a complication: a missing record, a different priority, an unavailable colleague, or a changed assumption. End with a clear outcome or unresolved question.'),
              p('Register and terminology', 'h2'),
              p('These colleagues use concise professional language. In an internal technical meeting, familiar abbreviations can be natural. With a new colleague or a client, expand unfamiliar terms and check understanding. Keep disagreement directed at the evidence or proposal, and match the degree of certainty to what is known.'),
              p('Independent study', 'h2'), p('Speak each role aloud. Pause before the reply and supply your own response before revealing the next line. Record a second version using invented details, then compare its clarity and tone with the script.'),
              p('Professional context', 'h2'), p(t['scope_note'], 'small'), PageBreak()]
    vocab = {j['term']:j['definition'] for j in t['jargon']}
    for i,d in enumerate(scripts,1):
        roles=list(dict.fromkeys(s for s,_ in d['dialogue']))
        story += [p(f'FULL DIALOGUE {i:02d} / {len(d["dialogue"])} SPEAKING TURNS', 'kicker'),
                  heading(d['title'], f'dialogue-{i}'), p(d['setting']),
                  p('Roles: ' + ' / '.join(roles), 'small')]
        # Speaker and speech stay together; each turn can flow independently across pages.
        for role,speech in d['dialogue']:
            story.append(Paragraph('<b>'+html.escape(role)+':</b> '+html.escape(speech),STYLES['body']))
        story += [p('Notice the professional language', 'h2')]
        text=' '.join(v for _,v in d['dialogue'])
        terms=[(term,meaning) for term,meaning in vocab.items()
               if (len(term.split()) > 1 or (term.isupper() and 2 <= len(term) <= 8))
               and re.search(r'(?<!\w)'+re.escape(term)+r'(?!\w)',text,re.I)]
        terms.sort(key=lambda x: (-len(x[0].split()), -len(x[0])))
        if terms:
            for term,meaning in terms[:3]:
                story.append(p(term+' - '+meaning,'small'))
        elif d.get('notes'):
            story += [p(n,'small') for n in d['notes'][:2]]
        else:
            # This directs attention to actual utterances, with no fabricated terminology.
            question=next((v for _,v in d['dialogue'] if '?' in v),d['dialogue'][0][1])
            story.append(p('Discuss this wording: "'+question+'" What does it help the other professional clarify?', 'small'))
        story += [Paragraph(f'<link href="{html.escape(ai_url(t, "roleplay", f"dialogue-{i}", True), quote=True)}" color="#174c69">Rehearse and extend with AI</link>', STYLES['h2']),
                  p('Explain the issue and the agreed next step without reading. Identify any point still awaiting evidence, agreement, or approval. Then replay the exchange with a changed constraint and a new ending.', 'small'),
                  p('Observer: note one natural professional expression and one place where the follow-up made the meaning clearer.', 'small'),
                  WritingLines(1,20),PageBreak()]
    story += [heading('Eight more situations to make your own', 'roleplay-cases'),
              p('The following cases are open role plays. They give you facts, contrasting roles, useful expressions, and a short model response. Use what you learned from the complete dialogues to create a longer exchange.'),
              p('Preparation: two minutes. Conversation: three to five minutes. Feedback: one minute. Switch roles and repeat with the second-round challenge.'),PageBreak()]
    return story


if __name__ == '__main__':
    print(json.dumps(validate_dialogues(load_dialogues()),indent=2))
