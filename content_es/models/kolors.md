---
title: 'Kolors'
name: 'Kolors'
slug: 'kolors'
subtitle: 'El modelo de texto a imagen de pesos abiertos de Kuaishou, fuerte con prompts en chino'
description: 'El modelo de texto a imagen de pesos abiertos de Kuaishou, fuerte con prompts en chino'
company: 'kuaishou'
model_type: 'Image Generation'
logo_url: ''
product_url: 'https://github.com/Kwai-Kolors/Kolors'
price: 'Free'
rank: 5
release_date: '2024-07-06'
param_count: '2.6B'
modality: [text, image]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Kuaishou API']
date: '2026-07-16'
tags: [image-generation, open-weight, api]
i18n_source: 'b566c88c4748'
---

Kolors es el modelo de texto a imagen de pesos abiertos de Kuaishou, publicado en julio de 2024. Es un modelo de difusión latente de unos 2600 millones de parámetros, construido sobre una arquitectura U-Net, y usa ChatGLM como codificador de texto en lugar de un codificador al estilo CLIP, lo que le da una ventaja clara al leer y dibujar prompts en chino y texto chino dentro de las imágenes. Genera a una resolución nativa de 1024x1024 y admite varias relaciones de aspecto. Kuaishou lo entrenó con miles de millones de pares texto-imagen y publicó los pesos en GitHub y Hugging Face, gratis para uso de investigación, con un proceso de registro aparte para el despliegue comercial. Junto a modelos como Flux y Stable Diffusion 3, Kolors es uno de los pocos modelos de imagen abiertos de uso amplio que trata bien las escrituras no latinas.
