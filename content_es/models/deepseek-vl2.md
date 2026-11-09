---
title: 'DeepSeek-VL2'
name: 'DeepSeek-VL2'
slug: 'deepseek-vl2'
subtitle: 'Modelo de visión-lenguaje de mezcla de expertos y pesos abiertos de DeepSeek'
description: 'Modelo de visión-lenguaje de mezcla de expertos y pesos abiertos de DeepSeek'
company: 'deepseek'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 5
release_date: '2024-12-13'
param_count: '27B (4.5B active)'
context_window_tokens: 4096
modality: [text, image]
open_weight: true
license: 'DeepSeek License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, multimodal, vision]
i18n_source: 'f06b4bb46852'
---

DeepSeek-VL2 es una familia de modelos de visión-lenguaje que DeepSeek publicó el 13 de diciembre de 2024, como continuación del DeepSeek-VL original de ese mismo año. Sale en tres tamaños, Tiny, Small y el VL2 completo, con 3000, 16 000 y 27 000 millones de parámetros en total y 1000, 2800 y 4500 millones activos, respectivamente, y usa la misma arquitectura DeepSeekMoE y Multi-head Latent Attention que impulsa los modelos de lenguaje de DeepSeek. Un método de tiling dinámico le permite procesar imágenes de alta resolución con distintas relaciones de aspecto sin perder detalle, lo que ayuda en tareas como leer documentos densos, gráficos y capturas de pantalla.

El diseño de mezcla de expertos hace que DeepSeek-VL2 rinda bien en benchmarks de respuesta a preguntas visuales, OCR y grounding visual, y que la inferencia siga barata respecto a su número total de parámetros, porque para cada entrada solo se activa una pequeña parte de los expertos. Los tres tamaños salieron con pesos abiertos, y DeepSeek-VL2 quedó como una de las familias de modelos multimodales abiertos más capaces de aquel momento.
