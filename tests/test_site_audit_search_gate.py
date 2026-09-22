"""The combined gate must still reject search defects without a second CLI audit."""
import contextlib
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import audit_site


class SiteAuditSearchGateTests(unittest.TestCase):
    def run_gate(self, search_error=None):
        with tempfile.TemporaryDirectory() as directory, \
             patch.object(audit_site, 'ROOT', Path(directory)), \
             patch('seo.published_pages', return_value=[]), \
             patch('grammar_curriculum.load_curriculum'), \
             patch('audit_seo.audit', side_effect=search_error) as search, \
             contextlib.redirect_stdout(io.StringIO()):
            if search_error:
                with self.assertRaisesRegex(AssertionError, 'Broken search metadata'):
                    audit_site.audit()
            else:
                self.assertEqual(0, audit_site.audit())
            search.assert_called_once_with()

    def test_combined_site_gate_always_runs_search_audit_once(self):
        self.run_gate()

    def test_search_failure_fails_the_combined_gate(self):
        self.run_gate(AssertionError('Broken search metadata'))


if __name__ == '__main__':
    unittest.main()
