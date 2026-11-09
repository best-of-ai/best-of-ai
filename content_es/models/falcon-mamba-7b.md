---
title: 'Falcon Mamba 7B'
name: 'Falcon Mamba 7B'
slug: 'falcon-mamba-7b'
subtitle: 'Modelo de pesos abiertos de TII construido sobre la arquitectura Mamba de espacio de estados'
description: 'Modelo de pesos abiertos de TII construido sobre la arquitectura Mamba de espacio de estados'
company: 'technology-innovation-institute'
model_type: 'Language'
logo_url: ''
product_url: 'https://falconllm.tii.ae/'
price: 'Free'
rank: 3
release_date: '2024-08-12'
param_count: '7B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'TII Falcon Mamba 7B License 1.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, hybrid-architecture, self-hosted]
i18n_source: '117aa18c3953'
---

Falcon Mamba 7B, publicado por el Technology Innovation Institute en agosto de 2024, fue el primer modelo de lenguaje abierto de 7000 millones sólido construido del todo sobre la arquitectura Mamba de espacio de estados, en lugar de la atención de los transformers. Como no tiene mecanismo de atención, el uso de memoria y la velocidad de inferencia se mantienen constantes cuando las secuencias generadas se alargan, a diferencia de los transformers, cuyo cómputo crece con la longitud del contexto. TII lo entrenó por etapas que llevaron el manejo efectivo de contexto desde 2048 hasta 8192 tokens. En comparaciones de benchmarks igualó o superó a modelos transformer de tamaño parecido, entre ellos Mistral 7B y el Llama 3.1 8B de Meta, y superó a otros modelos que no son transformers, como RecurrentGemma 9B y RWKV-v6. TII distribuye los pesos en Hugging Face bajo su propia licencia Falcon Mamba, dirigida a investigadores y desarrolladores que quieren una alternativa a las arquitecturas basadas en atención para cargas de secuencias largas.
