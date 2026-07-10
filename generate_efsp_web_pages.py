from __future__ import annotations

import html
import importlib
import json
import re
from pathlib import Path
from typing import Any

from generate_efsp_guarded_activities import bounded_activity_instruction, make_dialogue_cloze, make_module_cloze, term_learning_fields
from generate_efsp_industry_batch_pdfs import INDUSTRIES, pdf_name, term_definition


ROOT = Path(__file__).resolve().parent


STANDARD_TRACKS = [
    {
        "module": "generate_efsp_ai_development_pdfs",
        "title": "AI Development English",
        "slug": "ai-development",
        "summary": "High-level technical English for AI engineers, researchers, product managers, data specialists, and safety teams.",
        "roles": "AI engineers, researchers, product managers, data specialists, safety teams, and AI-adjacent leaders",
        "pdf_slug": "ai-development",
    },
    {
        "module": "generate_efsp_general_it_pdfs",
        "title": "General IT English",
        "slug": "general-it",
        "summary": "Technical workplace English for IT operations, service desk, infrastructure, cloud, endpoint, security, and platform teams.",
        "roles": "IT operations, service desk, infrastructure, cloud, endpoint, security, and platform teams",
        "pdf_slug": "general-it",
    },
    {
        "module": "generate_efsp_law_pdfs",
        "title": "Law English",
        "slug": "law",
        "summary": "Legal workplace English for client intake, privilege, litigation, discovery, contracts, compliance, settlement, and advocacy.",
        "roles": "lawyers, paralegals, compliance staff, contracts specialists, legal operations teams, and law-adjacent professionals",
        "pdf_slug": "law",
    },
    {
        "module": "generate_efsp_finance_pdfs",
        "title": "Finance English",
        "slug": "finance",
        "summary": "Professional English for accounting, FP&A, treasury, banking, investments, audit, risk, and corporate finance.",
        "roles": "accounting, FP&A, treasury, banking, investments, audit, risk, corporate finance, and finance-adjacent teams",
        "pdf_slug": "finance",
    },
    {
        "module": "generate_efsp_financial_advice_pdfs",
        "title": "Financial Advice English",
        "slug": "financial-advice",
        "summary": "Client-facing English for discovery, recommendations, disclosures, risk profiling, retirement planning, and difficult conversations.",
        "roles": "financial advisors, planners, wealth-management teams, retirement specialists, paraplanners, and client-service staff",
        "pdf_slug": "financial-advice",
    },
    {
        "module": "generate_efsp_marketing_pdfs",
        "title": "Marketing English",
        "slug": "marketing",
        "summary": "Professional English for audience strategy, positioning, campaign briefs, channels, attribution, compliance, and brand risk.",
        "roles": "brand, product marketing, growth, content, SEO, lifecycle, demand generation, marketing operations, social, and agency teams",
        "pdf_slug": "marketing",
    },
    {
        "module": "generate_efsp_real_estate_pdfs",
        "title": "Real Estate English",
        "slug": "real-estate",
        "summary": "Real estate English for agency, fair housing, buyer and seller consultations, pricing, offers, disclosures, financing, and closing.",
        "roles": "real estate agents, brokers, transaction coordinators, property managers, leasing teams, and commercial real estate staff",
        "pdf_slug": "real-estate",
    },
    {
        "module": "generate_efsp_corporate_strategy_pdfs",
        "title": "Corporate Strategy English",
        "slug": "corporate-strategy",
        "summary": "Executive-level English for strategic diagnosis, tradeoffs, portfolio choices, growth, M&A, uncertainty, KPIs, and board narratives.",
        "roles": "corporate strategy, CEO office, transformation, corporate development, strategic finance, product strategy, and internal consulting teams",
        "pdf_slug": "corporate-strategy",
    },
    {
        "module": "generate_efsp_pharmaceutical_pdfs",
        "title": "Pharmaceutical English",
        "slug": "pharmaceutical",
        "summary": "Pharmaceutical English for drug development, regulatory strategy, trials, safety, CMC, quality, labeling, medical affairs, access, and launch.",
        "roles": "clinical development, regulatory affairs, pharmacovigilance, quality, CMC, manufacturing, medical affairs, market access, and compliance teams",
        "pdf_slug": "pharmaceutical",
    },
]


