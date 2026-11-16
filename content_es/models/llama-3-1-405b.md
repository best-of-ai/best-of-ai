---
title: 'Llama 3.1 405B'
name: 'Llama 3.1 405B'
slug: 'llama-3-1-405b'
subtitle: 'El modelo denso de pesos abiertos más grande de Meta, a la altura de los modelos cerrados de frontera'
description: 'El modelo denso de pesos abiertos más grande de Meta, a la altura de los modelos cerrados de frontera'
company: 'meta-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 7
release_date: '2024-07-23'
param_count: '405B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Llama 3.1 Community License'
api_available: true
mmlu_score: 88.6
humaneval_score: 89.0
lmarena_score: 1265
access_methods: [API, Self-hosted]
runs_at_home: false
platforms: ['Hugging Face', 'Together AI', 'AWS Bedrock']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted, foundation-model]
extra_model_types: ['Code']
i18n_source: 'c720dd46ff12'
---

Llama 3.1 405B es el modelo Llama 3.1 más grande de Meta, publicado el 23 de julio de 2024 como un transformer denso de 405 000 millones de parámetros, no como un diseño de mezcla de expertos. Admite una ventana de contexto de 128 000 tokens y obtuvo 88,6 en MMLU y 89,0 en HumanEval, en la misma franja que GPT-4 tanto en conocimiento como en benchmarks de programación. Fue el primer modelo de pesos abiertos que igualó de verdad a un modelo cerrado de frontera, en lugar de ir una generación por detrás, y Meta lo publicó junto a versiones más pequeñas de 70B y 8B entrenadas del mismo modo, para que los desarrolladores eligieran el equilibrio entre calidad y coste. Se puede autoalojar a través de Hugging Face, y usar por inferencia alojada en Together AI, Fireworks, AWS Bedrock, Azure y Google Cloud; los proveedores lo cobran bastante por debajo de los modelos cerrados equivalentes, porque Meta no cobra por los pesos. Llama 3.1 405B reforzó el argumento de Meta: un modelo abierto puede situarse en la frontera, en lugar de quedar como una alternativa más barata y más floja.
