---
title: 'skills'
name: 'skills'
slug: 'builderio-skills'
subtitle: 'Skills pequenas e combináveis da Builder.io para acompanhar, revisar e entregar o trabalho de agentes.'
description: 'O conjunto de skills da Builder.io se concentra na supervisão de agentes. As skills podem acompanhar a sessão de outro agente, conduzir uma solicitação de pull request pelas verificações e revisão, executar uma fila de revisão e enviar resumos de trabalhos que exigem decisão humana. As skills “factory” são marcadas como experimentais. O repositório tem cerca de 26 skills.'
author: 'BuilderIO'
skill_type: 'Workflow & Productivity'
source_url: 'https://github.com/BuilderIO/skills'
compatible_with: ['Claude Code', 'Codex']
install: 'Run npx @agent-native/skills@latest add to pick from the recommended skills.'
price: 'Free'
open_source: true
license: 'MIT'
stars: 4685
stars_this_week: 0
stars_updated: '2026-11-24'
rank: 5
date: '2026-11-08'
tags: [workflow, pull-requests, orchestration, code-review]
i18n_source: 'cc76aba2ae7c'
---
Este repositório reúne as seguintes skills:

- **agent-watchdog**: Observa, audita ou corrige o trabalho de outro agente usando o ID de uma sessão.
- **efficient-orchestrator**: Executa uma tarefa maior com um agente orquestrador, somente quando invocado explicitamente.
- **factory-collect**: Coleta e classifica feedback, telemetria, erros e problemas.
- **factory-babysit-pr**: Acompanha uma pull request autorizada durante as verificações e a revisão.
- **factory-review-prs**: Revisa uma fila de pull requests com critérios separados para resposta, aprovação e merge.
- **factory-human-digest**: Resume o trabalho que ainda requer julgamento humano nos repositórios configurados.