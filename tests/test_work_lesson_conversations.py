"""Guard the requested web/print activity shape and the authored lesson mapping."""
import hashlib
import json
import unittest

from bs4 import BeautifulSoup
from pypdf import PdfReader
from work_curriculum import ROOT, load_tracks
from work_lesson_conversations import content_hash, load_course, render_activities
from work_icons import icon_asset


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
        self.assertEqual(len(all_scripts), 1728)
        self.assertEqual(len(scenarios), 576)

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

    def test_learner_book_artwork_and_source_are_current(self):
        from work_books import book_source
        manifest = json.loads((ROOT / 'content/work/documents.json').read_text())['documents']
        for track in self.tracks:
            href = track['pdfs'][0][1]
            meta = manifest[href]
            illustration_hash = hashlib.sha256((ROOT / icon_asset(track['slug'])[0]).read_bytes()).hexdigest()
            self.assertEqual(meta['illustration_sha256'], illustration_hash)
            standalone = icon_asset(track['slug'])[1:3] == (1, 1)
            # Standalone native illustrations retain 300-dpi print detail.
            self.assertLess(meta['bytes'], 1_300_000 if standalone else 1_000_000,
                            'Embed the course illustration, not the entire atlas: ' + href)
            reader = PdfReader(ROOT / href)
            self.assertGreaterEqual(len(list(reader.pages[0].images)), 2, href)
            if standalone:
                self.assertTrue(all(max(image.image.size) <= 672 for image in reader.pages[0].images))
            self.assertEqual(len(reader.pages), 114)
            self.assertEqual((ROOT / href).read_bytes(), book_source(track['slug']).read_bytes())
            self.assertEqual(meta['kind'], 'Learner book')
            self.assertNotIn('lesson_conversation_hash', meta)


if __name__ == '__main__':
    unittest.main()