CULTURE_TRACK = {
    "title": "Cultural Leadership in US Branches",
    "slug": "cultural-leadership-us-branches",
    "summary": "Practical leadership English for Japanese and Chinese managers navigating US directness, pushback, meetings, feedback, and branch tension.",
    "roles": "Japanese and Chinese managers, cross-border leaders, HR partners, and senior facilitators",
    "pdfs": [
        ("Instructor Guide", "pdf/efsp/efsp-cultural-leadership-in-us-branches-instructor-guide.pdf"),
        ("Participant Workbook", "pdf/efsp/efsp-cultural-leadership-in-us-branches-participant-workbook.pdf"),
        ("Scenario Cards", "pdf/efsp/efsp-cultural-leadership-scenario-cards.pdf"),
        ("Quick Reference", "pdf/efsp/efsp-american-pushback-quick-reference.pdf"),
    ],
}


def e(text: Any) -> str:
    return html.escape(str(text), quote=True)


def strip_module_number(title: str) -> str:
    return re.sub(r"^Module\s+\d+\.\s*", "", title).strip()


def pdfs_for_standard(pdf_slug: str) -> list[tuple[str, str]]:
    return [
        ("Instructor Guide", f"pdf/efsp/efsp-{pdf_slug}-english-instructor-guide.pdf"),
        ("Participant Workbook", f"pdf/efsp/efsp-{pdf_slug}-english-participant-workbook.pdf"),
        ("Dialogue Lab", f"pdf/efsp/efsp-{pdf_slug}-dialogue-lab.pdf"),
        ("Jargon Guide", f"pdf/efsp/efsp-{pdf_slug}-jargon-quick-reference.pdf"),
    ]


def flatten_jargon(groups: list[tuple[str, list[tuple[str, str]]]]) -> list[dict[str, str]]:
    terms = []
    for group, items in groups:
        for term, definition in items:
            terms.append({**term_learning_fields(term, definition, group), "group": group})
    return terms


def model_line(dialogue: dict[str, Any] | None) -> str:
    if not dialogue:
        return "I understand the pressure, but I want to separate urgency from evidence, risk, owner, and decision rights before we commit."
    for speaker, line in dialogue.get("dialogue", []):
        if str(speaker).lower() == "esl learner":
            return line
    if dialogue.get("dialogue"):
        return dialogue["dialogue"][-1][1]
    return "Let's define the risk, the evidence, the owner, and the next decision."


def normalize_standard_track(spec: dict[str, str]) -> dict[str, Any]:
    mod = importlib.import_module(spec["module"])
    jargon = flatten_jargon(getattr(mod, "JARGON_GROUPS", []))
    dialogues = getattr(mod, "DIALOGUES", [])
    modules = []
    for index, module in enumerate(getattr(mod, "MODULES", [])):
        dialogue = dialogues[index % len(dialogues)] if dialogues else None
        terms = [item["term"] for item in jargon[index * 4 : (index + 1) * 4]] or [
            concept.split(":", 1)[0] for concept in module.get("concepts", [])[:4]
        ]
        modules.append(
            {
                "title": strip_module_number(module["title"]),
                "focus": module.get("big_idea", ""),
                "goals": [bounded_activity_instruction(item) for item in module.get("objectives", [])[:4]],
                "activities": module.get("activities", [])[:3],
                "outputs": module.get("outputs", [])[:3],
                "terms": terms,
                "scenario": dialogue.get("setting", module.get("big_idea", "")) if dialogue else module.get("big_idea", ""),
                "pressure": dialogue["dialogue"][0][1] if dialogue and dialogue.get("dialogue") else module.get("activities", [""])[0],
                "model": model_line(dialogue),
                "notes": dialogue.get("notes", []) if dialogue else module.get("concepts", [])[:2],
                "cloze": make_dialogue_cloze(dialogue, terms)
                if dialogue
                else make_module_cloze(
                    {
                        "title": strip_module_number(module["title"]),
                        "scenario": module.get("big_idea", ""),
                        "pressure": module.get("activities", [""])[0],
                        "terms": terms,
                        "outputs": module.get("outputs", []),
                    },
                    module.get("outputs", []),
                ),
            }
        )
    phrases = []
    for group, items in getattr(mod, "PHRASE_BANK", {}).items():
        for phrase in items:
            phrases.append({"group": group, "phrase": phrase})
    return {
        "title": spec["title"],
        "slug": spec["slug"],
        "summary": spec["summary"],
        "roles": spec["roles"],
        "pdfs": pdfs_for_standard(spec["pdf_slug"]),
        "modules": modules,
        "jargon": jargon,
        "phrases": phrases,
    }


