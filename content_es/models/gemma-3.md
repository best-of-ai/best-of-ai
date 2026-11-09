---
title: 'Gemma 3'
name: 'Gemma 3'
slug: 'gemma-3'
subtitle: 'Familia de modelos de pesos abiertos de Google, construida a partir de la investigación de Gemini'
description: 'Familia de modelos de pesos abiertos de Google, construida a partir de la investigación de Gemini'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.google.dev/gemma'
price: 'Free'
rank: 7
release_date: '2025-03-12'
param_count: '27B'
context_window_tokens: 128000
modality: [text, image]
open_weight: true
license: 'Gemma License'
api_available: true
mmlu_score: 78.0
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Google Vertex AI']
date: '2026-07-16'
tags: [llm, open-weight, small-model, self-hosted]
i18n_source: '053632cde4ac'
---

Gemma 3 es la tercera generación de modelos de pesos abiertos de Google, construida con investigación y tecnología del proyecto Gemini 2.0. Sale en cuatro tamaños, 1B, 4B, 12B y 27B, cada uno como checkpoint base y como versión ajustada con instrucciones. Los modelos de 4B, 12B y 27B aceptan texto e imágenes, mientras que el de 1B es solo texto, y todos los tamaños trabajan más de 140 idiomas, con buen soporte de entrada para más de 35. La longitud de contexto llega a 128 000 tokens en los modelos más grandes, un salto grande respecto a los 8192 tokens de Gemma 2.

Google sitúa Gemma 3 como lo bastante pequeño para correr en un solo host de GPU o TPU y aun así competir con modelos cerrados mucho más grandes en benchmarks habituales. La variante de 27B, según los informes, supera a Gemini 1.5 Pro en varias evaluaciones, y las pruebas independientes la dejan claramente por delante del Gemma 2 27B anterior. Como los pesos se pueden descargar bajo la licencia Gemma, los desarrolladores lo usan para despliegue en local, fine-tuning y aplicaciones en el edge, allí donde enviar datos a una API alojada no es una opción.
