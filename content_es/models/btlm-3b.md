---
title: 'BTLM-3B'
name: 'BTLM-3B'
slug: 'btlm-3b'
subtitle: 'Modelo compacto de pesos abiertos de Cerebras, ajustado para rendir por encima de su número de parámetros'
description: 'Modelo compacto de pesos abiertos de Cerebras, ajustado para rendir por encima de su número de parámetros'
company: 'cerebras'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.cerebras.ai/blog/btlm-3b-8b-7b-parameter-performance-in-a-3-billion-parameter-model'
price: 'Free'
rank: 4
release_date: '2023-07-24'
param_count: '3B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, small-model]
i18n_source: '2c4fad8daa2c'
---

BTLM-3B-8K es un modelo de lenguaje de 3000 millones de parámetros que Cerebras construyó con la Opentensor Foundation y entrenó en los sistemas CS-2 de escala de oblea de Cerebras. Anunciado en el verano de 2023, se diseñó con un objetivo concreto: igualar la calidad de los modelos de 7000 millones de parámetros y seguir siendo lo bastante pequeño para correr en teléfonos y en dispositivos con poca memoria. Cerebras informa de que BTLM-3B, una vez cuantizado, cabe en unos 3 GB de memoria y se ejecuta en hardware como el iPhone, el Google Pixel e incluso una Raspberry Pi, con un rendimiento en la línea de modelos contemporáneos de 7B como RedPajama-INCITE-7B en benchmarks habituales.

El modelo se entrenó con 627 000 millones de tokens del conjunto SlimPajama, menos de los que usaron entonces varios modelos competidores de 3B, y emplea embeddings de posición ALiBi para admitir una ventana de contexto nativa de 8192 tokens, con una extrapolación razonable más allá de ese punto. Cerebras publicó BTLM-3B bajo Apache 2.0, así que es de uso comercial gratuito, y durante un tiempo tuvo el título de mejor modelo abierto de 3B antes de que modelos pequeños más nuevos de Microsoft, Google y otros lo superaran.
