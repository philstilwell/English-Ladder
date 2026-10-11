"""Exact identifier indexes must preserve every audit behavior they replace."""
import contextlib
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from bs4 import BeautifulSoup

import audit_site
from html_identifiers import find_identifier, index_identifiers


class HtmlIdentifierTests(unittest.TestCase):
    def test_index_preserves_first_match_tag_and_copy_prompt_text(self):
        soup = BeautifulSoup(
            '<p id="copy-prompt">Keep this prompt</p>'
            '<p id="copy-prompt">Later duplicate</p>',
            'html.parser',
        )

        identifiers, duplicate = index_identifiers(soup)
        prompt = find_identifier(identifiers, 'copy-prompt')

        self.assertTrue(duplicate)
        self.assertIs(prompt, soup.find(id='copy-prompt'))
        self.assertEqual('Keep this prompt', prompt.get_text(strip=True))

    def test_unique_identifiers_do_not_report_a_duplicate(self):
        soup = BeautifulSoup('<p id="one"></p><p id="two"></p>', 'html.parser')

        identifiers, duplicate = index_identifiers(soup)

        self.assertFalse(duplicate)
        self.assertEqual({'one', 'two'}, set(identifiers))

    def test_fragment_lookup_decodes_url_encoding_and_rejects_missing_ids(self):
        soup = BeautifulSoup('<section id="practice notes"></section>', 'html.parser')
        identifiers, _ = index_identifiers(soup)

        self.assertIsNotNone(find_identifier(identifiers, 'practice%20notes', encoded=True))
        self.assertIsNone(find_identifier(identifiers, 'missing', encoded=True))


class SiteAuditIdentifierTests(unittest.TestCase):
    def run_audit(self, *, fragment='target', prompt='Copy this prompt', extra=''):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            page = root / 'index.html'
            page.write_text(
                '<!doctype html><html><head>'
                '<meta name="description" content="Test description">'
                '<link rel="canonical" href="https://example.com/">'
                '</head><body>'
                '<a class="skip-link" href="#main">Skip</a>'
                '<main id="main"><h1>Test</h1>'
                f'<a href="#{fragment}">Fragment</a>'
                '<section id="target">Target</section>'
                f'<p id="copy-prompt">{prompt}</p>'
                '<button data-ai-copy-text="copy-prompt">Copy</button>'
                f'{extra}</main></body></html>'
            )
            with patch.object(audit_site, 'ROOT', root), \
                    patch('seo.published_pages', return_value=[page]), \
                    patch('grammar_curriculum.load_curriculum'), \
                    patch('audit_seo.audit'), \
                    contextlib.redirect_stdout(io.StringIO()):
                return audit_site.audit()

    def test_audit_accepts_present_plain_and_encoded_fragments(self):
        self.assertEqual(1, self.run_audit())
        self.assertEqual(1, self.run_audit(fragment='%74arget'))

    def test_audit_rejects_missing_fragment(self):
        with self.assertRaisesRegex(AssertionError, 'missing fragment #missing'):
            self.run_audit(fragment='missing')

    def test_audit_rejects_duplicate_identifiers(self):
        with self.assertRaisesRegex(AssertionError, 'duplicate page identifier'):
            self.run_audit(extra='<div id="target"></div>')

    def test_audit_rejects_empty_copy_prompt_text(self):
        with self.assertRaisesRegex(AssertionError, 'copy button has no prompt text'):
            self.run_audit(prompt='')


if __name__ == '__main__':
    unittest.main()
