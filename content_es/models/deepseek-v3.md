---
title: 'DeepSeek V3'
name: 'DeepSeek V3'
slug: 'deepseek-v3'
subtitle: 'Modelo eficiente de mezcla de expertos de DeepSeek, entrenado por una fracción del coste de los rivales'
description: 'Modelo eficiente de mezcla de expertos de DeepSeek, entrenado por una fracción del coste de los rivales'
company: 'deepseek'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 8
release_date: '2024-12-26'
param_count: '671B (37B active)'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 0.27
output_price_usd_per_m: 1.1
api_available: true
mmlu_score: 88.5
humaneval_score: 82.6
lmarena_score: 1330
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, mixture-of-experts, self-hosted]
extra_model_types: ['Code']
i18n_source: '3c9c049bbd9a'
---

DeepSeek V3 es un modelo de mezcla de expertos de 671 000 millones de parámetros, con 37 000 millones activos por token, que DeepSeek publicó el 26 de diciembre de 2024. Es un modelo base, no de razonamiento, construido sobre la misma arquitectura Multi-head Latent Attention y DeepSeekMoE que V2, y DeepSeek dijo haberlo entrenado por unos 5,6 millones de dólares en tiempo de GPU, una cifra muy por debajo de lo que gastaban los laboratorios occidentales en modelos comparables. Sacó 88,5 en MMLU y 82,6 en HumanEval, más o menos al nivel de GPT-4o y Claude 3.5 Sonnet en muchos benchmarks, pese al bajo coste de entrenamiento.

V3 se publica bajo la licencia MIT con pesos abiertos, y DeepSeek puso su API muy por debajo de los modelos de frontera de la competencia. Después sirvió de modelo base sobre el que se construyó el aprendizaje por refuerzo de R1, orientado al razonamiento, y su eficiencia de coste se convirtió en un tema de conversación en el sector: cuánto cómputo hace falta de verdad para llegar a un rendimiento de frontera.
