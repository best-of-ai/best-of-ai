---
title: 'DeepSeek-V2'
name: 'DeepSeek-V2'
slug: 'deepseek-v2'
subtitle: 'Modelo de mezcla de expertos de DeepSeek de 2024 que bajó el precio de la API por debajo de los rivales'
description: 'Modelo de mezcla de expertos de DeepSeek de 2024 que bajó el precio de la API por debajo de los rivales'
company: 'deepseek'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 5
release_date: '2024-05-06'
param_count: '236B (21B active)'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'DeepSeek License'
input_price_usd_per_m: 0.14
output_price_usd_per_m: 0.28
api_available: true
mmlu_score: 78.5
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, mixture-of-experts, legacy]
i18n_source: '988dda9730f9'
---

DeepSeek-V2 es un modelo de lenguaje de mezcla de expertos que DeepSeek publicó en mayo de 2024, con 236 000 millones de parámetros en total y 21 000 millones activos por token. Su aportación técnica principal fue Multi-head Latent Attention, un método para comprimir la caché clave-valor que recortó mucho el uso de memoria y permitió servir bastantes más tokens por segundo que el modelo denso anterior de 67B de DeepSeek, en el mismo hardware. Entrenado con 8,1 billones de tokens y una ventana de contexto de 128K, quedó en un nivel competitivo en MMLU y en benchmarks de programación frente a otros modelos abiertos de la época.

Lo que hizo notable a V2 no fue solo la arquitectura, sino el precio: DeepSeek lanzó su API a una fracción de lo que cobraban rivales chinos y occidentales, y abrió una ronda de bajadas de precios en el sector que los comentaristas de entonces llamaron «guerra de precios». Las técnicas MLA y DeepSeekMoE que aparecieron aquí pasaron a todos los modelos posteriores de DeepSeek, incluidos V3 y R1, y V2 quedó como la base arquitectónica de los lanzamientos de frontera posteriores de la empresa.
