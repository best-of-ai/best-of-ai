---
title: 'AudioLM'
name: 'AudioLM'
slug: 'audiolm'
subtitle: 'Framework de Google para generar habla realista y continuaciones de audio'
description: 'Framework de Google para generar habla realista y continuaciones de audio'
company: 'google-deepmind'
model_type: 'Audio Generation'
logo_url: ''
product_url: 'https://google-research.github.io/seanet/audiolm/examples/'
price: 'Paid'
rank: 5
release_date: '2022-09-07'
param_count: 'Undisclosed'
modality: [audio]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [audio, research, legacy]
i18n_source: '944df39235b8'
---

AudioLM es un framework de investigación que Google publicó en septiembre de 2022. Trata la generación de audio como un problema de modelado de lenguaje sobre tokens de audio discretos, en lugar de los enfoques habituales de regresión sobre espectrogramas o formas de onda. Combina dos representaciones: tokens semánticos de w2v-BERT, un modelo de habla auto-supervisado, que capturan la estructura a largo plazo, y tokens acústicos del códec neuronal SoundStream, que conservan el detalle fino del audio para una síntesis de alta calidad. Entrenado solo con audio en bruto, sin transcripciones ni anotaciones, puede continuar unos segundos de habla o de piano de un modo que se mantiene coherente durante decenas de segundos, algo con lo que los métodos anteriores de generación de audio tenían dificultades. Google nunca lo publicó como producto: se quedó en un artículo de investigación y una página de demostración, y Google DeepMind usó su enfoque basado en tokens como pieza de trabajos posteriores como MusicLM y partes de Lyria.
