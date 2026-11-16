---
title: 'jina-embeddings-v3'
name: 'jina-embeddings-v3'
slug: 'jina-embeddings-v3'
subtitle: 'El modelo de embeddings multilingüe de pesos abiertos de Jina AI'
description: 'El modelo de embeddings multilingüe de pesos abiertos de Jina AI'
company: 'jina-ai'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://jina.ai/embeddings/'
price: 'Free'
rank: 4
release_date: '2024-09-18'
param_count: '570M'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'CC-BY-NC 4.0'
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [embedding, open-weight, retrieval, multilingual]
i18n_source: '881f6947c894'
---

jina-embeddings-v3 es el modelo de embeddings de texto multilingüe de Jina AI, publicado en septiembre de 2024. Tiene 570 millones de parámetros y admite 89 idiomas, con una ventana de contexto de 8192 tokens mediante embeddings de posición rotatorios. El modelo usa adaptadores LoRA específicos de tarea para usos distintos, como recuperación de consulta y documento, agrupación, clasificación y emparejamiento de texto, de modo que un solo conjunto de pesos se adapta a trabajos diferentes sin un reentrenamiento completo. También admite aprendizaje de representaciones Matryoshka, que permite truncar el embedding de salida desde sus 1024 dimensiones por defecto hasta tan solo 32, y conservar la mayor parte de la calidad de recuperación. En el benchmark MTEB, Jina AI informó de que v3 superó a los embeddings propietarios de OpenAI y Cohere en tareas en inglés, y batió a multilingual-e5-large-instruct en tareas multilingües. Se publica bajo licencia CC BY-NC 4.0, que permite el uso gratuito para investigación y evaluación, pero exige una licencia comercial para el uso en producción a escala.
