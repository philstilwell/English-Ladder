import copy
import json
import tempfile
import unittest
from pathlib import Path
from bs4 import BeautifulSoup

import us_life_translations as translations
from vocabulary_translations import atomic_json, source_key


class EverydayTranslationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)
        self.source = translations.sources()['arrival']
        samples = {'ja': '必要なときに説明を頼みましょう。', 'ko': '필요할 때 설명을 요청하세요.',
                   'zh-Hans': '需要时请对方解释。', 'es': 'Pide una explicación cuando la necesites.',
                   'pt-BR': 'Peça uma explicação quando precisar.'}
        self.values = {lang: {'heading': text, 'points': [text] * 3} for lang, text in samples.items()}

    def test_all_existing_sidebars_have_complete_source_and_unchanged_english_practice(self):
        sources = translations.sources()
        self.assertEqual(24, len(sources))
        for key, source in sources.items():
            self.assertEqual(key, source['unit'])
            self.assertGreater(len(source['english_context']), 400)
            self.assertEqual(3, len(source['japanese_explanation']['points']))
            self.assertEqual(source['japanese_explanation']['practice'], source['existing_simplified_chinese']['practice'])

    def test_rejects_missing_points_languages_empty_text_and_markup(self):
        bad = []
        item = copy.deepcopy(self.values); item.pop('ko'); bad.append(item)
        item = copy.deepcopy(self.values); item['ja']['points'].pop(); bad.append(item)
        item = copy.deepcopy(self.values); item['es']['heading'] = ''; bad.append(item)
        item = copy.deepcopy(self.values); item['pt-BR']['points'][0] = '<script>bad</script>'; bad.append(item)
        item = copy.deepcopy(self.values); item['ko']['points'][0] = 'Wrong language.'; bad.append(item)
        item = copy.deepcopy(self.values); item['zh-Hans']['heading'] = '日本語です'; bad.append(item)
        for values in bad:
            with self.assertRaises(ValueError): translations.validate(values, self.source)

    def test_cache_requires_current_context_and_separate_review(self):
        path = self.directory / (source_key(self.source) + '.json')
        record = {'source': self.source, 'translations': self.values, 'review': {'status': 'draft'}}
        atomic_json(path, record)
        self.assertIsNone(translations.read_record(self.source, self.directory))
        record['review']['status'] = 'reviewed'; atomic_json(path, record)
        self.assertIsNotNone(translations.read_record(self.source, self.directory))
        changed = copy.deepcopy(self.source); changed['english_context'] += ' A changed lesson.'
        self.assertIsNone(translations.read_record(changed, self.directory))
        changed = copy.deepcopy(self.source); changed['japanese_explanation']['points'][0] += '更新。'
        self.assertIsNone(translations.read_record(changed, self.directory))
        path.write_text('{bad JSON')
        self.assertIsNone(translations.read_record(self.source, self.directory))

    def test_failed_review_resumes_from_saved_draft_and_completed_work_is_free(self):
        values = self.values
        class Budget:
            def __init__(self, fail=False): self.prompts = []; self.fail = fail
            def request(self, client, prompt, schema, thinking):
                self.prompts.append(prompt)
                if self.fail and 'INDEPENDENT REVIEW:' in prompt: raise ValueError('Temporary problem')
                return {'translations': values}
        failed = Budget(True)
        with self.assertRaises(RuntimeError): translations.translate(None, self.source, failed, self.directory)
        self.assertEqual(1, sum('INDEPENDENT REVIEW:' not in p for p in failed.prompts))
        self.assertIsNone(translations.read_record(self.source, self.directory))
        recovery = Budget()
        self.assertEqual('translated', translations.translate(None, self.source, recovery, self.directory))
        self.assertEqual(1, len(recovery.prompts))
        self.assertIn('INDEPENDENT REVIEW:', recovery.prompts[0])
        self.assertEqual('cached', translations.translate(None, self.source, recovery, self.directory))
        self.assertEqual(1, len(recovery.prompts))
        self.assertEqual('gemini-2.5-flash', translations.read_record(self.source, self.directory)['review']['model'])

    def test_published_page_embeds_all_reviewed_languages_without_changing_english_content(self):
        from us_life_language_ui import enhance_page
        soup = BeautifulSoup((translations.ROOT / 'us-life.html').read_text(), 'html.parser')
        original = [str(n) for n in soup.select('.us-life-main')]
        enhance_page(soup)
        payload = json.loads(soup.select_one('[data-us-life-translations]').string)
        self.assertEqual(24, len(payload))
        for key, source in translations.sources(soup).items():
            record = translations.read_record(source)
            self.assertIsNotNone(record, key)
            self.assertEqual(record['translations'], payload[key]['translations'])
            self.assertEqual(source['japanese_explanation']['practice'], payload[key]['practice'])
        self.assertEqual(original, [str(n) for n in soup.select('.us-life-main')])
        self.assertEqual(6, len(soup.select('[data-definition-language]')))
        self.assertIsNone(soup.select_one('#life-language-select'))

    def test_rebuilding_keeps_one_selector_one_payload_and_the_same_translation_sources(self):
        from us_life_language_ui import enhance_page
        soup = BeautifulSoup((translations.ROOT / 'us-life.html').read_text(), 'html.parser')
        before = translations.sources(soup)
        enhance_page(soup)
        first = str(soup)
        enhance_page(soup)
        self.assertEqual(first, str(soup))
        self.assertEqual(before, translations.sources(soup))
        self.assertEqual(1, len(soup.select('[data-us-life-translations]')))
        self.assertEqual(1, len(soup.select('#life-language-controls')))


if __name__ == '__main__':
    unittest.main()