def normalize_culture_track() -> dict[str, Any]:
    mod = importlib.import_module("generate_efsp_culture_pdfs")
    modules = []
    jargon = []
    source_modules = getattr(mod, "MODULES", [])
    scenarios = getattr(mod, "SCENARIOS", [])
    language_moves = getattr(mod, "CULTURE_LANGUAGE_MOVES", [])
    for index, module in enumerate(source_modules):
        terms = [concept.split(":", 1)[0] for concept in module.get("concepts", [])[:4]]
        for term, concept in zip(terms, module.get("concepts", [])[:4]):
            jargon.append({**term_learning_fields(term, concept, module["big_idea"]), "group": strip_module_number(module["title"])})
        scenario = scenarios[index % len(scenarios)] if scenarios else {}
        move = language_moves[index % len(language_moves)] if language_moves else "I want the strongest objection. Challenge the plan, not the person."
        dialogue = {
            "title": scenario.get("title", strip_module_number(module["title"])),
            "setting": scenario.get("context", module.get("big_idea", "")),
            "dialogue": [
                ("US colleague", scenario.get("colleague", module.get("activities", [""])[0])),
                ("ESL learner", move),
            ],
            "notes": [scenario.get("observer", "Keep the discussion focused on the work, the evidence, and a clear decision.")],
        }
        modules.append(
            {
                "title": strip_module_number(module["title"]),
                "focus": module.get("big_idea", ""),
                "goals": [bounded_activity_instruction(item) for item in module.get("objectives", [])[:4]],
                "activities": module.get("activities", [])[:3],
                "outputs": module.get("outputs", [])[:3],
                "terms": terms,
                "scenario": dialogue["setting"],
                "pressure": dialogue["dialogue"][0][1],
                "model": move,
                "notes": [scenario.get("observer", ""), *module.get("concepts", [])[:1]],
                "cloze": make_dialogue_cloze(dialogue, terms),
            }
        )
    phrases = []
    for group, items in getattr(mod, "PHRASE_BANK", {}).items():
        for phrase in items:
            phrases.append({"group": group, "phrase": phrase})
    return {**CULTURE_TRACK, "modules": modules, "jargon": jargon, "phrases": phrases}


