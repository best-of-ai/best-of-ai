---
title: 'Cohere Embed Multilingual v3'
name: 'Cohere Embed Multilingual v3'
slug: 'cohere-embed-multilingual-v3'
subtitle: 'Modelo de embeddings de Cohere ajustado para recuperación en más de 100 idiomas'
description: 'Modelo de embeddings de Cohere ajustado para recuperación en más de 100 idiomas'
company: 'cohere'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://cohere.com/blog/introducing-embed-v3'
price: 'Paid'
rank: 6
release_date: '2023-11-02'
param_count: 'Undisclosed'
context_window_tokens: 512
modality: [text]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.1
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['Cohere API']
date: '2026-07-16'
tags: [embedding, api, multilingual]
i18n_source: '5c2674ca56c9'
---

Cohere Embed Multilingual v3 es un modelo de embeddings de texto que Cohere publicó en noviembre de 2023 para búsqueda, generación aumentada por recuperación y tareas de similitud semántica en más de 100 idiomas. Toma texto de entrada de hasta 512 tokens y produce por defecto un vector de 1024 dimensiones, con soporte de embeddings más cortos de 384 o 768 dimensiones cuando un equipo quiere una búsqueda más rápida o un coste de almacenamiento menor. Cohere lo entrenó junto a un hermano solo en inglés, Embed English v3, y presentó ambos como mejora respecto a la v2 porque ponderan los pasajes por lo relevantes que es probable que sean, y no solo por lo parecidos que son, lo que reduce los resultados de recuperación ruidosos en los procesos de RAG. Cuesta 0,10 $ por millón de tokens a través de la API de Cohere y también se distribuye en los marketplaces de AWS, Azure y Oracle Cloud. Cohere ha publicado después modelos Embed v4 más nuevos, y algunos proveedores en la nube, como Oracle, listan ahora la v3 como opción heredada o en desuso, aunque sigue disponible a través de la propia API de Cohere y de Hugging Face.
