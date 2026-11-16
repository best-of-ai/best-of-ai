---
title: 'ESM-2'
name: 'ESM-2'
slug: 'esm-2'
subtitle: 'Modelo de lenguaje de proteínas de Meta, usado para predecir la estructura a partir de la secuencia'
description: 'Modelo de lenguaje de proteínas de Meta, usado para predecir la estructura a partir de la secuencia'
company: 'meta-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.meta.com/blog/protein-folding-esmfold-metagenomics/'
price: 'Free'
rank: 6
release_date: '2022-10-31'
param_count: '15B'
modality: [text]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [science, biology, open-weight]
i18n_source: '603d0e8b688e'
---

ESM-2 es un modelo de lenguaje de proteínas de Meta AI, publicado en octubre de 2022, entrenado con unos 250 millones de secuencias de proteínas y sin un paso de alineamiento múltiple de secuencias. Sale en varios tamaños, hasta 15 000 millones de parámetros, el modelo de lenguaje de proteínas más grande en el momento de la publicación, y Meta vio que, al escalar, sus representaciones internas empiezan a codificar información estructural en 3D de las proteínas sin haber sido entrenado de forma explícita para eso. Esa propiedad es la que impulsa ESMFold, el sistema de predicción de estructura de Meta, que lee una secuencia de proteína a través de ESM-2 y convierte la representación resultante directamente en coordenadas atómicas. Se salta las bases de datos de alineamiento de las que dependen herramientas como AlphaFold y hace la predicción de estructura mucho más rápida. Meta publicó los pesos en abierto y usó ESM-2 para construir el ESM Metagenomic Atlas, una base de datos pública de estructuras predichas para cientos de millones de proteínas que hasta entonces no estaban caracterizadas.
