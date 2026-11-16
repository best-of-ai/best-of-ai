---
title: 'Qwen4-Max'
name: 'Qwen4-Max'
slug: 'qwen4-max'
subtitle: 'El modelo propietario insignia de Alibaba para su API de Qwen y su plataforma en la nube'
description: 'El modelo propietario insignia de Alibaba para su API de Qwen y su plataforma en la nube'
company: 'alibaba'
model_type: 'Language'
logo_url: ''
product_url: 'https://qwen.ai/'
price: 'Paid'
rank: 8
release_date: '2026-07-11'
param_count: 'Undisclosed'
context_window_tokens: 1000000
modality: [text, image]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 1.20
output_price_usd_per_m: 4.80
api_available: true
mmlu_score: 88.0
lmarena_score: 1352
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['Alibaba Cloud', 'Qwen Chat', 'API']
date: '2026-07-19'
tags: [llm, proprietary, api, multimodal]
i18n_source: 'd9ca0c4f1096'
---
Qwen4-Max es el modelo propietario de nivel más alto de Alibaba, por encima de la familia Qwen3 de pesos abiertos que la empresa sigue publicando en Hugging Face. A diferencia de esos, Qwen4-Max es cerrado y solo se alcanza a través de la API de Alibaba Cloud, de Qwen Chat o de plataformas asociadas, a 1,20 $ por millón de tokens de entrada y 4,80 $ por millón de tokens de salida. Acepta texto e imagen, tiene una ventana de contexto de 1 millón de tokens, y Alibaba lo ha situado directamente frente a GPT-5.6 y Gemini 3.5 Pro en sus propias comparaciones de benchmarks.

El reparto entre los modelos Qwen3 abiertos y el Qwen4-Max cerrado copia un patrón en el que ya se han asentado otros laboratorios: dar gratis pesos capaces de tamaño medio para ganar presencia entre desarrolladores, y reservar el modelo más grande y más caro de entrenar para una API de pago. Alibaba se ha apoyado en este enfoque para ampliar el alcance de Qwen bastante más allá de China, sobre todo entre desarrolladores de Hugging Face que hacen fine-tuning de las versiones abiertas pero en producción siguen usando el nivel Max cuando necesitan más margen de razonamiento.
