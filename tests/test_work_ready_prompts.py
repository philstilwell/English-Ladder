"""Learners can copy the complete authored text without composing a prompt."""
import unittest
from bs4 import BeautifulSoup
from work_curriculum import ROOT, load_tracks
from work_dialogues import load_dialogues
from work_web_content import web_track


class ReadyPromptTests(unittest.TestCase):
    def test_every_lesson_and_dialogue_contains_its_actual_material_without_javascript(self):
        count = 0
        scripts = load_dialogues()
        for track in load_tracks():
            track = web_track(track)
            soup = BeautifulSoup((ROOT / f'efsp-{track["slug"]}.html').read_text(), 'html.parser')
            for module in track['modules']:
                prompts = soup.select(f'#{module["id"]} .finished-prompt pre')
                self.assertEqual(3, len(prompts))
                for prompt in prompts:
                    text = prompt.get_text()
                    self.assertTrue(text.startswith('TASK:'))
                    self.assertIn(module['brief'], text)
                    self.assertIn(module['workshop']['explanation'], text)
                    self.assertIn(module['writing_task'], text)
                    self.assertTrue(text.endswith('END REFERENCE'))
                    self.assertIn('stop and wait', text.lower())
                    count += 1
            for i, dialogue in enumerate(scripts[track['slug']], 1):
                for mode in ['roleplay', 'dialogues']:
                    prompt = soup.find(id=f'finished-dialogue-{i}-{mode}')
                    self.assertIsNotNone(prompt)
                    text = prompt.get_text()
                    self.assertIn(dialogue['setting'], text)
                    for role, speech in dialogue['dialogue']:
                        self.assertIn(f'{role}: {speech}', text)
                    self.assertIn(track['scope_note'], text)
                    count += 1
        self.assertEqual(2960, count)

    def test_downloads_contain_only_four_tasks_for_each_lesson_and_both_dialogue_tasks(self):
        total = 0
        scripts = load_dialogues()
        for track in load_tracks():
            track = web_track(track)
            text = (ROOT / 'prompts/work' / (track['slug'] + '.txt')).read_text()
            for title in ('Get feedback on a draft', 'Adjust tone and register', 'Test recall and transfer', 'Adapt a partner or class activity', 'Choose a clear message'):
                self.assertNotIn(' | ' + title, text)
            blocks = text.split('\nSTART PROMPT\n')[1:]
            self.assertEqual(32 + 2 * len(scripts[track['slug']]), len(blocks))
            self.assertEqual(len(blocks), text.splitlines().count('END PROMPT'))
            for block in blocks:
                self.assertTrue(block.startswith('TASK:'))
                self.assertIn('\nEND REFERENCE\nEND PROMPT', block)
                self.assertIn(track['title'], block)
                self.assertIn(track['scope_note'], block)
                total += 1
        self.assertEqual(3536, total)


if __name__ == '__main__':
    unittest.main()
