import json
import tempfile
import unittest
from datetime import date, datetime, timezone
from pathlib import Path
from unittest.mock import patch

from bs4 import BeautifulSoup
import editorial
import lesson_retention as retention
import site_quality
import update_site
from vocabulary_translations import source_data, source_key


def edition(released, word="example"):
    return {"release_date": released, "levels": {"beginner": {"lesson": {
        "news_brief_sentences": [f"This is an {word}."],
        "vocabulary": [{"term": word, "part_of_speech": "noun", "definition": word}]}}}}


class LessonRetentionTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.today = date(2026, 9, 22)

    def write(self, name, text="content"):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
        return path

    def archive(self, released, word="example"):
        record = edition(released, word)
        self.write(f"archive/lessons/{released}.json", json.dumps(record))
        return record

    def test_calendar_boundary_keeps_age_49_and_removes_age_50_even_with_gaps(self):
        for released in ("2026-08-02", "2026-08-03", "2026-08-04", "2026-09-22", "2030-01-01"):
            self.archive(released)
        plan = retention.prune_expired_lessons(self.root, self.today, dry_run=True)
        self.assertEqual(["2026-08-02", "2026-08-03"], plan["expired_dates"])
        self.assertEqual("2026-08-04", plan["oldest_allowed"])
        self.assertEqual(5, len(list((self.root / "archive/lessons").glob("*.json"))))
        retention.prune_expired_lessons(self.root, self.today)
        self.assertEqual(["2026-08-04", "2026-09-22", "2030-01-01"],
                         sorted(p.stem for p in (self.root / "archive/lessons").glob("*.json")))

    def test_clock_uses_fixed_est_in_summer_and_near_utc_midnight(self):
        self.assertEqual(date(2026, 9, 21), retention.retention_date(datetime(2026, 9, 22, 4, 59, tzinfo=timezone.utc)))
        self.assertEqual(date(2026, 9, 22), retention.retention_date(datetime(2026, 9, 22, 5, 0, tzinfo=timezone.utc)))
        self.assertEqual(date(2026, 1, 1), retention.retention_date(datetime(2026, 1, 2, 4, 59, tzinfo=timezone.utc)))
        with self.assertRaises(ValueError):
            retention.retention_date(datetime(2026, 9, 22))

    def test_prunes_orphan_daily_pages_and_assets_but_preserves_other_content(self):
        expired = [f"news/2026-08-03/{level}.html" for level in ("beginner", "intermediate", "advanced")]
        expired += ["assets/news/2026-08-03.json", "assets/news/2026-08-03-abcdef123456.webp",
                    "assets/news/2026-08-03-abcdef123456.webp.tmp"]
        retained = ["news/2026-08-04/beginner.html", "news/2026-08-03/editorial-note.txt",
                    "news/2026-02-30/beginner.html", "assets/news/2026-08-04.json",
                    "stories/food-market/beginner.html", "assets/editorial/food-market.webp",
                    "assets/news/credits.json", "data/vocabulary-translations/.usage-2026-08-03.json"]
        for name in expired + retained:
            self.write(name)
        plan = retention.prune_expired_lessons(self.root, self.today)
        self.assertEqual(sorted(expired), plan["files"])
        self.assertTrue(all(not (self.root / name).exists() for name in expired))
        self.assertTrue(all((self.root / name).exists() for name in retained))

    def test_caches_only_expire_when_their_known_source_is_no_longer_used(self):
        expired = self.archive("2026-08-03", "expired")
        self.archive("2026-08-02", "shared")
        self.archive("2026-08-04", "shared")
        from story_lessons import STORIES
        evergreen = STORIES[0]["levels"]["beginner"]
        self.write("archive/lessons/2026-08-01.json", json.dumps({"release_date": "2026-08-01",
            "levels": {"beginner": {"lesson": evergreen}}}))
        expired_key = source_key(source_data(expired["levels"]["beginner"]["lesson"], "beginner"))
        shared_key = source_key(source_data(edition("2026-08-04", "shared")["levels"]["beginner"]["lesson"], "beginner"))
        evergreen_key = source_key(source_data(evergreen, "beginner"))
        for key in (expired_key, shared_key, evergreen_key, "unknown"):
            self.write(f"data/vocabulary-translations/{key}.json")
            self.write(f"data/vocabulary-translations/.draft-{key}.json")
        retention.prune_expired_lessons(self.root, self.today)
        self.assertFalse((self.root / f"data/vocabulary-translations/{expired_key}.json").exists())
        self.assertFalse((self.root / f"data/vocabulary-translations/.draft-{expired_key}.json").exists())
        for key in (shared_key, evergreen_key, "unknown"):
            self.assertTrue((self.root / f"data/vocabulary-translations/{key}.json").exists())
            self.assertTrue((self.root / f"data/vocabulary-translations/.draft-{key}.json").exists())

    def test_invalid_archive_metadata_aborts_before_any_deletion(self):
        good = self.archive("2026-08-01")
        self.write("archive/lessons/2026-08-03.json", json.dumps(good))
        with self.assertRaisesRegex(ValueError, "archive date data is invalid"):
            retention.prune_expired_lessons(self.root, self.today)
        self.assertTrue((self.root / "archive/lessons/2026-08-01.json").exists())

    def test_unrecognized_dates_are_preserved_and_reported(self):
        self.write("archive/lessons/2026-02-30.json", "bad date")
        plan = retention.prune_expired_lessons(self.root, self.today)
        self.assertEqual([], plan["files"])
        self.assertTrue(plan["warnings"])

    def test_linked_path_is_never_followed_for_deletion(self):
        target = self.write("protected.html")
        path = self.root / "news/2026-08-03/beginner.html"
        path.parent.mkdir(parents=True)
        path.symlink_to(target)
        with self.assertRaisesRegex(ValueError, "linked daily-news path"):
            retention.prune_expired_lessons(self.root, self.today)
        self.assertTrue(target.exists())

    def test_repeated_cleanup_removes_expired_files_restored_by_a_publication_retry(self):
        for _ in range(2):
            self.archive("2026-08-03")
            self.write("news/2026-08-03/beginner.html")
            plan = retention.prune_expired_lessons(self.root, self.today)
            self.assertEqual(2, len(plan["files"]))
            self.assertFalse((self.root / "news/2026-08-03").exists())
        self.assertEqual([], retention.prune_expired_lessons(self.root, self.today)["files"])

    def test_empty_archive_clears_rolling_lessons_and_the_homepage_uses_an_evergreen_story(self):
        for level in ("beginner", "intermediate", "advanced"):
            self.write(f"{level}.html", '<html><body><div id="lesson-container"><details class="daily-lesson">Expired story</details></div></body></html>')
        self.write("lesson-data.json", '{"beginner":{"headline":"Expired story"}}')
        with patch.object(site_quality, "ROOT", self.root), patch.object(editorial, "ROOT", self.root), \
                patch.object(editorial, "decorate_page"):
            site_quality.rebuild_news_levels()
            site_quality.build_news_archive()
            editorial.build_homepage()
        for level in ("beginner", "intermediate", "advanced"):
            soup = BeautifulSoup((self.root / f"{level}.html").read_text(), "html.parser")
            self.assertIsNone(soup.select_one(".daily-lesson"))
            self.assertIn("last 50 days", soup.select_one("#empty-state").text)
        self.assertEqual({}, json.loads((self.root / "lesson-data.json").read_text()))
        home = (self.root / "index.html").read_text()
        self.assertNotIn("Expired story", home)
        self.assertIn('href="stories/city-trees/beginner.html"', home)

    def test_new_release_time_and_legacy_explicit_publication_times(self):
        expected = datetime(2026, 9, 22, 6, 15, tzinfo=timezone.utc)
        self.assertEqual(expected, update_site.release_datetime_from_date("2026-09-22"))
        self.assertEqual(expected, update_site.fallback_release_datetime("September 22, 2026"))
        old = {"release_date": "2026-09-21", "release_iso": "2026-09-21T10:00:00Z"}
        self.assertEqual(datetime(2026, 9, 21, 10, tzinfo=timezone.utc), update_site.release_datetime_from_archive(old))
        self.assertEqual(expected, update_site.release_datetime_from_archive({"release_date": "2026-09-22"}))


if __name__ == "__main__":
    unittest.main()
