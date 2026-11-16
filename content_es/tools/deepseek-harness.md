---
title: 'DeepSeek Harness'
name: 'DeepSeek Harness'
subtitle: 'Framework de código abierto, basado en plugins, para crear agentes de programación con modelos de DeepSeek'
slug: 'deepseek-harness'
description: 'DeepSeek Harness es un entorno de ejecución de código abierto para agentes de programación. Modelos, herramientas, sandboxes y orquestación son plugins intercambiables, y funciona con los modelos de DeepSeek y con otros proveedores.'
website: 'https://deepseek.com/harness/en/'
company: 'deepseek'
logo_url: ''
category: 'devtools'
category_name: 'Herramientas para desarrolladores'
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

DeepSeek Harness es un framework para ejecutar agentes que trabajan con código. Aporta el bucle que permite a un modelo planificar, llamar a herramientas, leer y editar archivos, ejecutar comandos de shell e informar del resultado, con un propósito parecido al de los agentes de terminal de otros laboratorios. Su decisión de diseño más notable es que casi todo es un plugin: el adaptador del modelo, el registro de herramientas, el registro de sesión y el propio bucle del agente se pueden sustituir.

Incluye preajustes para configuraciones habituales, como un agente de programación estándar con herramientas de sistema de archivos y shell, búsqueda web, subagentes y un modo de planificación, además de un modo para crear preajustes propios. El sandboxing usa los mecanismos del propio sistema operativo para limitar lo que el agente puede tocar. Aunque lo creó DeepSeek, puede conectarse con modelos de otros proveedores.

El proyecto es de código abierto con licencia MIT y sigue en una vista previa temprana, con avisos de que la compatibilidad puede romperse y con pocas contribuciones externas hasta ahora. DeepSeek no ha publicado evaluaciones del propio entorno de ejecución. Entre las alternativas están Claude Code, OpenAI Codex, Gemini CLI, OpenCode y Aider. DeepSeek Harness encaja con desarrolladores que quieren un entorno de ejecución de agentes fácil de modificar.
