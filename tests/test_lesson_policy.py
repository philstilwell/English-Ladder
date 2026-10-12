"""Protect checkpoint invalidation for every lesson-generation policy module."""
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import lesson_run


class LessonPolicyFingerprintTests(unittest.TestCase):
    def test_shared_model_policy_change_invalidates_saved_generation_state(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in lesson_run.GENERATION_POLICY_FILES:
                (root / name).write_text(f"unchanged fixture for {name}\n")

            with patch.object(lesson_run, 'ROOT', root):
                before = lesson_run.generation_policy_fingerprint()
                (root / 'lesson_model.py').write_text(
                    'MODEL_NAME = "a-future-model-change"\n')
                after = lesson_run.generation_policy_fingerprint()

        self.assertNotEqual(before, after)


if __name__ == '__main__':
    unittest.main()
