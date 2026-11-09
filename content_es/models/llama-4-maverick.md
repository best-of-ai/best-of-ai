---
title: 'Llama 4 Maverick'
name: 'Llama 4 Maverick'
slug: 'llama-4-maverick'
subtitle: 'El modelo insignia multimodal de mezcla de expertos y pesos abiertos de Meta'
description: 'El modelo insignia multimodal de mezcla de expertos y pesos abiertos de Meta'
company: 'meta-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 8
release_date: '2025-04-05'
param_count: '400B (17B active)'
context_window_tokens: 1000000
modality: [text, image]
open_weight: true
license: 'Llama 4 Community License'
api_available: true
mmlu_score: 86.0
humaneval_score: 85.0
lmarena_score: 1330
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Together AI', 'AWS Bedrock']
date: '2026-07-16'
tags: [llm, open-weight, multimodal, self-hosted, mixture-of-experts]
i18n_source: '1e256fde4e77'
---

Llama 4 Maverick es el modelo insignia de Meta en la publicación Llama 4 de abril de 2025. Es un modelo de mezcla de expertos con 400 000 millones de parámetros en total, pero solo 17 000 millones activos por token, repartidos en 128 expertos. Es multimodal de forma nativa: se entrenó para tratar texto e imágenes a la vez, en lugar de añadir después un codificador de visión a un modelo de texto, y admite una ventana de contexto de 1 millón de tokens. Meta informó de que Maverick supera a GPT-4o y a Gemini 2.0 Flash en una serie de benchmarks públicos, y de que iguala a DeepSeek V3 en razonamiento y programación usando menos de la mitad de parámetros activos. Se distribuye bajo la Llama 4 Community License, con pesos en Hugging Face y a través de proveedores en la nube como AWS Bedrock y Together AI.
