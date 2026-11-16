---
title: 'MiniMax-01'
name: 'MiniMax-01'
slug: 'minimax-01'
subtitle: 'El modelo de pesos abiertos de MiniMax de 2025, con una ventana de contexto de 4 millones de tokens'
description: 'El modelo de pesos abiertos de MiniMax de 2025, con una ventana de contexto de 4 millones de tokens'
company: 'minimax-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.minimaxi.com/'
price: 'Free'
rank: 6
release_date: '2025-01-15'
param_count: '456B (45.9B active)'
context_window_tokens: 4000000
modality: [text]
open_weight: true
license: 'Apache 2.0'
input_price_usd_per_m: 0.2
output_price_usd_per_m: 1.1
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, long-context, mixture-of-experts]
extra_model_types: ['Multimodal']
i18n_source: '7af458104dd5'
---

MiniMax-01 es una familia de modelos de pesos abiertos que el laboratorio chino de IA MiniMax publicó en enero de 2025. Junta un modelo de texto (MiniMax-Text-01) y un modelo de visión-lenguaje (MiniMax-VL-01) sobre la misma arquitectura híbrida. Usa un diseño de mezcla de expertos, con 456 000 millones de parámetros en total y unos 45 900 millones activos por token, y mezcla Lightning Attention con atención softmax normal para que las secuencias muy largas salgan viables en cómputo. El rasgo principal es la longitud de contexto: el modelo admite entradas de hasta 4 millones de tokens, muy por encima de lo que soportaban entonces la mayoría de los modelos competidores, mientras que las versiones alojadas por API suelen exponer una ventana de 1 millón de tokens.

MiniMax publicó los pesos bajo licencia Apache 2.0 en Hugging Face y también ofrece el modelo por su propia API, a 0,20 $ por millón de tokens de entrada y 1,10 $ por millón de tokens de salida, por debajo del precio de la mayoría de los modelos de frontera occidentales. Apunta a usos como el análisis de documentos largos, flujos de trabajo de agentes largos y razonamiento a escala de una base de código, donde el límite es la longitud de contexto y no el número bruto de parámetros.
