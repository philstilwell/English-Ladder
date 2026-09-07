"""Persist unfinished daily editions without trusting saved editorial approval.

The integrity digest detects damaged checkpoint data. It is not authentication:
callers must revalidate lessons and their content-bound approval before reuse.
"""
from datetime import date
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile


SCHEMA_VERSION = 1


def _canonical_json(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(',', ':'), allow_nan=False)


def _integrity_hash(source, levels, drafts):
    contents = {'source': source, 'levels': levels, 'drafts': drafts}
    return hashlib.sha256(_canonical_json(contents).encode('utf-8')).hexdigest()


class CheckpointStore:
    """Atomically save one date's source, approved levels, and unfinished drafts.

    A missing directory disables persistence. A changed policy fingerprint or
    invalid file makes ``load`` return None so the caller starts fresh.
    """

    def __init__(self, directory, release_date, policy_fingerprint):
        if not isinstance(release_date, str) or not re.fullmatch(
                r'\d{4}-\d{2}-\d{2}', release_date):
            raise ValueError('Checkpoint release_date must use YYYY-MM-DD.')
        try:
            date.fromisoformat(release_date)
        except ValueError as error:
            raise ValueError('Checkpoint release_date must be a valid calendar date.') from error
        if not isinstance(policy_fingerprint, str) or not policy_fingerprint.strip():
            raise ValueError('Checkpoint policy_fingerprint must be a nonempty string.')
        self.release_date = release_date
        self.policy_fingerprint = policy_fingerprint
        self.path = Path(directory) / f'{release_date}.json' if directory is not None else None

    def load(self):
        """Return a fresh checkpoint dictionary, or None when it cannot be reused."""
        if self.path is None:
            return None
        try:
            checkpoint = json.loads(self.path.read_text(encoding='utf-8'))
            if not isinstance(checkpoint, dict):
                return None
            if (type(checkpoint.get('schema_version')) is not int
                    or checkpoint['schema_version'] != SCHEMA_VERSION
                    or checkpoint.get('release_date') != self.release_date
                    or checkpoint.get('policy_fingerprint') != self.policy_fingerprint):
                return None
            if not all(isinstance(checkpoint.get(key), dict)
                       for key in ('source', 'levels', 'drafts')):
                return None
            digest = _integrity_hash(checkpoint['source'], checkpoint['levels'], checkpoint['drafts'])
            if checkpoint.get('integrity_hash') != digest:
                return None
            return checkpoint
        except (OSError, ValueError, TypeError, UnicodeError):
            return None

    def save(self, source, levels, drafts=None):
        """Replace the checkpoint only after a complete JSON file is safely written.

        Inputs are not modified. Disk errors propagate to the caller, which can
        report failed persistence while continuing the current generation run.
        """
        if self.path is None:
            return False
        if drafts is None:
            drafts = {}
        if not all(isinstance(section, dict) for section in (source, levels, drafts)):
            raise ValueError('Checkpoint source, levels, and drafts must be objects.')
        checkpoint = {
            'schema_version': SCHEMA_VERSION,
            'release_date': self.release_date,
            'policy_fingerprint': self.policy_fingerprint,
            'source': source,
            'levels': levels,
            'drafts': drafts,
            'integrity_hash': _integrity_hash(source, levels, drafts),
        }
        # Serialize before touching the old file, including rejecting NaN values.
        serialized = _canonical_json(checkpoint) + '\n'
        self.path.parent.mkdir(parents=True, exist_ok=True)
        temporary_path = None
        try:
            with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8',
                                             dir=self.path.parent,
                                             prefix=f'.{self.release_date}.',
                                             suffix='.tmp', delete=False) as temporary:
                temporary_path = Path(temporary.name)
                temporary.write(serialized)
                temporary.flush()
                os.fsync(temporary.fileno())
            os.replace(temporary_path, self.path)
            return True
        finally:
            if temporary_path is not None:
                temporary_path.unlink(missing_ok=True)
