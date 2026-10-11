"""Publication contracts for context-carrying prompts, links and printable copies."""
import json
import unittest
from urllib.parse import parse_qs, urlparse

from bs4 import BeautifulSoup
from pypdf import PdfReader
from work_curriculum import ROOT, load_tracks
from work_dialogues import load_dialogues
from work_ai_prompts import MODES, PRINT_MODES, compose, payload, prompt_hash, url
from work_web_content import web_track

RETAINED_MODES = ['vocabulary', 'grammar', 'roleplay', 'dialogues']
REMOVED_MODES = {'writing', 'register', 'review', 'teacher'}


def normalized(value):
    # Match typographic punctuation used by the print edition without importing
    # the ReportLab authoring dependency into the publishing test environment.
    substitutions = {'\u2011': '-', '\u2013': '-', '\u2014': ' - ', '\u2018': "'", '\u2019': "'", '\u201c': '"', '\u201d': '"', '\u2022': '-', '\u00a0': ' '}
    return ' '.join(value.translate(str.maketrans(substitutions)).split())


class WorkAIPromptTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tracks = [web_track(track) for track in load_tracks()]
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
        self.assertEqual(count, 1192)

    def test_web_has_static_prompt_and_exact_curriculum_data(self):
        for t in self.tracks:
            with self.subTest(course=t['slug']):
                soup = BeautifulSoup((ROOT / f'efsp-{t["slug"]}.html').read_text(), 'html.parser')
                section = soup.select_one('#ai-practice')
                published = json.loads(section.select_one('[data-ai-data]').string)
                expected = payload(t, self.dialogues[t['slug']])
                self.assertEqual(published, expected)
                self.assertEqual(section.select_one('[data-ai-prompt]').text, compose(expected))
                self.assertEqual([option['value'] for option in section.select('[data-ai-mode] option')], RETAINED_MODES)
                self.assertEqual([mode['id'] for mode in published['modes']], RETAINED_MODES)
                for link in soup.select('a[href]'):
                    self.assertFalse(REMOVED_MODES.intersection(parse_qs(urlparse(link['href']).query).get('ai', [])), link['href'])
                self.assertEqual(len(section.select('[data-ai-context] option')), len(expected['contexts']))
                self.assertTrue(soup.select_one('script[src^="work-ai.js"]'))
                for m in t['modules']:
                    links = soup.select(f'#{m["id"]} [data-ai-preset]')
                    self.assertEqual(len(links), 3)
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
        self.assertIn('context-dependent choices', modes['grammar'])
        for instructions in modes.values():
            self.assertIn('wait', instructions.lower())
            self.assertGreater(len(instructions.split()), 170)

    def test_books_link_to_the_course_without_claiming_printed_ai_appendices(self):
        manifest = json.loads((ROOT / 'content/work/documents.json').read_text())['documents']
        for t in self.tracks:
            href = t['pdfs'][0][1]
            with self.subTest(pdf=href):
                self.assertNotIn('ai_prompt_count', manifest[href])
                reader = PdfReader(ROOT / href)
                links = {str(a.get_object().get('/A', {}).get('/URI', ''))
                         for a in reader.pages[-1].get('/Annots', [])}
                self.assertIn(f'https://englishladder.com/efsp-{t["slug"]}.html', links)
                page = BeautifulSoup((ROOT / f'efsp-{t["slug"]}.html').read_text(), 'html.parser')
                self.assertIsNotNone(page.select_one('#ai-practice'))
                self.assertIsNotNone(page.select_one('#finished-dialogue-prompts'))
                download_text = page.select_one('#downloads').get_text(' ', strip=True)
                self.assertIn('answer keys with explanations', download_text)
                self.assertNotIn('AI extension prompt', download_text)


if __name__ == '__main__':
    unittest.main()
