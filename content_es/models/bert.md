---
title: 'BERT'
name: 'BERT'
slug: 'bert'
subtitle: 'Encoder bidireccional de Google de 2018 que reorientó la investigación en NLP'
description: 'Encoder bidireccional de Google de 2018 que reorientó la investigación en NLP'
company: 'google'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://github.com/google-research/bert'
price: 'Free'
rank: 6
release_date: '2018-10-11'
param_count: '340M'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [embedding, open-weight, nlp, legacy]
i18n_source: '9489893b9c63'
---

BERT (Bidirectional Encoder Representations from Transformers) es un modelo de lenguaje que Google Research publicó en octubre de 2018, y cambió la forma en que el campo abordaba el preentrenamiento para tareas de NLP. A diferencia de los modelos anteriores, que leían el texto de izquierda a derecha, BERT se entrena con predicción de palabras enmascaradas y predicción de la frase siguiente, lo que le permite construir representaciones que se apoyan en el contexto de las dos direcciones a la vez. Google publicó dos tamaños principales: BERT-base, de 110 millones de parámetros, y BERT-large, de 340 millones, ambos con un límite de 512 tokens, y dejó los pesos disponibles de forma gratuita bajo Apache 2.0 en GitHub y, más tarde, en Hugging Face. Las versiones con fine-tuning de BERT marcaron nuevos récords en once benchmarks distintos de NLP en el lanzamiento, entre ellos respuesta a preguntas e inferencia de lenguaje natural, y en poco tiempo se convirtió en el modelo base habitual para ajustar en tareas como clasificación, reconocimiento de entidades con nombre y ordenación de resultados de búsqueda. En gran parte lo han sustituido encoders más nuevos, como RoBERTa y DeBERTa, y los modelos de embeddings que vinieron después, pero sigue siendo uno de los artículos más citados en NLP y su arquitectura está debajo de una gran parte de los sistemas posteriores basados en encoders.
