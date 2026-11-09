---
title: 'GTE-large'
name: 'GTE-large'
slug: 'gte-large'
subtitle: 'El modelo general de embeddings de texto de Alibaba para recuperación y similitud semántica'
description: 'El modelo general de embeddings de texto de Alibaba para recuperación y similitud semántica'
company: 'alibaba'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://huggingface.co/thenlper/gte-large'
price: 'Free'
rank: 5
release_date: '2023-08-07'
param_count: '335M'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Alibaba Cloud']
date: '2026-07-16'
tags: [embedding, open-weight, api]
i18n_source: '25ba91e27698'
---

GTE-large es un modelo de embeddings de texto de Alibaba DAMO Academy, publicado en Hugging Face a mediados de 2023 como parte de la familia General Text Embeddings (GTE), junto a variantes más pequeñas GTE-base y GTE-small. Es un codificador al estilo BERT de 335 millones de parámetros, entrenado con aprendizaje contrastivo en varias etapas sobre una mezcla amplia de texto web y de dominio, y produce vectores de 1024 dimensiones a partir de entradas de hasta 512 tokens. El modelo está pensado para recuperación, búsqueda semántica, agrupación y reordenación, y en el lanzamiento puntuó bien en el ranking del benchmark MTEB frente a otros modelos de embeddings abiertos de tamaño parecido, en competencia directa con modelos del estilo BGE y E5 de otros laboratorios chinos. GTE-large es de pesos abiertos bajo Apache 2.0, se ejecuta con facilidad en una sola GPU o en CPU para inferencia y se distribuye por Hugging Face y Alibaba Cloud. Es una opción por defecto habitual para equipos que montan pipelines de RAG y quieren un modelo de embeddings compacto sin depender de una API.
