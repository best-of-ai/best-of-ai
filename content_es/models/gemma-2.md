---
title: 'Gemma 2'
name: 'Gemma 2'
slug: 'gemma-2'
subtitle: 'La familia de modelos de pesos abiertos de la generación anterior de Google'
description: 'La familia de modelos de pesos abiertos de la generación anterior de Google'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.google.dev/gemma'
price: 'Free'
rank: 6
release_date: '2024-06-27'
param_count: '27B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Gemma License'
api_available: true
mmlu_score: 75.2
humaneval_score: 51.8
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Google Vertex AI']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted]
extra_model_types: ['Code']
i18n_source: '4b34b113fc55'
---

Gemma 2 es la segunda generación de la familia de modelos de pesos abiertos de Google, construida a partir de la misma investigación que Gemini, pero publicada para que cualquiera la descargue y la ejecute. Google lanzó las versiones de 9000 y 27 000 millones de parámetros el 27 de junio de 2024, y más tarde una versión más pequeña, de 2000 millones, pensada para correr en portátiles y teléfonos. El modelo de 27B se ajustó para competir con modelos de más del doble de su tamaño, y la versión de 9B superó a Llama 3 8B y a otros modelos abiertos de tamaño parecido en varios benchmarks en el lanzamiento, con 75,2 en MMLU y 51,8 en HumanEval.

Google distribuye los pesos de Gemma 2 en Hugging Face y Kaggle para autoalojarlos, y también lo ofrece en Google AI Studio y Vertex AI para quien prefiera no ejecutarlo. Sale bajo la licencia Gemma propia de Google, que permite el uso comercial pero lleva algunas restricciones de uso, y no es una licencia totalmente permisiva como Apache 2.0. Google ha publicado después Gemma 3 como generación más nueva, así que Gemma 2 es ahora la opción de la generación anterior en la gama, mantenida por compatibilidad y para equipos que ya trabajan con ella.
