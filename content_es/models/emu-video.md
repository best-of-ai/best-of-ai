---
title: 'Emu Video'
name: 'Emu Video'
slug: 'emu-video'
subtitle: 'Modelo de texto a vídeo de Meta, construido sobre el generador de imágenes Emu'
description: 'Modelo de texto a vídeo de Meta, construido sobre el generador de imágenes Emu'
company: 'meta-ai'
model_type: 'Video Generation'
logo_url: ''
product_url: 'https://ai.meta.com/blog/emu-text-to-video-generation-image-editing-research/'
price: 'Paid'
rank: 5
release_date: '2023-11-16'
param_count: 'Undisclosed'
modality: [text, video]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [video-generation, research, legacy]
i18n_source: 'd734ff203780'
---

Emu Video es un modelo de investigación de texto a vídeo que Meta presentó en noviembre de 2023, construido sobre el generador de imágenes Emu de Meta. En lugar de generar el vídeo directamente desde un prompt de texto en un solo paso, divide el trabajo en dos: primero usa Emu para generar una imagen fija a partir del prompt y después genera un vídeo condicionado por el texto y por esa imagen. Meta informó de que este enfoque factorizado le permitió saltarse la cascada profunda de modelos separados de la que dependían sistemas anteriores, como Imagen Video de Google y el propio Make-A-Video de Meta, y aun así producir salida de más resolución. En evaluaciones de preferencia humana, Meta dijo que los evaluadores preferían los clips de Emu Video a los de Imagen Video y a los de Make-A-Video la gran mayoría de las veces. Salió como artículo de investigación y demo, no como producto público, y sus técnicas pasaron a funciones de vídeo posteriores de Meta en lugar de publicarse como modelo independiente.
