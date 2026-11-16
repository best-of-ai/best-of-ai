---
title: 'GLM-5'
name: 'GLM-5'
slug: 'glm-5'
subtitle: 'Modelo de frontera de pesos abiertos de Zhipu, entrenado por completo en hardware nacional de Huawei'
description: 'Modelo de frontera de pesos abiertos de Zhipu, entrenado por completo en hardware nacional de Huawei'
company: 'zhipu-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.zhipuai.cn/'
price: 'Free'
rank: 7
release_date: '2026-02-11'
param_count: '~744B (MoE, ~40B active)'
context_window_tokens: 203000
modality: [text, code]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 0.57
output_price_usd_per_m: 1.92
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-25'
tags: [llm, open-weight, coding, self-hosted]
extra_model_types: ['Code']
i18n_source: 'd5e3911c0704'
---

GLM-5 es el modelo de frontera de pesos abiertos de Zhipu AI, publicado el 11 de febrero de 2026 como un salto de escala de cerca del doble respecto a GLM-4.5: pasa de 355 000 millones a unos 744 000 millones de parámetros en total y mantiene unos 40 000 millones activos por token en su diseño de mezcla de expertos. Sale con una ventana de contexto de 203 000 tokens, muy por debajo del millón de tokens que su sucesor GLM-5.2 añadiría cuatro meses después, y Zhipu lo entrenó por completo en chips Huawei Ascend con el framework MindSpore, no en hardware de Nvidia. El precio de la API empieza en 0,57 $ por millón de tokens de entrada y 1,92 $ por millón de tokens de salida, a través de la plataforma propia de Zhipu y de la API de WaveSpeed. Salió bajo la licencia MIT, y la cobertura de entonces lo presentó como el primer modelo de clase de frontera de un laboratorio chino construido sobre hardware totalmente nacional.
