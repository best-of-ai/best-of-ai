---
title: 'GPT-4 Turbo'
name: 'GPT-4 Turbo'
slug: 'gpt-4-turbo'
subtitle: 'Sucesor de GPT-4 más rápido y barato, con una ventana de contexto mayor'
description: 'Sucesor de GPT-4 más rápido y barato, con una ventana de contexto mayor'
company: 'openai'
model_type: 'Language'
logo_url: ''
product_url: 'https://openai.com/index/new-models-and-developer-products-announced-at-devday/'
price: 'Paid'
rank: 6
release_date: '2023-11-06'
param_count: 'Undisclosed'
context_window_tokens: 128000
modality: [text, image]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 10
output_price_usd_per_m: 30
api_available: true
mmlu_score: 86.5
humaneval_score: 87.1
lmarena_score: 1250
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['ChatGPT', 'Azure OpenAI', 'API']
date: '2026-07-16'
tags: [llm, foundation-model, api]
extra_model_types: ['Code']
i18n_source: 'dfca7bbe4eb9'
---

GPT-4 Turbo es la actualización de GPT-4 que OpenAI presentó en noviembre de 2023, en la primera conferencia de desarrolladores de la empresa. Mantuvo el nivel de capacidad de GPT-4, pero amplió la ventana de contexto a 128 000 tokens, fijó el corte de conocimiento en abril de 2023 y bajó el precio a 10 $ por millón de tokens de entrada y 30 $ por millón de tokens de salida, bastante por debajo de las tarifas originales de GPT-4. Obtiene un 86,5 % en MMLU y un 87,1 % en HumanEval, y añadió entrada de visión, de modo que los desarrolladores pueden enviar imágenes junto al texto en la misma petición.

La ventana más grande tenía una salvedad práctica: pruebas independientes vieron que la calidad de la atención bajaba de forma clara a partir de unos 32 000 tokens, así que la ventana completa de 128K funcionaba mejor en teoría que en un uso denso con documentos largos. Aun así, GPT-4 Turbo fue el modelo por defecto de la clase GPT-4 para desarrolladores de API durante buena parte de 2024, disponible directamente en OpenAI, en Azure OpenAI y en ChatGPT, hasta que GPT-4o lo sustituyó como opción recomendada más adelante ese año.
