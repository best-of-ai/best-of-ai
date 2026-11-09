---
title: 'DeepSeek-VL'
name: 'DeepSeek-VL'
slug: 'deepseek-vl'
subtitle: 'El primer modelo de visión-lenguaje de DeepSeek, anterior a DeepSeek-VL2'
description: 'El primer modelo de visión-lenguaje de DeepSeek, anterior a DeepSeek-VL2'
company: 'deepseek'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://github.com/deepseek-ai/DeepSeek-VL'
price: 'Free'
rank: 5
release_date: '2024-03-11'
param_count: '7B'
context_window_tokens: 4096
modality: [text, image]
open_weight: true
license: 'DeepSeek License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'DeepSeek API']
date: '2026-07-16'
tags: [multimodal, open-weight, vision, legacy]
i18n_source: '08ae210ac767'
---

DeepSeek-VL es el primer modelo de visión-lenguaje de DeepSeek, publicado el 11 de marzo de 2024 en versiones de 1300 millones y 7000 millones de parámetros. Junta un codificador de visión híbrido, ajustado para imágenes de alta resolución de hasta 1024x1024 píxeles sin un coste de cómputo alto, con un modelo de lenguaje entrenado con una mezcla de capturas de páginas web, datos de OCR, gráficos y documentos, en lugar de limitarse a fotos descritas. Esa mezcla buscaba que sirviera para tareas prácticas, como leer un gráfico o una diapositiva, en lugar de describir solo imágenes genéricas. DeepSeek metió el entrenamiento de visión-lenguaje desde el inicio del preentrenamiento, de modo que el modelo conservó un buen rendimiento solo con texto junto a su grounding visual.

Fue una entrada temprana modesta, pero creíble, en el paso de DeepSeek más allá de los modelos solo de lenguaje, y preparó la arquitectura que DeepSeek amplió más adelante ese mismo año con DeepSeek-VL2, más grande y de mezcla de expertos.
