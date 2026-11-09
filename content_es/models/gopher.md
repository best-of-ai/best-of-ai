---
title: 'Gopher'
name: 'Gopher'
slug: 'gopher'
subtitle: 'Modelo de investigación de 280 000 millones de parámetros de DeepMind, que sirvió de base a las leyes de escalado de Chinchilla'
description: 'Modelo de investigación de 280 000 millones de parámetros de DeepMind, que sirvió de base a las leyes de escalado de Chinchilla'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://deepmind.google/discover/blog/language-modelling-at-scale-gopher-ethical-considerations-and-retrieval/'
price: 'Paid'
rank: 6
release_date: '2021-12-08'
param_count: '280B'
context_window_tokens: 2048
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: false
mmlu_score: 60.0
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [llm, research, legacy]
i18n_source: 'adb1e7eb1bf4'
---

Gopher es un modelo de lenguaje de 280 000 millones de parámetros que DeepMind entrenó y describió en un artículo de diciembre de 2021, como parte de un estudio sobre cómo el rendimiento escala con el tamaño. Se entrenó con MassiveText, un corpus de 10,5 terabytes, y se evaluó junto a cinco modelos más pequeños, de 44 millones a 7000 millones de parámetros, para ver cómo mejoraba la capacidad con la escala. En el benchmark MMLU, Gopher sacó un 60 % en un esquema five-shot, un salto claro respecto a los modelos anteriores de la época.

DeepMind nunca publicó Gopher en abierto ni por API; existió solo como herramienta de investigación. Su legado principal vino del análisis posterior, publicado como el artículo de Chinchilla, que usó Gopher y sus hermanos para mostrar que la mayoría de los modelos de lenguaje grandes de aquel periodo estaban infraentrenados respecto a su número de parámetros. Ese hallazgo cambió durante años cómo los laboratorios repartían el cómputo entre el tamaño del modelo y los datos de entrenamiento.
