---
title: 'Hunyuan3D'
name: 'Hunyuan3D'
slug: 'hunyuan3d'
subtitle: 'El modelo de pesos abiertos de Tencent para generar activos 3D a partir de texto o imágenes'
description: 'El modelo de pesos abiertos de Tencent para generar activos 3D a partir de texto o imágenes'
company: 'tencent'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://github.com/Tencent/Hunyuan3D-2'
price: 'Free'
rank: 5
release_date: '2025-01-21'
param_count: '2.6B (shape) + 1.3B (texture)'
modality: [text, image]
open_weight: true
license: 'Tencent Hunyuan License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Tencent Cloud']
date: '2026-07-16'
tags: [3d-generation, open-weight, api]
i18n_source: '07d08c139e5b'
---

Hunyuan3D es el sistema de pesos abiertos de Tencent para convertir prompts de texto o imágenes de referencia en activos 3D. La versión 2.0, muy usada, se publicó en enero de 2025. Divide el trabajo en dos modelos: un generador de forma de 2600 millones de parámetros, construido sobre un transformer de difusión basado en flujo, que produce una malla sin textura, y un modelo de textura de 1300 millones de parámetros que pinta después materiales PBR de alta resolución sobre esa malla. Esa división en dos etapas permite que cada parte se especialice: el modelo de forma se centra solo en la geometría y el de textura trata el color, la respuesta a la luz y el detalle de superficie. Tencent publicó los pesos en Hugging Face y GitHub bajo su licencia Hunyuan, y dio a estudios de juegos y a quienes trabajan en 3D una forma de generar activos en local en lugar de pasar por una API de pago. Compite con otros generadores 3D abiertos y semiabiertos, como TripoSR y TripoSG de Stability AI, y versiones posteriores de Hunyuan3D (2.1, 2.5) empujaron más la fidelidad de textura y el detalle geométrico.
