---
title: 'Claude Code'
name: 'Claude Code'
subtitle: "Outil de code agentique d'Anthropic, qui travaille directement dans le terminal"
slug: 'claude-code'
description: "Claude Code est l'agent de code d'Anthropic. Il lit le dépôt, modifie des fichiers, lance des commandes et avance dans les tâches dans le terminal, et il est aussi disponible dans les IDE, sur le bureau et sur le web."
website: 'https://claude.ai/code'
company: 'anthropic'
logo_url: ''
category: 'code-assistant'
category_name: 'Assistants de code'
price: 'Freemium'
featured: false
rank: 8
alternatives:
  - codex
  - cursor
  - gemini-cli
  - github-copilot
  - aider
  - cline
  - opencode
  - windsurf
date: '2025-09-21'
tags: [code_generation, developer_tools, productivity, coding, programming, autocomplete, debugging, refactoring, ide, extensible]
i18n_source: '012aa47ad99b'
---

Claude Code travaille comme un agent sur le projet réel, plutôt que comme un moteur de suggestions dans un éditeur. On le lance dans un dépôt depuis le terminal et on décrit la tâche, comme corriger un test qui échoue, ajouter un endpoint ou mettre à jour une dépendance. Il lit les fichiers pertinents, fait un plan, modifie le code à travers le projet, lance les tests et d'autres commandes, et itère sur les erreurs. Il demande la permission pour les actions qui pourraient être risquées, et on peut revoir les changements en diffs ou via git avant de committer.

Il est très personnalisable. Un fichier CLAUDE.md dans un projet contient les instructions et les conventions que l'agent suit à chaque fois, et des skills emballent des procédures répétables. Des hooks lancent tes propres scripts à des points du flux, des sous-agents répartissent le travail sur des contextes parallèles, et le Model Context Protocol le relie à des bases de données, des suivis d'issues et d'autres outils. Il fonctionne aussi dans des éditeurs comme VS Code et JetBrains, dans une app de bureau et dans le navigateur, et on peut le lancer dans des scripts et en CI pour des tâches automatisées.

Claude Code est inclus dans les offres Claude payantes et peut aussi s'utiliser avec une clé d'API facturée à l'usage, donc les coûts dépendent de combien on le fait tourner. De longues sessions autonomes peuvent consommer beaucoup de tokens. Sa sortie a encore besoin d'une relecture, surtout pour le code sensible à la sécurité. Codex d'OpenAI, Gemini CLI de Google, Cursor, l'agent de GitHub Copilot et Cline sont les principales alternatives.
