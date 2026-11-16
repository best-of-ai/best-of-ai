---
title: 'CLIP'
name: 'CLIP'
slug: 'clip'
subtitle: 'Modelo contrastivo de imagen y texto de OpenAI que está debajo de gran parte de la IA multimodal actual'
description: 'Modelo contrastivo de imagen y texto de OpenAI que está debajo de gran parte de la IA multimodal actual'
company: 'openai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://openai.com/index/clip/'
price: 'Free'
rank: 8
release_date: '2021-01-05'
param_count: '428M'
modality: [text, image]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'GitHub']
date: '2026-07-16'
tags: [multimodal, open-weight, vision, legacy, foundation-model]
i18n_source: 'bc970f441b1f'
---

CLIP (Contrastive Language-Image Pre-training) es un modelo que OpenAI publicó en enero de 2021 y que aprende a emparejar imágenes con descripciones de texto. Se entrenó con 400 millones de pares imagen-texto extraídos de internet, con un objetivo contrastivo que acerca los embeddings de imagen y texto que coinciden y aleja los pares que no coinciden. La variante publicada más grande, construida sobre un transformer de visión ViT-L/14 emparejado con un transformer de texto de 63 millones de parámetros, suma aproximadamente 428 millones de parámetros. En lugar de entrenarse para una tarea estrecha, CLIP aprende un espacio de embeddings conjunto de propósito general para imágenes y texto, lo que le permite hacer clasificación de imágenes zero-shot comparando una imagen con un conjunto de etiquetas de texto, sin fine-tuning específico de la tarea.

El impacto real de CLIP llegó después de la publicación, y no por cifras destacadas de benchmark. Sus encoders de imagen y de texto se convirtieron en la base de una oleada de sistemas posteriores, incluido el proceso de generación de imágenes de DALL-E 2, el condicionamiento por texto de Stable Diffusion y un gran número de herramientas de búsqueda y recuperación de imágenes. Meta, Salesforce y otros laboratorios han publicado sus propias variantes y ajustes de CLIP, pero los pesos originales de OpenAI, publicados bajo licencia MIT en GitHub y Hugging Face, siguen siendo un punto de partida habitual para proyectos multimodales incluso años después de la publicación.
