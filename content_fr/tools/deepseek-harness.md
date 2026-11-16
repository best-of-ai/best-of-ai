---
title: 'DeepSeek Harness'
name: 'DeepSeek Harness'
subtitle: "Framework open source, d'abord par plugins, pour construire des agents de code sur les modèles DeepSeek"
slug: 'deepseek-harness'
description: "DeepSeek Harness est un runtime d'agents open source pour des agents de code. Modèles, outils, bacs à sable et orchestration sont des plugins interchangeables, et il fonctionne avec les modèles de DeepSeek et d'autres fournisseurs."
website: 'https://deepseek.com/harness/en/'
company: 'deepseek'
logo_url: ''
category: 'devtools'
category_name: "Outils de développement"
price: 'Free'
featured: false
rank: 5
alternatives:
  - claude-code
  - cline
  - continue-dev
  - aider
  - opencode
  - gemini-cli
date: '2026-08-17'
tags: [developer_tools, code_generation, infrastructure, deployment, development, devops, ci_cd, cloud, api, open_source, autonomous, model_based]
i18n_source: '4473743a4f49'
---

DeepSeek Harness est un framework pour faire tourner des agents qui travaillent sur du code. Il fournit la boucle qui laisse un modèle planifier, appeler des outils, lire et modifier des fichiers, lancer des commandes shell et rendre compte, dans un but proche des agents en terminal d'autres labos. Son choix de design notable, c'est que presque chaque partie est un plugin : l'adaptateur de modèle, le registre d'outils, le journal de session et la boucle d'agent elle-même peuvent être remplacés.

Il inclut des préréglages pour des configurations courantes, comme un agent de code standard avec des outils de système de fichiers et de shell, la recherche web, des sous-agents et un mode de planification, et un mode pour construire des préréglages personnalisés. Le bac à sable utilise les mécanismes du système d'exploitation pour limiter ce que l'agent peut toucher. Bien que DeepSeek l'ait fait, il peut se connecter à des modèles d'autres fournisseurs.

Le projet est open source sous licence MIT et encore en aperçu précoce, avec des avertissements que la compatibilité peut casser et peu de contributions extérieures pour l'instant. DeepSeek n'a pas publié d'évaluations du runtime lui-même. Les alternatives incluent Claude Code, OpenAI Codex, Gemini CLI, OpenCode et Aider. DeepSeek Harness convient aux développeurs qui veulent un runtime d'agent que l'on peut modifier.
