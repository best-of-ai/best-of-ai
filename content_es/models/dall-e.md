---
title: 'DALL-E'
name: 'DALL-E'
slug: 'dall-e'
subtitle: 'Modelo original de texto a imagen de OpenAI, de 2021'
description: 'Modelo original de texto a imagen de OpenAI, de 2021'
company: 'openai'
model_type: 'Image Generation'
logo_url: ''
product_url: 'https://openai.com/index/dall-e/'
price: 'Paid'
rank: 5
release_date: '2021-01-05'
param_count: '12B'
modality: [text, image]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [image-generation, legacy]
i18n_source: '69880ba7eb3a'
---

DALL-E es el modelo original de texto a imagen de OpenAI, presentado en enero de 2021 como una variante de GPT-3 de 12 000 millones de parámetros entrenada para generar imágenes a partir de pies de foto. Funcionaba tratando la generación de imágenes como un problema de predicción de secuencias: un autoencoder variacional discreto convertía las imágenes en tokens, y un transformer autorregresivo aprendía a predecir esos tokens a partir de un prompt de texto, con un modelo CLIP usado después para ordenar las imágenes resultantes. Se entrenó con unos 250 millones de pares texto-imagen extraídos de internet y podía producir imágenes plausibles de combinaciones de conceptos que nunca había visto juntos, como un sillón con forma de aguacate. DALL-E nunca se publicó como producto público: OpenAI lo mantuvo como preview de investigación y después lo sustituyó por el DALL-E 2, basado en difusión, que producía imágenes más nítidas con una fracción del número de parámetros.
