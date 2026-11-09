---
title: 'BGE-M3'
name: 'BGE-M3'
slug: 'bge-m3'
subtitle: 'Modelo de embeddings de pesos abiertos de BAAI, multilingüe y de varias granularidades'
description: 'Modelo de embeddings de pesos abiertos de BAAI, multilingüe y de varias granularidades'
company: 'baai'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://huggingface.co/BAAI/bge-m3'
price: 'Free'
rank: 4
release_date: '2024-02-06'
param_count: '568M'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'MIT'
api_available: true
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [embedding, open-weight, multilingual, retrieval]
i18n_source: 'dc0d8e73a2f9'
---

BGE-M3 es un modelo de embeddings de texto de BAAI, descrito en un artículo publicado en febrero de 2024. El nombre se refiere a tres cosas que hace a la vez: multilingüismo en más de 100 idiomas, manejo de varias granularidades con entradas de hasta 8192 tokens, y varias funciones, porque produce vectores densos, pesos léxicos dispersos y vectores de tokens al estilo de ColBERT en una sola pasada. Tiene 568 millones de parámetros, una cifra modesta al lado de los LLM grandes, pero está entrenado de forma específica para la recuperación y no para la generación. Esa combinación le permitió marcar, en su momento, los mejores resultados en el benchmark multilingüe MIRACL y en el benchmark entre idiomas MKQA, porque un solo modelo podía sustituir lo que antes exigía sistemas de recuperación densa y dispersa por separado. BAAI lo publicó bajo licencia MIT en Hugging Face, y se usa mucho en procesos de generación aumentada por recuperación que tienen que buscar en documentos de varios idiomas o en documentos más largos que el límite de 512 tokens típico de los modelos de embeddings anteriores basados en BERT.
