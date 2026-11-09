---
title: 'GLM-5.2'
name: 'GLM-5.2'
slug: 'glm-5-2'
subtitle: 'El modelo insignia de pesos abiertos de Zhipu, publicado junto a Kimi K2.7 a mediados de 2026'
description: 'El modelo insignia de pesos abiertos de Zhipu, publicado junto a Kimi K2.7 a mediados de 2026'
company: 'zhipu-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.zhipuai.cn/'
price: 'Free'
rank: 7
release_date: '2026-06-13'
param_count: '~744B (MoE, ~40B active)'
context_window_tokens: 1000000
modality: [text, code]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 1.4
output_price_usd_per_m: 4.4
api_available: true
mmlu_score: 91.72
humaneval_score: 88.0
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, coding, self-hosted]
extra_model_types: ['Code']
i18n_source: 'd5b4b307c39a'
---

GLM-5.2 es el modelo insignia de pesos abiertos de Zhipu AI, publicado el 13 de junio de 2026 bajo la licencia MIT. Es un modelo de mezcla de expertos con unos 744 000 millones de parámetros en total y cerca de 40 000 millones activos por token, y sale con una ventana de contexto de 1 millón de tokens, muy por encima de los 128 000 tokens de su predecesor GLM-4.6. Zhipu lo construyó en concreto para agentes de programación de horizonte largo, y lo entrenó durante meses en escenarios de ingeniería de software agéntica, no en chat general.

En benchmarks saca un 91,72 % en MMLU, un 80,3 % en GPQA Diamond y un 62,1 % en SWE-bench Pro; este último supera el 58,6 % informado de GPT-5.5. Zhipu cobra el acceso por API a 1,40 $ por millón de tokens de entrada y 4,40 $ por millón de tokens de salida, una fracción de lo que cuestan modelos propietarios comparables, y la empresa presenta la combinación de pesos abiertos y rendimiento en programación como un desafío directo a los modelos de frontera cerrados de OpenAI y Anthropic.
