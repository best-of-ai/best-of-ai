---
title: 'Imagen'
name: 'Imagen'
slug: 'imagen'
subtitle: 'El modelo original de difusión de texto a imagen de Google, presentado junto a Parti como vista previa de investigación'
description: 'El modelo original de difusión de texto a imagen de Google, presentado junto a Parti como vista previa de investigación'
company: 'google-deepmind'
model_type: 'Image Generation'
logo_url: ''
product_url: 'https://imagen.research.google/'
price: 'Paid'
rank: 6
release_date: '2022-05-24'
param_count: 'Undisclosed'
modality: [text, image]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [image-generation, research, legacy]
i18n_source: '6e5bc6e9c169'
---

Imagen es el modelo original de difusión de texto a imagen de Google Research, descrito en un artículo titulado «Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding» y publicado en arXiv en mayo de 2022. Empareja un gran modelo de lenguaje congelado, T5, con una cascada de modelos de difusión: un modelo base que genera una imagen pequeña de 64x64, seguido de dos etapas de superresolución que la amplían a 256x256 y después a 1024x1024. El hallazgo central del artículo fue que escalar el codificador de texto mejoraba la calidad de imagen y el ajuste al prompt más que escalar la propia red de difusión de imagen, un resultado que influyó en sistemas posteriores de texto a imagen en todo el sector. Imagen informó de una puntuación FID de referencia de 7,27 en el benchmark COCO, a pesar de no haber entrenado nunca con datos de COCO.

Google nunca publicó Imagen como producto público. Se quedó en una vista previa de investigación, mostrada junto al modelo autorregresivo Parti y comparada con DALL-E 2 de OpenAI, que había salido unos meses antes. El nombre y la línea siguieron en los modelos de imagen comerciales posteriores de Google, Imagen 2, 3 y 4, que se apoyaron en el mismo enfoque de difusión pero añadieron infraestructura de producción, filtrado de seguridad y acceso por API, de lo que carecía el modelo de investigación original.
