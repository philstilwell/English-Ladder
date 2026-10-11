"""Lesson-specific conversation scripts and bounded speaking scenarios."""
from functools import lru_cache
import hashlib
import json
from pathlib import Path
from work_occupations import OCCUPATION_SLUGS, load_occupation, source_paths

SOURCE = Path(__file__).resolve().parent / "content/work/lesson-conversations"
EDITION = "2026-09-28"


@lru_cache(maxsize=None)
def load_course(slug):
    data = (load_occupation(slug)['lesson_conversations'] if slug in OCCUPATION_SLUGS
            else json.loads((SOURCE / f"{slug}.json").read_text()))
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
    paths = sorted(SOURCE.glob('*.json')) + source_paths()
    return hashlib.sha256(b"".join(p.name.encode() + p.read_bytes() for p in paths)).hexdigest()


def render_activities(track, module):
    from work_web_lessons import render_practice
    return render_practice(track, module)
