"""Publication checks for complete lessons and synchronized web/print editions."""
import hashlib
import json
import unittest
from pathlib import Path
from urllib.parse import unquote, urlparse

from bs4 import BeautifulSoup
from work_curriculum import ROOT, content_hash, load_tracks, validate_tracks, related_tracks


class WorkCurriculumTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tracks = load_tracks()

    def test_complete_inventory_and_authored_cases(self):
        result = validate_tracks(self.tracks)
        self.assertEqual((result['courses'], result['lessons'], result['pdfs']), (41, 328, 164))
        models = [m['model'] for t in self.tracks for m in t['modules']]
        self.assertEqual(len(models), len(set(models)))

    def test_topic_alignment_regressions(self):
        tracks = {t['slug']:t for t in self.tracks}
        self.assertIn('Token', tracks['ai-development']['modules'][1]['terms'])
        self.assertIn('Conflict of interest', tracks['law']['modules'][1]['terms'])
        self.assertIn('CPC', [j['term'] for j in tracks['marketing']['jargon']])
        self.assertIn('AE', tracks['pharmaceutical']['modules'][4]['terms'])
        self.assertIn('Outage', tracks['telecommunications']['modules'][0]['title'])

    def test_numeric_models_preserve_case_arithmetic(self):
        tracks = {t['slug']:t for t in self.tracks}
        self.assertIn('160 units below', tracks['manufacturing']['modules'][0]['model'])
        self.assertIn('130 orders', tracks['supply-chain-logistics']['modules'][3]['model'])
        self.assertIn('6% and 7%', tracks['marketing']['modules'][6]['model'])
        self.assertIn('$20,000', tracks['finance']['modules'][2]['model'])

    def test_culture_does_not_assign_national_personalities(self):
        t = self.tracks[0]
        text = json.dumps(t).lower()
        for phrase in ['equality theater', 'idea-combat', 'americans always', 'japanese managers are']:
            self.assertNotIn(phrase, text)
        self.assertIn('individual preferences', t['scope_note'])

    def test_sbar_includes_background(self):
        t = next(t for t in self.tracks if t['slug']=='nursing-allied-health')
        definition = next(j['definition'] for j in t['jargon'] if j['term']=='SBAR')
        self.assertIn('Situation, Background, Assessment', definition)

    def test_insurance_terms_use_insurance_meanings(self):
        track = next(t for t in self.tracks if t['slug'] == 'insurance')
        terms = {term['term']: term['definition'] for term in track['jargon']}
        self.assertIn('insurance contract', terms['policy'])
        self.assertIn('request for payment or benefits', terms['claim'])
        self.assertIn('coverage review', terms['claim'])

    def test_every_page_contains_full_lessons_without_javascript(self):
        for t in self.tracks:
            with self.subTest(course=t['slug']):
                soup = BeautifulSoup((ROOT/f'efsp-{t["slug"]}.html').read_text(), 'html.parser')
                self.assertEqual(len(soup.select('.work-module')),8)
                self.assertEqual(len(soup.select('.work-quiz')),16)
                self.assertEqual(len(soup.select('textarea[data-work-note]')),0)
                for m in t['modules']:
                    module = soup.find(id=m['id'])
                    self.assertIn(m['brief'], module.get_text())
                    self.assertIn(m['model'], module.get_text())
                    self.assertIn('05 · Conversations', module.get_text())
                    self.assertIn('06 · Say it', module.get_text())
                    self.assertIn(m['workshop']['role_b'], module.get_text())
                ids = [node['id'] for node in soup.select('[id]')]
                self.assertEqual(len(ids),len(set(ids)))
                self.assertIsNotNone(soup.select_one('a[aria-current="page"][href="efsp.html"]'))

    def test_all_work_links_and_fragments_resolve(self):
        paths=[ROOT/'efsp.html',*[ROOT/f'efsp-{t["slug"]}.html' for t in self.tracks]]
        for path in paths:
            soup=BeautifulSoup(path.read_text(),'html.parser')
            for node in soup.select('[href], [src]'):
                url=urlparse(node.get('href') or node.get('src'))
                if url.scheme or url.netloc: continue
                target=(ROOT/unquote(url.path).lstrip('/') if url.path.startswith('/') else path.parent/unquote(url.path)) if url.path else path
                if target==ROOT:target=ROOT/'index.html'
                self.assertTrue(target.is_file(),f'{path.name}: {url.geturl()}')
                if url.fragment and not url.path:
                    self.assertIsNotNone(soup.find(id=url.fragment),f'{path.name}: #{url.fragment}')

    def test_pdf_edition_and_bytes_match_manifest(self):
        manifest=json.loads((ROOT/'content/work/documents.json').read_text())
        self.assertEqual(manifest['content_hash'],content_hash())
        expected={href for t in self.tracks for _label,href in t['pdfs']}
        self.assertEqual(set(manifest['documents']),expected)
        for path,meta in manifest['documents'].items():
            with self.subTest(path=path):
                data=(ROOT/path).read_bytes()
                self.assertEqual(hashlib.sha256(data).hexdigest(),meta['sha256'])
                self.assertEqual(meta['content_hash'],content_hash())
                self.assertEqual(len(data),meta['bytes'])
                self.assertGreater(meta['pages'],3)

    def test_related_courses_share_a_relevant_field(self):
        for t in self.tracks:
            related=related_tracks(t,self.tracks)
            self.assertTrue(related)
            self.assertTrue(all(r['category']==t['category'] and r['slug']!=t['slug'] for r in related))

    def test_answer_positions_are_varied_and_explanations_complete(self):
        positions=set()
        for t in self.tracks:
            for m in t['modules']:
                for q in m['workshop']['questions']:
                    positions.add(q['correct_index'])
                    self.assertEqual(q['answer'],q['options'][q['correct_index']])
                    self.assertTrue(all(len(f.split())>=5 for f in q['feedback']))
        self.assertEqual(positions,{0,1,2})


if __name__=='__main__': unittest.main()
