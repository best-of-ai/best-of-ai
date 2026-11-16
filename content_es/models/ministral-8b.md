---
title: 'Ministral 8B'
name: 'Ministral 8B'
slug: 'ministral-8b'
subtitle: 'Modelo compacto de Mistral pensado para despliegue en dispositivos y en el edge'
description: 'Modelo compacto de Mistral pensado para despliegue en dispositivos y en el edge'
company: 'mistral-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://mistral.ai/news/ministraux/'
price: 'Free'
rank: 4
release_date: '2024-10-16'
param_count: '8B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Mistral Research License'
input_price_usd_per_m: 0.1
output_price_usd_per_m: 0.1
api_available: true
mmlu_score: 65.0
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, small-model, on-device]
i18n_source: '5f9757c587f7'
---

Ministral 8B es un modelo de 8000 millones de parámetros que Mistral AI lanzó en octubre de 2024 como parte de «Les Ministraux», un par de modelos pequeños pensados para despliegue en dispositivos y en el edge, junto al más pequeño Ministral 3B. Usa atención de ventana deslizante intercalada para admitir una ventana de contexto de 128 000 tokens a pesar de su tamaño reducido, y Mistral lo posicionó frente a modelos de tamaño similar como Llama 3.1 8B y Gemma 2 9B, con mejores resultados en benchmarks de conocimiento, razonamiento y multilingüismo dentro de esa categoría.

Mistral lo publicó con la Mistral Research License, que permite el uso gratuito para investigación y pruebas pero exige una licencia comercial para desplegarlo en producción, a diferencia de los términos totalmente abiertos Apache 2.0 de Mistral 7B. Está dirigido a desarrolladores que crean aplicaciones para teléfonos, portátiles y otro hardware limitado, como asistentes locales, traducción y agentes ligeros, donde no es práctico ejecutar un modelo de tamaño completo.
