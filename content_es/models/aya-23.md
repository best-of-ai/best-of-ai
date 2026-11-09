---
title: 'Aya 23'
name: 'Aya 23'
slug: 'aya-23'
subtitle: 'Modelo multilingüe de pesos abiertos de Cohere For AI, con cobertura de 23 idiomas'
description: 'Modelo multilingüe de pesos abiertos de Cohere For AI, con cobertura de 23 idiomas'
company: 'cohere'
model_type: 'Language'
logo_url: ''
product_url: 'https://cohere.com/research/aya'
price: 'Free'
rank: 5
release_date: '2024-05-27'
param_count: '35B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'CC-BY-NC 4.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, multilingual]
i18n_source: '7472f170a470'
---

Aya 23 es una familia de modelos de lenguaje multilingües que Cohere For AI, el laboratorio de investigación de Cohere, publicó en mayo de 2024. Cubre 23 idiomas, entre ellos árabe, chino, hindi, japonés, ruso y español, además del inglés. Salió en dos tamaños, 8B y 35B de parámetros, ambos construidos sobre la arquitectura Command de Cohere e inicializados a partir de un checkpoint preentrenado antes de un entrenamiento multilingüe adicional. La versión de 35B es la que se sigue aquí, con una ventana de contexto de 8192 tokens pensada para recuperación y seguimiento de instrucciones en idiomas que los modelos abiertos centrados en el inglés suelen atender peor. Cohere publicó los pesos bajo licencia CC-BY-NC 4.0 con un anexo de uso aceptable, así que es gratuito para investigación y uso no comercial, pero exige un acuerdo comercial aparte para desplegarlo en producción. Siguió al proyecto Aya original, centrado en datos y evaluación para 101 idiomas, y estrechó el alcance a un conjunto menor de idiomas a cambio de más calidad en cada uno.
