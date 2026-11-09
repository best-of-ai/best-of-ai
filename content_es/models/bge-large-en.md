---
title: 'BGE-large-en'
name: 'BGE-large-en'
slug: 'bge-large-en'
subtitle: 'Modelo de embeddings de uso general de BAAI, muy usado para recuperación en inglés'
description: 'Modelo de embeddings de uso general de BAAI, muy usado para recuperación en inglés'
company: 'baai'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://huggingface.co/BAAI/bge-large-en-v1.5'
price: 'Free'
rank: 6
release_date: '2023-09-15'
param_count: '335M'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'MIT'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [embedding, open-weight, api]
i18n_source: 'f70b29aa405b'
---

BGE-large-en-v1.5 es un modelo de embeddings de texto de BAAI, la Beijing Academy of Artificial Intelligence, publicado en septiembre de 2023 como actualización del BGE-large-en original, de unas semanas antes. Tiene 335 millones de parámetros, produce embeddings de 1024 dimensiones y trata secuencias de hasta 512 tokens, así que queda en la misma clase de tamaño que otros encoders a escala de BERT, y no en la de los modelos de embeddings más grandes basados en decoders que llegaron después. La actualización v1.5 corrigió sobre todo un problema de distribución de las puntuaciones de similitud de la publicación original y mejoró la calidad de la recuperación cuando se usa sin un prefijo de instrucción específico de la tarea, que había sido un punto áspero de la v1. BAAI lo publicó bajo licencia MIT, y se convirtió en uno de los modelos de embeddings abiertos más usados para recuperación en inglés y procesos de RAG, en buena parte porque era gratuito, rápido de ejecutar y puntuaba bien en el benchmark MTEB para su tamaño. Desde entonces se le han sumado modelos de BAAI más grandes y capaces, como BGE-M3, pero sigue siendo un valor por defecto habitual para recuperación ligera autoalojada.
