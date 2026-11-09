#!/usr/bin/env python3
"""
Generate README.md (English) and README_<LANG>.md (one per translated language)
from the Hugo content files. Each README links to the others, and its website
links point at the matching /<lang>/ pages.

Usage:
    python3 scripts/generate-readme.py
"""

import re
from pathlib import Path
from collections import defaultdict

ROOT       = Path(__file__).parent.parent
TOOLS_DIR  = ROOT / "content" / "tools"
PROFS_DIR  = ROOT / "content" / "professionals"
CATS_FILE  = ROOT / "data" / "categories.yaml"
LB_FILE    = ROOT / "data" / "leaderboard.yaml"

REPO_URL   = "https://github.com/best-of-ai/best-of-ai"
SITE_URL   = "https://bestofai.io"


# ── Parsers ───────────────────────────────────────────────────────────────────

def parse_frontmatter(text):
    """Extract key: 'value' pairs from YAML frontmatter."""
    m = re.match(r'^---\n(.*?)\n---', text, re.DOTALL)
    if not m:
        return {}
    block = m.group(1)
    result = {}
    for line in block.splitlines():
        kv = re.match(r"^(\w+):\s*'(.*)'$", line)
        if kv:
            result[kv.group(1)] = kv.group(2).replace("''", "'")
            continue
        kv2 = re.match(r'^(\w+):\s*(true|false|-?\d+)$', line)
        if kv2:
            v = kv2.group(2)
            result[kv2.group(1)] = True if v == 'true' else (False if v == 'false' else int(v))
    return result


def parse_categories_yaml(text):
    """Parse the flat YAML list into a list of dicts."""
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


def parse_leaderboard_yaml(text):
    """Parse leaderboard.yaml into a list of {rank, slug, badge} dicts."""
    entries = []
    current = {}
    for line in text.splitlines():
        if line.startswith('- '):
            if current:
                entries.append(current)
            current = {}
            kv = re.match(r'^-\s+(\w+):\s*(.+)$', line)
            if kv:
                key, val = kv.group(1), kv.group(2).strip().strip('"')
                current[key] = int(val) if val.lstrip('-').isdigit() else val
        elif line.strip():
            kv = re.match(r'^\s+(\w+):\s*(.+)$', line)
            if kv:
                key, val = kv.group(1), kv.group(2).strip().strip('"')
                current[key] = int(val) if val.lstrip('-').isdigit() else val
    if current:
        entries.append(current)
    return entries


# ── Languages ─────────────────────────────────────────────────────────────────
# To add a language: add an entry here, a STRINGS block below, and (optionally) a
# data/badges_<code>.yaml overlay. The code must match the Hugo language code.

LANGS = [
    {'code': 'en', 'label': 'English', 'out': 'README.md',    'content': ROOT / 'content',    'prefix': '',    'cats': None},
    {'code': 'es', 'label': 'Español', 'out': 'README_ES.md', 'content': ROOT / 'content_es', 'prefix': '/es', 'cats': ROOT / 'data' / 'categories_es.yaml'},
]

