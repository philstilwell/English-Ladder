import unittest
from urllib.parse import urlsplit

from bs4 import BeautifulSoup
import study_routes


class StudyRouteTests(unittest.TestCase):
    def test_every_step_resolves_at_every_offered_level(self):
        for key, route in study_routes.routes().items():
            for step in route['steps']:
                for level in study_routes.LEVELS if key == 'reading' else ['beginner']:
                    with self.subTest(route=key, step=step['title'], level=level):
                        url = urlsplit(study_routes.step_href(key, step, level))
                        path = study_routes.ROOT / url.path
                        self.assertTrue(path.is_file(), path)
                        if url.fragment:
                            soup = BeautifulSoup(path.read_text(), 'html.parser')
                            self.assertIsNotNone(soup.find(id=url.fragment))

    def test_guide_has_usable_ordered_links_without_javascript(self):
        soup = BeautifulSoup((study_routes.ROOT / 'study-routes.html').read_text(), 'html.parser')
        for route in study_routes.routes():
            card = soup.find(id=route)
            self.assertEqual(3, len(card.select('ol > li > a[href]')))
            self.assertIsNotNone(card.find('h2'))
        self.assertIsNotNone(soup.select_one('#reading noscript'))

    def test_route_enhancement_is_repeatable_and_never_rewrites_lesson_text(self):
        soup = BeautifulSoup((study_routes.ROOT / 'us-life.html').read_text(), 'html.parser')
        original = str(soup.main)
        for _ in range(2):
            study_routes.enhance_page(soup, 'us-life.html', '')
        self.assertEqual(original, str(soup.main))
        self.assertEqual(1, len(soup.select('[data-study-routes]')))
        self.assertEqual(1, len(soup.select('script[src*="study-routes.js"]')))
        self.assertEqual(1, len(soup.select('link[href*="study-routes.css"]')))
