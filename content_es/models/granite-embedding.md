---
title: 'Granite Embedding'
name: 'Granite Embedding'
slug: 'granite-embedding'
subtitle: 'La familia de modelos de embeddings de texto empresariales de IBM para recuperación'
description: 'La familia de modelos de embeddings de texto empresariales de IBM para recuperación'
company: 'ibm'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://www.ibm.com/granite'
price: 'Free'
rank: 4
release_date: '2024-12-18'
param_count: '278M'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['IBM watsonx', 'Hugging Face']
date: '2026-07-16'
tags: [embedding, open-weight, enterprise]
i18n_source: '623d675b4ebd'
---

Granite Embedding es la familia de modelos de embeddings de texto de IBM para recuperación y búsqueda semántica, pensada para encajar en sistemas RAG empresariales en watsonx o en infraestructura propia. La variante multilingüe de 278 millones de parámetros cubre doce idiomas, entre ellos inglés, alemán, japonés, árabe y chino, y produce vectores de 768 dimensiones a partir de entradas de hasta 512 tokens. IBM lo entrenó con fine-tuning contrastivo, destilación de conocimiento y fusión de modelos, sobre una mezcla de conjuntos abiertos de pares de relevancia y datos propios seleccionados, con preferencia por fuentes de licencia permisiva y apta para empresas. Como el resto de la línea Granite, los modelos de embeddings salen bajo Apache 2.0 y se distribuyen por Hugging Face, Ollama e IBM watsonx. Compiten con otras familias abiertas de embeddings, como BGE y GTE, en benchmarks de recuperación, y ponen el acento en el cumplimiento y en unos datos de entrenamiento trazables para clientes regulados.
