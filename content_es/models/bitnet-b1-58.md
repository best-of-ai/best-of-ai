---
title: 'BitNet b1.58'
name: 'BitNet b1.58'
slug: 'bitnet-b1-58'
subtitle: 'Modelo de investigación de Microsoft que muestra un rendimiento de LLM competitivo con pesos ternarios de 1,58 bits'
description: 'Modelo de investigación de Microsoft que muestra un rendimiento de LLM competitivo con pesos ternarios de 1,58 bits'
company: 'microsoft'
model_type: 'Language'
logo_url: ''
product_url: 'https://github.com/microsoft/BitNet'
price: 'Free'
rank: 6
release_date: '2024-02-27'
param_count: '2B (2B4T release)'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'GitHub']
date: '2026-07-16'
tags: [llm, open-weight, research, efficiency]
i18n_source: '4d1b2822f6ff'
---

BitNet b1.58 es una línea de investigación de Microsoft sobre modelos de lenguaje construidos con pesos ternarios: cada peso se restringe a -1, 0 o 1, en lugar de los valores habituales en coma flotante de 16 o 32 bits. El artículo original, The Era of 1-bit LLMs, salió en febrero de 2024 y mostró que los modelos entrenados de forma nativa así, y no cuantizados a posteriori, podían igualar a modelos de precisión completa como Llama 2 en tamaños comparables, a la vez que recortaban de forma clara el uso de memoria y la energía de inferencia. Microsoft continuó en abril de 2025 con BitNet b1.58 2B4T, un checkpoint de 2000 millones de parámetros publicado en abierto y entrenado con 4 billones de tokens, cuya huella de memoria fuera de los embeddings ronda los 0,4 GB, muy por debajo de modelos de tamaño parecido como Gemma 3 1B o MiniCPM 2B. Los pesos y el código de inferencia están en GitHub y Hugging Face bajo licencia MIT, y el proyecto destaca menos por ganar a otros modelos en benchmarks que por demostrar que el entrenamiento de 1 bit funciona sin una penalización grande de rendimiento, algo que importa para ejecutar modelos capaces en teléfonos o en dispositivos en el edge.
