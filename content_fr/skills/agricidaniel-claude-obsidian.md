---
title: 'claude-obsidian'
name: 'claude-obsidian'
slug: 'agricidaniel-claude-obsidian'
subtitle: "Une collection de 15 Agent Skills pour construire un coffre Obsidian avec Claude Code."
description: "Claude Obsidian est un système de gestion des connaissances, d'abord en local, construit comme un ensemble d'Agent Skills coordonnés pour Claude Code. Il capture les sources avec leurs citations, range les résultats dans des notes Obsidian et des Maps of Content, et permet d'interroger le coffre plus tard, tout en gardant tous les fichiers sous le contrôle de l'utilisateur."
author: 'AgriciDaniel'
skill_type: 'Workflow & Productivity'
source_url: 'https://github.com/AgriciDaniel/claude-obsidian'
compatible_with: ['Claude Code', 'Codex', 'OpenCode', 'Cursor']
install: 'Clone the repo, run python3 scripts/claude-obsidian.py init to create a vault, then invoke skills from Claude Code run in that directory.'
price: 'Free'
open_source: true
license: 'MIT'
stars: 16143
stars_this_week: 157
stars_updated: '2026-11-04'
rank: 7
date: '2026-11-04'
tags: [obsidian, knowledge-management]
i18n_source: '00ed212456fc'
---
Ce dépôt réunit les skills suivants :

- **wiki** : Skill de base pour construire et tenir des notes de type wiki.
- **save** : Capture et conserve les sources avant la synthèse.
- **wiki-ingest** : Fait entrer le nouveau contenu source dans le coffre.
- **wiki-query** : Retrouve des réponses fondées sur le contenu déjà présent dans le coffre.
- **wiki-lint** : Vérifie la cohérence des notes du coffre et leur état.
- **autoresearch** : Automatise les flux de recherche sur plusieurs sources.
- **canvas** : Crée des vues Obsidian Canvas de notes reliées.
- **obsidian-markdown** : Skill de référence sur la syntaxe Markdown propre à Obsidian.
