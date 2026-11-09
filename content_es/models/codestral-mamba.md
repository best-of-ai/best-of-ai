---
title: 'Codestral Mamba'
name: 'Codestral Mamba'
slug: 'codestral-mamba'
subtitle: 'Modelo de código de Mistral construido sobre la arquitectura de espacio de estados Mamba, y no sobre un transformer'
description: 'Modelo de código de Mistral construido sobre la arquitectura de espacio de estados Mamba, y no sobre un transformer'
company: 'mistral-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://mistral.ai/news/codestral-mamba/'
price: 'Free'
rank: 6
release_date: '2024-07-16'
param_count: '7B'
context_window_tokens: 256000
modality: [text, code]
open_weight: true
license: 'Apache 2.0'
input_price_usd_per_m: 0.25
output_price_usd_per_m: 0.25
api_available: true
humaneval_score: 75.0
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Mistral API']
date: '2026-07-16'
tags: [code, open-weight, api]
i18n_source: '071ce3f5be62'
---

Codestral Mamba es un modelo de generación de código que Mistral AI publicó en julio de 2024. Destaca sobre todo por su arquitectura: en lugar del diseño transformer que usa casi cualquier otro modelo de código, está construido sobre Mamba, una arquitectura de modelo de espacio de estados. Los modelos de espacio de estados procesan secuencias con un escalado lineal y no cuadrático respecto a la longitud, lo que significa que la velocidad de inferencia no se degrada de forma tan brusca a medida que crece el contexto. Mistral lo dimensionó en unos 7000 millones de parámetros y le dio una ventana de contexto de 256 000 tokens, y la empresa informó de un rendimiento fiable de recuperación en contexto incluso a esa longitud.

En HumanEval, Codestral Mamba obtiene alrededor de un 75 % de pass@1, competitivo con modelos de código basados en transformers mucho más grandes. Se publica bajo licencia Apache 2.0, así que los pesos se pueden descargar, ajustar con fine-tuning y usar de forma comercial con libertad, y también está disponible a través de la API de Mistral a 0,25 $ por millón de tokens de entrada y de salida. Mistral lo presentó como prueba de concepto de que las arquitecturas de espacio de estados pueden igualar a los transformers en tareas reales de programación y, a la vez, ofrecer una inferencia más rápida y barata en usos de contexto largo, como razonar sobre repositorios grandes.
