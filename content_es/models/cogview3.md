---
title: 'CogView3'
name: 'CogView3'
slug: 'cogview3'
subtitle: 'Modelo de texto a imagen de Zhipu basado en difusión por relevos'
description: 'Modelo de texto a imagen de Zhipu basado en difusión por relevos'
company: 'zhipu-ai'
model_type: 'Image Generation'
logo_url: ''
product_url: 'https://github.com/THUDM/CogView3'
price: 'Free'
rank: 5
release_date: '2024-09-29'
param_count: '3B'
modality: [text, image]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Zhipu API']
date: '2026-07-16'
tags: [image-generation, open-weight, api]
i18n_source: 'e06af9d7cbba'
---

CogView3 es un modelo de texto a imagen de Zhipu AI y la Universidad de Tsinghua, descrito en un artículo de investigación de marzo de 2024 y publicado en abierto en Hugging Face en septiembre de 2024. Se construye en torno a la difusión por relevos (relay diffusion), un enfoque en cascada en el que una etapa base de 3000 millones de parámetros genera una imagen de baja resolución de 512x512 y una segunda etapa vuelve a añadir ruido a esa imagen antes de ejecutar encima un pase de difusión de superresolución más corto, en lugar de condicionar la segunda etapa directamente a la salida de baja resolución como hacían los modelos en cascada más antiguos. Zhipu informa de que CogView3 supera a Stable Diffusion XL en evaluaciones humanas por un margen amplio y necesita solo alrededor de la mitad del tiempo de inferencia, y una versión destilada iguala esa calidad usando aproximadamente una décima parte de los pasos de inferencia de SDXL. El modelo y el código se publican bajo Apache 2.0, y Zhipu lo siguió con CogView-3Plus, una variante más grande de transformer de difusión de la misma familia, más una versión alojada a través de la API de Zhipu para quien no quiera ejecutarlo por su cuenta.
