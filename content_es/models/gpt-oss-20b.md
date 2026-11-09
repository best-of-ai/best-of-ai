---
title: 'GPT-OSS-20B'
name: 'GPT-OSS-20B'
slug: 'gpt-oss-20b'
subtitle: 'El nivel más pequeño del lanzamiento de modelos de pesos abiertos de OpenAI, pensado para una sola GPU'
description: 'El nivel más pequeño del lanzamiento de modelos de pesos abiertos de OpenAI, pensado para una sola GPU'
company: 'openai'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://openai.com/index/introducing-gpt-oss/'
price: 'Free'
rank: 7
release_date: '2025-08-05'
param_count: '21B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
mmlu_score: 85.3
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Together AI']
date: '2026-07-16'
tags: [llm, reasoning, open-weight, small-model, api]
i18n_source: '7a4a62f3cc31'
---

GPT-OSS-20B es el más pequeño de los dos modelos de pesos abiertos que OpenAI publicó el 5 de agosto de 2025, junto al más grande GPT-OSS-120B, en su primer lanzamiento de modelo abierto desde GPT-2. Usa un diseño de mezcla de expertos con unos 21 000 millones de parámetros en total y cerca de 3600 millones activos por token, lo bastante ligero para funcionar en una sola GPU de consumo con 16 GB o más de memoria. Ese era el objetivo: OpenAI lo hizo para desarrolladores y aficionados que querían un modelo de razonamiento capaz sin hardware de servidor. En el lanzamiento obtuvo 85,3 en MMLU, un resultado alto para su clase de tamaño, y cubre programación, matemáticas y razonamiento general bastante cerca de su hermano mayor, a pesar de la huella mucho menor. Publicado bajo la licencia Apache 2.0, se puede ajustar y redistribuir con libertad, y está disponible en Hugging Face, Together AI y la API de OpenAI para equipos que prefieren una opción gestionada al autoalojamiento.
