---
title: 'Kimi K2'
name: 'Kimi K2'
slug: 'kimi-k2'
subtitle: 'El modelo base original de pesos abiertos de la generación K2 de Moonshot'
description: 'El modelo base original de pesos abiertos de la generación K2 de Moonshot'
company: 'moonshot-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.moonshot.ai/'
price: 'Free'
rank: 7
release_date: '2025-07-11'
param_count: '1T (32B active)'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Modified MIT'
input_price_usd_per_m: 0.55
output_price_usd_per_m: 2.2
api_available: true
humaneval_score: 85.0
lmarena_score: 1340
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, mixture-of-experts, self-hosted]
extra_model_types: ['Code']
i18n_source: '611eb2c97d06'
---

Kimi K2 es el modelo base original de la generación K2 de Moonshot AI, publicado en julio de 2025 como uno de los modelos de lenguaje de pesos abiertos más grandes disponibles entonces. Usa un diseño de mezcla de expertos con cerca de 1 billón de parámetros en total y 32 000 millones activos por token, y admite una ventana de contexto de 128 000 tokens. Moonshot lo construyó alrededor de usos de agentes, como llamadas a herramientas y ejecución de tareas en varios pasos, y no del chat puro. En benchmarks de programación como la variante multilingüe de HumanEval, MultiPL-E, puntuó cerca de los mejores modelos cerrados disponibles aquel verano. Los pesos se publican bajo una licencia MIT modificada, de modo que las empresas pueden descargarlo, hacer fine-tuning y autoalojarlo en lugar de pasar por la API de Moonshot, y se convirtió en la base sobre la que se apoyaron lanzamientos posteriores de Moonshot, entre ellos K2.5, K2.6 y K2.7 Code.
