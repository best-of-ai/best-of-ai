---
title: 'Hy4 Preview'
name: 'Hy4 Preview'
slug: 'hy4-preview'
subtitle: 'El modelo principal de pesos abiertos de Tencent Hunyuan, diseñado junto a sus propias herramientas de desarrollo'
description: 'El modelo principal de pesos abiertos de Tencent Hunyuan, diseñado junto a sus propias herramientas de desarrollo'
company: 'tencent'
model_type: 'Code'
logo_url: ''
product_url: 'https://www.tencent.com/tencent-releases-and-open-sources-tencent-hy4-preview/'
price: 'Paid'
rank: 6
release_date: '2026-08-28'
param_count: '770B (MoE, 49B active)'
context_window_tokens: 1000000
modality: [text, code]
open_weight: true
license: 'Apache 2.0'
input_price_usd_per_m: 0.834
output_price_usd_per_m: 2.501
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Tencent Cloud']
date: '2026-09-18'
tags: [llm, open-weight, code, moe, apache-2.0, agentic]
extra_model_types: ['Reasoning']
i18n_source: '24e04c87a390'
---

Tencent publicó Hy4 Preview en código abierto el 28 de agosto de 2026, un modelo de mezcla de expertos de 770 000 millones de parámetros, con 49 000 millones activos y una ventana de contexto de 1 millón de tokens, bajo Apache 2.0. En lugar de construir un modelo de chat general, el equipo Hunyuan de Tencent lo entrenó con datos de trabajo de ingenieros de software, desarrolladores de juegos, analistas financieros y expertos en seguridad, y lo diseñó junto a los propios productos CodeBuddy y WorkBuddy de la empresa.

En la evaluación ciega interna de Tencent, en la que 163 expertos juzgaron 203 tareas reales de ingeniería, Hy4 Preview obtuvo una media de 2,99 sobre 4,00, por delante de GLM-5.3 con 2,92 y de Kimi K3 con 2,94. El precio de la API es 0,834 $ por millón de tokens de entrada y 2,501 $ por millón de tokens de salida, con la entrada en caché a 0,042 $ por millón.
