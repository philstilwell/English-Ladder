import copy
import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from datetime import date
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock, patch

from bs4 import BeautifulSoup
from PIL import Image

import daily_images
import editorial
import update_site
from verify_discover import discover_mismatches


def lesson(release="2020-01-02", title="Scientists discover a new forest"):
    brief = {"title": title, "overview": "Scientists learn how a forest grows.",
             "news_brief_sentences": ["Trees grow in the forest."],
             "vocabulary": [{"term": "forest"}], "prediction": "How do trees help us?"}
    return {"release_date": release, "source": {"link": "https://example.com/science"},
            "levels": {level: {"lesson": copy.deepcopy(brief)}
                       for level in ("beginner", "intermediate", "advanced")}}


def client_with_image():
    buffer = io.BytesIO()
    Image.new("RGB", (800, 600), "#718a76").save(buffer, format="PNG")
    part = SimpleNamespace(inline_data=SimpleNamespace(mime_type="image/png", data=buffer.getvalue()), thought=False)
    response = SimpleNamespace(candidates=[SimpleNamespace(content=SimpleNamespace(parts=[part]))])
    client = Mock()
    client.models.generate_content.return_value = response
    return client


class DailyImageTests(unittest.TestCase):
    def setUp(self):
        # Simulated provider failures must not become real GitHub warning annotations.
        self.enterContext(redirect_stdout(io.StringIO()))
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "archive/lessons").mkdir(parents=True)

    def archive(self, value):
        path = self.root / "archive/lessons" / (value["release_date"] + ".json")
        path.write_text(json.dumps(value))
        return path

    def homepage(self):
        with patch.object(editorial, "ROOT", self.root):
            editorial.build_homepage()
        return BeautifulSoup((self.root / "index.html").read_text(), "html.parser")

    def test_selects_latest_complete_archive_not_future_or_malformed(self):
        expected = self.archive(lesson())
        self.archive(lesson("2030-01-01"))
        broken = lesson("2020-01-03")
        broken["levels"]["advanced"]["lesson"] = None
        self.archive(broken)
        (self.root / "archive/lessons/2020-01-04.json").write_text("not json")
        self.assertEqual(expected, daily_images.latest_lesson(self.root, date(2020, 1, 5))[0])

    def test_one_image_is_saved_and_reused_without_another_request(self):
        value = lesson()
        path = self.archive(value)
        client = client_with_image()
        first = daily_images.ensure_daily_image(path, self.root, client)
        second = daily_images.ensure_daily_image(path, self.root, client)
        self.assertEqual(first, second)
        self.assertEqual(1, client.models.generate_content.call_count)
        self.assertEqual(first, daily_images.image_for_lesson(value, self.root))
        with Image.open(self.root / first["path"]) as picture:
            self.assertEqual("WEBP", picture.format)
            self.assertEqual((800, 600), picture.size)

    def test_replaced_story_never_reuses_an_unrelated_image(self):
        value = lesson()
        path = self.archive(value)
        first = daily_images.ensure_daily_image(path, self.root, client_with_image())
        value["levels"]["beginner"]["lesson"]["title"] = "A new train service opens"
        self.archive(value)
        self.assertIsNone(daily_images.image_for_lesson(value, self.root))
        second = daily_images.ensure_daily_image(path, self.root, client_with_image())
        self.assertNotEqual(first["path"], second["path"])

    def test_failure_is_bounded_and_does_not_break_the_lesson(self):
        path = self.archive(lesson())
        client = Mock()
        client.models.generate_content.side_effect = RuntimeError("provider unavailable")
        for _ in range(5):
            self.assertIsNone(daily_images.ensure_daily_image(path, self.root, client))
        self.assertEqual(3, client.models.generate_content.call_count)
        self.assertEqual("failed", daily_images.read_metadata(self.root / "assets/news/2020-01-02.json")["status"])
        home = self.homepage()
        self.assertIsNotNone(home.select_one(".feature-preview"))
        self.assertNotIn("Before you read", home.get_text())
        self.assertNotIn("How do trees help us?", home.get_text())
        self.assertEqual("beginner.html#lesson-2020-01-02", home.select_one("#feature-start")["href"])

    def test_empty_image_response_can_be_retried_successfully(self):
        value = lesson()
        path = self.archive(value)
        client = Mock()
        client.models.generate_content.return_value = SimpleNamespace(candidates=[])
        self.assertIsNone(daily_images.ensure_daily_image(path, self.root, client))
        self.assertEqual("ready", daily_images.ensure_daily_image(path, self.root, client_with_image())["status"])

    def test_missing_or_corrupt_image_is_not_rendered(self):
        value = lesson()
        path = self.archive(value)
        meta = daily_images.ensure_daily_image(path, self.root, client_with_image())
        (self.root / meta["path"]).write_bytes(b"broken")
        self.assertIsNone(daily_images.image_for_lesson(value, self.root))
        self.assertIsNone(self.homepage().select_one(".feature-story img"))

    def test_no_archive_retains_the_evergreen_feature(self):
        home = self.homepage()
        self.assertEqual("stories/city-trees/beginner.html", home.select_one("#feature-start")["href"])
        self.assertIsNone(home.select_one(".feature-story time"))

    def test_feature_updates_title_date_image_and_every_level_together(self):
        self.archive(lesson("2020-01-01", "Yesterday's story"))
        value = lesson(title="Trees & cities <today>")
        path = self.archive(value)
        meta = daily_images.ensure_daily_image(path, self.root, client_with_image())
        home = self.homepage()
        feature = home.select_one(".feature-story")
        self.assertEqual("Title: Trees & cities <today>", feature.select_one('#feature-title').get_text())
        self.assertEqual("Trees & cities <today>", feature.select_one('#feature-title .lesson-title-text').get_text())
        self.assertEqual('Free English lessons for real life.', home.h1.get_text())
        self.assertEqual(1,len(home.select('h1')))
        self.assertEqual("2020-01-02", feature.time["datetime"])
        self.assertEqual(meta["path"], feature.img["src"])
        self.assertIn("AI-generated illustration", feature.figcaption.get_text())
        self.assertIn("not a news photograph", feature.figcaption.get_text())
        self.assertIsNone(feature.find("today"))
        for level in ("beginner", "intermediate", "advanced"):
            target = f"{level}.html#lesson-2020-01-02"
            self.assertEqual(target, feature.select_one(f'input[value="{level}"]')["data-lesson-href"])
            self.assertIsNotNone(feature.find("a", href=target))

    def test_deployment_check_requires_matching_feature_and_exact_image(self):
        path = self.archive(lesson())
        daily_images.ensure_daily_image(path, self.root, client_with_image())
        home = str(self.homepage()).encode()
        picture = (self.root / self.homepage().select_one(".feature-story img")["src"]).read_bytes()
        fetch = Mock(side_effect=[home, picture])
        self.assertEqual([], discover_mismatches("https://example.com", self.root, fetch))
        self.assertTrue(discover_mismatches("https://example.com", self.root, Mock(side_effect=[home, b"wrong"])))
        stale = home.replace(b"2020-01-02", b"2020-01-01")
        self.assertTrue(discover_mismatches("https://example.com", self.root, Mock(return_value=stale)))

    def test_push_refresh_never_calls_an_image_or_text_model(self):
        args = SimpleNamespace(refresh_feature=False, refresh_pages=True)
        with patch.object(update_site, "parse_args", return_value=args), \
                patch("site_quality.rebuild_news_levels"), \
                patch.object(update_site, "refresh_existing_pages"), \
                patch.object(editorial, "publish_editorial_pages"), \
                patch.object(daily_images, "ensure_daily_image") as image, \
                patch.object(update_site, "configure_gemini") as text:
            update_site.main()
        image.assert_not_called()
        text.assert_not_called()

    def test_scheduled_existing_lesson_retries_only_its_image(self):
        args = SimpleNamespace(refresh_feature=False, refresh_pages=False, release_date="2020-01-02", skip_existing=True)
        with patch.object(update_site, "parse_args", return_value=args), \
                patch.object(update_site, "archive_exists_for_release_dt", return_value=True), \
                patch.object(editorial, "publish_editorial_pages") as publish, \
                patch.object(daily_images, "ensure_daily_image") as image, \
                patch.object(update_site, "get_daily_news") as news:
            update_site.main()
        image.assert_called_once()
        publish.assert_called_once()
        news.assert_not_called()

    def test_initial_feature_refresh_does_not_generate_lesson_text(self):
        path = self.archive(lesson())
        args = SimpleNamespace(refresh_feature=True)
        with patch.object(update_site, "parse_args", return_value=args), \
                patch.object(daily_images, "latest_lesson", return_value=(path, lesson())), \
                patch.object(editorial, "publish_editorial_pages"), \
                patch.object(daily_images, "ensure_daily_image") as image, \
                patch.object(update_site, "get_daily_news") as news:
            update_site.main()
        image.assert_called_once_with(path)
        news.assert_not_called()
