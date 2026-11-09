---
title: 'GPT-1'
name: 'GPT-1'
slug: 'gpt-1'
subtitle: 'El modelo del artículo original de 2018 de OpenAI, que introdujo la arquitectura GPT'
description: 'El modelo del artículo original de 2018 de OpenAI, que introdujo la arquitectura GPT'
company: 'openai'
model_type: 'Language'
logo_url: ''
product_url: 'https://openai.com/index/language-unsupervised/'
price: 'Free'
rank: 5
release_date: '2018-06-11'
param_count: '117M'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Research']
date: '2026-07-16'
tags: [llm, legacy, foundation-model]
i18n_source: '99d5a246579a'
---

GPT-1 es el primer Generative Pre-trained Transformer de OpenAI, presentado en un artículo de junio de 2018 titulado «Improving Language Understanding by Generative Pre-Training». Tenía 117 millones de parámetros y se entrenó con BookCorpus, una colección de novelas inéditas, con una ventana de contexto de 512 tokens. La idea central era sencilla: preentrenar un Transformer con texto sin etiquetas y después hacer fine-tuning del mismo modelo en tareas concretas, como la respuesta a preguntas o la implicación textual.

Ese enfoque superó a arquitecturas específicas de cada tarea en 9 de los 12 benchmarks con los que OpenAI lo probó, y ese era el verdadero objetivo del artículo. GPT-1 en sí nunca fue un producto; fue la prueba de que el preentrenamiento generativo seguido de fine-tuning podía ganar a modelos construidos y entrenados por separado para cada tarea. Ese resultado fijó el esquema que OpenAI escaló con GPT-2, GPT-3 y todo lo que vino después.
