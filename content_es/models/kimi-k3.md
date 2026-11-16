---
title: 'Kimi K3'
name: 'Kimi K3'
slug: 'kimi-k3'
subtitle: 'El modelo de pesos abiertos de 2,8 billones de parámetros de Moonshot, el modelo abierto más grande publicado hasta la fecha'
description: 'El modelo de pesos abiertos de 2,8 billones de parámetros de Moonshot, el modelo abierto más grande publicado hasta la fecha'
company: 'moonshot-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.moonshot.ai/'
price: 'Free'
rank: 8
release_date: '2026-07-16'
param_count: '2.8T (MoE)'
context_window_tokens: 1000000
modality: [text, image, video]
open_weight: true
license: 'Modified MIT'
input_price_usd_per_m: 3
output_price_usd_per_m: 15
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-08-09'
tags: [llm, open-weight, multimodal, reasoning, mixture-of-experts]
extra_model_types: ['Reasoning']
i18n_source: 'bf5cebe9bf5c'
---

Kimi K3 es el lanzamiento más grande de Moonshot AI hasta ahora, un modelo de mezcla de expertos de 2,8 billones de parámetros que la empresa dice que es el modelo de pesos abiertos más grande que nadie ha publicado hasta el momento. Lee texto, imágenes y vídeo de forma nativa, lleva una ventana de contexto de 1 millón de tokens y funciona en un modo de pensamiento siempre activo, en lugar de ofrecer una vía rápida aparte. Moonshot fijó el acceso por API en 3 $ por millón de tokens de entrada (que bajan a 0,30 $ con un acierto de caché) y 15 $ por millón de tokens de salida, bastante por debajo de los modelos cerrados de frontera de los laboratorios occidentales. Los pesos completos llegaron a Hugging Face poco después del anuncio del 16 de julio, con cuantización MXFP4 que deja la descarga en unos 1,4 TB, lo bastante pequeña para que montajes serios de autoalojamiento funcionen sin un clúster dedicado.
