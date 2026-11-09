---
title: 'Nemotron 5'
name: 'Nemotron 5'
slug: 'nemotron-5'
subtitle: 'El modelo de pesos abiertos de NVIDIA, ajustado para una inferencia eficiente en su propio hardware'
description: 'El modelo de pesos abiertos de NVIDIA, ajustado para una inferencia eficiente en su propio hardware'
company: 'nvidia'
model_type: 'Language'
logo_url: ''
product_url: 'https://developer.nvidia.com/nemotron'
price: 'Free'
rank: 6
release_date: '2026-07-10'
param_count: '70B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'NVIDIA Open Model License'
api_available: true
mmlu_score: 82.0
humaneval_score: 80.0
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'NVIDIA NIM', 'NGC']
date: '2026-07-19'
tags: [llm, open-weight, self-hosted, efficiency]
i18n_source: '528d47e90cc1'
---

Nemotron 5 sigue la línea de modelos de pesos abiertos de NVIDIA, hecha menos para encabezar rankings y más para mostrar lo bien que corren los modelos en las GPU y en la pila de inferencia de la propia empresa. Es un modelo denso de 70 000 millones de parámetros, con una ventana de contexto de 128 000 tokens, distribuido bajo la NVIDIA Open Model License y empaquetado para desplegarlo en un clic con los microservicios NVIDIA NIM, además de la descarga normal en Hugging Face.

NVIDIA usa la línea Nemotron desde Nemotron-4 340B para mostrar técnicas como la poda y la destilación, que reducen los modelos sin hundir la calidad, y Nemotron 5 mantiene ese foco. El tamaño de 70B se eligió para caber en una sola H100, o en un par de GPU de consumo con una cuantización razonable. El argumento de NVIDIA aquí es la pila de hardware y de software que hay debajo del modelo, no el modelo en sí.
