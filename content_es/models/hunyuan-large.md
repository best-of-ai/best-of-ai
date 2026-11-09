---
title: 'Hunyuan Large'
name: 'Hunyuan Large'
slug: 'hunyuan-large'
subtitle: 'El modelo de mezcla de expertos y pesos abiertos de Tencent'
description: 'El modelo de mezcla de expertos y pesos abiertos de Tencent'
company: 'tencent'
model_type: 'Language'
logo_url: ''
product_url: 'https://llm.hunyuan.tencent.com/'
price: 'Free'
rank: 5
release_date: '2024-11-05'
param_count: '389B (52B active)'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Tencent Hunyuan License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Tencent Cloud']
date: '2026-07-16'
tags: [llm, open-weight, mixture-of-experts]
i18n_source: '12052bfcac4f'
---

Hunyuan-Large es el modelo de lenguaje de mezcla de expertos y pesos abiertos de Tencent, publicado en noviembre de 2024 con 389 000 millones de parámetros en total y 52 000 millones activados por token. Tencent lo describió en el lanzamiento como el modelo MoE abierto basado en Transformer más grande disponible entonces. Admite una ventana de contexto de 256K y se entrenó con una mezcla de datos sintéticos y reales, orientada a mejorar el razonamiento, la programación y el recuerdo de contexto largo respecto a los modelos Hunyuan densos anteriores de Tencent. La empresa publicó un informe técnico junto a los pesos, con el detalle de sus decisiones de enrutado de expertos y de escala de datos, y lanzó el modelo en Hugging Face bajo la licencia Hunyuan para autoalojamiento, además del acceso por API en Tencent Cloud. Compite de forma directa con otros lanzamientos MoE abiertos y grandes de ese periodo, entre ellos DeepSeek-V2 y la familia Mixtral de Mistral, por la fuerza de un grupo de expertos muy grande respecto al coste de parámetros activos.
