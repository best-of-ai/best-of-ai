---
title: 'Falcon 3'
name: 'Falcon 3'
slug: 'falcon-3'
subtitle: 'Familia de pesos abiertos de modelos pequeños y eficientes de TII'
description: 'Familia de pesos abiertos de modelos pequeños y eficientes de TII'
company: 'technology-innovation-institute'
model_type: 'Language'
logo_url: ''
product_url: 'https://falconllm.tii.ae/'
price: 'Free'
rank: 4
release_date: '2024-12-17'
param_count: '10B'
context_window_tokens: 32000
modality: [text]
open_weight: true
license: 'Falcon License'
api_available: false
mmlu_score: 73.1
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, small-model, self-hosted]
i18n_source: 'c646be262a46'
---

Falcon 3 es una familia de modelos de lenguaje de pesos abiertos del Technology Innovation Institute de Abu Dabi, publicada en diciembre de 2024 en cuatro tamaños: 1000, 3000, 7000 y 10 000 millones de parámetros, cada uno con versiones base e instruct. TII construyó la línea para que corriera en hardware modesto, incluida una sola GPU o un portátil, y aun así compitiera con modelos abiertos más grandes. El modelo de 10 000 millones encabezó el ranking de Hugging Face de modelos por debajo de 13 000 millones de parámetros en el lanzamiento, con 73,1 en MMLU y 83,1 en GSM8K, por delante de variantes comparables de Llama y Gemma de entonces. La mayoría de tamaños admite una ventana de contexto de 32K tokens (el de 1000 millones se queda en 8K), y TII distribuye los pesos en Hugging Face bajo su propia Falcon License para uso autoalojado. Falcon 3 siguió a los lanzamientos anteriores de Falcon y Falcon Mamba, y refleja el giro de TII hacia modelos más pequeños y baratos de ejecutar, en lugar de perseguir recuentos de parámetros de frontera.
