---
title: 'Llama 3.1 8B'
name: 'Llama 3.1 8B'
slug: 'llama-3-1-8b'
subtitle: 'El nivel compacto de Meta en la generación Llama 3.1'
description: 'El nivel compacto de Meta en la generación Llama 3.1'
company: 'meta-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 6
release_date: '2024-07-23'
param_count: '8B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Llama 3.1 Community License'
api_available: true
mmlu_score: 69.4
humaneval_score: 72.6
lmarena_score: 1180
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Ollama']
date: '2026-07-16'
tags: [llm, open-weight, small-model, self-hosted]
extra_model_types: ['Code']
i18n_source: 'fa37d1d53ede'
---

Llama 3.1 8B es el nivel pequeño de la misma publicación de julio de 2024, pensado para quien quiere ejecutar un modelo capaz en una sola GPU o incluso en un portátil de gama alta. Comparte la ventana de contexto de 128 000 tokens y el entrenamiento multilingüe de sus hermanos mayores, y puntúa por encima del Llama 3 8B original en MMLU y HumanEval gracias a más datos de entrenamiento y a un post-entrenamiento más afinado. Los desarrolladores lo usan para asistentes en el dispositivo, procesamiento por lotes barato y experimentos de fine-tuning en los que el 70B o el 405B sobrarían o saldrían demasiado caros de servir. Se ejecuta con facilidad con herramientas como Ollama y es uno de los modelos más descargados de Hugging Face.
