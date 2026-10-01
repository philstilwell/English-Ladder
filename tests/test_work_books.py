"""Single-book downloads, publication safety, and retirement of old work PDFs."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from urllib.parse import urlparse

from bs4 import BeautifulSoup

from work_curriculum import ROOT, load_tracks
from work_books import book_href, book_source, publish_books, validate_publication


class WorkBookPublicationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tracks = load_tracks()
        cls.manifest = json.loads((ROOT / 'content/work/documents.json').read_text())

    def test_public_assets_are_exactly_the_66_approved_books(self):
        expected = {book_href(t['slug']) for t in self.tracks}
        actual = {str(p.relative_to(ROOT)) for p in (ROOT / 'pdf/efsp').glob('*.pdf')}
        self.assertEqual(actual, expected)
        self.assertEqual(len(actual), 66)
        self.assertEqual(set(self.manifest['documents']), expected)
        validate_publication(self.tracks)
        for track in self.tracks:
            with self.subTest(course=track['slug']):
                self.assertEqual((ROOT / book_href(track['slug'])).read_bytes(),
                                 book_source(track['slug']).read_bytes())

    def test_every_course_has_one_described_download_and_shortcut_links(self):
        for track in self.tracks:
            with self.subTest(course=track['slug']):
                page = BeautifulSoup((ROOT / f'efsp-{track["slug"]}.html').read_text(), 'html.parser')
                section = page.select_one('#downloads')
                links = section.select('a[href]')
                self.assertEqual(len(links), 1)
                self.assertEqual(links[0].get_text(' ', strip=True), 'Open learner book (PDF) ↗')
                self.assertEqual(urlparse(links[0]['href']).path, book_href(track['slug']))
                self.assertIn('v=', links[0]['href'])
                description = page.find(id=links[0]['aria-describedby']).get_text()
                for phrase in ('20-turn', '192 vocabulary', '128 reusable phrases',
                               'word banks', 'answer keys with explanations', 'page references'):
                    self.assertIn(phrase.lower(), description.lower())
                self.assertIn('102 pages', section.get_text())
                for selector in ('.work-study-card', '#lessons'):
                    self.assertTrue(any(urlparse(a['href']).path == book_href(track['slug'])
                                        for a in page.select(selector + ' a[href]')))
                for a in page.select('a[href]'):
                    if urlparse(a['href']).path.startswith('pdf/efsp/'):
                        self.assertEqual(urlparse(a['href']).path, book_href(track['slug']))

    def test_directory_and_search_metadata_describe_one_book(self):
        directory = BeautifulSoup((ROOT / 'efsp.html').read_text(), 'html.parser')
        self.assertIn('66 complete learner books', directory.get_text())
        self.assertEqual(len(directory.select('.work-card-footer')), 66)
        self.assertTrue(all('1 learner book' in x.get_text() for x in directory.select('.work-card-footer')))
        for track in self.tracks:
            page = BeautifulSoup((ROOT / f'efsp-{track["slug"]}.html').read_text(), 'html.parser')
            for text in ("teacher's guide", '4 printable guides', 'Four guides.'):
                self.assertNotIn(text, page.get_text())
            data = ' '.join(x.get_text() for x in page.select('script[type="application/ld+json"]'))
            self.assertIn(book_href(track['slug']), data)
            self.assertNotIn('pdf/efsp/efsp-', data)
        sitemap = (ROOT / 'sitemaps/pdfs.xml').read_text()
        self.assertNotIn('/pdf/efsp/efsp-', sitemap)
        for track in self.tracks:
            self.assertIn(book_href(track['slug']), sitemap)

    def test_preflight_failure_does_not_replace_any_asset(self):
        tracks = [{'slug': 'one'}, {'slug': 'two'}]
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            target = root / book_href('one')
            target.parent.mkdir(parents=True)
            target.write_bytes(b'previous approved book')
            with patch('work_books.ROOT', root), patch('work_curriculum.load_tracks', return_value=tracks), \
                 patch('work_curriculum.validate_tracks'), patch('work_curriculum.content_hash', return_value='hash'), \
                 patch('work_books.book_metadata', side_effect=[{'course': 'one'}, ValueError('stale book')]):
                with self.assertRaisesRegex(ValueError, 'stale book'):
                    publish_books()
            self.assertEqual(target.read_bytes(), b'previous approved book')

    def test_missing_unselected_book_does_not_publish_partial_edition(self):
        tracks = [{'slug': 'one'}, {'slug': 'two'}]
        metadata = [dict(course=slug, sha256='hash') for slug in ('one', 'two')]
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            with patch('work_books.ROOT', root), patch('work_curriculum.load_tracks', return_value=tracks), \
                 patch('work_curriculum.validate_tracks'), patch('work_curriculum.content_hash', return_value='hash'), \
                 patch('work_books.book_metadata', side_effect=metadata):
                with self.assertRaisesRegex(ValueError, 'missing or stale'):
                    publish_books(['one'])
            self.assertFalse((root / book_href('one')).exists())

    def test_legacy_generation_routes_to_books(self):
        from generate_work_documents import main
        with patch('work_books.publish_books', return_value={'documents': {}}) as publish:
            main(['manufacturing'], [2])
            publish.assert_called_once_with(['manufacturing'])

    def test_audit_recognizes_only_the_intentional_margin_tab(self):
        from audit_work_documents import is_book_margin_tab
        tab = dict(text='1', size=8, x0=597, x1=602.57, top=66.9218752)
        self.assertTrue(is_book_margin_tab(tab))
        for change in (dict(text='a'), dict(x1=613), dict(top=400), dict(size=10)):
            self.assertFalse(is_book_margin_tab({**tab, **change}))


if __name__ == '__main__':
    unittest.main()
