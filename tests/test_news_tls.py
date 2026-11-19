"""Keep verified HTTPS working on Python installations with an empty CA store."""
import ssl
import unittest
from unittest.mock import patch

import certifi
import update_site


class NewsCertificateTests(unittest.TestCase):
    def test_empty_store_gains_trusted_roots_without_disabling_verification(self):
        empty = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        # Some runtimes preload certificates into a fresh context. Simulate
        # only the empty-store check; keep certificate loading and the security
        # settings real so this test also exercises the fallback on those runtimes.
        with patch.object(update_site.ssl, "create_default_context", return_value=empty), \
                patch.object(empty, "get_ca_certs", return_value=[]), \
                patch.object(empty, "load_verify_locations", wraps=empty.load_verify_locations) as load:
            context = update_site.news_tls_context()
        load.assert_called_once_with(cafile=certifi.where())
        self.assertIs(context, empty)
        expected = ssl.create_default_context(cafile=certifi.where())
        roots = set(context.get_ca_certs(binary_form=True))
        self.assertTrue(roots)
        self.assertTrue(set(expected.get_ca_certs(binary_form=True)).issubset(roots))
        self.assertEqual(ssl.CERT_REQUIRED, context.verify_mode)
        self.assertTrue(context.check_hostname)

    def test_existing_trust_store_is_preserved(self):
        configured = ssl.create_default_context(cafile=certifi.where())
        roots = configured.get_ca_certs(binary_form=True)
        with patch.object(update_site.ssl, "create_default_context", return_value=configured), \
                patch.object(update_site.certifi, "where", side_effect=AssertionError("Must preserve existing roots")):
            context = update_site.news_tls_context()
        self.assertIs(context, configured)
        self.assertEqual(roots, context.get_ca_certs(binary_form=True))
        self.assertEqual(ssl.CERT_REQUIRED, context.verify_mode)
        self.assertTrue(context.check_hostname)

    def test_missing_fallback_bundle_fails_closed(self):
        empty = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        with patch.object(update_site.ssl, "create_default_context", return_value=empty), \
                patch.object(empty, "get_ca_certs", return_value=[]), \
                patch.object(update_site.certifi, "where", return_value="/nonexistent/english-ladder-ca-bundle"):
            with self.assertRaises(FileNotFoundError):
                update_site.news_tls_context()
        self.assertEqual(ssl.CERT_REQUIRED, empty.verify_mode)
        self.assertTrue(empty.check_hostname)


if __name__ == "__main__":
    unittest.main()
