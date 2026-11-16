---
title: 'Falcon 7B'
name: 'Falcon 7B'
slug: 'falcon-7b'
subtitle: 'El nivel compacto de Falcon de TII, que ayudó a extender el lanzamiento original'
description: 'El nivel compacto de Falcon de TII, que ayudó a extender el lanzamiento original'
company: 'technology-innovation-institute'
model_type: 'Language'
logo_url: ''
product_url: 'https://falconllm.tii.ae/'
price: 'Free'
rank: 5
release_date: '2023-05-25'
param_count: '7B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, small-model, legacy]
i18n_source: '61f475ea6988'
---

Falcon 7B es el hermano pequeño del lanzamiento original de Falcon de TII, entrenado con el mismo conjunto de datos RefinedWeb que Falcon 40B, pero dimensionado para un despliegue más barato en una sola GPU. TII lo entrenó durante unas dos semanas a principios de 2023 y lo publicó bajo la licencia permisiva Apache 2.0, que permite usarlo, modificarlo y desplegarlo con fines comerciales sin regalías. Ese movimiento de licencia llamó la atención entonces, porque muchos modelos abiertos comparables llevaban restricciones solo para investigación. Falcon 7B comparte la arquitectura transformer solo decodificadora del modelo de 40B, con multiquery attention, pero con una ventana de contexto de 2048 tokens y menos requisitos de cómputo, y fue una opción habitual para experimentos de fine-tuning y usos en el dispositivo en 2023 y principios de 2024. TII ha pasado después a las familias Falcon 3 y Falcon Mamba, y Falcon 7B queda como un modelo legado, todavía muy replicado en Hugging Face.
