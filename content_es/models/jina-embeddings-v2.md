---
title: 'Jina Embeddings v2'
name: 'Jina Embeddings v2'
slug: 'jina-embeddings-v2'
subtitle: 'El modelo de embeddings de Jina AI, notable por una ventana de contexto de 8k tokens en el lanzamiento'
description: 'El modelo de embeddings de Jina AI, notable por una ventana de contexto de 8k tokens en el lanzamiento'
company: 'jina-ai'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://jina.ai/news/jina-embeddings-2-the-best-solution-for-embedding-long-documents/'
price: 'Free'
rank: 5
release_date: '2023-10-30'
param_count: '137M'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Jina API']
date: '2026-07-16'
tags: [embedding, open-weight, api, legacy]
i18n_source: '9b381be032d7'
---

Jina Embeddings v2 es un modelo de embeddings de texto de Jina AI, publicado en octubre de 2023. Salió en dos tamaños principales, una versión small de 33 millones de parámetros y una versión base de 137 millones, ambas sobre una arquitectura BERT modificada que usa codificación de posición ALiBi en lugar de embeddings posicionales estándar. Esa decisión le permitió tratar secuencias de hasta 8192 tokens, algo poco habitual entonces en un modelo de embeddings abierto, y competir con el text-embedding-ada-002 propietario de OpenAI en la recuperación de documentos largos siendo mucho más pequeño. El modelo se publica bajo licencia Apache 2.0 y se puede ejecutar en local o por la API de Jina. Desde entonces lo ha sustituido jina-embeddings-v3, que añade soporte multilingüe y adaptadores por tarea, pero v2 sigue en uso para recuperación en inglés, donde su tamaño menor es una ventaja.
