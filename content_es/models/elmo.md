---
title: 'ELMo'
name: 'ELMo'
slug: 'elmo'
subtitle: 'Modelo de AI2 de representaciones de palabras contextualizadas en profundidad, anterior a la era de los transformers'
description: 'Modelo de AI2 de representaciones de palabras contextualizadas en profundidad, anterior a la era de los transformers'
company: 'allen-institute-for-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://allenai.org/allennlp/software/elmo'
price: 'Free'
rank: 5
release_date: '2018-02-15'
param_count: '93.6M'
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['AllenNLP']
date: '2026-07-16'
tags: [llm, open-weight, legacy, foundation-model]
i18n_source: 'b789397d7327'
---

ELMo, siglas de Embeddings from Language Models, salió del Allen Institute for AI y de la Universidad de Washington en febrero de 2018, descrito en el artículo «Deep Contextualized Word Representations», de Matthew Peters, Mark Neumann y coautores. En lugar de asignar a cada palabra un único vector fijo, como hacían embeddings anteriores como word2vec y GloVe, ELMo pasa una LSTM bidireccional por la frase y produce una representación de cada palabra que depende del contexto que la rodea, de modo que la misma palabra recibe un vector distinto según cómo se use. Entrenado con unos mil millones de palabras, mejoró los resultados en seis tareas de NLP de la época, entre ellas la respuesta a preguntas y el reconocimiento de entidades con nombre, al incorporarlo como rasgo en modelos ya existentes. ELMo es anterior a la arquitectura transformer y BERT y sus sucesores lo dejaron atrás en gran medida en cerca de un año desde su publicación, pero sigue citándose como uno de los modelos que fijaron las representaciones contextuales de palabras como el enfoque habitual en NLP.
