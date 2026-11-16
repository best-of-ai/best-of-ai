---
title: 'Inkling'
name: 'Inkling'
slug: 'inkling'
subtitle: 'El primer modelo de pesos abiertos del laboratorio Thinking Machines de Mira Murati'
description: 'El primer modelo de pesos abiertos del laboratorio Thinking Machines de Mira Murati'
company: 'thinking-machines'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://thinkingmachines.ai/model-card/inkling/'
price: 'Free'
rank: 6
release_date: '2026-07-15'
param_count: '975B (41B active)'
context_window_tokens: 1000000
modality: [text, image, audio]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Tinker']
date: '2026-07-25'
tags: [llm, open-weight, multimodal, self-hosted]
i18n_source: '010a5c004d85'
---

Inkling es el primer modelo de producción de Thinking Machines Lab, la startup de IA fundada por Mira Murati, antigua CTO de OpenAI. Salió el 15 de julio de 2026 como un modelo de mezcla de expertos multimodal de origen, con 975 000 millones de parámetros en total y 41 000 millones activos por token, preentrenado con 45 billones de tokens de texto, imágenes, audio y vídeo en sistemas Nvidia GB300 NVL72. Los pesos están en Hugging Face, con una ventana de contexto de 1 millón de tokens, mientras que el acceso por la plataforma de fine-tuning Tinker de la empresa queda limitado a 256 000 tokens, y el modelo se publica bajo la licencia Apache 2.0, de modo que se puede ajustar y redistribuir con libertad. En el Artificial Analysis Intelligence Index debutó con una puntuación de 41, lo que lo convirtió en el lanzamiento de pesos abiertos más fuerte de un laboratorio de EE. UU. en aquel momento, y encaja con el objetivo declarado de Thinking Machines: construir modelos ajustados a usuarios concretos, no un sistema único pensado para servir a todo el mundo.
