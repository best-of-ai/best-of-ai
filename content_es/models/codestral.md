---
title: 'Codestral'
name: 'Codestral'
slug: 'codestral'
subtitle: 'Modelo de generación y completado de código de Mistral'
description: 'Modelo de generación y completado de código de Mistral'
company: 'mistral-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://mistral.ai/news/codestral/'
price: 'Free'
rank: 6
release_date: '2024-05-29'
param_count: '22B'
context_window_tokens: 256000
modality: [text, code]
open_weight: true
license: 'Apache 2.0'
input_price_usd_per_m: 0.3
output_price_usd_per_m: 0.9
api_available: true
humaneval_score: 81.1
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, code, open-weight, api]
i18n_source: '0c94b2ec4923'
---

Codestral es el modelo de generación de código dedicado de Mistral AI, publicado por primera vez en mayo de 2024 con 22 000 millones de parámetros. Está pensado para el completado fill-in-the-middle y la generación de código en varios lenguajes, y se lanzó con un 81,1 % de pass@1 en HumanEval, por delante de modelos de código más grandes como Code Llama 70B y DeepSeek Coder 33B en aquel momento. La publicación original usaba una ventana de contexto de 32 000 tokens y salió bajo la Mistral AI Non-Production License, que limitaba el uso gratuito a investigación y pruebas y exigía una licencia comercial aparte para el despliegue en producción.

Mistral amplió después la ventana de contexto de Codestral a 256 000 tokens y, en abril de 2026, volvió a licenciar el modelo bajo Apache 2.0, lo que eliminó la restricción anterior de uso comercial y lo dejó libre para usarlo en IDE, asistentes de programación y procesos de CI. Codestral está disponible tanto como pesos descargables en Hugging Face como a través de la API de Mistral, con un precio actual de 0,30 $ por millón de tokens de entrada y 0,90 $ por millón de tokens de salida. Compite de forma directa con otros modelos de código abiertos de tamaño medio, como Codestral Mamba y Code Llama, y su paso a una licencia permisiva se vio de forma amplia como un cambio relevante en el espacio de los modelos de programación de código abierto.
