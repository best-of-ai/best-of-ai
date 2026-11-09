---
title: 'MiniCPM'
name: 'MiniCPM'
slug: 'minicpm'
subtitle: 'El modelo pequeño y eficiente de OpenBMB, pensado para ir bien en teléfonos y dispositivos edge'
description: 'El modelo pequeño y eficiente de OpenBMB, pensado para ir bien en teléfonos y dispositivos edge'
company: 'openbmb'
model_type: 'Language'
logo_url: ''
product_url: 'https://github.com/OpenBMB/MiniCPM'
price: 'Free'
rank: 5
release_date: '2024-02-01'
param_count: '2.4B'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, small-model, on-device]
i18n_source: '0dcdb45ddc3c'
---

MiniCPM es un modelo de lenguaje de 2400 millones de parámetros que OpenBMB publicó en febrero de 2024, hecho para ir bien en teléfonos y otros dispositivos edge, donde un modelo completo de 7B o de 13B pesaría demasiado. Pese a su tamaño, OpenBMB informó de que rinde cerca de Mistral 7B en benchmarks generales y por delante de modelos más grandes, como Llama 2 13B y Falcon 40B, en varias tareas, sobre todo en comprensión del chino, matemáticas y código. Una variante aparte de contexto largo, MiniCPM-2B-128k, alarga la ventana de contexto a 128 000 tokens para usos con muchos documentos.

El modelo es de pesos abiertos bajo licencia Apache 2.0 y se distribuye en Hugging Face. Va dirigido a desarrolladores que construyen aplicaciones sin conexión o de bajo coste y necesitan un modelo capaz que quepa en presupuestos ajustados de memoria y de cómputo. Sirvió de base a los modelos multimodales MiniCPM-V posteriores de OpenBMB, y ayudó a fijar el foco del laboratorio en la IA eficiente en el dispositivo, como alternativa a escalarlo todo.
