#!/usr/bin/env python3
"""Generate content/company-pages/*.md: one stub per company per list that has items.

Run scripts/i18n/sync-stubs.py afterwards: each stub sets an explicit `url:`, and Hugo adds no language
prefix to that, so the Spanish copies in content_es/company-pages/ are generated from these.

Each stub renders at /companies/<slug>/{tools,models,hardware}/ and holds the full
list the company page only previews. Deletes and recreates the directory, so run it
after adding tools, models or hardware for a company.
"""

import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).parent.parent
CONTENT = ROOT / "content"
OUT = CONTENT / "company-pages"

# kind -> (content dir, frontmatter field naming the company)
KINDS = {
    "tools": ("tools", "company"),
    "models": ("models", "company"),
    "hardware": ("hardware", "manufacturer"),
}


def field(text, key):
    m = re.search(rf"^{key}:\s*['\"]?([^'\"\n]*)['\"]?\s*$", text, re.M)
    return m.group(1).strip() if m else ""


def main():
    companies = {}
    for f in (CONTENT / "companies").glob("*.md"):
        text = f.read_text()
        companies[field(text, "slug") or f.stem] = field(text, "name") or f.stem

    counts = {k: Counter() for k in KINDS}
    for kind, (folder, key) in KINDS.items():
        for f in (CONTENT / folder).glob("*.md"):
            slug = field(f.read_text(), key)
            if slug in companies:
                counts[kind][slug] += 1

    OUT.mkdir(exist_ok=True)
    for old in OUT.glob("*.md"):
        old.unlink()

    total = 0
    for kind in KINDS:
        for slug, n in counts[kind].items():
            name = companies[slug].replace("'", "''")
            (OUT / f"{slug}-{kind}.md").write_text(
                "---\n"
                f"title: '{name} {kind}'\n"
                f"name: '{name}'\n"
                f"company: '{slug}'\n"
                f"list_kind: '{kind}'\n"
                f"url: '/companies/{slug}/{kind}/'\n"
                "---\n"
            )
            total += 1
    print(f"Wrote {total} pages to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
