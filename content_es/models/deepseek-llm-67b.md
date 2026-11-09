---
title: 'DeepSeek LLM 67B'
name: 'DeepSeek LLM 67B'
slug: 'deepseek-llm-67b'
subtitle: 'Primer modelo fundacional denso de pesos abiertos de DeepSeek'
description: 'Primer modelo fundacional denso de pesos abiertos de DeepSeek'
company: 'deepseek'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 4
release_date: '2023-11-29'
param_count: '67B'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'DeepSeek License'
api_available: false
mmlu_score: 71.9
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted, legacy]
i18n_source: 'b8bff96ba077'
---

DeepSeek LLM 67B es el primer modelo fundacional denso de DeepSeek, publicado en noviembre de 2023, antes de que la empresa pivotara hacia las arquitecturas de mezcla de expertos que usa en sus líneas posteriores V2 y V3. Es un transformer denso de 67 000 millones de parámetros, entrenado con 2 billones de tokens de texto en inglés y en chino, y obtuvo alrededor de 71,9 en MMLU, más o menos en línea con Llama 2 70B en benchmarks de conocimiento general y por delante en varias tareas en lengua china. El modelo tiene una ventana de contexto comparativamente corta, de 4096 tokens, para los estándares posteriores, lo que refleja las costumbres de las tandas de entrenamiento de finales de 2023. Se publicó con variantes base y de chat bajo una licencia permisiva de DeepSeek que permite el uso comercial, y sirvió de base sobre la que DeepSeek construyó sus modelos posteriores, de uso más amplio.
