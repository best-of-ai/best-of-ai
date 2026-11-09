---
title: 'GLM-5.3'
name: 'GLM-5.3'
slug: 'glm-5-3'
subtitle: 'Actualización de GLM-5.2 de Zhipu centrada en programación, ajustada sobre todo con investigación de vulnerabilidades'
description: 'Actualización de GLM-5.2 de Zhipu centrada en programación, ajustada sobre todo con investigación de vulnerabilidades'
company: 'zhipu-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://www.zhipuai.cn/'
price: 'Paid'
rank: 7
release_date: '2026-08-14'
param_count: '~744B (MoE, ~40B active)'
context_window_tokens: 1000000
modality: [text, code]
open_weight: false
license: 'Proprietary'
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['GLM Coding Plan', 'API']
date: '2026-08-17'
tags: [llm, coding, cybersecurity, agentic, mixture-of-experts]
extra_model_types: ['Reasoning']
i18n_source: '87f3720943f0'
---

Zhipu AI publicó GLM-5.3 el 14 de agosto de 2026 y lo llamó el modelo de programación de pesos abiertos más fuerte disponible, aunque los pesos en sí no llegan hasta dos semanas después del anuncio. Comparte la arquitectura base con GLM-5.2, así que el salto de cerca del 50 % en capacidad de programación que informa Zhipu viene entero de un post-entrenamiento más largo, no de un modelo más grande. La empresa señala en particular un ángulo de seguridad: GLM-5.3 sacó un 84,5 % en CyberGym, un benchmark para encontrar y validar vulnerabilidades a partir del código fuente, por delante del Claude Mythos de Anthropic, con un 83,8 %, y del GPT-5.6 Sol de OpenAI, con un 83,6 %. Zhipu dice que equipos internos de seguridad usaron el modelo para sacar a la luz 2 436 vulnerabilidades en 269 proyectos.

De momento, el acceso pasa por el GLM Coding Plan de Zhipu, y el modelo funciona con agentes de programación como Claude Code, OpenCode y el ZCode propio de Zhipu. El despliegue escalonado, primero el acceso por API y después los pesos abiertos, es un patrón que Zhipu ya había usado con la línea GLM.
