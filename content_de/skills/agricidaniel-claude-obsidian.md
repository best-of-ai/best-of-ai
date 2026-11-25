---
title: 'claude-obsidian'
name: 'claude-obsidian'
slug: 'agricidaniel-claude-obsidian'
subtitle: 'Sammlung mit 15 Agent Skills, um mit Claude Code einen Obsidian-Vault aufzubauen.'
description: 'Claude Obsidian ist ein lokales Wissensmanagementsystem aus mehreren aufeinander abgestimmten Agent Skills für Claude Code. Es erfasst Quellenmaterial mit Zitaten, verknüpft Ergebnisse mit Obsidian-Notizen und Inhaltsübersichten (Maps of Content) und macht den Vault später durchsuchbar. Alle Dateien bleiben dabei unter deiner Kontrolle.'
author: 'AgriciDaniel'
skill_type: 'Workflow & Productivity'
source_url: 'https://github.com/AgriciDaniel/claude-obsidian'
compatible_with: ['Claude Code', 'Codex', 'OpenCode', 'Cursor']
install: 'Clone the repo, run python3 scripts/claude-obsidian.py init to create a vault, then invoke skills from Claude Code run in that directory.'
price: 'Free'
open_source: true
license: 'MIT'
stars: 16735
stars_this_week: 60
stars_updated: '2026-11-24'
rank: 7
date: '2026-11-04'
tags: [obsidian, knowledge-management]
i18n_source: 'b260df1ea0b7'
---
Dieses Repository bündelt folgende Skills:

- **wiki**: Kern-Skill zum Erstellen und Pflegen von Notizen im Wiki-Stil.
- **save**: Erfasst und bewahrt Quellenmaterial vor der Zusammenfassung.
- **wiki-ingest**: Übernimmt neue Quelleninhalte in den Vault.
- **wiki-query**: Ruft belegte Antworten aus dem vorhandenen Vault ab.
- **wiki-lint**: Prüft Notizen im Vault auf Konsistenz und Probleme.
- **autoresearch**: Automatisiert Rechercheabläufe über mehrere Quellen hinweg.
- **canvas**: Erstellt Obsidian-Canvas-Ansichten verknüpfter Notizen.
- **obsidian-markdown**: Referenz zu Syntax und Funktionen von Obsidian-Markdown.
