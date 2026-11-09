---
title: 'CLIP (LAION variant)'
name: 'CLIP (LAION variant)'
slug: 'clip-laion-variant'
subtitle: 'Modelo de embeddings de visión y lenguaje de pesos abiertos de LAION, un reentrenamiento de CLIP'
description: 'Modelo de embeddings de visión y lenguaje de pesos abiertos de LAION, un reentrenamiento de CLIP'
company: 'laion'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://laion.ai/'
price: 'Free'
rank: 4
release_date: '2022-09-15'
param_count: '428M'
modality: [text, image]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [embedding, open-weight, vision, self-hosted]
i18n_source: '40efbd85bd2a'
---

Esta variante de CLIP es un reentrenamiento de pesos abiertos de la arquitectura CLIP original de OpenAI, producido por LAION y distribuido a través del proyecto open_clip, y no por la propia OpenAI. Usa la columna vertebral del transformer de visión ViT-L/14, tiene unos 428 millones de parámetros y se entrenó con LAION-2B, el subconjunto en inglés de 2000 millones de pares imagen-texto del conjunto más grande LAION-5B, con 384 GPU A100 en el superordenador JUWELS. Como el CLIP original, proyecta imágenes y texto a un espacio de embeddings compartido, de modo que se puede hacer clasificación de imágenes zero-shot, recuperación de imagen y texto y búsqueda por similitud sin ningún fine-tuning específico de la tarea, y llega a cerca de un 75,3 % de precisión zero-shot en ImageNet-1k. Como los pesos se publican bajo una licencia abierta y están alojados en Hugging Face, se ha convertido en un sustituto habitual de los checkpoints CLIP cerrados de OpenAI en procesos de código abierto de búsqueda de imágenes, descripción y arte generativo, incluido su uso como encoder de texto dentro de varias variantes de Stable Diffusion.
