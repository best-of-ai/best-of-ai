---
title: 'DeepSeek V3.2'
name: 'DeepSeek V3.2'
slug: 'deepseek-v3-2'
subtitle: 'Actualización de V3.1 de DeepSeek, construida en torno a un mecanismo nuevo de atención dispersa'
description: 'Actualización de V3.1 de DeepSeek, construida en torno a un mecanismo nuevo de atención dispersa'
company: 'deepseek'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 8
release_date: '2025-12-01'
param_count: '685B (MoE)'
context_window_tokens: 163840
modality: [text, code]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 0.21
output_price_usd_per_m: 0.32
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-25'
tags: [llm, open-weight, reasoning, coding, mixture-of-experts]
extra_model_types: ['Code']
i18n_source: 'd6a4a3b7b4f4'
---

DeepSeek V3.2 es la actualización de DeepSeek sobre V3.1, detallada en público el 1 de diciembre de 2025 tras una vista previa experimental en septiembre. Introduce DeepSeek Sparse Attention, un mecanismo de atención dispersa de grano fino que baja el coste de entrenamiento y de inferencia sin perder calidad en tareas de contexto largo, y la variante insignia Speciale lleva unos 685 000 millones de parámetros en un diseño de mezcla de expertos. La ventana de contexto queda en 163 840 tokens, con hasta 64 000 tokens de salida, y DeepSeek informa de resultados de nivel de medalla de oro en los problemas de 2025 de la Olimpiada Internacional de Matemática y de la Olimpiada Internacional de Informática. El precio de la API ronda los 0,21 $ por millón de tokens de entrada y los 0,32 $ por millón de tokens de salida, cerca de la mitad de lo que costaba V3.1-Terminus, sobre todo en la decodificación de contexto largo. Como el resto de la gama de DeepSeek, sale bajo la licencia MIT con los pesos en Hugging Face, y fue la base sobre la que DeepSeek construyó V4-Pro la primavera siguiente.
