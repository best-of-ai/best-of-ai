---
title: 'Hunyuan Video'
name: 'Hunyuan Video'
slug: 'hunyuan-video'
subtitle: 'El modelo de generación de texto a vídeo de pesos abiertos de Tencent'
description: 'El modelo de generación de texto a vídeo de pesos abiertos de Tencent'
company: 'tencent'
model_type: 'Video Generation'
logo_url: ''
product_url: 'https://aivideo.hunyuan.tencent.com/'
price: 'Free'
rank: 6
release_date: '2024-12-03'
param_count: '13B'
modality: [text, video]
open_weight: true
license: 'Tencent Hunyuan License'
api_available: true
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [video-generation, open-weight, text-to-video]
i18n_source: '840cb7f4cbbc'
---

HunyuanVideo es el modelo de generación de vídeo de pesos abiertos de Tencent, publicado en diciembre de 2024 con unos 13 000 millones de parámetros, lo que lo convirtió en el modelo de vídeo abierto más grande disponible entonces. Genera clips de texto a vídeo y de imagen a vídeo de hasta unos 720p y cinco segundos, con un seguimiento del prompt y una calidad de movimiento que los revisores compararon de forma favorable con modelos cerrados como Runway Gen-3 y Kling. Tencent publicó el código completo de entrenamiento e inferencia junto a los pesos preentrenados en GitHub y Hugging Face, bajo una licencia que permite el uso comercial en la mayoría de las jurisdicciones, algo poco habitual para un modelo de esta escala en el lanzamiento. Los pesos abiertos permiten a investigadores y estudios hacer fine-tuning para estilos o sujetos concretos, en lugar de trabajar solo por una API. Tencent siguió después con HunyuanVideo-1.5, un modelo más pequeño de 8300 millones de parámetros que alcanza una calidad comparable con menos cómputo.
