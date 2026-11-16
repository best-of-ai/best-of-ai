---
title: 'Hunyuan DiT'
name: 'Hunyuan DiT'
slug: 'hunyuan-dit'
subtitle: 'El transformer de difusión de pesos abiertos de Tencent para texto a imagen en chino e inglés'
description: 'El transformer de difusión de pesos abiertos de Tencent para texto a imagen en chino e inglés'
company: 'tencent'
model_type: 'Image Generation'
logo_url: ''
product_url: 'https://github.com/Tencent/HunyuanDiT'
price: 'Free'
rank: 5
release_date: '2024-05-14'
param_count: '1.5B'
modality: [text, image]
open_weight: true
license: 'Tencent Hunyuan License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Tencent Cloud']
date: '2026-07-16'
tags: [image-generation, open-weight, api]
i18n_source: '7a104e51d815'
---

Hunyuan-DiT es el modelo de texto a imagen de pesos abiertos de Tencent, construido sobre una arquitectura de transformer de difusión y no sobre el diseño U-Net que usaban la mayoría de los modelos de difusión anteriores. Tencent lo publicó en mayo de 2024, y empareja un transformer de eliminación de ruido de 1500 millones de parámetros con codificadores de texto CLIP bilingüe y T5 multilingüe, de modo que puede seguir prompts en chino o en inglés con una fidelidad parecida. Ese foco bilingüe es su principal argumento: la mayoría de los modelos abiertos de texto a imagen de entonces trataban mal los prompts en chino, y Hunyuan-DiT se entrenó de forma específica para cerrar esa brecha. Genera imágenes de 1024x1024 e incluye un componente de chat multimodal integrado que permite refinar una imagen a lo largo de varios turnos de diálogo, en lugar de reescribir el prompt entero cada vez. Tencent publicó los pesos en Hugging Face y GitHub bajo su licencia Hunyuan, y después envió una actualización 1.1 que corrigió la sobresaturación y los artefactos de marca de agua del checkpoint original.
