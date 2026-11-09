---
title: 'Hunyuan-A13B'
name: 'Hunyuan-A13B'
slug: 'hunyuan-a13b'
subtitle: 'El modelo de razonamiento de mezcla de expertos y pesos abiertos de Tencent'
description: 'El modelo de razonamiento de mezcla de expertos y pesos abiertos de Tencent'
company: 'tencent'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://llm.hunyuan.tencent.com/'
price: 'Free'
rank: 4
release_date: '2025-06-27'
param_count: '80B (13B active)'
context_window_tokens: 256000
modality: [text]
open_weight: true
license: 'Tencent Hunyuan License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Tencent Cloud']
date: '2026-07-16'
tags: [llm, open-weight, reasoning, mixture-of-experts]
i18n_source: '1fc3c97bd4e4'
---

Hunyuan-A13B es el modelo de lenguaje de mezcla de expertos y pesos abiertos de Tencent, publicado en junio de 2025 con 80 000 millones de parámetros en total, pero solo 13 000 millones activos por token, lo que deja el coste de inferencia cerca del de un modelo denso mucho más pequeño. Admite de forma nativa una ventana de contexto de 256K, aunque muchos montajes autoalojados la recortan para caber en la memoria de la GPU. El modelo ofrece un diseño de doble modo que permite alternar entre una respuesta rápida y un modo más lento de razonamiento paso a paso para problemas más difíciles de matemáticas, ciencia y programación. Tencent publicó los pesos en Hugging Face bajo su propia licencia Hunyuan, y el modelo también está en la API de Tencent Cloud para equipos que no quieren ejecutarlo ellos mismos. Se sitúa frente a otros modelos abiertos de razonamiento MoE eficientes, como los lanzamientos más pequeños de DeepSeek y Qwen de Alibaba, y compite más por la eficiencia de parámetros activos que por el recuento bruto.
