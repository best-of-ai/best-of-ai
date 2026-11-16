---
title: 'Jamba 1.5 Large'
name: 'Jamba 1.5 Large'
slug: 'jamba-1-5-large'
subtitle: 'El modelo híbrido transformer-Mamba de AI21, pensado para un contexto muy largo'
description: 'El modelo híbrido transformer-Mamba de AI21, pensado para un contexto muy largo'
company: 'ai21-labs'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.ai21.com/jamba/'
price: 'Free'
rank: 5
release_date: '2024-08-22'
param_count: '398B (94B active)'
context_window_tokens: 256000
modality: [text]
open_weight: true
license: 'Jamba Open Model License'
input_price_usd_per_m: 2
output_price_usd_per_m: 8
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: false
platforms: ['Hugging Face', 'AWS Bedrock']
date: '2026-07-16'
tags: [llm, open-weight, long-context, hybrid-architecture]
i18n_source: '53e8093cdb62'
---

Jamba 1.5 Large es el modelo principal de AI21 Labs en la familia Jamba, publicado el 22 de agosto de 2024. Usa una arquitectura híbrida que mezcla bloques de atención Transformer con capas de espacio de estados Mamba en un esquema de mezcla de expertos, lo que le da 398 000 millones de parámetros en total y solo 94 000 millones activos durante la inferencia. Ese diseño le permite una ventana de contexto de 256 000 tokens, de las más largas que ofrecía entonces cualquier modelo con licencia abierta, y mantiene el uso de memoria y el coste de inferencia por debajo de lo que necesitaría un Transformer denso de calidad comparable. AI21 lo fijó en 2 $ por millón de tokens de entrada y 8 $ por millón de tokens de salida por su propia API, y el modelo también se distribuye en Hugging Face y AWS Bedrock bajo la Jamba Open Model License de AI21. Apunta a cargas empresariales como análisis de documentos largos, resumen y generación aumentada por recuperación, y compite en ese segmento con modelos como Mixtral 8x22B y Command R+.
