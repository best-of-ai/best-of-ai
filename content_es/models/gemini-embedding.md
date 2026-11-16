---
title: 'Gemini Embedding'
name: 'Gemini Embedding'
slug: 'gemini-embedding'
subtitle: 'Modelo unificado de embeddings de texto de Google, construido a partir de Gemini'
description: 'Modelo unificado de embeddings de texto de Google, construido a partir de Gemini'
company: 'google-deepmind'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://ai.google.dev/gemini-api/docs/embeddings'
price: 'Freemium'
rank: 5
release_date: '2025-03-07'
param_count: 'Undisclosed'
context_window_tokens: 2048
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['Google Vertex AI']
date: '2026-07-16'
tags: [embedding, retrieval, api]
i18n_source: '8ad624583fe8'
---

Gemini Embedding es el modelo de embeddings de texto de Google, construido a partir de la familia Gemini y puesto en disponibilidad general a través de la API de Gemini a partir de marzo de 2025. Convierte el texto en una única representación vectorial que los desarrolladores usan para búsqueda, agrupamiento, clasificación y generación aumentada por recuperación, y sustituye a los modelos de embeddings separados anteriores de Google por un modelo unificado entrenado en más de 100 idiomas, más código. Admite Matryoshka Representation Learning, de modo que se puede truncar el embedding por defecto a tamaños más pequeños, como 768 o 256 dimensiones, para ahorrar almacenamiento sin reentrenar nada.

En el lanzamiento encabezó el ranking multilingüe de MTEB con bastante margen sobre el siguiente modelo. Google ha seguido ampliando la línea desde entonces, incluida una versión más nueva que añade soporte nativo de imágenes, audio y vídeo junto al texto, en el mismo espacio vectorial. Se accede por la API de Gemini y por Vertex AI, y se cobra por token de entrada, como el resto de modelos Gemini de Google.
