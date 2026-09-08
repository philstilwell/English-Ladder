import copy
import json
import unittest
from datetime import datetime, timezone
from pathlib import Path

from bs4 import BeautifulSoup
from grammar_curriculum import load_curriculum, question_html
from teaching_typography import GUIDANCE, corrections, teaching_text
from update_site import LEVELS, render_lesson_html, render_quiz_question_html

ROOT = Path(__file__).resolve().parents[1]


class TeachingTypographyTests(unittest.TestCase):
    def test_reviewed_replacements_are_idempotent_and_only_change_quotes(self):
        for old, new in corrections().items():
            with self.subTest(text=old):
                self.assertEqual(old.replace('“', '').replace('”', ''), new.replace('“', '').replace('”', ''))
                self.assertEqual(new.count('“'), new.count('”'))
                self.assertEqual(new, teaching_text(teaching_text(old)))
        ordinary = 'I talked about the trip while she was waiting for the bus.'
        self.assertEqual(ordinary, teaching_text(ordinary))

    def test_screenshot_questions_and_feedback_preserve_word_boundaries(self):
        c = load_curriculum()[6]
        self.assertEqual('What does “about” mean in “about twenty people”?', c['checks'][2]['prompt'])
        self.assertIn('after “talk” and after “discuss”', c['application']['prompt'])
        page = BeautifulSoup(question_html(c, c['checks'][2], 3), 'html.parser')
        self.assertIn('“about twenty people”', page.legend.get_text())
        self.assertTrue(any('“About”' in i['data-choice-feedback'] for i in page.select('input')))
        self.assertEqual([o['text'] for o in c['checks'][2]['options']], [s.get_text() for s in page.select('label span')])

    def test_archive_display_keeps_reading_evidence_choices_and_translations_intact(self):
        record = json.loads((ROOT / 'archive/lessons/2026-09-06.json').read_text())
        lesson = record['levels']['advanced']
        lesson = lesson.get('lesson', lesson)
        before = copy.deepcopy(lesson)
        markup = render_lesson_html(lesson, LEVELS[2], datetime(2026, 9, 6, tzinfo=timezone.utc), record['source'])
        self.assertEqual(before, lesson)
        page = BeautifulSoup(markup, 'html.parser')
        self.assertIn('“Might need to”', page.get_text())
        self.assertIn('“consequently”', page.get_text())
        self.assertTrue(page.select('[data-translations]'))
        for q in lesson['quiz']:
            rendered = BeautifulSoup(render_quiz_question_html(1, q), 'html.parser')
            self.assertEqual(set(q['options']), {b.get_text()[3:] for b in rendered.select('button')})

    def test_guidance_and_ai_material_name_words_clearly(self):
        from ai_extensions import grammar_prompts
        self.assertIn('What does “about” mean', GUIDANCE)
        for p in grammar_prompts(load_curriculum()[6]):
            self.assertIn('“talk about a film”', p['text'])
            self.assertIn('quotation marks', p['text'])
