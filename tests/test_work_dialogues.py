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
        self.assertEqual(validate_dialogues(load_dialogues())['courses'], 41)
        self.assertGreaterEqual(validate_dialogues(load_dialogues())['dialogues'], 368)

    def test_all_spoken_turns_and_current_metadata_reach_the_pdf(self):
        groups=load_dialogues()
        manifest=json.loads((ROOT/'content/work/documents.json').read_text())['documents']
        for track in load_tracks():
            slug=track['slug']; href=track['pdfs'][2][1]
            with self.subTest(course=slug):
                meta=manifest[href]
                self.assertEqual(meta['dialogue_hash'],dialogue_hash())
                self.assertEqual(meta['dialogue_count'],len(groups[slug]))
                self.assertEqual(meta['sha256'],hashlib.sha256((ROOT/href).read_bytes()).hexdigest())
                reader=PdfReader(ROOT/href)
                text=normalized(' '.join(page.extract_text() or '' for page in reader.pages))
                for d in groups[slug]:
                    self.assertIn(normalized(d['title']),text)
                    for role,speech in d['dialogue']:
                        self.assertIn(normalized(role+': '+speech),text)
                self.assertNotIn('ESL learner:',text)
                self.assertIn('Eight more situations to make your own',text)
                self.assertEqual(len(reader.pages),meta['pages'])

    def test_technical_regressions(self):
        groups=load_dialogues()
        it=' '.join(v for d in groups['general-it'] for _,v in d['dialogue'])
        self.assertIn('does not itself explain container restarts',it)
        advice=' '.join(v for d in groups['financial-advice'] for _,v in d['dialogue'])
        self.assertIn('does not guarantee recovery',advice)
        self.assertNotIn('temporary loss permanent',advice)


if __name__=='__main__':unittest.main()
