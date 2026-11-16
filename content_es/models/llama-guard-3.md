---
title: 'Llama Guard 3'
name: 'Llama Guard 3'
slug: 'llama-guard-3'
subtitle: 'El clasificador de seguridad de pesos abiertos de Meta para moderar la entrada y la salida de un LLM'
description: 'El clasificador de seguridad de pesos abiertos de Meta para moderar la entrada y la salida de un LLM'
company: 'meta-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 4
release_date: '2024-07-23'
param_count: '8B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Llama 3.1 Community License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, safety, self-hosted]
i18n_source: 'f0c740f9e81b'
---

Llama Guard 3 es el clasificador de seguridad de Meta, publicado en julio de 2024 junto a Llama 3.1, y sustituyó a Llama Guard 2 como modelo de moderación que Meta recomienda. Construido sobre una base Llama 3.1 de 8B, amplía al anterior con tres categorías de riesgo nuevas, hasta 14 en la taxonomía, y mejora la cobertura de moderación multilingüe. Como Llama Guard 2, va en una canalización y no sirve de asistente independiente: lee un prompt o la respuesta de un modelo y devuelve una etiqueta safe o unsafe, más la categoría incumplida. Es de pesos abiertos bajo la Llama 3.1 Community License, y lo usan mucho las empresas que despliegan LLM de código abierto y necesitan una capa de moderación sin depender de una API de terceros.
