"""Reject missing scripts, stale printed dialogue editions, and lost spoken text."""
import hashlib
import json
import re
import unittest
from pathlib import Path
from pypdf import PdfReader
from work_dialogues import ROOT, dialogue_hash, load_dialogues, validate_dialogues
from work_curriculum import load_tracks


def normalized(text):
    return re.sub(r'\s+', ' ', text.replace('\u2019', "'").replace('\u2018', "'")).strip()


class DialoguePublicationTests(unittest.TestCase):
    def test_full_inventory_and_substantial_conversations(self):
        self.assertEqual(validate_dialogues(load_dialogues())['courses'], 66)
        self.assertGreaterEqual(validate_dialogues(load_dialogues())['dialogues'], 568)

    def test_published_books_use_the_new_extended_dialogue_edition(self):
        from build_leadership_book import content_hash
        from books.supplements import load_supplements
        from work_books import book_source, book_units
        manifest = json.loads((ROOT / 'content/work/documents.json').read_text())['documents']
        for track in load_tracks():
            href = track['pdfs'][0][1]
            with self.subTest(course=track['slug']):
                meta = manifest[href]
                units = book_units(track['slug'])
                self.assertEqual(meta['book_content_hash'], content_hash(units, load_supplements(track['slug'])))
                self.assertEqual(meta['dialogue_count'], 11)
                self.assertEqual(meta['dialogue_turns'], 220)
                self.assertEqual(meta['transfer_dialogue_count'], 11)
                self.assertEqual((ROOT / href).read_bytes(), book_source(track['slug']).read_bytes())
                self.assertEqual(meta['sha256'], hashlib.sha256((ROOT / href).read_bytes()).hexdigest())

    def test_course_pages_preserve_shared_site_features(self):
        from bs4 import BeautifulSoup
        for t in load_tracks():
            with self.subTest(course=t['slug']):
                soup=BeautifulSoup((ROOT/f'efsp-{t["slug"]}.html').read_text(),'html.parser')
                self.assertIsNotNone(soup.select_one('script[src*="site.js"]'))
                self.assertIsNotNone(soup.select_one('link[rel="canonical"]'))
                self.assertIsNone(soup.select_one('.site-footer a[href="continue.html"]'))
                self.assertIsNotNone(soup.select_one('.site-footer a[href="archive.html"]'))
                self.assertEqual(len(soup.select('.work-download')), 1)
                self.assertIn('20-turn cloze conversations', soup.select_one('#downloads').get_text())

    def test_technical_regressions(self):
        groups=load_dialogues()
        it=' '.join(v for d in groups['general-it'] for _,v in d['dialogue'])
        self.assertIn('does not itself explain container restarts',it)
        advice=' '.join(v for d in groups['financial-advice'] for _,v in d['dialogue'])
        self.assertIn('does not guarantee recovery',advice)
        self.assertNotIn('temporary loss permanent',advice)


if __name__=='__main__':unittest.main()
