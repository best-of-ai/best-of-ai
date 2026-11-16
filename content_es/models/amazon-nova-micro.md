---
title: 'Amazon Nova Micro'
name: 'Amazon Nova Micro'
slug: 'amazon-nova-micro'
subtitle: 'El nivel Nova de Amazon más rápido y barato, para tareas de texto sencillas'
description: 'El nivel Nova de Amazon más rápido y barato, para tareas de texto sencillas'
company: 'amazon'
model_type: 'Language'
logo_url: ''
product_url: 'https://aws.amazon.com/ai/generative-ai/nova/'
price: 'Paid'
rank: 5
release_date: '2024-12-03'
param_count: 'Undisclosed'
context_window_tokens: 128000
modality: [text]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.035
output_price_usd_per_m: 0.14
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['AWS Bedrock']
date: '2026-07-16'
tags: [llm, low-cost, api]
i18n_source: '8a91538f6295'
---

Amazon Nova Micro es el modelo más pequeño y barato de la gama Nova de Amazon, anunciado en diciembre de 2024 junto al resto de la familia y disponible a través de Amazon Bedrock. Solo trata texto, de entrada y de salida, con una ventana de contexto de 128 000 tokens, y cuesta 0,035 $ por millón de tokens de entrada y 0,14 $ por millón de tokens de salida. Es la respuesta de Amazon a modelos ligeros como GPT-4o mini y Gemini Flash-Lite. Amazon lo construyó para cargas de mucho volumen y sensibles a la latencia, como clasificación de texto, extracción sencilla y lógica de enrutado dentro de flujos de agentes más grandes.

Como deja fuera por completo la comprensión de imagen y de vídeo, Nova Micro es más rápido y barato que sus hermanos multimodales, Lite y Pro, a cambio de no poder procesar entrada visual. Admite fine-tuning y destilación de modelos en Bedrock, de modo que se puede entrenar con las salidas de un modelo más grande para acercarse a la calidad de ese modelo en tareas estrechas, a una fracción del coste.