STRINGS = {
    'en': {
        'tagline': 'Handpicked AI tools — no fluff, no mediocre apps. Every tool carefully selected for quality, innovation, and real-world impact.',
        'website': 'Website', 'submit': 'Submit a Tool', 'contributing': 'Contributing',
        'what_h': 'What is this?',
        'what_p': '**Best of AI** is a curated, community-driven directory of the best AI tools across {cats} categories. We track {tools}+ tools and hand-pick the ones worth your time — filtering out the noise so you can find tools that actually deliver.',
        'different': 'What makes this list different:',
        'b_quality': '**Quality over quantity** — every tool is reviewed and ranked, not just scraped from a list',
        'b_practical': '**Practical focus** — tools are selected for real-world usefulness, not hype',
        'b_coverage': '**Broad coverage** — {cats} categories from [Code Assistants]({code}) to [Video]({video}) to [Healthcare]({health})',
        'b_updated': '**Always updated** — new tools added regularly as the AI landscape evolves',
        'b_prof': '**Browse by profession** — curated tool stacks for [designers, developers, marketers, and more]({url})',
        'visit': 'Visit **[bestofai.io]({url})** for the full interactive directory with search, filters, and detailed reviews.',
        'contents': 'Contents', 'leaderboard': 'Leaderboard', 'categories': 'Categories', 'professionals': 'AI for Professionals',
        'lb_note': 'The top-ranked AI tools by quality, innovation, and real-world impact.',
        'prof_note': 'Curated AI tool collections tailored for specific roles and industries.',
        'review': 'review',
        'view_all': '*[View all {n} {name} tools on bestofai.io →]({url})*',
        'contrib_p': 'See [CONTRIBUTING.md](CONTRIBUTING.md) to add or update tools.',
        'issue_p': 'Found a bug or want to suggest something? [Open an issue]({url}).',
        'license_h': 'License', 'license_p': 'MIT — see [LICENSE](LICENSE).',
        'auto': 'This file is auto-generated from [`{src}`]({src}). Edit the source files, not this file directly.',
        'price': {'Free': 'Free', 'Freemium': 'Freemium', 'Paid': 'Paid'},
        'cat_url': '{site}/categories/code-assistant/',
    },
    'es': {
        'tagline': 'Herramientas de IA elegidas a mano, sin relleno ni apps mediocres. Cada una está seleccionada por su calidad, su innovación y su impacto real.',
        'website': 'Sitio web', 'submit': 'Enviar una herramienta', 'contributing': 'Contribuir',
        'what_h': '¿Qué es esto?',
        'what_p': '**Best of AI** es un directorio curado y hecho por la comunidad con las mejores herramientas de IA en {cats} categorías. Seguimos más de {tools} herramientas y elegimos a mano las que merecen tu tiempo, para que encuentres las que de verdad funcionan.',
        'different': 'Qué hace distinta a esta lista:',
        'b_quality': '**Calidad antes que cantidad**: cada herramienta se revisa y se puntúa, no se copia de otra lista',
        'b_practical': '**Enfoque práctico**: se eligen por su utilidad real, no por el bombo',
        'b_coverage': '**Amplia cobertura**: {cats} categorías, desde [asistentes de código]({code}) hasta [vídeo]({video}) y [salud]({health})',
        'b_updated': '**Siempre al día**: se añaden herramientas nuevas a medida que cambia el panorama de la IA',
        'b_prof': '**Explora por profesión**: selecciones de herramientas para [diseñadores, desarrolladores, profesionales del marketing y más]({url})',
        'visit': 'Visita **[bestofai.io]({url})** para ver el directorio interactivo completo, con búsqueda, filtros y reseñas detalladas.',
        'contents': 'Contenido', 'leaderboard': 'Ranking', 'categories': 'Categorías', 'professionals': 'IA para profesionales',
        'lb_note': 'Las herramientas de IA mejor valoradas por calidad, innovación e impacto real.',
        'prof_note': 'Colecciones de herramientas de IA pensadas para cada profesión y sector.',
        'review': 'reseña',
        'view_all': '*[Ver las {n} herramientas de {name} en bestofai.io →]({url})*',
        'contrib_p': 'Consulta [CONTRIBUTING.md](CONTRIBUTING.md) para añadir o actualizar herramientas.',
        'issue_p': '¿Has encontrado un error o quieres proponer algo? [Abre un issue]({url}).',
        'license_h': 'Licencia', 'license_p': 'MIT — consulta [LICENSE](LICENSE).',
        'auto': 'Este archivo se genera automáticamente a partir de [`{src}`]({src}). Edita los archivos fuente, no este.',
        'price': {'Free': 'Gratis', 'Freemium': 'Freemium', 'Paid': 'De pago'},
    },
}

PRICE_COLOR = {'Free': '3fb950', 'Freemium': 'd29922', 'Paid': '8b949e'}


def price_badge(price, labels):
    if price not in PRICE_COLOR:
        return f'`{price}`'
    label = labels.get(price, price)
    return f'![{label}](https://img.shields.io/badge/-{label.replace(" ", "_")}-{PRICE_COLOR[price]}?style=flat-square)'


