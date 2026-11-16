---
title: 'Grok-1'
name: 'Grok-1'
slug: 'grok-1'
subtitle: 'El primer modelo de xAI, después publicado con pesos abiertos bajo Apache 2.0'
description: 'El primer modelo de xAI, después publicado con pesos abiertos bajo Apache 2.0'
company: 'xai'
model_type: 'Language'
logo_url: ''
product_url: 'https://x.ai/blog/grok-os'
price: 'Free'
rank: 5
release_date: '2023-11-04'
param_count: '314B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: false
platforms: ['Hugging Face', 'GitHub']
date: '2026-07-16'
tags: [llm, open-weight, legacy]
i18n_source: '1027c6ce5f38'
---

Grok-1 es el primer gran modelo de lenguaje de xAI, construido por el laboratorio de IA de Elon Musk y ofrecido al principio a suscriptores de X Premium+ desde noviembre de 2023. Es un modelo de mezcla de expertos de 314 000 millones de parámetros, con 8 expertos y enrutado top-2, de modo que solo se activa cerca de una cuarta parte de sus pesos para un token dado, y usa una ventana de contexto de 8192 tokens. xAI publicó los pesos y la arquitectura del modelo base el 17 de marzo de 2024 bajo la licencia Apache 2.0, y Grok-1 pasó a ser el modelo MoE de pesos abiertos más grande disponible entonces de forma pública. La publicación incluía solo los pesos preentrenados en bruto, no una versión ajustada a instrucciones ni lista para chat, así que lo recogieron sobre todo investigadores y equipos de infraestructura, no usuarios finales. xAI entrenó Grok-1 en una pila propia de JAX y Rust, no en PyTorch, y el preentrenamiento había terminado en octubre de 2023, antes de que Grok-2 lo sustituyera más adelante en 2024.
