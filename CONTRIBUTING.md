# Contributing to Awesome Best of AI

Thanks for helping make this the best curated AI tools list. This guide explains how to add tools, fix data, and run the project locally.

---

## Ways to contribute

| What | How |
|---|---|
| Add a tool | [Open an issue](https://github.com/best-of-ai/best-of-ai/issues/new?template=submit-tool.md) or submit a PR (see below) |
| Fix tool info | Edit `content/tools/{slug}.md` and open a PR |
| Add a category | Edit `data/categories.yaml` and open a PR |
| Report a bug | [Open an issue](https://github.com/best-of-ai/best-of-ai/issues/new) |
| Fix or add a translation | Edit or add the file under `content_es/` and open a PR (see "Translations") |

---

## Adding a tool via PR

Each tool is a Markdown file in `content/tools/`. Write it in English only; we translate it into the other languages. Create a new file named after the tool's slug:

```
content/tools/my-tool.md
```

With this front matter:

```yaml
---
title: 'My Tool'
name: 'My Tool'
slug: 'my-tool'
description: 'One or two sentences describing what the tool does.'
website: 'https://mytool.com'
logo_url: ''
category: 'productivity'
category_name: 'Productivity'
price: 'Freemium'
featured: false
date: '2025-01-01'
---
```

### Field reference

| Field | Required | Notes |
|---|---|---|
| `name` | ✅ | Display name of the tool |
| `slug` | ✅ | URL-safe, lowercase, hyphens — must match filename |
| `description` | ✅ | 1–2 sentences, factual, no marketing fluff |
| `website` | ✅ | Full URL including `https://` |
| `category` | ✅ | Slug of an existing category in `data/categories.yaml` |
| `category_name` | ✅ | Human-readable category name (must match) |
| `price` | ✅ | One of: `Free`, `Freemium`, `Paid` |
| `logo_url` | — | Direct URL to a square logo image |
| `featured` | — | `true` for highlighted tools (default `false`) |
| `date` | — | Date added, `YYYY-MM-DD` |

### Guidelines

- **Quality over quantity** — the goal is a curated list, not a complete directory. Tools should be genuinely useful and notable.
- **No self-promotion** — don't submit your own tool unless it's already well-known in the community.
- **Accurate pricing** — use `Freemium` when there's a meaningful free tier, `Paid` when there's no free usage.
- **Neutral descriptions** — describe what the tool does, not how great it is.
- **One tool per PR** — keeps review fast and history clean.

---

## Adding a category

Categories are defined in `data/categories.yaml`. Each entry looks like:

```yaml
-
  id: 99
  name: 'My Category'
  description: 'Short description of what belongs here.'
  slug: 'my-category'
  sort_order: 0
```

- Use `sort_order: 1–20` for top-level categories that should appear first.
- Use `sort_order: 0` for everything else (sorted alphabetically).

---

## Running locally

**Prerequisites:** [Hugo](https://gohugo.io/installation/) and Python 3.

```bash
# Clone the repo
git clone https://github.com/best-of-ai/best-of-ai.git
cd best-of-ai

# Preview the website
hugo server
# → open http://localhost:1313/

# Regenerate README.md and README_ES.md from content files
python3 scripts/generate-readme.py
```

If you have a fresh SQL export to import:

```bash
python3 scripts/import-data.py
```

---

## How README auto-update works

On every push to `main` that touches `content/tools/`, `content_es/tools/`, `content_fr/tools/`, `content_ja/tools/`, `data/categories.yaml`, or `scripts/generate-readme.py`, the [Update README](.github/workflows/update-readme.yml) workflow runs `generate-readme.py` and commits the updated `README.md` and `README_<LANG>.md` files back automatically. Each README links to the others. The Spanish one links to `/es/` pages, the French one to `/fr/` pages, and the Japanese one to `/ja/` pages. To add a language, see the `LANGS` and `STRINGS` blocks in `scripts/generate-readme.py`.

---

## Code of Conduct

Be respectful. Submissions and reviews should be about the tools and the data, not the people.

---

## Translations

**You only need to add or change things in English.** Open your PR with the English files in `content/` (and English strings in `i18n/en.yaml`); the maintainers translate it into the other languages and keep those versions in sync. Please don't add or edit `content_es/` or other language files in a regular contribution, unless you are specifically fixing a translation.

The site is available in English (`/`), Spanish (`/es/`), French (`/fr/`), and Japanese (`/ja/`). English files live in `content/`. Spanish files live in `content_es/`, French files in `content_fr/`, and Japanese files in `content_ja/`, with the same path and filename. If a translation is missing, that language's page shows the English text and is hidden from search engines until someone translates it.

To translate or fix a page (optional, for translation contributors):

1. Read the style guide: `scripts/i18n/glossary-es.md` or `scripts/i18n/glossary-fr.md`.
2. Copy `content/<section>/<name>.md` to `content_es/<section>/<name>.md`, `content_fr/<section>/<name>.md`, or `content_ja/<section>/<name>.md`. Translate the text fields and the body. Leave slugs, URLs, tags, prices, ranks, dates and tool lists exactly as they are.
3. Run `python3 scripts/validate-translation.py --stamp --lang es content_es/<section>/<name>.md` (or `--lang fr` / `--lang ja` and the matching `content_<lang>` path). Fix anything it reports.
4. Open a PR.

Changing an English file makes its Spanish, French, and Japanese copies stale. `python3 scripts/translation-status.py` lists what is missing or stale. UI text (menus, buttons, labels) is in `i18n/en.yaml`, `i18n/es.yaml`, `i18n/fr.yaml`, and `i18n/ja.yaml`; keep them in sync (`python3 scripts/check-i18n.py`).