def gh_anchor(text):
    """GitHub heading anchor: lowercase, drop punctuation, spaces to hyphens."""
    t = re.sub(r'[^\w\s-]', '', text.lower(), flags=re.UNICODE)
    return re.sub(r'\s', '-', t.strip())


def parse_badges_overlay(path):
    out = {}
    if not path.exists():
        return out
    for line in path.read_text().splitlines():
        m = re.match(r'^"(.*)":\s*"(.*)"\s*$', line)
        if m:
            out[m.group(1)] = m.group(2)
    return out


# ── Build ─────────────────────────────────────────────────────────────────────

def build(lang):
    code, S = lang['code'], STRINGS[lang['code']]
    content = lang['content']
    site = SITE_URL + lang['prefix']
    home = site if not lang['prefix'] else site + '/'
    submit = (f'{REPO_URL}/issues/new?template=submit-tool.md&title=Submit+Tool%3A+'
              if not lang['prefix'] else f'{site}/submit/')

    categories = parse_categories_yaml(CATS_FILE.read_text())
    if lang['cats'] and lang['cats'].exists():
        overlay = {c['slug']: c for c in parse_categories_yaml(lang['cats'].read_text())}
        for c in categories:
            o = overlay.get(c['slug'])
            if o:
                c['name'] = o.get('name', c['name'])
                c['description'] = o.get('description', c.get('description', ''))
    categories.sort(key=lambda c: (0 if c.get('sort_order', 0) > 0 else 1, c.get('sort_order', 99), c.get('name', '')))

    tools_by_cat, tools_by_slug = defaultdict(list), {}
    for f in sorted((content / 'tools').glob('*.md')):
        tool = parse_frontmatter(f.read_text())
        if tool.get('category'):
            tools_by_cat[tool['category']].append(tool)
        if tool.get('slug'):
            tools_by_slug[tool['slug']] = tool
    for slug in tools_by_cat:
        tools_by_cat[slug].sort(key=lambda t: t.get('name', '').lower())

    total_tools = sum(len(v) for v in tools_by_cat.values())
    active_cats = [c for c in categories if tools_by_cat.get(c['slug'])]
    leaderboard = parse_leaderboard_yaml(LB_FILE.read_text())
    badges = parse_badges_overlay(ROOT / 'data' / f'badges_{code}.yaml')

    professions = []
    for f in sorted((content / 'professionals').glob('*.md')):
        if f.name == '_index.md':
            continue
        prof = parse_frontmatter(f.read_text())
        if prof.get('slug'):
            professions.append(prof)
    professions.sort(key=lambda p: (p.get('sort_order', 999) or 999, p.get('name', '')))

    def pb(price):
        return price_badge(price, S['price'])

    switch = ' &nbsp;·&nbsp; '.join(
        f"**{l['label']}**" if l['code'] == code else f"[{l['label']}]({l['out']})" for l in LANGS)

    lines = [
        '<div align="center">', '',
        f'🌐 {switch}', '',
        '# Awesome Best of AI', '',
        f'> {S["tagline"]}', '',
        '[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)',
        f'[![Tools](https://img.shields.io/badge/tools-{total_tools}-f97316?style=flat-square)]({REPO_URL})',
        f'[![Categories](https://img.shields.io/badge/categories-{len(active_cats)}-f97316?style=flat-square)]({REPO_URL})',
        '[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)', '',
        f'**[🌐 {S["website"]}]({home})** &nbsp;·&nbsp; **[➕ {S["submit"]}]({submit})** &nbsp;·&nbsp; **[🤝 {S["contributing"]}](CONTRIBUTING.md)**', '',
        '</div>', '', '---', '',
        f'## {S["what_h"]}', '',
        S['what_p'].format(cats=len(active_cats), tools=total_tools), '',
        S['different'], '',
        '- ' + S['b_quality'],
        '- ' + S['b_practical'],
        '- ' + S['b_coverage'].format(cats=len(active_cats), code=f'{site}/categories/code-assistant/',
                                       video=f'{site}/categories/video/', health=f'{site}/categories/healthcare/'),
        '- ' + S['b_updated'],
        '- ' + S['b_prof'].format(url=f'{site}/professionals/'), '',
        S['visit'].format(url=home), '', '---', '',
    ]

    # Table of contents
    lines += [f'## {S["contents"]}', '']
    lines.append(f'- [🏆 {S["leaderboard"]}](#{gh_anchor(S["leaderboard"])})')
    lines.append(f'- **{S["categories"]}**')
    for cat in active_cats:
        lines.append(f'  - [{cat["name"]}](#{gh_anchor(cat["name"])}) ({len(tools_by_cat[cat["slug"]])})')
    lines.append(f'- [👔 {S["professionals"]}](#{gh_anchor(S["professionals"])})')
    lines += ['', '---', '']

    # Leaderboard
    lines += [f'## {S["leaderboard"]}', '', f'> {S["lb_note"]}', '']
    for entry in leaderboard:
        slug = entry.get('slug', '')
        tool = tools_by_slug.get(slug)
        if not tool:
            continue
        name, website, price = tool.get('name', slug), tool.get('website', ''), tool.get('price', '')
        badge = entry.get('badge', '')
        badge = badges.get(badge, badge)
        name_part = f'**[{name}]({website})**' if website else f'**{name}**'
        line = f'{entry.get("rank", "")}. {name_part} — [{S["review"]}]({site}/tools/{slug}/)'
        if badge:
            line += f' — `{badge}`'
        if price:
            line += f' {pb(price)}'
        lines.append(line)
    lines += ['', '---', '']

    # Categories (top 4 by rank each)
    for cat in active_cats:
        slug, name = cat['slug'], cat['name']
        desc = cat.get('description', '').strip()
        count = len(tools_by_cat[slug])
        cat_url = f'{site}/categories/{slug}/'
        top = sorted(tools_by_cat[slug], key=lambda t: t.get('rank', 0), reverse=True)[:4]

        lines += [f'## [{name}]({cat_url})', '']
        if desc:
            lines += [f'> {desc}', '']
        for t in top:
            tname, website, tslug = t.get('name', ''), t.get('website', ''), t.get('slug', '')
            text = t.get('subtitle', '') or t.get('description', '')
            price = t.get('price', '')
            if len(text) > 120:
                text = text[:117].rstrip() + '...'
            entry = f'- **[{tname}]({website})**' if website else f'- **{tname}**'
            entry += f' — [{S["review"]}]({site}/tools/{tslug}/)'
            if text:
                entry += f' — {text}'
            if price:
                entry += f' {pb(price)}'
            lines.append(entry)
        lines.append('- ' + S['view_all'].format(n=count, name=name, url=cat_url))
        lines += ['', '---', '']

    # Professions
    lines += [f'## {S["professionals"]}', '', f'> {S["prof_note"]}', '']
    for prof in professions:
        name, slug, icon = prof.get('name', ''), prof.get('slug', ''), prof.get('icon', '')
        subtitle = prof.get('subtitle', '') or prof.get('description', '')
        if len(subtitle) > 100:
            subtitle = subtitle[:97].rstrip() + '...'
        entry = f'- {icon + " " if icon else ""}**[{name}]({site}/professionals/{slug}/)**'
        if subtitle:
            entry += f' — {subtitle}'
        lines.append(entry)
    lines += ['', '---', '']

    src = f'{content.name}/tools/'
    lines += [
        f'## {S["contributing"]}', '', S['contrib_p'], '',
        S['issue_p'].format(url=REPO_URL + '/issues/new'), '',
        f'## {S["license_h"]}', '', S['license_p'], '', '---', '',
        f'<sub>{S["auto"].format(src=src)}</sub>', '',
    ]

    (ROOT / lang['out']).write_text('\n'.join(lines), encoding='utf-8')
    print(f"{lang['out']} written — {total_tools} tools, {len(active_cats)} categories, "
          f"{len(leaderboard)} leaderboard entries, {len(professions)} professions")


for lang in LANGS:
    build(lang)
