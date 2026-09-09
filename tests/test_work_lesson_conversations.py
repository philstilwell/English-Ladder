"""Guard the requested web/print activity shape and the authored lesson mapping."""
import hashlib
import json
import unittest

from bs4 import BeautifulSoup
from pypdf import PdfReader
from work_curriculum import ROOT, load_tracks
from work_lesson_conversations import content_hash, load_course, render_activities


class LessonConversationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tracks = load_tracks()

    def test_every_lesson_has_unique_ten_turn_scripts_and_bounded_scenario(self):
        all_scripts = set()
        scenarios = set()
        for track in self.tracks:
            data = load_course(track['slug'])
            for module in track['modules']:
                lesson = data[module['id']]
                self.assertEqual(len({c['title'] for c in lesson['conversations']}), 3)
                for conversation in lesson['conversations']:
                    turns = conversation['turns']
                    self.assertEqual(len(turns), 10)
                    self.assertGreaterEqual(len(' '.join(s for _, s in turns).split()), 80)
                    self.assertTrue(all(a[0] != b[0] for a, b in zip(turns, turns[1:])), conversation['title'])
                    script = json.dumps(turns)
                    self.assertNotIn(script, all_scripts)
                    all_scripts.add(script)
                brief = lesson['additional_scenario']['brief']
                self.assertNotEqual(brief, module['brief'])
                self.assertNotIn(brief, scenarios)
                scenarios.add(brief)
        self.assertEqual(len(all_scripts), 984)
        self.assertEqual(len(scenarios), 328)

    def test_accordions_are_closed_and_complete_without_javascript(self):
        for track in self.tracks:
            page = BeautifulSoup((ROOT / f'efsp-{track["slug"]}.html').read_text(), 'html.parser')
            for module in track['modules']:
                rendered = BeautifulSoup(render_activities(track, module), 'html.parser')
                published = page.find(id=module['id']).select_one('.work-practice')
                self.assertEqual(str(published), str(rendered.select_one('.work-practice')))
                conversations = published.select('details.work-conversation')
                self.assertEqual(len(conversations), 3)
                for conversation in conversations:
                    self.assertFalse(conversation.has_attr('open'))
                    self.assertEqual(len(conversation.select('ol > li')), 10)
                    self.assertTrue(conversation.select_one('summary').get_text().strip())
                self.assertEqual(len(published.select('.work-speaking-scenario')), 2)
                self.assertFalse(published.select('textarea'))

    def test_pdf_activity_content_and_artwork_are_current(self):
        from generate_work_documents import clean
        manifest = json.loads((ROOT / 'content/work/documents.json').read_text())['documents']
        illustration_hash = hashlib.sha256((ROOT / 'assets/work/professional-icons.png').read_bytes()).hexdigest()
        for track in self.tracks:
            for index, (_, href) in enumerate(track['pdfs']):
                meta = manifest[href]
                self.assertEqual(meta['illustration_sha256'], illustration_hash)
                self.assertLess(meta['bytes'], 1_000_000, 'Embed the course icon, not the entire atlas: ' + href)
                reader = PdfReader(ROOT / href)
                images = list(reader.pages[0].images)
                self.assertGreaterEqual(len(images), 2, href)
                if index == 3:
                    continue
                self.assertEqual(meta['lesson_conversation_hash'], content_hash())
                text = ' '.join(' '.join(page.extract_text().split()) for page in reader.pages)
                for lesson in load_course(track['slug']).values():
                    self.assertIn(' '.join(clean(lesson['additional_scenario']['title']).split()), text)
                    for conversation in lesson['conversations']:
                        self.assertIn(' '.join(clean(conversation['title']).split()), text)
                        if index in (1, 2):
                            for role, speech in conversation['turns']:
                                self.assertIn(' '.join(clean(speech).split()), text)


if __name__ == '__main__':
    unittest.main()
