"""Approved lesson corrections must stay aligned across source, pages, and prompts."""
import json
import re
from pathlib import Path
import unittest

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]


class EditorialCorrectionTests(unittest.TestCase):
    @staticmethod
    def edition(date):
        path = ROOT / 'archive' / 'lessons' / f'{date}.json'
        if not path.is_file():
            raise unittest.SkipTest(f'{date} is no longer in the retained daily archive')
        return json.loads(path.read_text())

    @staticmethod
    def lesson_nodes(date, level):
        permanent = ROOT / 'news' / date / f'{level}.html'
        soup = BeautifulSoup(permanent.read_text(), 'html.parser')
        node = soup.find(class_='daily-lesson', attrs={'data-lesson-key': date})
        if node is None:
            raise AssertionError(f'{permanent}: missing {date} lesson')
        yield permanent, node

        # Level feeds intentionally retain only the latest 14 editions. Check
        # this copy while it is present without making an older retained lesson
        # fail merely because it has rotated out of the feed.
        feed = ROOT / f'{level}.html'
        soup = BeautifulSoup(feed.read_text(), 'html.parser')
        node = soup.find(class_='daily-lesson', attrs={'data-lesson-key': date})
        if node is not None:
            yield feed, node

    def assert_rendered_quiz_item(self, date, level, index, item):
        for path, node in self.lesson_nodes(date, level):
            question = node.select('.quiz-question')[index]
            self.assertEqual(
                f'{index + 1}. {item["question"]}',
                question.find('p', recursive=False).get_text(' ', strip=True),
                str(path),
            )
            buttons = question.select('button')
            options = [re.sub(r'^[abc]\)\s*', '', button.get_text(' ', strip=True))
                       for button in buttons]
            self.assertEqual(sorted(item['options']), sorted(options), str(path))
            expected_answer = item['options'][item['correct_option_index']]
            rendered_answer = [re.sub(r'^[abc]\)\s*', '', button.get_text(' ', strip=True))
                               for button in buttons
                               if button.get('data-bg') == '#e6ffe6']
            self.assertEqual([expected_answer], rendered_answer, str(path))
            expected_feedback = {
                option: ('Correct: ' if option_index == item['correct_option_index']
                         else 'Incorrect: ') + item['option_feedback'][option_index]
                for option_index, option in enumerate(item['options'])
            }
            rendered_feedback = {
                re.sub(r'^[abc]\)\s*', '', button.get_text(' ', strip=True)):
                    button.get('data-feedback')
                for button in buttons
            }
            self.assertEqual(expected_feedback, rendered_feedback, str(path))

    def assert_prompts_contain(self, date, level, required, forbidden):
        for path, node in self.lesson_nodes(date, level):
            prompts = node.select('.ai-prompt-text')
            self.assertEqual(3, len(prompts), str(path))
            for prompt in prompts:
                text = prompt.get_text(' ', strip=True)
                for phrase in required:
                    self.assertIn(phrase, text, f'{path}: {prompt.get("id")}')
                for phrase in forbidden:
                    self.assertNotIn(phrase, text, f'{path}: {prompt.get("id")}')

    def test_october_10_return_question_uses_hammonds_stated_reason(self):
        edition = self.edition('2026-10-10')
        lesson = edition['levels']['intermediate']['lesson']
        item = lesson['quiz'][4]
        self.assertEqual(0, item['correct_option_index'])
        self.assertEqual(
            'She feared that if she delayed her return, she might never come back.',
            item['options'][item['correct_option_index']],
        )
        self.assertIn("if I don't come back today, I probably wouldn't come back",
                      edition['source']['evidence_text'])
        self.assert_rendered_quiz_item('2026-10-10', 'intermediate', 4, item)
        self.assert_prompts_contain(
            '2026-10-10', 'intermediate',
            ["fearing that if she didn't come back immediately, she might never do so"],
            ['She feared the show itself was causing her panic'],
        )

    def test_october_11_attributes_each_affected_intermediate_copy_to_roberts(self):
        edition = self.edition('2026-10-11')
        lesson = edition['levels']['intermediate']['lesson']
        self.assertIn('Liz Saville Roberts', edition['source']['evidence_text'])
        self.assertEqual(
            'Plaid Cymru MP Liz Saville Roberts highlighted the need for proper regulations '
            'and community benefits from large-scale developments.',
            lesson['news_brief_sentences'][9],
        )
        self.assertEqual(
            'She also noted Wales has a history of extractive industries that often left '
            'little benefit for communities.',
            lesson['news_brief_sentences'][10],
        )
        self.assertTrue(lesson['grammar']['example_quote'].startswith('She also noted'))
        for index in (4, 5, 7):
            self.assert_rendered_quiz_item('2026-10-11', 'intermediate', index,
                                           lesson['quiz'][index])
        for path, node in self.lesson_nodes('2026-10-11', 'intermediate'):
            text = node.get_text(' ', strip=True)
            self.assertIn('Liz Saville Roberts', text, str(path))
            self.assertNotIn('What concern does Ernest Dyson', text, str(path))
            self.assertNotIn('Why does Ernest Dyson', text, str(path))
            self.assertNotIn('He also noted Wales has a history of extractive industries',
                             text, str(path))
        self.assert_prompts_contain(
            '2026-10-11', 'intermediate',
            ['Liz Saville Roberts highlighted the need for proper regulations',
             'She also noted Wales has a history of extractive industries'],
            ['Local opponent Ernest Dyson highlighted the need for appropriate regulations',
             'He also noted Wales has a history of extractive industries'],
        )

        advanced = edition['levels']['advanced']['lesson']
        self.assertTrue(any(sentence.startswith('Liz Saville Roberts,')
                            for sentence in advanced['news_brief_sentences']))
        self.assertIn("Roberts highlighted Wales's", advanced['grammar']['example_quote'])

    def test_october_12_names_ukraines_operations_in_every_advanced_copy(self):
        edition = self.edition('2026-10-12')
        lesson = edition['levels']['advanced']['lesson']
        corrected = ("Moscow asserts these installations are legitimate targets supporting "
                     "Ukraine's military operations, while Kyiv views its attacks as essential "
                     "to curtailing Russia's war finance capabilities.")
        self.assertEqual(corrected, lesson['news_brief_sentences'][10])
        self.assertIn("supported Ukraine's military operation",
                      edition['source']['evidence_text'])
        item = lesson['quiz'][9]
        self.assertEqual(1, item['correct_option_index'])
        self.assertIn("support Ukraine's military operations",
                      item['options'][item['correct_option_index']])
        self.assert_rendered_quiz_item('2026-10-12', 'advanced', 9, item)
        self.assert_prompts_contain(
            '2026-10-12', 'advanced',
            ["supporting Ukraine's military operations"],
            ['supporting its military operations'],
        )
        current = json.loads((ROOT / 'lesson-data.json').read_text())
        if current['advanced'].get('url') == 'news/2026-10-12/advanced.html':
            self.assertIn("supporting Ukraine's military operations",
                          current['advanced']['brief'])
            self.assertNotIn('supporting its military operations',
                             current['advanced']['brief'])

    def test_october_13_advanced_quiz_labels_clause_and_post_mortem_purpose(self):
        edition = self.edition('2026-10-13')
        lesson = edition['levels']['advanced']['lesson']

        clause_item = lesson['quiz'][5]
        self.assertEqual(0, clause_item['correct_option_index'])
        self.assertEqual(
            'Incorrect. This is a non-defining relative clause adding information about '
            'friendship. It does not explain when Cranston felt despair.',
            clause_item['option_feedback'][2],
        )
        self.assert_rendered_quiz_item('2026-10-13', 'advanced', 5, clause_item)

        post_mortem_item = lesson['quiz'][9]
        self.assertEqual(
            'What is the purpose of the post-mortem examination mentioned in the reading?',
            post_mortem_item['question'],
        )
        self.assertEqual(0, post_mortem_item['correct_option_index'])
        self.assertEqual(
            "To medically determine the exact circumstances surrounding Mitte's death.",
            post_mortem_item['options'][post_mortem_item['correct_option_index']],
        )
        self.assertIn('adding that a post-mortem examination would be performed',
                      edition['source']['evidence_text'])
        self.assert_rendered_quiz_item('2026-10-13', 'advanced', 9, post_mortem_item)

        for path, node in self.lesson_nodes('2026-10-13', 'advanced'):
            rendered = str(node)
            self.assertNotIn('functions as an adjective phrase modifying', rendered, str(path))
            self.assertNotIn('Why did the local justice of the peace order', rendered, str(path))
            prompts = node.select('.ai-prompt-text')
            self.assertEqual(3, len(prompts), str(path))
            for prompt in prompts:
                prompt_text = prompt.get_text(' ', strip=True)
                self.assertNotIn('functions as an adjective phrase modifying', prompt_text,
                                 f'{path}: {prompt.get("id")}')
                self.assertNotIn('Why did the local justice of the peace order', prompt_text,
                                 f'{path}: {prompt.get("id")}')


if __name__ == '__main__':
    unittest.main()
