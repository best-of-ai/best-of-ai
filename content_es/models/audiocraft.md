---
title: 'AudioCraft'
name: 'AudioCraft'
slug: 'audiocraft'
subtitle: 'Framework de código abierto de Meta para generar música y efectos de sonido'
description: 'Framework de código abierto de Meta para generar música y efectos de sonido'
company: 'meta-ai'
model_type: 'Audio Generation'
logo_url: ''
product_url: 'https://ai.meta.com/blog/audiocraft-musicgen-audiogen-encodec-generative-ai-audio/'
price: 'Free'
rank: 6
release_date: '2023-08-02'
param_count: '300M-3.3B (MusicGen), 1.5B (AudioGen)'
modality: [audio, text]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['GitHub']
date: '2026-07-16'
tags: [audio, open-weight, music-generation]
i18n_source: '0ed2f655dea3'
---

AudioCraft es una biblioteca de código que Meta publicó en agosto de 2023 y que agrupa tres modelos generativos de audio: MusicGen para generar música a partir de texto, AudioGen para efectos de sonido ambientales y EnCodec, el códec de audio neuronal del que ambos dependen para convertir las formas de onda en tokens. MusicGen llega en varios tamaños (300M, 1,5B y 3,3B de parámetros), con variantes que también pueden seguir una melodía junto a un prompt de texto, mientras que AudioGen se distribuye como un modelo de 1,5B de parámetros entrenado con efectos de sonido y no con música. Meta publicó el código y los pesos bajo licencia MIT, lo que convirtió a AudioCraft en uno de los primeros kits completamente abiertos para generar audio a partir de texto, frente a sistemas cerrados de empresas como Google. Los checkpoints más pequeños corren en una sola GPU de consumo, y se ha convertido en una base habitual de proyectos de generación musical de código abierto y de investigación sobre síntesis de audio controlable.
