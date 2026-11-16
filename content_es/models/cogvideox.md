---
title: 'CogVideoX'
name: 'CogVideoX'
slug: 'cogvideox'
subtitle: 'Familia de modelos de texto a vídeo de pesos abiertos de Zhipu'
description: 'Familia de modelos de texto a vídeo de pesos abiertos de Zhipu'
company: 'zhipu-ai'
model_type: 'Video Generation'
logo_url: ''
product_url: 'https://github.com/THUDM/CogVideo'
price: 'Free'
rank: 6
release_date: '2024-08-27'
param_count: '5B'
modality: [text, video]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Zhipu API']
date: '2026-07-16'
tags: [video-generation, open-weight, api]
i18n_source: '892ae410997f'
---

CogVideoX es el modelo de texto a vídeo de pesos abiertos de Zhipu AI, construido con el laboratorio KEG de la Universidad de Tsinghua y publicado en agosto de 2024 como sucesor del proyecto CogVideo original. Sale en variantes de 2B y 5B de parámetros, con un VAE causal 3D para la compresión espacial y temporal junto a un transformer con LayerNorm adaptativa de expertos, y admite texto a vídeo, imagen a vídeo y continuación de vídeo a partir de un solo fotograma o de un prompt. El modelo de 5B genera clips de hasta 10 segundos, a una resolución de hasta 768p y 16 fotogramas por segundo, y Zhipu publicó después una actualización CogVideoX-1.5 en noviembre de 2024, con salida más larga y de mayor resolución. Los pesos se publican bajo Apache 2.0 y están alojados en Hugging Face, y Zhipu también sirve los modelos a través de su propia API, así que CogVideoX funciona tanto como modelo abierto autoalojado como servicio alojado, de un modo parecido a cómo Stability AI y Runway sitúan sus generadores de vídeo.
