"""Complete prompts at the point of use: no learner-authored prompt is required."""
import html
from work_ai_prompts import COMMON, LEVELS, MODE_BY_ID, payload
from work_dialogues import load_dialogues
from work_curriculum import ROOT

LESSON_MODES = ('vocabulary', 'grammar', 'roleplay', 'writing')
DIALOGUE_MODES = ('roleplay', 'dialogues')


def finished_prompt(data, mode, context):
    task = next(m for m in data['modes'] if m['id'] == mode)
    reference = next(c for c in data['contexts'] if c['id'] == context)
    common = COMMON.replace('Follow the practice instructions after the REFERENCE block.',
                            'Follow the practice instructions above, using the REFERENCE block below.')
    return '\n\n'.join([task['instructions'], common, LEVELS['B2'],
                         'REFERENCE\n' + data['course'] + '\n' + reference['text'] + '\nEND REFERENCE'])


def cards(data, context, modes):
    result = []
    for mode in modes:
        key = f'finished-{context}-{mode}'
        result.append(f'''<details class="finished-prompt"><summary>{html.escape(MODE_BY_ID[mode]['title'])} — complete prompt</summary>
<div class="finished-prompt-body"><p>Copy the full text below into your preferred AI. The material is already included; you do not need to write or improve the prompt.</p>
<button type="button" class="work-button" data-copy-finished="{key}" hidden>Copy this complete prompt</button>
<p data-finished-status="{key}" role="status" aria-live="polite"></p>
<pre id="{key}" tabindex="0" aria-label="Complete {html.escape(MODE_BY_ID[mode]['title'])} prompt">{html.escape(finished_prompt(data,mode,context))}</pre></div></details>''')
    return ''.join(result)


def lesson_prompts(t, m):
    data = payload(t, [])
    return f'<section class="finished-prompts" data-nosnippet><h4>Copy a finished AI prompt for this lesson</h4><p>These prompts are fully written and include this lesson\'s facts and language. Open one, copy it as written, and paste it into a new AI chat.</p>{cards(data,m["id"],LESSON_MODES)}</section>'


def dialogue_prompts(t):
    scripts = load_dialogues()[t['slug']]
    data = payload(t, scripts)
    cases = ''.join(f'<details class="finished-dialogue"><summary>Dialogue {i:02d}: {html.escape(d["title"])}</summary>{cards(data,f"dialogue-{i}",DIALOGUE_MODES)}</details>' for i,d in enumerate(scripts,1))
    return f'''<section class="work-section finished-dialogue-library" id="finished-dialogue-prompts" data-nosnippet><p class="work-kicker">Already written for you</p><h2>Copy a prompt for your Conversation Lab dialogue</h2><p>Each dialogue has two complete prompts: rehearse with an AI colleague, or ask for additional professional scenarios and full scripts. Every prompt includes the original exchange.</p><p><a class="work-button" href="prompts/work/{t['slug']}.txt" download>Download all finished prompts for this course</a></p>{cases}</section>'''


def write_prompt_packs(tracks):
    folder = ROOT/'prompts/work';folder.mkdir(parents=True,exist_ok=True)
    scripts=load_dialogues()
    count=0
    for t in tracks:
        data=payload(t,scripts[t['slug']])
        blocks=[f'{t["title"]} — COMPLETE AI PRACTICE PROMPTS',
                'Every block is a finished prompt. Copy one entire block between START PROMPT and END PROMPT into a new chat in your preferred AI. No prompt-writing is required. Use fictional or anonymized details when the exercise asks for your own response.']
        for c in data['contexts']:
            modes=tuple(MODE_BY_ID) if c['kind']=='lesson' else DIALOGUE_MODES
            for mode in modes:
                blocks += [c['title']+' | '+MODE_BY_ID[mode]['title'],
                           'START PROMPT\n'+finished_prompt(data,mode,c['id'])+'\nEND PROMPT']
                count+=1
        (folder/(t['slug']+'.txt')).write_text('\n\n'+'\n\n'.join(blocks)+'\n')
    return count
