---
title: 'Gemma'
name: 'Gemma'
slug: 'gemma'
subtitle: 'El lanzamiento original de Gemma de pesos abiertos de Google, construido a partir de la misma investigación que Gemini'
description: 'El lanzamiento original de Gemma de pesos abiertos de Google, construido a partir de la misma investigación que Gemini'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://blog.google/technology/developers/gemma-open-models/'
price: 'Free'
rank: 7
release_date: '2024-02-21'
param_count: '7B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Gemma License'
api_available: true
mmlu_score: 64.3
humaneval_score: 32.3
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Google AI Studio']
date: '2026-07-16'
tags: [llm, open-weight, legacy]
i18n_source: 'b40c9be3f894'
---

Gemma es la primera familia de modelos de lenguaje de pesos abiertos de Google, publicada en febrero de 2024 y construida a partir de la misma investigación que se usa dentro de Gemini. Salió en dos tamaños, 2B y 7B, cada uno con un checkpoint base y otro ajustado con instrucciones, entrenados respectivamente con 2 billones y 6 billones de tokens de texto web, matemáticas y código. La ventana de contexto es modesta, 8192 tokens, en la línea de otros modelos de aquella época.

El lanzamiento importó porque dio a los desarrolladores un modelo pequeño de verdad usable, que se podía ejecutar en una sola GPU de consumo o incluso en un portátil, en lugar de depender de una API. Su licencia permite el uso comercial, pero bloquea una lista de usos dañinos que Google especifica, un punto intermedio entre licencias del todo abiertas como Apache 2.0 y las condiciones cerradas de la mayoría de modelos propietarios. Gemma quedó después superado por Gemma 2 y Gemma 3, pero fijó el patrón de nombres y de licencias que Google ha seguido desde entonces.
