---
title: 'Llama 4 Scout'
name: 'Llama 4 Scout'
slug: 'llama-4-scout'
subtitle: 'El nivel Llama 4 de Meta, más pequeño y más rápido, con una ventana de contexto de 10 millones de tokens'
description: 'El nivel Llama 4 de Meta, más pequeño y más rápido, con una ventana de contexto de 10 millones de tokens'
company: 'meta-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 7
release_date: '2025-04-05'
param_count: '109B (17B active)'
context_window_tokens: 10000000
modality: [text, image]
open_weight: true
license: 'Llama 4 Community License'
api_available: true
mmlu_score: 80.5
lmarena_score: 1290
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Together AI']
date: '2026-07-16'
tags: [llm, open-weight, multimodal, long-context, self-hosted]
i18n_source: 'a01f39772dca'
---

Llama 4 Scout es el hermano menor en la publicación Llama 4 de Meta de abril de 2025: un modelo de mezcla de expertos con 109 000 millones de parámetros en total y 17 000 millones activos por token, repartidos en 16 expertos. Lo que más lo distingue es la longitud de contexto: Scout admite hasta 10 millones de tokens, muy por encima de lo que ofrecían otros modelos disponibles en abierto en el lanzamiento, lo que encaja con tareas como resumir una base de código entera o una colección larga de documentos en una sola pasada. Como Maverick, es multimodal de forma nativa y se entrenó para procesar texto e imágenes juntos. Meta lo situó como una opción más rápida y más barata que aun así supera a modelos como Gemma 3 y Gemini 2.0 Flash-Lite en benchmarks públicos, y cuantizado cabe en una sola GPU H100, lo que lo hizo popular para despliegues autoalojados.
