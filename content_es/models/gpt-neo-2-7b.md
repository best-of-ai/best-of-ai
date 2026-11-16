---
title: 'GPT-Neo 2.7B'
name: 'GPT-Neo 2.7B'
slug: 'gpt-neo-2-7b'
subtitle: 'El primer modelo abierto al estilo GPT-3 de EleutherAI, anterior a GPT-J y GPT-NeoX'
description: 'El primer modelo abierto al estilo GPT-3 de EleutherAI, anterior a GPT-J y GPT-NeoX'
company: 'eleuther-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://huggingface.co/EleutherAI/gpt-neo-2.7B'
price: 'Free'
rank: 4
release_date: '2021-03-21'
param_count: '2.7B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, legacy]
i18n_source: '8f6eeabfc72f'
---

GPT-Neo 2.7B es el modelo de lenguaje de 2700 millones de parámetros de EleutherAI, publicado el 21 de marzo de 2021 junto a versiones más pequeñas de 125M y 1,3B, como los primeros modelos públicos del grupo. Replica la arquitectura de GPT-3 con la biblioteca mesh-tensorflow y se entrenó en the Pile durante unos 420 000 millones de tokens, con una ventana de contexto de 2048 tokens y una capacidad de generación de texto general comparable a los niveles más pequeños de GPT-3 de OpenAI en aquel momento. EleutherAI lo publicó bajo la licencia Apache 2.0 precisamente porque OpenAI no había hecho descargable GPT-3, y quienes investigan y quienes lo usan por afición lo emplearon para todo, desde chatbots hasta herramientas de escritura creativa, en los meses anteriores a que llegaran GPT-J y GPT-NeoX-20B con más parámetros. Es anterior a esos dos lanzamientos posteriores de EleutherAI y hoy tiene sobre todo interés histórico, aunque sigue funcionando con holgura en una sola GPU de consumo, lo que lo mantuvo en uso en proyectos con pocos recursos bastante después de que hubiera modelos abiertos más grandes.
