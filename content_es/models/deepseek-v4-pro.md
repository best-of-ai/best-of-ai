---
title: 'DeepSeek V4-Pro'
name: 'DeepSeek V4-Pro'
slug: 'deepseek-v4-pro'
subtitle: 'El principal modelo de pesos abiertos de 2026, a la cabeza en programación agéntica y razonamiento de posgrado'
description: 'El principal modelo de pesos abiertos de 2026, a la cabeza en programación agéntica y razonamiento de posgrado'
company: 'deepseek'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 9
release_date: '2026-04-24'
param_count: '1.6T (49B active)'
context_window_tokens: 1000000
modality: [text, code]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 0.43
output_price_usd_per_m: 0.87
api_available: true
mmlu_score: 90.0
humaneval_score: 91.0
lmarena_score: 1390
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API', 'Together AI']
date: '2026-07-16'
tags: [llm, open-weight, reasoning, coding, mixture-of-experts]
extra_model_types: ['Code']
i18n_source: '3dcf4ddbbacd'
---

DeepSeek V4-Pro es el modelo insignia de DeepSeek, publicado el 24 de abril de 2026 junto a un hermano más pequeño, V4-Flash. Es un modelo de mezcla de expertos con 1,6 billones de parámetros en total y 49 000 millones activos por token, e introduce un diseño de atención híbrida que combina Compressed Sparse Attention y Heavily Compressed Attention. Eso recorta con claridad el cómputo de inferencia y el tamaño de la KV-cache frente a V3.2, y le permite una ventana de contexto de 1 millón de tokens. El modelo funciona en un modo «thinking», de razonamiento paso a paso, y en un modo sin ese razonamiento, para respuestas rápidas. DeepSeek dice que lidera los modelos de pesos abiertos en benchmarks de matemáticas, ciencias y programación agéntica, con una puntuación en SWE-bench Verified por encima del 80 %.

Como el resto de la gama de DeepSeek, V4-Pro sale con pesos abiertos bajo la licencia MIT y un precio de API muy por debajo de modelos cerrados comparables de OpenAI, Anthropic y Google. Se presenta como la respuesta de DeepSeek a los modelos de razonamiento de frontera que publicaron los laboratorios occidentales a principios de 2026, y el lanzamiento tuvo mucha cobertura como prueba de que la distancia entre modelos de frontera abiertos y cerrados sigue acortándose.
