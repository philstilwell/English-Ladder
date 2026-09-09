"""Publication contracts for context-carrying prompts, links and printable copies."""
import json
import unittest
from urllib.parse import parse_qs, urlparse

from bs4 import BeautifulSoup
from pypdf import PdfReader
from work_curriculum import ROOT, load_tracks
from work_dialogues import load_dialogues
from work_ai_prompts import MODES, PRINT_MODES, compose, payload, prompt_hash, url


def normalized(value):
    # Match typographic punctuation used by the print edition without importing
    # the ReportLab authoring dependency into the publishing test environment.
    substitutions = {'\u2011': '-', '\u2013': '-', '\u2014': ' - ', '\u2018': "'", '\u2019': "'", '\u201c': '"', '\u201d': '"', '\u2022': '-', '\u00a0': ' '}
    return ' '.join(value.translate(str.maketrans(substitutions)).split())


class WorkAIPromptTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tracks = load_tracks()
        cls.dialogues = load_dialogues()

    def test_all_published_cases_and_complete_dialogues_are_available(self):
        count = 0
        for t in self.tracks:
            data = payload(t, self.dialogues[t['slug']])
            contexts = {c['id']: c for c in data['contexts']}
            self.assertEqual(len(contexts), 8 + len(self.dialogues[t['slug']]))
            count += len(contexts)
            for m in t['modules']:
                text = contexts[m['id']]['text']
                for expected in [m['brief'], m['model'], m['writing_task'], m['workshop']['explanation']]:
                    self.assertIn(expected, text)
                for term in m['vocabulary']:
                    self.assertIn(term['definition'], text)
            for i, d in enumerate(self.dialogues[t['slug']], 1):
                text = contexts[f'dialogue-{i}']['text']
                for role, speech in d['dialogue']:
                    self.assertIn(role + ': ' + speech, text)
            for mode in MODES:
                for level in ('B1', 'B2', 'C1'):
                    prompt = compose(data, mode['id'], level=level)
                    self.assertIn(t['scope_note'], prompt)
                    self.assertIn(t['title'], prompt)
                    self.assertLess(len(prompt), 30000)
        self.assertEqual(count, 696)

    def test_web_has_static_prompt_and_exact_curriculum_data(self):
        for t in self.tracks:
            with self.subTest(course=t['slug']):
                soup = BeautifulSoup((ROOT / f'efsp-{t["slug"]}.html').read_text(), 'html.parser')
                section = soup.select_one('#ai-practice')
                published = json.loads(section.select_one('[data-ai-data]').string)
                expected = payload(t, self.dialogues[t['slug']])
                self.assertEqual(published, expected)
                self.assertEqual(section.select_one('[data-ai-prompt]').text, compose(expected))
                self.assertEqual(len(section.select('[data-ai-mode] option')), 8)
                self.assertEqual(len(section.select('[data-ai-context] option')), len(expected['contexts']))
                self.assertTrue(soup.select_one('script[src^="work-ai.js"]'))
                for m in t['modules']:
                    links = soup.select(f'#{m["id"]} [data-ai-preset]')
                    self.assertEqual(len(links), 4)
                    for link in links:
                        params = parse_qs(urlparse(link['href']).query)
                        self.assertEqual(params['context'], [m['id']])
                        self.assertEqual(urlparse(link['href']).fragment, 'ai-practice')

    def test_roleplay_and_script_prompts_have_distinct_pedagogical_contracts(self):
        modes = {m['id']: m['instructions'] for m in MODES}
        self.assertIn('Do not write my replies', modes['roleplay'])
        self.assertIn('six to ten learner turns', modes['roleplay'])
        self.assertIn('12-18 substantial speaking turns', modes['dialogues'])
        self.assertIn('six distinct, common scenarios', modes['dialogues'])
        self.assertIn('two or three professionals', modes['dialogues'])
        self.assertIn('Stop and wait', modes['writing'])
        self.assertIn('Do not write the message for me first', modes['writing'])
        self.assertIn('context-dependent choices', modes['grammar'])
        for instructions in modes.values():
            self.assertIn('wait', instructions.lower())
            self.assertGreater(len(instructions.split()), 170)

    def test_all_print_guides_contain_two_complete_prompt_endings_and_working_context_links(self):
        manifest = json.loads((ROOT / 'content/work/documents.json').read_text())['documents']
        ai_hash = prompt_hash()
        for t in self.tracks:
            for kind, (_, href) in enumerate(t['pdfs']):
                with self.subTest(pdf=href):
                    meta = manifest[href]
                    self.assertEqual(meta['ai_prompt_hash'], ai_hash)
                    self.assertEqual(meta['ai_prompt_count'], 2)
                    reader = PdfReader(ROOT / href)
                    texts = [page.extract_text() or '' for page in reader.pages]
                    text = normalized('\n'.join(texts))
                    self.assertIn('Extend your practice with AI', text)
                    # Starts and ends ensure a long copyable prompt was not silently truncated.
                    self.assertEqual(text.count('START PROMPT / COPY THROUGH END PROMPT'), 2)
                    lines = [line.strip() for page_text in texts for line in page_text.splitlines()]
                    self.assertEqual(lines.count('END REFERENCE'), 2)
                    self.assertEqual(lines.count('END PROMPT'), 2)
                    for mode in PRINT_MODES[kind]:
                        instructions = next(m['instructions'] for m in MODES if m['id'] == mode)
                        self.assertIn(normalized(instructions.splitlines()[-1][-95:]), text)
                    urls = {str(a.get_object().get('/A', {}).get('/URI', '')) for page in reader.pages for a in page.get('/Annots', [])}
                    context = 'dialogue-1' if kind == 2 else 'module-1'
                    for mode in PRINT_MODES[kind]:
                        self.assertIn(url(t, mode, context, True), urls)
                    if kind == 2:
                        for i in range(1, len(self.dialogues[t['slug']]) + 1):
                            self.assertIn(url(t, 'roleplay', f'dialogue-{i}', True), urls)
                    for m in t['modules']:
                        mode = ['teacher', 'roleplay', 'roleplay', 'vocabulary'][kind]
                        self.assertIn(url(t, mode, m['id'], True), urls)


if __name__ == '__main__':
    unittest.main()
