---
title: 'skills'
name: 'skills'
slug: 'builderio-skills'
subtitle: "De petits skills composables de Builder.io pour surveiller, relire et livrer le travail des agents."
description: "L'ensemble de skills de Builder.io penche vers la supervision des agents. Les skills peuvent surveiller la session d'un autre agent, accompagner un pull request pendant les vérifications et la revue, tenir une file de revue et envoyer des synthèses du travail qui demande une décision humaine. Les skills « factory » sont marqués expérimentaux. Le dépôt en compte environ 26."
author: 'BuilderIO'
skill_type: 'Workflow & Productivity'
source_url: 'https://github.com/BuilderIO/skills'
compatible_with: ['Claude Code', 'Codex']
install: 'Run npx @agent-native/skills@latest add to pick from the recommended skills.'
price: 'Free'
open_source: true
license: 'MIT'
stars: 4651
stars_this_week: 0
stars_updated: '2026-11-08'
rank: 5
date: '2026-11-08'
tags: [workflow, pull-requests, orchestration, code-review]
i18n_source: '0bfb058224a8'
---
Ce dépôt regroupe les skills suivants :

- **agent-watchdog**: Surveille, audite ou corrige le travail d'un autre agent à partir d'un ID de session.
- **efficient-orchestrator**: Mène une tâche plus large avec un agent qui orchestre, seulement si on l'invoque explicitement.
- **factory-collect**: Collecte et trie les retours, la télémétrie, les erreurs et les issues.
- **factory-babysit-pr**: Suit un pull request autorisé à travers les vérifications et la revue.
- **factory-review-prs**: Relit une file de pull requests, avec des critères distincts pour la réponse, l'approbation et le merge.
- **factory-human-digest**: Résume le travail qui demande encore un jugement humain, dans les dépôts configurés.
