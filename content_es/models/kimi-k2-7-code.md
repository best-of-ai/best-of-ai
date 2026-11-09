---
title: 'Kimi K2.7 Code'
name: 'Kimi K2.7 Code'
slug: 'kimi-k2-7-code'
subtitle: 'El modelo de programación agéntica de pesos abiertos de Moonshot, ajustado al uso de herramientas y a tareas largas'
description: 'El modelo de programación agéntica de pesos abiertos de Moonshot, ajustado al uso de herramientas y a tareas largas'
company: 'moonshot-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://www.moonshot.ai/'
price: 'Free'
rank: 8
release_date: '2026-06-12'
param_count: '1T (32B active)'
context_window_tokens: 256000
modality: [text, code]
open_weight: true
license: 'Modified MIT'
input_price_usd_per_m: 0.95
output_price_usd_per_m: 4.0
api_available: true
humaneval_score: 90.0
lmarena_score: 1360
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, code, agentic, mixture-of-experts]
extra_model_types: ['Reasoning']
i18n_source: '7d2adc3dc4a7'
---

Kimi K2.7 Code es el modelo de Moonshot AI centrado en programación, publicado en junio de 2026 como una construcción especializada sobre Kimi K2.6. Mantiene la misma arquitectura de mezcla de expertos de un billón de parámetros, con unos 32 000 millones activos y una ventana de contexto de 256 000 tokens, pero ajusta el modelo de forma específica a la programación de horizonte largo y a la descomposición de tareas de agentes. Moonshot informa de ganancias de cerca de un 22 % en su Kimi Code Bench v2, un 11 % en Program Bench y un 31,5 % en MLS Bench Lite respecto a K2.6, junto a cerca de un 30 % menos de tokens de razonamiento por tarea, lo que baja el coste efectivo de ejecutarlo en un bucle de agente. El modelo funciona siempre en modo de pensamiento y no admite un modo sin pensamiento, y acepta texto, imagen y vídeo además de código. Los pesos están abiertos en Hugging Face, y la propia API de Moonshot lo cobra bastante por debajo de competidores cerrados como Claude Opus y GPT-5.5, tanto en tokens de entrada como de salida.
