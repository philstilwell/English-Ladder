import json
import unittest
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote, urlparse

from bs4 import BeautifulSoup
import editorial
import update_site
from story_lessons import STORIES

ROOT = Path(__file__).resolve().parents[1]


class EditorialTests(unittest.TestCase):
    def test_all_grammar_lessons_and_directory_keep_their_original_graphics(self):
        from grammar_curriculum import load_curriculum
        directory=BeautifulSoup((ROOT/'grammar-concepts.html').read_text(),'html.parser')
        previews=directory.select('[data-library-item] .grammar-thumb img')
        self.assertEqual(44,len(previews))
        for concept,preview in zip(load_curriculum(),previews):
            number=concept['number']
            image=f'assets/grammar-concepts/concept-{number:02}.png'
            with self.subTest(concept=number):
                page=BeautifulSoup((ROOT/f'grammar-concepts/concept-{number:02}.html').read_text(),'html.parser')
                images=page.select('.concept-graphic img')
                self.assertEqual(1,len(images))
                self.assertEqual('../'+image,images[0]['src'])
                self.assertEqual(('1880','1576'),(images[0]['width'],images[0]['height']))
                self.assertIn(concept['title'],images[0]['alt'])
                trigger=images[0].parent
                self.assertEqual('../'+image,trigger['href'])
                self.assertEqual(trigger['href'],trigger['data-lightbox-src'])
                self.assertIsNotNone(page.select_one('.image-lightbox [role="dialog"]'))
                self.assertEqual('https://englishladder.com/'+image,page.select_one('meta[property="og:image"]')['content'])
                self.assertEqual(image,preview['src'])
                self.assertEqual('lazy',preview['loading'])
                self.assertEqual(f'grammar-concepts/concept-{number:02}.html',preview.parent['href'])
                self.assertTrue((ROOT/image).is_file())

    def test_all_curated_lessons_are_consistent_and_level_specific(self):
        for story in STORIES:
            readings = set()
            for level in update_site.LEVELS:
                data = story["levels"][level["name"].lower()]
                config = dict(level, min_sentence_count=6, vocabulary_count=3, quiz_count=5)
                self.assertEqual([], update_site.validate_lesson_data(data, config))
                readings.add(tuple(data["news_brief_sentences"]))
            self.assertEqual(3, len(readings))

    def test_news_selection_avoids_repeats_and_varies_emotional_tone(self):
        entries = [
            dict(title="War leaves people dead", summary="A report on war victims.", link="https://example.com/war"),
            dict(title="A new discovery", summary="Scientists have discovered a new species.", link="https://example.com/science"),
            dict(title="A different discovery", summary="A discovery about local birds.", link="https://example.com/birds"),
        ]
        self.assertEqual("https://example.com/science", update_site.select_news_entry(entries)["link"])
        self.assertEqual("https://example.com/birds", update_site.select_news_entry(entries, ["https://example.com/science"])["link"])
        self.assertIsNone(update_site.select_news_entry([dict(title="Missing evidence", link="javascript:alert(1)")]))

    def test_guided_rendering_is_repeatable_and_escapes_prompt_content(self):
        data = dict(STORIES[0]["levels"]["beginner"])
        data["prediction"] = '<img src=x onerror="alert(1)">'
        lesson = BeautifulSoup(update_site.render_lesson_html(data, update_site.LEVELS[0], datetime(2026, 9, 5, tzinfo=timezone.utc)), "html.parser").details
        before = str(lesson)
        editorial.enhance_lesson(lesson, data)
        self.assertEqual(before, str(lesson))
        self.assertIsNone(lesson.select_one(".prediction img"))
        self.assertEqual(3, len(lesson.select(".learning-panel")))
        self.assertEqual(5, len(lesson.select(".quiz-question")))

    def test_every_published_page_has_shared_design_and_valid_local_links(self):
        paths = [*ROOT.glob("*.html"), *ROOT.glob("grammar-concepts/*.html"), *ROOT.glob("stories/*/*.html")]
        parsed = {path.resolve(): BeautifulSoup(path.read_text(), "html.parser") for path in paths}
        failures = []
        for path, soup in parsed.items():
            self.assertTrue(any(urlparse(link["href"]).path.endswith("editorial.css")
                                for link in soup.select("link[href]")), str(path))
            self.assertEqual(1, len(soup.select(".site-header")), str(path))
            self.assertEqual(1, len(soup.select("#main-content")), str(path))
            ids = [tag["id"] for tag in soup.select("[id]")]
            self.assertEqual(len(ids), len(set(ids)), str(path))
            for tag in soup.select("a[href], img[src], script[src], link[href]"):
                ref = tag.get("href", tag.get("src", ""))
                url = urlparse(ref)
                if not ref or url.scheme or url.netloc:
                    continue
                target = ((ROOT / unquote(url.path).lstrip("/")) if url.path.startswith("/") else (path.parent / unquote(url.path))).resolve() if url.path else path
                if not target.exists():
                    failures.append(f"{path.relative_to(ROOT)}: {ref}")
                elif url.fragment and target in parsed and not parsed[target].find(id=unquote(url.fragment)):
                    failures.append(f"{path.relative_to(ROOT)}: missing anchor {ref}")
        self.assertEqual([], failures)

    def test_homepage_latest_story_matches_archive_and_points_to_all_levels(self):
        archive = sorted((ROOT / "archive/lessons").glob("*.json"))[-1]
        data = json.loads(archive.read_text())
        home = BeautifulSoup((ROOT / "index.html").read_text(), "html.parser")
        self.assertIn(data["levels"]["beginner"]["lesson"]["title"], home.get_text())
        for level in ["beginner", "intermediate", "advanced"]:
            href = f'{level}.html#lesson-{data["release_date"]}'
            self.assertIsNotNone(home.find("a", href=href))

    def test_external_sources_require_https(self):
        self.assertEqual("", editorial.safe_url("javascript:alert(1)"))
        self.assertEqual("", editorial.safe_url("//example.com"))
        self.assertEqual("https://example.com/story", editorial.safe_url("https://example.com/story"))


if __name__ == "__main__":
    unittest.main()
