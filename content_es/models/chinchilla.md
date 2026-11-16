---
title: 'Chinchilla'
name: 'Chinchilla'
slug: 'chinchilla'
subtitle: 'Modelo de investigación de DeepMind de 2022 que rehízo las hipótesis de las leyes de escalado para entrenar LLM'
description: 'Modelo de investigación de DeepMind de 2022 que rehízo las hipótesis de las leyes de escalado para entrenar LLM'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://deepmind.google/discover/blog/an-empirical-analysis-of-compute-optimal-large-language-model-training/'
price: 'Paid'
rank: 4
release_date: '2022-03-29'
param_count: '70B'
context_window_tokens: 2048
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: false
mmlu_score: 67.5
access_methods: [Self-hosted]
runs_at_home: false
platforms: []
date: '2026-07-16'
tags: [llm, research, legacy]
i18n_source: '14414c05c298'
---

Chinchilla es un modelo de lenguaje de investigación que DeepMind describió en un artículo de marzo de 2022 sobre entrenamiento óptimo en cómputo. Con 70 000 millones de parámetros es mucho más pequeño que el Gopher anterior de DeepMind, de 280 000 millones, y aun así Chinchilla se entrenó con aproximadamente cuatro veces más datos y superó a Gopher, a GPT-3 y a otros modelos más grandes de la época en un amplio abanico de benchmarks, incluida una puntuación media de MMLU de alrededor del 67,5 %. El hallazgo central del artículo fue que la mayoría de los grandes modelos de lenguaje hasta ese momento estaban infraentrenados respecto a su tamaño: para un presupuesto de cómputo fijo, el tamaño del modelo y los datos de entrenamiento deben escalar juntos, y no solo el tamaño del modelo.

Ese resultado, conocido ahora de forma amplia como la ley de escalado de Chinchilla, cambió la forma en que los laboratorios planearon después las tandas de entrenamiento, y empujó al campo hacia modelos más pequeños entrenados con conjuntos de datos mucho más grandes, en lugar de limitarse a aumentar el número de parámetros. DeepMind nunca publicó los pesos de Chinchilla ni ofreció ningún acceso público: existe solo como artefacto de investigación descrito en el artículo. Su influencia aparece de forma indirecta en casi todos los modelos importantes entrenados desde entonces, de LLaMA a GPT-4, que citan el escalado óptimo en cómputo como parte de su método de entrenamiento.
