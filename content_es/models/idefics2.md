---
title: 'IDEFICS2'
name: 'IDEFICS2'
slug: 'idefics2'
subtitle: 'El modelo abierto de visión y lenguaje de Hugging Face, pensado para preguntas sobre documentos y gráficos'
description: 'El modelo abierto de visión y lenguaje de Hugging Face, pensado para preguntas sobre documentos y gráficos'
company: 'hugging-face'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://huggingface.co/blog/idefics2'
price: 'Free'
rank: 5
release_date: '2024-04-15'
param_count: '8B'
context_window_tokens: 32768
modality: [text, image]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, vision]
i18n_source: 'd3fac35a3fdd'
---

IDEFICS2 es el modelo abierto de visión y lenguaje de Hugging Face, publicado en abril de 2024 como continuación de su modelo IDEFICS anterior. Tiene 8000 millones de parámetros y combina Mistral-7B como columna de lenguaje con un codificador de visión SigLIP. Procesa las imágenes en su resolución y relación de aspecto nativas, en lugar de forzar todo a un recorte cuadrado fijo. Esa decisión, más el entrenamiento con una mezcla más eficiente de tokens de imagen, le da una ventaja clara en comprensión de documentos, lectura de gráficos y tareas con mucho OCR frente a modelos varias veces más grandes, incluido LLaVA-NeXT-34B. Hugging Face publicó los pesos bajo Apache 2.0, así que queda del todo abierto para uso comercial y fine-tuning sin restricciones de licencia. Está pensado para ejecutarse autoalojado, no por una API alojada, en línea con el empeño más amplio de Hugging Face de mantener referencias abiertas sólidas de visión y lenguaje a disposición de investigadores y desarrolladores.
