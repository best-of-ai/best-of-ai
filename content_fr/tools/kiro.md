---
title: 'Kiro'
name: 'Kiro'
subtitle: "IDE agentique d'AWS, piloté par une spec"
slug: 'kiro'
description: "Kiro est un IDE agentique d'AWS qui prend une spec écrite, et non un prompt de chat, comme unité de travail. L'agent planifie une fonction, rédige les exigences et le design, puis l'implémente, la teste et la documente."
website: 'https://kiro.dev'
company: 'amazon'
logo_url: ''
category: 'code-assistant'
category_name: "Assistants de code"
price: 'Freemium'
featured: false
rank: 5
alternatives:
  - cursor
  - windsurf
  - claude-code
  - codex
  - google-antigravity
  - github-copilot
  - myspec-ai
date: '2026-07-29'
tags: [code_generation, developer_tools, productivity, coding, programming, autocomplete, debugging, refactoring, ide, extensible]
i18n_source: '85f0afaed192'
---
Kiro est construit autour du développement piloté par une spec. Un développeur décrit une fonction, et Kiro produit un document d'exigences, un design technique et une liste de tâches. Le développeur relit et modifie ces documents, puis l'agent enchaîne les tâches, en écrivant le code et les tests. L'idée est de garder un agent aligné sur l'intention pour un travail plus large, au lieu d'improviser à partir du chat.

L'éditeur est basé sur Code OSS, donc les extensions et les réglages de VS Code se transfèrent. Des hooks déclenchent des actions de l'agent sur des événements comme l'enregistrement d'un fichier, des fichiers de pilotage donnent des consignes persistantes sur un projet, et la prise en charge du Model Context Protocol connecte des outils externes. Il utilise les modèles Claude via AWS.

Kiro a une offre gratuite et des offres payantes selon l'usage. Les specs ajoutent de la structure et un peu de surcharge, ce qui convient mieux aux fonctions larges qu'aux petits correctifs. Les alternatives incluent Cursor, Claude Code, Windsurf, GitHub Copilot et GitHub Spec Kit. Kiro convient aux développeurs qui veulent de la discipline de planification avec des agents.
