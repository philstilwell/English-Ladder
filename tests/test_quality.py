import copy
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import news_quality
import update_site
import publish_snapshot

ROOT=Path(__file__).resolve().parents[1]
class QualityTests(unittest.TestCase):
    def setUp(self):
        self.data=json.loads((ROOT/'archive/lessons/2026-09-06.json').read_text())
        self.lesson=copy.deepcopy(self.data['levels']['beginner']['lesson'])
        self.source=self.data['source']
    def test_current_reviewed_news_has_valid_evidence_and_structure(self):
        for path in sorted((ROOT/'archive/lessons').glob('*.json'))[-7:]:
            data=json.loads(path.read_text())
            for config in update_site.LEVELS:
                lesson=data['levels'][config['name'].lower()]['lesson']
                self.assertEqual([],update_site.validate_lesson_data(lesson,config))
                self.assertEqual([],news_quality.validate_evidence(lesson,data['source']))
    def test_new_quantity_and_fabricated_evidence_are_rejected(self):
        self.lesson['news_brief_sentences'][0]='Exactly 8472 planes changed routes.'
        self.assertTrue(any('8472' in issue for issue in news_quality.validate_evidence(self.lesson,self.source)))
        self.lesson['sentence_evidence'][0]='An invented quotation that is not in the source.'
        self.assertTrue(any('exact source excerpt' in issue for issue in news_quality.validate_evidence(self.lesson,self.source)))
    def test_a_pass_flag_with_issues_still_fails_review(self):
        client=SimpleNamespace(models=SimpleNamespace(generate_content=lambda **kw:SimpleNamespace(text=json.dumps({'approved':True,'issues':['This adds an unsupported cause.']}))))
        self.assertEqual(['This adds an unsupported cause.'],news_quality.review_lesson(client,self.source,self.lesson,update_site.LEVELS[0],'fake'))
    def test_generation_requires_separate_editorial_approval(self):
        calls=[]
        def generate(**kwargs):
            calls.append(kwargs)
            return SimpleNamespace(text=json.dumps(self.lesson if len(calls)==1 else {'approved':False,'issues':['Unsupported cause in the reading.']}))
        client=SimpleNamespace(models=SimpleNamespace(generate_content=generate))
        with patch.object(update_site,'MAX_GENERATION_ATTEMPTS',1):
            with self.assertRaisesRegex(RuntimeError,'Unsupported cause'):
                update_site.generate_lesson(client,self.source,update_site.LEVELS[0],update_site.release_datetime_from_date('2026-09-06'))
        self.assertEqual(2,len(calls))
        self.assertIn('Review an English lesson for publication',calls[1]['contents'])
    def test_short_evidence_does_not_require_ten_sentences(self):
        self.assertEqual(4,len(self.lesson['news_brief_sentences']))
        self.assertEqual([],update_site.validate_lesson_data(self.lesson,update_site.LEVELS[0]))
        self.lesson['news_brief_sentences']=self.lesson['news_brief_sentences'][:2]
        self.assertTrue(update_site.validate_lesson_data(self.lesson,update_site.LEVELS[0]))
    def test_newly_generated_lessons_retain_source_topic_notices(self):
        calls=[]
        def generate(**kwargs):
            calls.append(kwargs)
            return SimpleNamespace(text=json.dumps(self.lesson if len(calls)==1 else {'approved':True,'issues':[]}))
        source=dict(self.source,summary=self.source['summary']+' A separate report concerns deaths.')
        client=SimpleNamespace(models=SimpleNamespace(generate_content=generate))
        _,rendered=update_site.generate_lesson(client,source,update_site.LEVELS[0],update_site.release_datetime_from_date('2026-09-06'))
        self.assertIn('This report includes distressing events',rendered)
    def test_snapshot_refuses_to_overwrite_concurrent_source_change(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)/'repo';snap=Path(directory)/'snapshot';root.mkdir();snap.mkdir()
            name='archive/lessons/2030-01-01.json';current=root/name;current.parent.mkdir(parents=True);current.write_bytes(b'new editorial correction')
            incoming=snap/name;incoming.parent.mkdir(parents=True);incoming.write_bytes(b'automatic draft')
            (snap/'manifest.json').write_text(json.dumps([{'path':name,'baseline':publish_snapshot.digest(b'old version'),'incoming':publish_snapshot.digest(b'automatic draft')}]))
            with patch.object(publish_snapshot,'ROOT',root):
                with self.assertRaisesRegex(RuntimeError,'Concurrent source edit'):publish_snapshot.restore(snap)
            self.assertEqual(b'new editorial correction',current.read_bytes())
    def test_snapshot_will_not_restore_html(self):
        self.assertFalse(publish_snapshot.allowed('beginner.html'))
        self.assertFalse(publish_snapshot.allowed('archive/lessons/../../tools.js'))
        self.assertTrue(publish_snapshot.allowed('archive/lessons/2030-01-01.json'))
