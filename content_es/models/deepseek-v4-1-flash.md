---
title: 'DeepSeek-V4.1-Flash'
name: 'DeepSeek-V4.1-Flash'
slug: 'deepseek-v4-1-flash'
subtitle: 'El seguimiento más barato de V4-Flash de DeepSeek, con visión y precios por tramos en hora punta'
description: 'El seguimiento más barato de V4-Flash de DeepSeek, con visión y precios por tramos en hora punta'
company: 'deepseek'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://api-docs.deepseek.com/quick_start/pricing/'
price: 'Paid'
rank: 7
release_date: '2026-09-10'
param_count: '552B (MoE)'
context_window_tokens: 1048576
modality: [text, image]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.15
output_price_usd_per_m: 0.60
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['DeepSeek API']
date: '2026-09-18'
tags: [llm, multimodal, api, cost-efficient, moe]
i18n_source: '9bfa801c726b'
---

DeepSeek publicó V4.1-Flash el 10 de septiembre de 2026: un modelo de mezcla de expertos de 552 000 millones de parámetros, con visión nativa y una ventana de contexto de 1 048 576 tokens que llega a 393 216 tokens de salida. El precio se parte entre hora punta y valle: fuera de punta, 0,003 $ por millón de tokens de entrada con acierto de caché, 0,15 $ con fallo de caché y 0,60 $ por millón de tokens de salida; en hora punta (mañanas de días laborables en UTC) es exactamente el doble.

El precio por tramos es DeepSeek con su estrategia de siempre: bajar con fuerza el precio de las API occidentales en las ventanas de poca demanda, para atraer cargas por lotes y las que no dependen de la latencia, y cobrar lo bastante en hora punta como para gestionar la capacidad.
