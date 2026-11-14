"""Shared rules and helpers for the translation scripts.

content_<lang>/ mirrors content/. A translated file keeps every non-text frontmatter key identical to
its English source and only changes the keys listed in TEXT_KEYS plus (optionally) the body.
"""
import hashlib
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "content"
LANGS = {"es": ROOT / "content_es", "fr": ROOT / "content_fr", "ja": ROOT / "content_ja"}

# Sections that are frontmatter-only stubs with no prose of their own (page titles come from templates).
SKIP_SECTIONS = {"alternatives", "company-pages"}

# Frontmatter keys holding human-readable text, per section. Every other key must match English exactly.
TEXT_KEYS = {
    "tools": {"subtitle", "description", "category_name", "dead_reason"},
    "professionals": {"title", "name", "subtitle", "description"},
    "categories": {"title", "name", "description"},
    "model-categories": {"title", "name", "description"},
    "skill-categories": {"title", "name", "description"},
    "companies": {"subtitle", "description"},
    "hardware": {"subtitle", "description"},
    "models": {"subtitle", "description"},
    "skills": {"subtitle", "description"},
    "help": {"title", "subtitle", "description"},
    "journal": {"title", "subtitle", "description"},
    "leaderboard": {"title", "description", "params"},
    "new-tools": {"title", "description"},
    "": {"title", "description", "keywords"},  # top-level pages (about.md, submit.md, ...) and section _index.md files
}

# Keys whose value may legitimately equal the English text (names, URLs, short labels).
MAY_EQUAL_MIN_LEN = 40


def section_of(rel: Path) -> str:
    """'tools/chatgpt.md' -> 'tools'; 'about.md' -> ''."""
    return rel.parts[0] if len(rel.parts) > 1 else ""


def text_keys(rel: Path) -> set:
    return TEXT_KEYS.get(section_of(rel), {"title", "description", "keywords"})


def split_frontmatter(text: str):
    """Return (raw_frontmatter, body). Raises ValueError when there is no frontmatter block."""
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, flags=re.S)
    if not m:
        raise ValueError("no frontmatter block")
    return m.group(1), m.group(2)


def load(path: Path):
    raw, body = split_frontmatter(path.read_text(encoding="utf-8"))
    data = yaml.safe_load(raw) or {}
    return data, body


def source_hash(path: Path) -> str:
    return hashlib.sha1(path.read_bytes()).hexdigest()[:12]


def english_files():
    """All English files that need a translation, as paths relative to content/."""
    out = []
    for p in sorted(SOURCE.rglob("*.md")):
        rel = p.relative_to(SOURCE)
        if section_of(rel) in SKIP_SECTIONS:
            continue
        out.append(rel)
    return out
