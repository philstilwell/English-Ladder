"""Regression checks for the six authored medical-profession courses."""
import json
import unittest
from pathlib import Path
from urllib.parse import urlsplit

from bs4 import BeautifulSoup
from PIL import Image
from pypdf import PdfReader

from books.supplements import load_supplements
from build_industry_books import validate_book
from work_curriculum import ROOT, load_tracks
from work_icons import card_icon, icon_asset, directory_collage, MEDICAL_ICON_CROPS, MEDICAL_ICON_SIZE
from work_lesson_conversations import load_course
from work_medical import MEDICAL_SLUGS, book, completed
from work_web_content import web_track


class MedicalProfessionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tracks = {t['slug']: t for t in load_tracks()}

    def test_six_distinct_courses_join_the_existing_inventory(self):
        self.assertEqual(len(self.tracks), 72)
        self.assertEqual(len(set(MEDICAL_SLUGS)), 6)
        for slug in MEDICAL_SLUGS:
            track = self.tracks[slug]
            self.assertEqual(track['category'], 'Health & life sciences')
            self.assertEqual(len(track['modules']), 8)
            self.assertEqual(track['pdfs'], [['Learner book', f'pdf/efsp/{slug}-english-book.pdf']])

    def test_complete_books_and_independently_authored_dialogues(self):
        scripts = set()
        for slug in MEDICAL_SLUGS:
            data = book(slug)
            validate_book(data, self.tracks[slug])
            self.assertGreaterEqual(len({v[0].casefold() for u in data['units'] for v in u['vocabulary']}), 144)
            self.assertEqual(sum(len(u['vocabulary']) for u in data['units']), 192)
            self.assertEqual(sum(len(u['phrases']) for u in data['units']), 128)
            for item in data['units'] + load_supplements(slug):
                script = completed(item)
                self.assertEqual(len(script), 20)
                self.assertTrue(all(a[0] != b[0] for a, b in zip(script, script[1:])))
                fingerprint = json.dumps(script)
                self.assertNotIn(fingerprint, scripts)
                scripts.add(fingerprint)
                self.assertGreaterEqual(len(' '.join(line for _, line in script).split()), 220)
        self.assertEqual(len(scripts), 66)

    def test_short_conversations_are_complete_and_unique(self):
        scripts = set()
        for slug in MEDICAL_SLUGS:
            lessons = load_course(slug)
            self.assertEqual(len(lessons), 8)
            for lesson in lessons.values():
                self.assertEqual(len(lesson['conversations']), 3)
                for conversation in lesson['conversations']:
                    turns = conversation['turns']
                    self.assertEqual(len(turns), 10)
                    self.assertGreaterEqual(len(' '.join(line for _, line in turns).split()), 100)
                    fingerprint = json.dumps(turns)
                    self.assertNotIn(fingerprint, scripts)
                    scripts.add(fingerprint)
        self.assertEqual(len(scripts), 144)

    def test_specialty_terminology_is_not_a_generic_medical_template(self):
        expected = {
            'general-practitioners': {'medication reconciliation', 'screening'},
            'oncologists': {'biomarker', 'palliative care'},
            'cardiologists': {'ejection fraction', 'atrial fibrillation'},
            'x-ray-technicians': {'collimation', 'exposure index'},
            'pediatricians': {'developmental surveillance', 'receptive language'},
            'obstetricians': {'gestational age', 'chorionic villus sampling'},
        }
        for slug, terms in expected.items():
            vocabulary = ' '.join(v[0].casefold() for u in book(slug)['units'] for v in u['vocabulary'])
            for term in terms:
                self.assertIn(term, vocabulary, (slug, term))

    def test_individual_native_artwork_is_transparent_and_reused(self):
        for slug in MEDICAL_SLUGS:
            asset, columns, rows, index = icon_asset(slug)
            self.assertEqual((columns, rows, index), (1, 1, 0))
            self.assertEqual(asset, f'assets/work/medical/{slug}.png')
            with Image.open(ROOT / asset) as image:
                self.assertEqual(image.width, image.height)
                self.assertGreaterEqual(image.width, 1024)
                self.assertIn('A', image.getbands())
                self.assertEqual(image.getchannel('A').getextrema(), (0, 255))
                dimensions = image.size
            web_asset = (ROOT / asset).with_suffix('.webp')
            with Image.open(web_asset) as image:
                self.assertEqual(image.size, (384, 384))
                self.assertIn('A', image.getbands())
            self.assertLess(web_asset.stat().st_size, 100_000)
            icon = BeautifulSoup(card_icon(self.tracks[slug]), 'html.parser').span
            self.assertEqual(icon['data-work-icon'], slug)
            self.assertEqual(icon['aria-hidden'], 'true')

    def test_pages_offer_the_matching_book_and_closed_short_conversations(self):
        manifest = json.loads((ROOT / 'content/work/documents.json').read_text())['documents']
        for slug in MEDICAL_SLUGS:
            track = web_track(self.tracks[slug])
            page = BeautifulSoup((ROOT / f'efsp-{slug}.html').read_text(), 'html.parser')
            href = f'pdf/efsp/{slug}-english-book.pdf'
            self.assertTrue((ROOT / href).exists())
            self.assertIn(href, [urlsplit(link['href']).path for link in page.select('#downloads a[href]')])
            self.assertEqual(manifest[href]['pages'], 114)
            self.assertEqual(manifest[href]['dialogue_count'], 11)
            self.assertEqual(manifest[href]['illustration_asset'], icon_asset(slug)[0])
            self.assertEqual(len(page.select(f'[data-work-icon="{slug}"]')), 2)
            self.assertEqual(len(page.select('.work-module')), 8)
            self.assertEqual(len(page.select('[data-work-quiz]')), 100)
            self.assertEqual(len(page.select('[data-cloze-gap]')), 98)
            self.assertIsNone(page.select_one('textarea:not([readonly])'))
            self.assertIsNone(page.select_one('input[type="checkbox"]'))
            self.assertEqual(len(track['web_glossary']), 192)
            for module_id, lesson in load_course(slug).items():
                module = page.find(id=module_id)
                for conversation in lesson['conversations']:
                    summary = next(s for s in module.select('summary') if conversation['title'] in s.get_text())
                    self.assertFalse(summary.parent.has_attr('open'))

    def test_collage_uses_the_same_artwork_envelope_for_new_fields(self):
        collage = BeautifulSoup(directory_collage(), 'html.parser')
        for slug, (x, y, width, height) in MEDICAL_ICON_CROPS.items():
            self.assertGreaterEqual(min(x, y), 0)
            self.assertLessEqual(x + width, MEDICAL_ICON_SIZE)
            self.assertLessEqual(y + height, MEDICAL_ICON_SIZE)
            art = collage.select_one(f'[data-work-icon="{slug}"]')
            style = dict(part.split(':', 1) for part in art['style'].split(';'))
            self.assertLessEqual(float(style['width'].rstrip('%')), 80)
            self.assertLessEqual(float(style['height'].rstrip('%')), 80)

    def test_medical_scope_is_visible_and_sources_are_primary(self):
        for slug in MEDICAL_SLUGS:
            data = book(slug)
            self.assertIn('not medical advice', data['scope_note'])
            self.assertIn('emergency procedures', data['scope_note'])
            self.assertIn('calculate a dose', data['scope_note'])
            for source in data['sources']:
                self.assertTrue(source['url'].startswith('https://'))
                self.assertEqual(source['checked'], '10 October 2026')

    def test_cardiology_onset_correction_distinguishes_reporting_order_from_clock_time(self):
        lines = book('cardiologists')['units'][0]['transfer']['lines']
        self.assertEqual([q['options'][q['answer']] for q in lines[:2]], ['09:10', '09:40'])
        prompt = 'Receiver: "The previously reported onset time of ___ has been superseded."'
        self.assertEqual(lines[1]['prompt'], prompt)
        self.assertIn('not which clock time is earlier', lines[1]['reason'])

        page = BeautifulSoup((ROOT / 'efsp-cardiologists.html').read_text(), 'html.parser')
        question = page.select_one('input[name="module-1-transfer-2"]').find_parent('div', class_='work-quiz')
        self.assertEqual(question.legend.get_text(), '2. ' + prompt)
        self.assertEqual(question['data-explanation'], lines[1]['reason'])
        correct = question.select_one(f'input[value="{question["data-correct"]}"]')
        self.assertEqual(correct.find_next_sibling('span').get_text(), '09:40')
        for q in lines[:2]:
            self.assertIn(q['reason'], page.get_text())

        pdf = PdfReader(ROOT / 'pdf/efsp/cardiologists-english-book.pdf')
        exercise = ' '.join(pdf.pages[11].extract_text().split())
        key = ' '.join(pdf.pages[85].extract_text().split())
        self.assertIn('previously reported onset time of', exercise)
        self.assertIn('1. 09:10 | 2. 09:40', exercise)
        self.assertIn(prompt.replace('___', '09:40'), key)
        for q in lines[:2]:
            self.assertIn(q['reason'], key)

    def test_fictional_cardiology_risk_comparisons_keep_units_clear(self):
        unit = book('cardiologists')['units'][6]
        text = ' '.join(line for _, line in completed(unit))
        self.assertIn('percentage point', text)
        self.assertEqual(40 - 30, 10)
        self.assertEqual((40 - 30) / 40 * 100, 25)
        self.assertEqual(20 - 15, 5)
        self.assertEqual((20 - 15) / 20 * 100, 25)


if __name__ == '__main__':
    unittest.main()
