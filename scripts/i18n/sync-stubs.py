#!/usr/bin/env python3
"""Create the content_<lang>/ copies of frontmatter-only stub pages that set an explicit `url:`.

Hugo does not add the /<lang>/ prefix to a `url:` front-matter value, so a shared stub would make every
language write to the same path. The generated copy keeps the stub as is and prefixes `url` with the
language. Run it after anything that regenerates content/company-pages/ (generate-companies.py).

usage: sync-stubs.py [--lang es]
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import rules  # noqa: E402

SECTIONS = ["company-pages"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", default="es")
    a = ap.parse_args()
    root = rules.LANGS[a.lang]
    n = 0
    for sec in SECTIONS:
        out_dir = root / sec
        out_dir.mkdir(parents=True, exist_ok=True)
        keep = set()
        for src in sorted((rules.SOURCE / sec).glob("*.md")):
            text = src.read_text(encoding="utf-8")
            if not re.search(r"^url:\s*'?/", text, flags=re.M):
                continue
            text = re.sub(r"^(url:\s*'?)(/)", rf"\g<1>/{a.lang}\g<2>", text, flags=re.M)
            (out_dir / src.name).write_text(text, encoding="utf-8")
            keep.add(src.name)
            n += 1
        for old in out_dir.glob("*.md"):
            if old.name not in keep:
                old.unlink()
    print(f"synced {n} stub pages into content_{a.lang}/")


if __name__ == "__main__":
    main()
