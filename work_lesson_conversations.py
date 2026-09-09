"""Lesson-specific conversation scripts and bounded speaking scenarios."""
from functools import lru_cache
import hashlib
import html
import json
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "content/work/lesson-conversations"
EDITION = "2026-09-09"


@lru_cache(maxsize=41)
def load_course(slug):
    data = json.loads((SOURCE / f"{slug}.json").read_text())
    if set(data) != {f"module-{n}" for n in range(1, 9)}:
        raise ValueError(f"Incomplete conversation lessons: {slug}")
    seen = set()
    for module_id, lesson in data.items():
        conversations = lesson["conversations"]
        if len(conversations) != 3:
            raise ValueError(f"Expected three conversations: {slug}/{module_id}")
        if len({c["title"] for c in conversations}) != 3:
            raise ValueError(f"Repeated conversation title: {slug}/{module_id}")
        for conversation in conversations:
            turns = conversation["turns"]
            if not conversation["title"].strip() or not conversation["setting"].strip():
                raise ValueError(f"Untitled conversation: {slug}/{module_id}")
            if len(turns) != 10 or any(len(turn) != 2 or not all(s.strip() for s in turn) for turn in turns):
                raise ValueError(f"Expected ten complete speaking turns: {slug}/{module_id}")
            if len({role for role, speech in turns}) < 2:
                raise ValueError(f"Expected multiple speakers: {slug}/{module_id}")
            if any(a[0] == b[0] for a, b in zip(turns, turns[1:])):
                raise ValueError(f"Expected an exchange between speakers: {slug}/{module_id}")
            if len(" ".join(speech for role, speech in turns).split()) < 80:
                raise ValueError(f"Conversation lacks developed content: {slug}/{module_id}")
            fingerprint = json.dumps(turns)
            if fingerprint in seen:
                raise ValueError(f"Repeated script: {slug}/{module_id}")
            seen.add(fingerprint)
        scenario = lesson["additional_scenario"]
        for key in ("title", "brief", "role_a", "role_b", "opening_line", "complication"):
            if not scenario[key].strip():
                raise ValueError(f"Missing scenario {key}: {slug}/{module_id}")
        if len(scenario["success_checks"]) != 3 or not all(s.strip() for s in scenario["success_checks"]):
            raise ValueError(f"Expected three speaking checks: {slug}/{module_id}")
    return data


def lesson_content(track, module):
    return load_course(track["slug"])[module["id"]]


def content_hash():
    return hashlib.sha256(b"".join(p.name.encode() + p.read_bytes() for p in sorted(SOURCE.glob("*.json")))).hexdigest()


def render_activities(track, module):
    e = html.escape
    lesson = lesson_content(track, module)
    conversations = []
    for i, conversation in enumerate(lesson["conversations"], 1):
        turns = "".join(f'<li><strong>{e(role)}:</strong> {e(speech)}</li>' for role, speech in conversation["turns"])
        conversations.append(f'<details class="work-conversation"><summary>{i}. {e(conversation["title"])}</summary>'
                             f'<p>{e(conversation["setting"])}</p><ol class="work-conversation-lines">{turns}</ol></details>')
    scenario = lesson["additional_scenario"]
    workshop = module["workshop"]
    checks = "".join(f"<li>{e(check)}</li>" for check in scenario["success_checks"])
    return f'''<div class="work-practice">
<section class="work-conversations"><p class="work-kicker">05 · Conversations</p>
<h4>Three conversations at work</h4><p class="work-small">Original fictional training conversations. Each line is one speaking turn.</p>{''.join(conversations)}</section>
<section class="work-speaking"><p class="work-kicker">06 · Say it</p><h4>Two scenarios to practice</h4>
<div class="work-two-column"><section class="work-speaking-scenario"><h5>Scenario 1 · {e(module['title'])}</h5>
<p>{e(module['brief'])}</p><p>{e(module['speaking_task'])}</p>
<details><summary>Partner's role and follow-up</summary><p>{e(workshop['role_b'])}</p></details>
<details><summary>Try a harder second round</summary><p>{e(workshop['challenge'])}</p></details></section>
<section class="work-speaking-scenario"><h5>Scenario 2 · {e(scenario['title'])}</h5><p>{e(scenario['brief'])}</p>
<p><strong>Role A:</strong> {e(scenario['role_a'])}</p><p><strong>Role B:</strong> {e(scenario['role_b'])}</p>
<p><strong>Possible opening:</strong> “{e(scenario['opening_line'])}”</p>
<details><summary>Success checks</summary><ul>{checks}</ul></details>
<details><summary>Add a complication</summary><p>{e(scenario['complication'])}</p></details></section></div>
<p class="work-support"><strong>Studying alone?</strong> Speak both roles aloud. For each scenario, prepare for two minutes, speak for one minute, then answer a follow-up. Switch roles and repeat using fewer notes. Use only the supplied facts; identify missing information instead of inventing it.</p></section></div>'''