def normalize_batch_track(profile: dict[str, Any]) -> dict[str, Any]:
    modules = []
    jargon = []
    all_outputs = [module["output"] for module in profile["modules"]]
    for module in profile["modules"]:
        for term in module["terms"]:
            jargon.append(
                {
                    **term_learning_fields(term, term_definition(term, profile, module), module["scenario"]),
                    "group": module["title"],
                }
            )
        modules.append(
            {
                "title": module["title"],
                "focus": module["skill"],
                "goals": [
                    f"Use these terms accurately: {', '.join(module['terms'])}.",
                    f"Explain the constraint: {module['constraint']}",
                    f"Respond to pressure: {module['pressure']}",
                ],
                "activities": [
                    "Select the field term that names the decision variable in context.",
                    "Choose the strongest evidence-based pushback response.",
                    f"Choose the facts, owner, and next decision that belong in a {module['output']}.",
                ],
                "outputs": [module["output"]],
                "terms": module["terms"],
                "scenario": module["scenario"],
                "pressure": module["pressure"],
                "model": (
                    f"I understand the urgency. Before we act, I need to verify {module['terms'][0]} and "
                    f"{module['terms'][1]} against the stated constraint, then I can recommend the next decision."
                ),
                "notes": [module["constraint"], f"Output: {module['output']}"],
                "cloze": make_module_cloze(module, all_outputs),
            }
        )
    return {
        "title": profile["title"],
        "slug": profile["slug"],
        "summary": profile["summary"],
        "roles": profile["roles"],
        "pdfs": [
            ("Instructor Guide", f"pdf/efsp/{pdf_name(profile, 'english-instructor-guide')}"),
            ("Participant Workbook", f"pdf/efsp/{pdf_name(profile, 'english-participant-workbook')}"),
            ("Dialogue Lab", f"pdf/efsp/{pdf_name(profile, 'dialogue-lab')}"),
            ("Jargon Guide", f"pdf/efsp/{pdf_name(profile, 'jargon-quick-reference')}"),
        ],
        "modules": modules,
        "jargon": jargon,
        "phrases": [
            {"group": "Pushback", "phrase": "I understand the urgency. The risk is that we move faster than the evidence or process supports."},
            {"group": "Decision", "phrase": "If we accept this risk, we should name the owner, document the assumption, and define the trigger for escalation."},
            {"group": "Scope", "phrase": "That may be possible, but not under the current scope, timeline, or approval path."},
        ],
        "collocations": [
            {"phrase": phrase, "use": use}
            for phrase, use in profile.get("collocations", [])
        ],
        "extra_dialogues": [
            {
                "title": dialogue["title"],
                "setting": dialogue["setting"],
                "turns": [
                    {"speaker": speaker, "line": line}
                    for speaker, line in dialogue.get("turns", [])
                ],
                "coach_notes": dialogue.get("coach_notes", []),
                "collocations": dialogue.get("collocations", []),
            }
            for dialogue in profile.get("dialogues", [])
        ],
        "nomenclature": [
            {"category": category, "term": term, "meaning": meaning}
            for category, term, meaning in profile.get("nomenclature", [])
        ],
    }


def all_tracks() -> list[dict[str, Any]]:
    tracks = [normalize_culture_track()]
    tracks.extend(normalize_standard_track(spec) for spec in STANDARD_TRACKS)
    tracks.extend(normalize_batch_track(profile) for profile in INDUSTRIES)
    return tracks


def json_script(data: dict[str, Any]) -> str:
    payload = json.dumps(data, ensure_ascii=True).replace("</", "<\\/")
    return f'<script id="efsp-page-data" type="application/json">{payload}</script>'


def pdf_links(pdfs: list[tuple[str, str]]) -> str:
    return "\n".join(f'<a class="efsp-download-link" href="{e(href)}">{e(label)}</a>' for label, href in pdfs)


def participant_workbook_href(pdfs: list[tuple[str, str]]) -> str:
    for label, href in pdfs:
        if label == "Participant Workbook":
            return href
    return pdfs[0][1]


def render_module_summaries(track: dict[str, Any]) -> str:
    items = []
    for index, module in enumerate(track["modules"], start=1):
        terms = ", ".join(module["terms"][:4])
        items.append(
            f"""<article class="efsp-module-summary">
<span class="efsp-module-number">{index}</span>
<h3>{e(module['title'])}</h3>
<p>{e(module['focus'])}</p>
<p class="efsp-term-line">{e(terms)}</p>
</article>"""
        )
    return "\n".join(items)


