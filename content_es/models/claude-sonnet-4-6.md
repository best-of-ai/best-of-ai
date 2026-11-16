---
title: 'Claude Sonnet 4.6'
name: 'Claude Sonnet 4.6'
slug: 'claude-sonnet-4-6'
subtitle: 'Modelo Sonnet por defecto de Anthropic, pensado para acercarse a resultados de la clase Opus a una quinta parte del precio'
description: 'Modelo Sonnet por defecto de Anthropic, pensado para acercarse a resultados de la clase Opus a una quinta parte del precio'
company: 'anthropic'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.anthropic.com/news/claude-sonnet-4-6'
price: 'Paid'
rank: 9
release_date: '2026-02-17'
param_count: 'Undisclosed'
context_window_tokens: 1000000
modality: [text, image]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 3
output_price_usd_per_m: 15
api_available: true
lmarena_score: 1380
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['Claude.ai', 'AWS Bedrock', 'Google Vertex AI', 'API']
date: '2026-07-25'
tags: [llm, reasoning, frontier-model, api, agentic]
extra_model_types: ['Code']
i18n_source: '1c6e036cc247'
---

Claude Sonnet 4.6 salió el 17 de febrero de 2026 y se convirtió en el modelo por defecto de claude.ai y de Claude Cowork, el producto de espacio de trabajo de Anthropic. Iguala la ventana de contexto de 1 millón de tokens y el límite de salida de 128 000 tokens de Opus 4.6, con un precio de 3 $ por millón de tokens de entrada y 15 $ por millón de tokens de salida, aproximadamente una quinta parte de la tarifa de Opus 4.6. En SWE-bench Verified puntuó un 79,6 %, a unos pocos puntos del modelo Opus a pesar de la diferencia de precio, y obtuvo un 59,1 % en Terminal-Bench 2.0 y un 72,5 % en OSWorld-Verified, benchmarks que prueban tareas agénticas de terminal y de uso del ordenador. Anthropic incorporó cadenas de razonamiento extendido que pueden llegar hasta 100 pasos, dirigidas a desarrolladores que quieren una fiabilidad del nivel de Opus sin pagar precios de Opus.
