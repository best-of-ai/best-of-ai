---
title: 'Command R7B'
name: 'Command R7B'
slug: 'command-r7b'
subtitle: 'El modelo Command de la generación actual más pequeño de Cohere'
description: 'El modelo Command de la generación actual más pequeño de Cohere'
company: 'cohere'
model_type: 'Language'
logo_url: ''
product_url: 'https://cohere.com/command'
price: 'Free'
rank: 3
release_date: '2024-12-13'
param_count: '7B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'CC-BY-NC 4.0'
input_price_usd_per_m: 0.0375
output_price_usd_per_m: 0.15
api_available: true
mmlu_score: 70.4
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Cohere Platform', 'Hugging Face']
date: '2026-07-16'
tags: [llm, small-model, open-weight, low-latency]
i18n_source: 'a4ee277c137e'
---

Command R7B es el modelo más pequeño de la serie R de Cohere, publicado en diciembre de 2024 como lo que la empresa llamó la última entrada de esa gama. Con 7000 millones de parámetros está pensado para correr en hardware barato, incluidas CPU y GPU sueltas, y aun así cubrir generación aumentada por recuperación, uso de herramientas y tareas de razonamiento para las que se diseñaron los modelos más grandes de Cohere. En el lanzamiento encabezó el Open LLM Leaderboard de Hugging Face entre los modelos de pesos abiertos de tamaño parecido, por delante de Gemma 2 9B, Ministral 8B y Llama 3.1 8B en la media de benchmarks que incluyen MMLU, IFEval y GPQA. El modelo conserva la misma ventana de contexto de 128 000 tokens que sus hermanos mayores y tiene un precio muy por debajo, así que encaja en aplicaciones de mucho volumen y sensibles a la latencia, y no en tareas de nivel de frontera.