def render_practical_expansion(track: dict[str, Any]) -> str:
    collocations = track.get("collocations", [])
    dialogues = track.get("extra_dialogues", [])
    nomenclature = track.get("nomenclature", [])
    if not (collocations or dialogues or nomenclature):
        return ""

    collocation_html = ""
    if collocations:
        collocation_html = "\n".join(
            f"""<li>
<strong>{e(item['phrase'])}</strong>
<span>{e(item['use'])}</span>
</li>"""
            for item in collocations
        )
        collocation_html = f"""<article class="efsp-expansion-panel">
<h3>Collocation rehearsal</h3>
<p>Practice these as complete field moves: say the phrase, name the evidence it requires, then add the owner and next action.</p>
<ul class="efsp-collocation-list">
{collocation_html}
</ul>
</article>"""

    dialogue_html = ""
    if dialogues:
        dialogue_items = []
        for dialogue in dialogues:
            turns = "\n".join(
                f"""<div class="efsp-dialogue-turn">
<strong>{e(turn['speaker'])}</strong>
<span>{e(turn['line'])}</span>
</div>"""
                for turn in dialogue["turns"]
            )
            targets = ", ".join(dialogue.get("collocations", []))
            dialogue_items.append(
                f"""<details class="efsp-dialogue-preview">
<summary>{e(dialogue['title'])}</summary>
<p>{e(dialogue['setting'])}</p>
<div class="efsp-dialogue-turns">
{turns}
</div>
<p class="efsp-target-line">Target collocations: {e(targets)}</p>
</details>"""
            )
        dialogue_html = f"""<article class="efsp-expansion-panel">
<h3>Dialogue rehearsal</h3>
<p>Open a situation, assign roles, then replace one technical fact with a similar issue from the learner's workplace.</p>
{''.join(dialogue_items)}
</article>"""

    nomenclature_html = ""
    if nomenclature:
        by_category: dict[str, list[dict[str, str]]] = {}
        for item in nomenclature:
            by_category.setdefault(item["category"], []).append(item)
        category_blocks = []
        for category, items in by_category.items():
            rows = "\n".join(
                f"""<tr>
<th scope="row">{e(item['term'])}</th>
<td>{e(item['meaning'])}</td>
</tr>"""
                for item in items
            )
            category_blocks.append(
                f"""<details class="efsp-nomenclature-group">
<summary>{e(category)} <span>{len(items)} terms</span></summary>
<table class="efsp-nomenclature-table">
<tbody>
{rows}
</tbody>
</table>
</details>"""
            )
        nomenclature_html = f"""<article class="efsp-expansion-panel">
<h3>Specialized nomenclature</h3>
<p>Use the categories for sorting practice: term, plain-English meaning, business risk, and where the term appears in a real meeting.</p>
{''.join(category_blocks)}
</article>"""

    return f"""<section class="efsp-section efsp-practical-expansion">
<p class="eyebrow">Practical Language Expansion</p>
<h2>Collocations, dialogues, and specialized nomenclature</h2>
<div class="efsp-expansion-grid">
{collocation_html}
{dialogue_html}
{nomenclature_html}
</div>
</section>"""


def render_industry_page(track: dict[str, Any], tracks: list[dict[str, Any]]) -> str:
    module_summaries = render_module_summaries(track)
    practical_expansion = render_practical_expansion(track)
    student_pdf = participant_workbook_href(track["pdfs"])
    related = [item for item in tracks if item["slug"] != track["slug"]][:6]
    related_links = "\n".join(
        f'<a href="efsp-{e(item["slug"])}.html">{e(item["title"])}</a>' for item in related
    )
    page_data = {
        "title": track["title"],
        "modules": track["modules"],
        "jargon": track["jargon"],
        "phrases": track["phrases"],
    }
    for key in ["collocations", "extra_dialogues", "nomenclature"]:
        if track.get(key):
            page_data[key] = track[key]
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<title>English Ladder | {e(track['title'])}</title>
<link href="favicon.png" rel="icon" type="image/png">
<link href="styles.css" rel="stylesheet">
<!-- Cloudflare Web Analytics --><script defer src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{{"token": "c9c5fc6fc0f947efb5b32e0139ad4459"}}'></script><!-- End Cloudflare Web Analytics -->
</head>
<body class="theme-efsp">
<main class="page-shell">
<nav class="top-nav">
<a href="efsp.html">Back to EFSP Directory</a>
<span>{e(track['title'])}</span>
</nav>

