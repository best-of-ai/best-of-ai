---
title: 'FLUX.1 dev'
name: 'FLUX.1 dev'
slug: 'flux-1-dev'
subtitle: 'El nivel de pesos abiertos de FLUX de Black Forest Labs, para uso no comercial'
description: 'El nivel de pesos abiertos de FLUX de Black Forest Labs, para uso no comercial'
company: 'black-forest-labs'
model_type: 'Image Generation'
logo_url: ''
product_url: 'https://blackforestlabs.ai/'
price: 'Free'
rank: 7
release_date: '2024-08-01'
param_count: '12B'
modality: [text, image]
open_weight: true
license: 'FLUX.1 dev Non-Commercial License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Replicate']
date: '2026-07-16'
tags: [image-generation, open-weight, text-to-image, diffusion]
i18n_source: 'e2afd3b7f17c'
---

FLUX.1 dev es el nivel de pesos abiertos de la familia de generación de imágenes FLUX de Black Forest Labs, publicado en agosto de 2024 junto al FLUX.1 Pro cerrado. Black Forest Labs la fundaron antiguos investigadores de Stability AI, entre ellos parte de quienes estuvieron detrás del Stable Diffusion original, y FLUX usa una arquitectura de transformador de rectified flow de 12 000 millones de parámetros, en lugar de los diseños de difusión U-Net habituales en los modelos de texto a imagen anteriores. Dev es una versión destilada con guidance del modelo Pro completo, lo que hace que se ejecute más rápido y conserve la mayor parte de la calidad de imagen y del seguimiento del prompt de su hermano cerrado. Black Forest Labs lo licencia solo para uso no comercial y distribuye los pesos en Hugging Face; las empresas que quieran usarlo con fines comerciales tienen que comprar una licencia aparte a través de BFL. Poco después del lanzamiento se convirtió en uno de los modelos de imagen abiertos con más fine-tuning y remezclas, con mucha adopción en plataformas como Replicate y en herramientas de la comunidad de Stable Diffusion, como ComfyUI.
