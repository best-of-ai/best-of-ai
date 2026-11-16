---
title: 'Emu3'
name: 'Emu3'
slug: 'emu3'
subtitle: 'Modelo de predicción del siguiente token de BAAI que une generación y comprensión de texto, imagen y vídeo'
description: 'Modelo de predicción del siguiente token de BAAI que une generación y comprensión de texto, imagen y vídeo'
company: 'baai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://baai-agents.github.io/Emu3/'
price: 'Free'
rank: 5
release_date: '2024-09-27'
param_count: '8B'
modality: [text, image, video]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, research]
extra_model_types: ['Image Generation']
i18n_source: '6fd97391d2f7'
---

Emu3 es un modelo multimodal de pesos abiertos de la Beijing Academy of Artificial Intelligence, publicado en septiembre de 2024, construido en torno a una sola idea: tratar texto, imágenes y vídeo como secuencias de tokens discretos y entrenar un solo transformer para predecir el siguiente token en los tres, sin un componente aparte de difusión ni al estilo de CLIP. BAAI lo publicó como un modelo de 8000 millones de parámetros en variantes Chat y Gen, una ajustada para la comprensión visión-lenguaje y otra para la generación. Pese al diseño simplificado de un solo objetivo, BAAI informó de que Emu3 superó a modelos abiertos ya establecidos y específicos de cada tarea, entre ellos SDXL en generación de imágenes y LLaVA-1.6 en comprensión visión-lenguaje. El proyecto es anterior al Emu3.5 más grande de BAAI, publicado a finales de 2025, que escala el mismo enfoque de predicción del siguiente token hasta 34 000 millones de parámetros.