<section class="efsp-industry-hero">
<div>
<p class="eyebrow">English for Special Purposes</p>
<h1>{e(track['title'])}</h1>
<p>{e(track['summary'])}</p>
<ul class="efsp-stat-list">
<li>{len(track['modules'])} modules</li>
<li>{len(track['jargon']) + len(track.get('nomenclature', []))} field terms</li>
<li>Interactive practice</li>
</ul>
</div>
<img alt="English Ladder logo" class="efsp-industry-logo" src="English-Ladder.png">
</section>

<section class="efsp-pdf-strip">
<div>
<p class="eyebrow">Printable Curriculum</p>
<h2>Download the full materials</h2>
</div>
<div class="efsp-download-grid" aria-label="{e(track['title'])} PDF downloads">
{pdf_links(track['pdfs'])}
</div>
</section>

<section class="efsp-workbench" data-efsp-workbench>
<div class="efsp-workbench-copy">
<p class="eyebrow">Web Practice Lab</p>
<h2>Rehearse the language, response, and decision</h2>
<p>Work through a three-step sequence: identify the field language, choose the strongest response, then select the next controlled decision move.</p>
</div>
<div class="efsp-module-picker" data-module-buttons></div>
<div class="efsp-practice-layout">
<article class="efsp-practice-panel">
<p class="eyebrow">Module Focus</p>
<h3 data-module-title></h3>
<p data-module-focus></p>
<ul data-module-goals></ul>
</article>
<article class="efsp-practice-panel">
<p class="eyebrow">Guided Decision Lab</p>
<h3 data-cloze-title></h3>
<p class="efsp-scenario-text" data-cloze-setting></p>
<div class="efsp-dialogue-lines" data-cloze-lines></div>
<div class="efsp-activity-steps" data-cloze-steps aria-label="Practice stages"></div>
<p class="efsp-field-label" data-cloze-instruction></p>
<p data-cloze-prompt></p>
<div class="efsp-choice-grid" data-cloze-options></div>
<div class="efsp-feedback" data-cloze-feedback></div>
</article>
<article class="efsp-practice-panel">
<p class="eyebrow">Jargon Flashcard</p>
<h3 data-card-term></h3>
<p data-card-definition hidden></p>
<p class="efsp-card-contrast" data-card-contrast hidden></p>
<ul class="efsp-card-collocations" data-card-collocations hidden></ul>
<p class="efsp-card-example" data-card-example hidden></p>
<div class="efsp-tool-row">
<button type="button" class="efsp-tool-button" data-action="reveal-card">Reveal</button>
<button type="button" class="efsp-tool-button efsp-tool-button-secondary" data-action="next-card">Next</button>
</div>
</article>
<article class="efsp-practice-panel">
<p class="eyebrow">Answer Rationale</p>
<h3>Why the strongest phrase fits</h3>
<p data-cloze-rationale>Choose an option to see the workplace rationale.</p>
<ul data-cloze-notes></ul>
</article>
<article class="efsp-practice-panel">
<p class="eyebrow">Dialogue Coach</p>
<h3>Model line</h3>
<p data-model-line></p>
<details>
<summary>Language notes</summary>
<ul data-language-notes></ul>
</details>
</article>
<article class="efsp-practice-panel">
<p class="eyebrow">Progress</p>
<h3>Practice checklist</h3>
<label><input type="checkbox" data-progress-item> I used at least two field terms accurately.</label>
<label><input type="checkbox" data-progress-item> I named the evidence or policy boundary.</label>
<label><input type="checkbox" data-progress-item> I gave a concrete next step.</label>
<label><input type="checkbox" data-progress-item> I avoided overpromising.</label>
<meter min="0" max="4" value="0" data-progress-meter></meter>
<p data-progress-label>0 of 4 complete</p>
</article>
</div>
</section>

