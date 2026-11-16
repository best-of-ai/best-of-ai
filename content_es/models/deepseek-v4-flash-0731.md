---
title: 'DeepSeek-V4-Flash-0731'
name: 'DeepSeek-V4-Flash-0731'
slug: 'deepseek-v4-flash-0731'
subtitle: 'Modelo MoE de 284 000 millones de DeepSeek, con licencia MIT, reentrenado para una programación agéntica más sólida'
description: 'Modelo MoE de 284 000 millones de DeepSeek, con licencia MIT, reentrenado para una programación agéntica más sólida'
company: 'deepseek'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 6
release_date: '2026-07-31'
param_count: '284B (13B active)'
context_window_tokens: 1000000
modality: [text, code]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 0.14
output_price_usd_per_m: 0.28
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'DeepSeek API']
date: '2026-08-09'
tags: [llm, open-weight, code, agentic, mixture-of-experts]
extra_model_types: ['Code']
i18n_source: '247907c6207f'
---

DeepSeek-V4-Flash-0731 saca a DeepSeek-V4-Flash de la vista previa y lo pasa a beta pública como un checkpoint con un nuevo post-entrenamiento, anunciado el 31 de julio de 2026 en el registro de cambios de la API de la empresa. La arquitectura no cambia respecto al debut del modelo en abril: un diseño de mezcla de expertos de 284 000 millones de parámetros, con 13 000 millones activos por token, un experto compartido más 256 expertos enrutados y una ventana de contexto de 1 millón de tokens. Lo que cambia es el proceso de post-entrenamiento: DeepSeek lo reajustó en concreto para programación, uso agéntico de herramientas y razonamiento, y la API admite de forma nativa el formato Responses y funciona con Codex de serie. Sigue con licencia MIT y sin restricciones de acceso, así que los equipos pueden autoalojarlo con fines comerciales sin límites, con unos 110 GB de memoria en cuantización de 3 bits o un nodo 4x GB300 a precisión completa. El precio de la API se mantuvo bajo: 0,14 $ por millón de tokens de entrada y 0,28 $ por millón de tokens de salida.
