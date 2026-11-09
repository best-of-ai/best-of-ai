---
title: 'Qwen3.8-27B'
name: 'Qwen3.8-27B'
slug: 'qwen3-8-27b'
subtitle: 'Modelo multimodal de pesos abiertos de Alibaba, de un tamaño que cabe en una sola GPU local'
description: 'Modelo multimodal de pesos abiertos de Alibaba, de un tamaño que cabe en una sola GPU local'
company: 'alibaba'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://qwen.ai/'
price: 'Free'
rank: 7
release_date: '2026-08-14'
param_count: '27B'
context_window_tokens: 262144
modality: [text, image, video]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Alibaba Cloud', 'API']
date: '2026-08-17'
tags: [llm, open-weight, multimodal, single-gpu, apache-2.0, local]
i18n_source: '1e091b27bdc3'
---
El equipo Qwen de Alibaba publicó Qwen3.8-27B el 14 de agosto de 2026, con los pesos abiertos disponibles de inmediato bajo la licencia Apache 2.0. Es un modelo denso de 27 000 millones de parámetros, no un diseño de mezcla de expertos, y trabaja con texto, imágenes y vídeo, incluidos diagramas, documentos y vídeo de varias horas. El contexto llega de forma nativa a 262 000 tokens y puede estirarse hasta un millón con el método de escalado YaRN. Alibaba dice que supera al Qwen3.7-Plus, más grande, en programación y tareas de oficina, y que ha afinado la planificación agéntica, de modo que completa tareas de varios pasos con menos supervisión.

El lanzamiento iba dirigido a desarrolladores que quieren un modelo capaz y que quepa en una sola GPU de consumo o de estación de trabajo, no en un clúster de centro de datos, y lo sitúa frente a lanzamientos de Meta y Google igual de orientados al uso local. Alibaba acompañó el anuncio con los pesos abiertos de Qwen3.8-2.4T-A95B, el modelo de clase Max de la misma generación, para que se pueda elegir entre esta versión ligera y un modelo a escala de frontera pensado para cargas agénticas más pesadas.
