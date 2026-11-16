---
title: 'Qwen3.8-Flash-Next'
name: 'Qwen3.8-Flash-Next'
slug: 'qwen3-8-flash-next'
subtitle: 'Vista previa de pesos abiertos de Alibaba de su arquitectura Qwen4'
description: 'Vista previa de pesos abiertos de Alibaba de su arquitectura Qwen4'
company: 'alibaba'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://qwen.ai/'
price: 'Free'
rank: 7
release_date: '2026-08-26'
param_count: '125B (6B active)'
context_window_tokens: 262144
modality: [text, image, video]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Alibaba Cloud', 'API']
date: '2026-09-05'
tags: [llm, open-weight, multimodal, moe, apache-2.0, cost-efficient]
i18n_source: '6dac4a7632ca'
---
Alibaba publicó Qwen3.8-Flash-Next en código abierto el 26 de agosto de 2026, para que se pudiera ver la arquitectura Qwen4 antes de la familia completa de modelos. Es un modelo multimodal de mezcla de expertos con un backbone de 125 000 millones de parámetros, de los que solo 6000 millones están activos por token, más una tabla de embeddings n-gram de 51 000 millones de parámetros y un módulo de predicción multi-token de 4000 millones de parámetros. El contexto llega de forma nativa a 262 144 tokens y se extiende a un millón. Alibaba dice que supera al Qwen3.7-Plus anterior, sobre todo en programación y tareas de oficina, y que entrenarlo cuesta cerca de una novena parte y ejecutarlo cerca de una doceava parte. En el lanzamiento se publicaron un checkpoint estándar y otro FP8.
