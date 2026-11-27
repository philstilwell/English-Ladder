"""Separate editorial evidence from the public lesson archive."""
import argparse
import json
import os
from pathlib import Path
import tempfile

PRIVATE_KEYS = frozenset({"evidence_text", "sentence_evidence", "evidence_retrieved_at"})


def public_archive(value):
    """Return a non-mutating projection without the private evidence fields."""
    if isinstance(value, dict):
        return {key: public_archive(item) for key, item in value.items() if key not in PRIVATE_KEYS}
    if isinstance(value, list):
        return [public_archive(item) for item in value]
    return value


def require_public_archive(value, name):
    if value != public_archive(value):
        raise ValueError(f"{name}: private editorial evidence in a public lesson archive")


def write_archive_json(path, value, *, private=False):
    """Atomically commit complete JSON; evidence files stay owner-readable."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700 if private else 0o755)
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                     prefix=f".{path.name}.", delete=False) as file:
        temporary = Path(file.name)
        try:
            json.dump(value, file, ensure_ascii=False, indent=2)
            file.write("\n")
            file.close()
            if not private:
                temporary.chmod(0o644)
            os.replace(temporary, path)
        finally:
            temporary.unlink(missing_ok=True)


def clean_archives(directory):
    """Remove only private keys from existing public archives, without rebuilding pages."""
    updates = []
    for path in sorted(Path(directory).glob("*.json")):
        original = json.loads(path.read_text(encoding="utf-8"))
        projected = public_archive(original)
        if original != projected:
            updates.append((path, projected))
    for path, projected in updates:
        write_archive_json(path, projected)
    return len(updates)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--clean-existing", action="store_true", required=True)
    parser.add_argument("--directory", default="archive/lessons")
    args = parser.parse_args()
    print(f"Cleaned {clean_archives(args.directory)} public lesson archives.")
