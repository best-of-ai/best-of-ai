---
title: 'Kimi-VL'
name: 'Kimi-VL'
slug: 'kimi-vl'
subtitle: 'El modelo de visión y lenguaje de pesos abiertos de Moonshot'
description: 'El modelo de visión y lenguaje de pesos abiertos de Moonshot'
company: 'moonshot-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.moonshot.ai/'
price: 'Free'
rank: 4
release_date: '2025-04-10'
param_count: '16B (2.8B active)'
context_window_tokens: 128000
modality: [text, image]
open_weight: true
license: 'MIT'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, multimodal, vision]
extra_model_types: ['Reasoning']
i18n_source: 'edae211c40fc'
---

Kimi-VL es el modelo de visión y lenguaje de pesos abiertos de Moonshot AI, publicado en abril de 2025. Usa un diseño de mezcla de expertos con 16 000 millones de parámetros en total, pero solo unos 2800 millones activos en su decodificador de lenguaje, lo que mantiene la inferencia barata respecto a su capacidad. El modelo empareja ese decodificador con MoonViT, un codificador de visión de resolución nativa que puede leer imágenes de resolución muy alta sin reducirlas antes, y trata una ventana de contexto de 128 000 tokens para documentos y vídeos largos. Kimi-VL está orientado a tareas al estilo de agentes, como navegar por la pantalla de un ordenador (rinde bien en OSWorld), junto a OCR, razonamiento matemático a partir de imágenes y comparación de varias imágenes. Moonshot también publicó una variante Kimi-VL-Thinking, entrenada con aprendizaje por refuerzo sobre datos de cadena de pensamiento, que extiende el razonamiento del modelo base a horizontes más largos.
