"""Keep verified HTTPS working on Python installations with an empty CA store."""
import ssl
import unittest
from unittest.mock import patch

import certifi
import update_site


class NewsCertificateTests(unittest.TestCase):
    def test_empty_store_gains_trusted_roots_without_disabling_verification(self):
        empty = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        self.assertEqual([], empty.get_ca_certs())
        with patch.object(update_site.ssl, "create_default_context", return_value=empty):
            context = update_site.news_tls_context()
        self.assertIs(context, empty)
        self.assertGreater(len(context.get_ca_certs()), 0)
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
                patch.object(update_site.certifi, "where", return_value="/nonexistent/english-ladder-ca-bundle"):
            with self.assertRaises(FileNotFoundError):
                update_site.news_tls_context()
        self.assertEqual(ssl.CERT_REQUIRED, empty.verify_mode)
        self.assertTrue(empty.check_hostname)


if __name__ == "__main__":
    unittest.main()