<section class="efsp-section">
<div class="efsp-section-action-header">
<div>
<p class="eyebrow">Student PDF in Web Form</p>
<h2>Module map</h2>
</div>
<a class="efsp-student-pdf-link" href="{e(student_pdf)}">Open Participant Workbook PDF</a>
</div>
<div class="efsp-module-summary-grid">
{module_summaries}
</div>
</section>
{practical_expansion}
<section class="efsp-section">
<p class="eyebrow">More EFSP Tracks</p>
<h2>Related pages</h2>
<div class="efsp-related-links">
{related_links}
</div>
</section>
</main>
{json_script(page_data)}
<script src="app.js"></script>
</body>
</html>
"""


def render_directory(tracks: list[dict[str, Any]]) -> str:
    links = []
    pdf_count = sum(len(track["pdfs"]) for track in tracks)
    for track in tracks:
        links.append(
            f"""<a class="efsp-directory-link" href="efsp-{e(track['slug'])}.html" data-efsp-directory-link data-search="{e(track['title'] + ' ' + track['summary'] + ' ' + track['roles'])}">
<span>{e(track['title'])}</span>
<small>{e(track['summary'])}</small>
</a>"""
        )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<title>English Ladder | English for Special Purposes</title>
<link href="favicon.png" rel="icon" type="image/png">
<link href="styles.css" rel="stylesheet">
<!-- Cloudflare Web Analytics --><script defer src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{{"token": "c9c5fc6fc0f947efb5b32e0139ad4459"}}'></script><!-- End Cloudflare Web Analytics -->
</head>
<body class="theme-efsp">
<main class="page-shell">
<nav class="top-nav">
<a href="index.html">Back to Level Hub</a>
<span>English for Special Purposes curricula</span>
</nav>

<section class="efsp-hero efsp-directory-hero">
<div class="efsp-hero-copy">
<p class="eyebrow">English for Special Purposes</p>
<h1>Industry-specific English practice labs</h1>
<p>Choose an EFSP track to open a dedicated web page with practical module summaries, PDF downloads, and interactive activities built from the curriculum materials.</p>
<ul class="efsp-stat-list">
<li>{len(tracks)} tracks</li>
<li>{pdf_count} PDFs</li>
<li>Interactive web practice</li>
<li>Instructor-ready materials</li>
</ul>
</div>
<div class="efsp-hero-visual">
<img alt="English Ladder illustration" class="efsp-hero-image" src="English-Ladder.png">
</div>
</section>

<section class="efsp-section efsp-directory-section">
<div class="efsp-directory-header">
<div>
<p class="eyebrow">Curriculum Directory</p>
<h2>Open an industry page</h2>
</div>
<label class="efsp-search-label" for="efsp-search">Search tracks</label>
<input id="efsp-search" class="efsp-directory-search" type="search" placeholder="Search by industry, role, or situation" data-efsp-search>
</div>
<p class="efsp-directory-count" data-efsp-directory-count>{len(tracks)} tracks shown</p>
<div class="efsp-directory-list">
{''.join(links)}
</div>
</section>

<section class="efsp-section efsp-framework">
<p class="eyebrow">How To Use These Pages</p>
<h2>Web practice plus printable depth</h2>
<div class="efsp-pathway-grid">
<article>
<h3>Browse</h3>
<p>Use each page for a fast, practical view of the modules, situations, jargon, and decision language.</p>
</article>
<article>
<h3>Practice</h3>
<p>Use the web activities to rehearse pushback, scenario responses, jargon recall, and model dialogue lines.</p>
</article>
<article>
<h3>Print</h3>
<p>Download the PDFs when you need the full instructor guide, participant workbook, dialogue lab, or reference material.</p>
</article>
</div>
</section>
</main>
<script src="app.js"></script>
</body>
</html>
"""


def main() -> None:
    tracks = all_tracks()
    (ROOT / "efsp.html").write_text(render_directory(tracks))
    for track in tracks:
        (ROOT / f"efsp-{track['slug']}.html").write_text(render_industry_page(track, tracks))
    print(f"Generated {len(tracks)} EFSP industry pages plus efsp.html")


if __name__ == "__main__":
    main()
