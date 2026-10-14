"""Approval-edition checks, separate from the unchanged published-book contract."""
from collections import Counter
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import unittest
from xml.etree import ElementTree as ET
import zipfile

import pdfplumber
from pypdf import PdfReader

from books.leadership_pilot import UNITS, SUPPLEMENTS, CHECKPOINTS, AUTHOR, COPYRIGHT, validate
from books.cross_cultural_leadership_content import UNITS as ORIGINAL_UNITS
from build_leadership_pilot import OUT, STEM, ROOT


def normalized(text):
    return ' '.join(re.sub(r'(?<=\w)-\s+(?=\w)', '-', text).split())


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'a' and attrs.get('href', '').startswith('#'):
            self.links.append(attrs['href'][1:])


class LeadershipPilotContentTests(unittest.TestCase):
    def test_structure_and_isolation(self):
        self.assertTrue(validate())
        self.assertEqual([u['title'] for u in UNITS], [u['title'] for u in ORIGINAL_UNITS])
        for u, original in zip(UNITS, ORIGINAL_UNITS):
            self.assertNotEqual(u['dialogue'], original['dialogue'])
            self.assertIsNot(u['vocabulary'], original['vocabulary'])
        self.assertEqual(sum(len(u['vocabulary']) for u in UNITS), 192)
        self.assertEqual(len({p[1] for u in UNITS for p in u['phrases']}), 128)
        self.assertEqual(len(UNITS) + len(SUPPLEMENTS), 11)
        self.assertEqual(sum(len(s['dialogue']) for s in UNITS + SUPPLEMENTS), 220)
        self.assertGreaterEqual(sum(len({name for name, _ in u['dialogue']}) >= 3 for u in UNITS), 2)

    def test_all_question_choices_explained_and_no_length_shortcut(self):
        questions = [q for u in UNITS for group in ('checks', 'choices', 'repair') for q in u[group]]
        questions += [u['second_take'] for u in UNITS]
        questions += [q for c in CHECKPOINTS for q in c['questions']]
        self.assertEqual(len(questions), 96)
        positions = Counter(q['answer'] for q in questions)
        self.assertLessEqual(max(positions.values()) - min(positions.values()), 4)
        longest = shortest = 0
        for q in questions:
            self.assertEqual(len(q['options']), 4)
            self.assertEqual(len(q['reasons']), 4)
            # A short distinction can be complete: "Unconfirmed does not mean lost."
            self.assertTrue(all(len(reason.split()) >= 4 for reason in q['reasons']))
            lengths = [len(option.split()) for option in q['options']]
            correct = lengths[q['answer']]
            longest += correct == max(lengths) and lengths.count(correct) == 1
            shortest += correct == min(lengths) and lengths.count(correct) == 1
        self.assertLess(longest / len(questions), .35)
        self.assertLess(shortest / len(questions), .35)

    def test_every_gap_has_an_explanation_and_correct_turn(self):
        scenes = UNITS + [u['transfer'] for u in UNITS] + SUPPLEMENTS + [s['pilot_transfer'] for s in SUPPLEMENTS]
        self.assertEqual(sum(len(s['gaps']) for s in scenes), 142)
        for scene in scenes:
            gaps = scene['gaps']
            tokens = []
            self.assertEqual(len({g['answer'].casefold() for g in gaps}), len(gaps))
            for turn, (speaker, text) in enumerate(scene['dialogue'], 1):
                self.assertTrue(speaker)
                self.assertNotRegex(text.lower(), r'language exercise|in the exercise|fictional procedure')
                for token in re.findall(r'\{\{(\d+)\}\}', text):
                    tokens.append(int(token))
                    self.assertEqual(gaps[int(token) - 1]['turn'], turn)
                    self.assertGreaterEqual(len(gaps[int(token) - 1]['reason'].split()), 7)
            self.assertEqual(tokens, list(range(1, len(gaps) + 1)))

    def test_supplement_capacity_and_date_correction(self):
        scene = SUPPLEMENTS[0]
        self.assertIn('across the team', scene['setup'])
        self.assertIn('scheduling update Tuesday', scene['dialogue'][13][1])
        self.assertNotIn('Wednesday is the date', ' '.join(t for _, t in scene['dialogue']))


class LeadershipPilotDeliverableTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.reader = PdfReader(OUT / (STEM + '.pdf'))
        cls.layout = json.loads((OUT / (STEM + '-layout.json')).read_text())
        cls.text = [normalized(p.extract_text()) for p in cls.reader.pages]
        cls.all_text = ' '.join(cls.text)

    def assert_printed(self, value):
        self.assertTrue(normalized(value) in self.all_text, 'Missing printed text: ' + value)

    def test_page_geometry_tags_metadata_and_fonts(self):
        root = self.reader.trailer['/Root']
        self.assertEqual(len(self.reader.pages), self.layout['pages'])
        self.assertEqual(root.get('/Lang'), 'en-US')
        self.assertTrue(root['/MarkInfo']['/Marked'])
        self.assertTrue(root['/StructTreeRoot'])
        self.assertEqual(self.reader.metadata.author, AUTHOR)
        self.assertTrue(self.reader.outline)
        fonts = set()
        for p in self.reader.pages:
            self.assertAlmostEqual(float(p.mediabox.width), 612)
            self.assertAlmostEqual(float(p.mediabox.height), 792)
            for ref in p['/Resources']['/Font'].values():
                font = ref.get_object()
                fonts.add(str(font['/BaseFont']))
                for descendant in font.get('/DescendantFonts', [font]):
                    descriptor = descendant.get_object().get('/FontDescriptor')
                    self.assertIsNotNone(descriptor)
                    self.assertTrue(any(k in descriptor.get_object() for k in ('/FontFile', '/FontFile2', '/FontFile3')))
        self.assertEqual(len(fonts), 3)

    def test_all_content_and_explanations_printed(self):
        self.assertIn(COPYRIGHT, self.text[0])
        self.assertIn('English Ladder', self.text[0])
        self.assertNotRegex(self.all_text, r'\{\{\d+\}\}|\ufffd')
        self.assertNotRegex(self.all_text.lower(), r'approval draft|review copy|think about it')
        for u in UNITS:
            for entry in u['vocabulary']:
                for part in entry:
                    self.assert_printed(part)
            for _, phrase in u['phrases']:
                self.assert_printed(phrase)
            for group in ('checks', 'choices', 'repair'):
                for q in u[group]:
                    for value in [q['prompt']] + q['options'] + q['reasons']:
                        self.assert_printed(value)
            for value in u['second_take']['options'] + u['second_take']['reasons']:
                self.assert_printed(value)
        for c in CHECKPOINTS:
            for q in c['questions']:
                for value in q['options'] + q['reasons']:
                    self.assert_printed(value)
        for s in UNITS + SUPPLEMENTS + [u['transfer'] for u in UNITS] + [s['pilot_transfer'] for s in SUPPLEMENTS]:
            for g in s['gaps']:
                self.assert_printed(g['reason'])

    def test_layout_links_index_and_blank_width(self):
        self.assertEqual(self.layout['overflows'], [])
        self.assertEqual(self.layout['invalidLinks'], [])
        self.assertEqual(self.layout['duplicateIds'], [])
        self.assertEqual(self.layout['blankCount'], 142)
        self.assertAlmostEqual(self.layout['minBlankWidth'], self.layout['maxBlankWidth'], places=3)
        html = (OUT / (STEM + '.html')).read_text()
        links = Links()
        links.feed(html)
        self.assertEqual(len(links.ids), len(set(links.ids)))
        self.assertFalse(set(links.links) - set(links.ids))
        self.assertEqual(html.count('class="index-entry flow-block"'), 191)
        for page, text in enumerate(self.text, 1):
            self.assertIn('ENGLISHLADDER.COM', text)
            self.assertIn(f'Phil Stilwell | {page:02d}', text)
            self.assertGreater(len(text.split()), 35)
        with pdfplumber.open(OUT / (STEM + '.pdf')) as pdf:
            cover_art = max(pdf.pages[0].images, key=lambda i: i['width'])
            effective_dpi = cover_art['srcsize'][0] / (cover_art['width'] / 72)
            self.assertGreaterEqual(effective_dpi, 300)

    def test_pdf_answer_links_and_printed_references_agree(self):
        destinations = self.reader.named_destinations
        for page in self.reader.pages:
            text = normalized(page.extract_text())
            if 'Answers and explanations, page' not in text and 'Why these answers fit, page' not in text:
                continue
            numbers = [int(n) for n in re.findall(r'(?:Answers and explanations|Why these answers fit), page (\d+)', text)]
            actual = set()
            for annotation in page.get('/Annots', []):
                dest = annotation.get_object().get('/Dest')
                if dest and str(dest).startswith('/key-'):
                    actual.add(self.reader.get_destination_page_number(destinations[str(dest)]) + 1)
            self.assertEqual(set(numbers), actual)

    def test_all_printed_text_inside_safe_margins(self):
        with pdfplumber.open(OUT / (STEM + '.pdf')) as pdf:
            for page in pdf.pages:
                for char in page.chars:
                    self.assertGreaterEqual(char['x0'], 36, page.page_number)
                    self.assertLessEqual(char['x1'], 576, page.page_number)
                    self.assertGreaterEqual(char['top'], 18, page.page_number)
                    self.assertLessEqual(char['bottom'], 774, page.page_number)
                    self.assertGreaterEqual(char['size'], 7, page.page_number)
                page.close()

    def test_epub_structure_internal_links_and_reflow(self):
        ns = {'x': 'http://www.w3.org/1999/xhtml', 'opf': 'http://www.idpf.org/2007/opf'}
        with zipfile.ZipFile(OUT / (STEM + '.epub')) as z:
            self.assertEqual(z.namelist()[0], 'mimetype')
            self.assertEqual(z.getinfo('mimetype').compress_type, zipfile.ZIP_STORED)
            self.assertEqual(z.read('mimetype'), b'application/epub+zip')
            book = ET.fromstring(z.read('EPUB/book.xhtml'))
            ET.fromstring(z.read('EPUB/nav.xhtml'))
            package = ET.fromstring(z.read('EPUB/package.opf'))
            ids = [n.get('id') for n in book.iter() if n.get('id')]
            self.assertEqual(len(ids), len(set(ids)))
            for a in book.findall('.//x:a', ns):
                href = a.get('href', '')
                if href.startswith('#'):
                    self.assertIn(href[1:], ids)
            for img in book.findall('.//x:img', ns):
                self.assertIn('EPUB/' + img.get('src'), z.namelist())
                self.assertTrue(img.get('alt'))
            self.assertIn('reflowable', ''.join(package.itertext()))
            self.assertNotIn('print-reference', z.read('EPUB/book.xhtml').decode())


if __name__ == '__main__':
    unittest.main()
