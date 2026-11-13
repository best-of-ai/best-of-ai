#!/usr/bin/env python3
"""Generate content/categories/*.md from data/categories.yaml.

If data/categories_<lang>.yaml exists, also writes content_<lang>/categories/*.md
(translated name and description) with an i18n_source hash of the English page,
which scripts/translation-status.py uses to spot stale translations.
"""

import hashlib
import re
from pathlib import Path

ROOT     = Path(__file__).parent.parent
CATS_FILE = ROOT / "data" / "categories.yaml"
CATS_DIR  = ROOT / "content" / "categories"

# title is the category page title. {name} is the overlay name.
LANG_OVERLAYS = {
    "es": {
        "file": ROOT / "data" / "categories_es.yaml",
        "out": ROOT / "content_es" / "categories",
        "title": "Mejores herramientas de IA: {name}",
    },
    "fr": {
        "file": ROOT / "data" / "categories_fr.yaml",
        "out": ROOT / "content_fr" / "categories",
        "title": "Meilleurs outils d'IA : {name}",
    },
}


def parse_categories_yaml(text):
    cats = []
    current = {}
    for line in text.splitlines():
        if line.strip() == '-':
            if current:
                cats.append(current)
            current = {}
        else:
            kv = re.match(r"^\s+(\w+):\s*'(.*)'$", line)
            if kv:
                current[kv.group(1)] = kv.group(2).replace("''", "'")
                continue
            kv2 = re.match(r'^\s+(\w+):\s*(-?\d+)$', line)
            if kv2:
                current[kv2.group(1)] = int(kv2.group(2))
    if current:
        cats.append(current)
    return cats


def yaml_str(val):
    return "'" + str(val).replace("'", "''") + "'"


def write_md(path, fields):
    lines = ["---"]
    for k, v in fields.items():
        if isinstance(v, int):
            lines.append(f"{k}: {v}")
        else:
            lines.append(f"{k}: {yaml_str(v)}")
    lines.append("---\n")
    path.write_text('\n'.join(lines), encoding='utf-8')


CATS_DIR.mkdir(parents=True, exist_ok=True)
for f in CATS_DIR.glob('*.md'):
    f.unlink()

cats = parse_categories_yaml(CATS_FILE.read_text())
for cat in cats:
    slug = cat.get('slug', '')
    name = cat.get('name', '')
    desc = cat.get('description', '').strip()
    if not slug:
        continue

    fields = {
        'title':       f"Best AI {name} Tools",
        'name':        name,
        'slug':        slug,
        'description': desc or f"The best AI tools for {name.lower()}.",
        'sort_order':  cat.get('sort_order', 0),
    }
    write_md(CATS_DIR / f"{slug}.md", fields)

print(f"Generated {len(cats)} category pages → content/categories/")

by_slug = {c['slug']: c for c in cats if c.get('slug')}
for code, spec in LANG_OVERLAYS.items():
    overlay = spec["file"]
    if not overlay.exists():
        continue
    out_dir = spec["out"]
    out_dir.mkdir(parents=True, exist_ok=True)
    for f in out_dir.glob('*.md'):
        f.unlink()
    count = 0
    for tr in parse_categories_yaml(overlay.read_text()):
        slug = tr.get('slug', '')
        if slug not in by_slug:
            continue
        en = by_slug[slug]
        source = hashlib.sha1((CATS_DIR / f"{slug}.md").read_bytes()).hexdigest()[:12]
        fields = {
            'title':       spec["title"].format(name=tr['name']),
            'name':        tr['name'],
            'slug':        slug,
            'description': tr['description'].strip(),
            'sort_order':  en.get('sort_order', 0),
            'i18n_source': source,
        }
        write_md(out_dir / f"{slug}.md", fields)
        count += 1
    print(f"Generated {count} {code} category pages → {out_dir.relative_to(ROOT)}/")
