---
title: 'DeepSeek-V4-Flash-Vision-Exp'
name: 'DeepSeek-V4-Flash-Vision-Exp'
slug: 'deepseek-v4-flash-vision-exp'
subtitle: 'Variante multimodal experimental de V4-Flash de DeepSeek, para comprender documentos y gráficos'
description: 'Variante multimodal experimental de V4-Flash de DeepSeek, para comprender documentos y gráficos'
company: 'deepseek'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://api-docs.deepseek.com/news/news260821/'
price: 'Paid'
rank: 6
release_date: '2026-08-21'
param_count: '284B (MoE, 13B active)'
context_window_tokens: 1048576
modality: [text, image]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.22
output_price_usd_per_m: 0.66
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['DeepSeek API']
date: '2026-08-31'
tags: [multimodal, vision, api, document-understanding, mixture-of-experts]
i18n_source: '1264f839812e'
---

DeepSeek publicó DeepSeek-V4-Flash-Vision-Exp el 21 de agosto de 2026 como variante experimental con entrada de imagen de DeepSeek-V4-Flash, el modelo de mezcla de expertos dispersa con 284 000 millones de parámetros en total y 13 000 millones activos por token. Iguala al V4-Flash solo de texto en tareas agénticas y de razonamiento, y añade comprensión de imágenes, orientada a leer documentos y gráficos, responder preguntas visuales y flujos de trabajo de agentes que mezclan texto e imágenes. Las imágenes se pueden pasar como datos base64 en línea, como URL o por la Files API de DeepSeek, y el modelo tokeniza cada imagen a 384 tokens, muy por debajo de lo que suelen usar por imagen los modelos de GPT y Claude.

En los benchmarks internos de agentes multimodales de DeepSeek, la empresa dice que V4-Flash-Vision-Exp recorta buena parte de la distancia con el Opus-4.8 de Anthropic en tareas que exigen razonar sobre entrada visual, un salto notable respecto al V4-Flash solo de texto. Cuesta 0,22 $ por millón de tokens de entrada y 0,66 $ por millón de tokens de salida, con una tarifa más baja aparte para la entrada en caché, y de momento solo está en la API de DeepSeek, mientras la empresa recoge comentarios antes de una versión que ya no sea experimental.
