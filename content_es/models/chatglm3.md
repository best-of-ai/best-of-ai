---
title: 'ChatGLM3'
name: 'ChatGLM3'
slug: 'chatglm3'
subtitle: 'Modelo de diálogo bilingüe de pesos abiertos de tercera generación de Zhipu'
description: 'Modelo de diálogo bilingüe de pesos abiertos de tercera generación de Zhipu'
company: 'zhipu-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.zhipuai.cn/'
price: 'Free'
rank: 4
release_date: '2023-10-27'
param_count: '6B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted, legacy]
i18n_source: '9a38147f22d8'
---

ChatGLM3 es la tercera generación de la línea de modelos de diálogo ChatGLM, construida de forma conjunta por Zhipu AI y el laboratorio KEG de la Universidad de Tsinghua y publicada a finales de octubre de 2023. El modelo base ChatGLM3-6B usa un diseño bilingüe de chino e inglés y añadió un soporte más sólido para llamadas a funciones, ejecución de código y uso de herramientas al estilo de un agente respecto a sus predecesores, junto con una mezcla de preentrenamiento más diversa, con más tokens de entrenamiento y un mejor entrenamiento de alineación. En la publicación, Zhipu informó de que el modelo base de 6B encabezaba otros modelos preentrenados de menos de 10 000 millones de parámetros en decenas de benchmarks de razonamiento, matemáticas, código y conocimiento general.

Zhipu publicó ChatGLM3 en varias variantes de longitud de contexto: el ChatGLM3-6B estándar junto a versiones de contexto más largo de 32K y 128K, para documentos y conversaciones más grandes. El modelo es de pesos abiertos bajo Apache 2.0 y está muy disponible en Hugging Face, lo que lo convierte en una opción habitual para aplicaciones de chat en chino autoalojadas. Zhipu ha pasado después a modelos más nuevos de la serie GLM-4, de mayor escala y con mejores resultados de benchmark, y ahora opera bajo la marca Z.ai, de modo que ChatGLM3 queda como opción heredada, usada sobre todo donde su tamaño menor y el bajo coste de alojamiento importan más que una capacidad de primer nivel.
