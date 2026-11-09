---
title: 'Devstral'
name: 'Devstral'
slug: 'devstral'
subtitle: 'Modelo de pesos abiertos de Mistral, ajustado para programación agéntica y exploración de bases de código'
description: 'Modelo de pesos abiertos de Mistral, ajustado para programación agéntica y exploración de bases de código'
company: 'mistral-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://mistral.ai/news/devstral/'
price: 'Free'
rank: 6
release_date: '2025-05-21'
param_count: '24B'
context_window_tokens: 128000
modality: [text, code]
open_weight: true
license: 'Apache 2.0'
input_price_usd_per_m: 0.1
output_price_usd_per_m: 0.3
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Mistral API']
date: '2026-07-16'
tags: [code, open-weight, agentic, api]
i18n_source: '10cd7f3fca31'
---

Devstral es un modelo de código de 24 000 millones de parámetros que Mistral AI publicó el 21 de mayo de 2025, hecho en colaboración con All Hands AI, el equipo del framework de agentes OpenHands. A diferencia de la mayoría de modelos de código, ajustados sobre todo para autocompletado o generación en un solo turno, Devstral está entrenado en concreto para programación agéntica: explorar una base de código en varios archivos, usar herramientas y completar tareas de ingeniería de software de varios pasos. En SWE-bench Verified sacó un 46,8 %, por delante de todos los modelos abiertos disponibles en el lanzamiento e incluso de algunos propietarios más grandes.

Mistral publicó los pesos bajo la licencia Apache 2.0, y el modelo es lo bastante pequeño para ejecutarse en una sola GPU de consumo de gama alta, lo que lo convirtió en una base habitual para agentes de programación en local. Mistral publicó después Devstral Small 1.1 y el Devstral 2, más grande, cada uno con puntuaciones más altas en SWE-bench, pero el Devstral original sigue siendo relevante como uno de los primeros modelos de pesos abiertos hechos en concreto para ingeniería de software agéntica, y no para completar código de uso general.
