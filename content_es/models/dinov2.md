---
title: 'DINOv2'
name: 'DINOv2'
slug: 'dinov2'
subtitle: 'Modelo de visión autosupervisado de Meta que produce características de imagen de uso general, sin etiquetas'
description: 'Modelo de visión autosupervisado de Meta que produce características de imagen de uso general, sin etiquetas'
company: 'meta-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://ai.meta.com/blog/dino-v2-computer-vision-self-supervised-learning/'
price: 'Free'
rank: 6
release_date: '2023-04-17'
param_count: '1.1B'
modality: [image]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'GitHub']
date: '2026-07-16'
tags: [computer-vision, open-weight, self-supervised]
i18n_source: '35d54331b555'
---

DINOv2 es un modelo de visión por ordenador que Meta AI publicó en abril de 2023, entrenado del todo sin etiquetas sobre un conjunto de datos seleccionado de 142 millones de imágenes llamado LVD-142M. En lugar de aprender a clasificar imágenes en categorías predefinidas, aprende características visuales de uso general por destilación autosupervisada, y esas características acaban funcionando bien en muchas tareas posteriores —clasificación de imágenes, estimación de profundidad, segmentación y recuperación—, a menudo sin fine-tuning alguno. El modelo publicado más grande tiene 1100 millones de parámetros.

Como las características se transfieren tan bien de entrada, DINOv2 se convirtió en una base habitual de otros sistemas de visión por ordenador, también en campos como la imagen médica, donde escasean los datos etiquetados. Meta publicó el código y los pesos bajo la licencia Apache 2.0, y después llegó DINOv3, pero DINOv2 sigue muy usado como extractor general de características visuales.
