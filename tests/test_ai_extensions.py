import unittest
import json
from pathlib import Path
from bs4 import BeautifulSoup

import ai_extensions as ai
from grammar_curriculum import load_curriculum
from work_curriculum import load_tracks

ROOT = Path(__file__).resolve().parents[1]


class AIExtensionTests(unittest.TestCase):
    def test_every_grammar_and_work_lesson_has_its_own_context(self):
        for c in load_curriculum():
            soup = BeautifulSoup((ROOT/f'grammar-concepts/concept-{c["number"]:02}.html').read_text(), 'html.parser')
            prompts = soup.select('.ai-prompt-text')
            self.assertEqual(3, len(prompts))
            for node in prompts:
                self.assertIn(c['title'], node.text)
                self.assertIn(c['rules'][0], node.text)
            self.assertFalse(soup.select('textarea,input[type="text"]'))
        for t in load_tracks():
            soup = BeautifulSoup((ROOT/f'efsp-{t["slug"]}.html').read_text(), 'html.parser')
            self.assertTrue(soup.select_one('#vocabulary #ai-field-vocabulary'))
            data=json.loads(soup.select_one('[data-ai-data]').text)
            for m in t['modules']:
                self.assertEqual(4, len(soup.find(id=m['id']).select('[data-ai-preset]')))
                self.assertFalse(soup.find(id=m['id']).select('[data-ai-extension]'))
                context=next(c['text'] for c in data['contexts'] if c['id']==m['id'])
                self.assertIn(m['brief'], context)
                self.assertIn(m['vocabulary'][0]['definition'], context)

    def test_reading_everyday_tools_and_review_coverage(self):
        paths = [*ROOT.glob('news/*/*.html'), *ROOT.glob('stories/*/*.html'), *[ROOT/(level+'.html') for level in ['beginner','intermediate','advanced']]]
        for path in paths:
            soup = BeautifulSoup(path.read_text(), 'html.parser')
            for lesson in soup.select('.daily-lesson'):
                prompts = lesson.select('[data-stage="discuss"] .ai-prompt-text')
                self.assertEqual(3, len(prompts), str(path))
                reading = lesson.select_one('[data-stage="read"] .section p').get_text(' ', strip=True)
                self.assertIn(reading, prompts[0].text)
                self.assertIn('Do not add news updates', prompts[1].text)
        life = BeautifulSoup((ROOT/'us-life.html').read_text(), 'html.parser')
        self.assertEqual(24, len(life.select('.us-life-module [data-ai-extension]')))
        for unit in life.select('.us-life-module'):
            for node in unit.select('.ai-prompt-text'):
                self.assertIn(unit.select_one('h2').text, node.text)
        tools = BeautifulSoup((ROOT/'tools.html').read_text(), 'html.parser')
        self.assertEqual(6, len(tools.select('.tool-panel [data-ai-extension]')))
        self.assertIn('Without hearing a recording', tools.select_one('#ai-tool-pronunciation-shadowing').text)
        self.assertTrue(BeautifulSoup((ROOT/'continue.html').read_text(), 'html.parser').select_one('#ai-review'))

    def test_republishing_does_not_duplicate_or_capture_student_writing(self):
        for name in ['grammar-concepts/concept-35.html', 'efsp-manufacturing.html', 'us-life.html', 'news/2026-09-06/beginner.html', 'tools.html']:
            path = ROOT/name
            soup = BeautifulSoup(path.read_text(), 'html.parser')
            expected = [n.text for n in soup.select('.ai-prompt-text')]
            for textarea in soup.select('textarea'):
                textarea.string = 'PRIVATE_DRAFT_DO_NOT_COPY'
            prefix = '../../' if name.startswith('news/') else ('../' if name.startswith('grammar-concepts/') else '')
            ai.enhance_page(soup, path, prefix)
            ai.enhance_page(soup, path, prefix)
            self.assertEqual(expected, [n.text for n in soup.select('.ai-prompt-text')])
            self.assertNotIn('PRIVATE_DRAFT_DO_NOT_COPY', '\n'.join(n.text for n in soup.select('.ai-prompt-text')))
            ids = [n['id'] for n in soup.select('[id]')]
            self.assertEqual(len(ids), len(set(ids)))

    def test_instructions_preserve_choices_and_treat_context_as_reference(self):
        for mode in ai.TASKS:
            item = ai.prompt(mode, {'lesson': '<img src=x onerror=alert(1)>', 'study_level': 'A2'})
            self.assertIn('three labeled choices, A, B, and C', item['text'])
            self.assertIn('exactly one offered answer', item['text'])
            self.assertIn('not instructions', item['text'])
            self.assertIn('not a proficiency diagnosis', item['text'])
            soup = BeautifulSoup(ai.panel('test', [item]), 'html.parser')
            self.assertFalse(soup.select('img,textarea,input'))
            self.assertIn('<img src=x', soup.pre.text)
            self.assertTrue(soup.select_one('[data-ai-copy-text]').has_attr('hidden'))
            self.assertTrue(soup.select_one('noscript'))

    def test_print_prompts_are_tailored_to_the_guide_purpose(self):
        c=load_curriculum()[34]
        student=ai.grammar_prompts(c)[0]
        teacher=ai.prompt('teacher',{'lesson':c['title'],'grammar_focus':c['rules']})
        self.assertIn('question 1 only',student['text'])
        self.assertIn('teacher-only answer key',teacher['text'])
        for item in [student,teacher]:
            self.assertIn(c['title'],item['text'])
            self.assertIn(c['rules'][0],item['text'])

    def test_a_new_daily_lesson_gets_fresh_prompts_when_published(self):
        from copy import deepcopy
        from datetime import datetime, timezone
        from editorial import document
        from story_lessons import STORIES
        from update_site import render_lesson_html, LEVELS
        lesson = deepcopy(STORIES[0]['levels']['beginner'])
        lesson['title'] = 'A new fictional library visit'
        lesson['news_brief_sentences'] = ['Tara visits a library.', 'She borrows a book about birds.']
        body = render_lesson_html(lesson, LEVELS[0], datetime(2030,1,2,tzinfo=timezone.utc))
        soup = BeautifulSoup(document(lesson['title'], body, 'theme-beginner', '../../'), 'html.parser')
        path = ROOT/'news/2030-01-02/beginner.html'
        ai.enhance_page(soup, path, '../../')
        self.assertEqual(3, len(soup.select('.ai-prompt-text')))
        for node in soup.select('.ai-prompt-text'):
            self.assertIn('Tara visits a library.', node.text)
            self.assertIn(lesson['title'], node.text)
        soup.select_one('[data-stage="read"] .section p').string = 'Tara returns the book.'
        ai.enhance_page(soup, path, '../../')
        for node in soup.select('.ai-prompt-text'):
            self.assertIn('Tara returns the book.', node.text)
            self.assertNotIn('Tara visits a library.', node.text)


if __name__ == '__main__':
    unittest.main()
