---
title: 'DeepFloyd IF'
name: 'DeepFloyd IF'
slug: 'deepfloyd-if'
subtitle: 'Modelo de texto a imagen en espacio de píxeles (no latente), del laboratorio DeepFloyd respaldado por Stability'
description: 'Modelo de texto a imagen en espacio de píxeles (no latente), del laboratorio DeepFloyd respaldado por Stability'
company: 'stability-ai'
model_type: 'Image Generation'
logo_url: ''
product_url: 'https://stability.ai/news/deepfloyd-if-text-to-image-model'
price: 'Free'
rank: 5
release_date: '2023-04-28'
param_count: '4.3B'
modality: [text, image]
open_weight: true
license: 'Stability Community License'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [image-generation, open-weight, legacy]
i18n_source: 'e6c34510f10f'
---

DeepFloyd IF es un modelo de texto a imagen publicado en abril de 2023 por DeepFloyd, un laboratorio de investigación respaldado por Stability AI. Sigue un enfoque distinto de la difusión en espacio latente de Stable Diffusion: opera de forma directa en el espacio de píxeles a través de una cascada de tres módulos, primero genera una imagen de baja resolución de 64x64 y luego la remuestrea por etapas hasta 1024x1024, lo que le dio fama de renderizar texto legible dentro de las imágenes, una tarea que los modelos de difusión latente de aquella época a menudo estropeaban. DeepFloyd entrenó tres tamaños del módulo base, el mayor con 4300 millones de parámetros, y el proceso completo se publicó como preview de investigación no comercial bajo una Stability Community License, y no bajo una licencia completamente abierta. Nunca se convirtió en un producto de gran público como lo hizo Stable Diffusion, pero sus resultados al renderizar texto influyeron en modelos comerciales posteriores que mejoraron esa misma debilidad.
