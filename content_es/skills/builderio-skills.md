---
title: 'skills'
name: 'skills'
slug: 'builderio-skills'
subtitle: 'Skills pequeños y combinables de Builder.io para vigilar, revisar y publicar el trabajo de los agentes.'
description: 'El conjunto de skills de Builder.io se inclina a supervisar agentes. Los skills pueden mirar la sesión de otro agente, acompañar un pull request por las comprobaciones y la revisión, llevar una cola de revisiones y enviar resúmenes del trabajo que necesita una decisión humana. Los skills factory están marcados como experimentales. El repo tiene unos 26 skills.'
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
Este repositorio reúne los siguientes skills:

- **agent-watchdog**: Vigila, audita o corrige el trabajo de otro agente a partir de un ID de sesión.
- **efficient-orchestrator**: Ejecuta una tarea mayor con un agente orquestador, solo cuando se invoca de forma explícita.
- **factory-collect**: Recoge y clasifica comentarios, telemetría, errores e issues.
- **factory-babysit-pr**: Sigue un pull request autorizado por las comprobaciones y la revisión.
- **factory-review-prs**: Revisa una cola de pull requests con criterios distintos de respuesta, aprobación y merge.
- **factory-human-digest**: Resume el trabajo que todavía necesita juicio humano en los repos configurados.
