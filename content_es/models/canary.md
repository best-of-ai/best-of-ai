---
title: 'Canary'
name: 'Canary'
slug: 'canary'
subtitle: 'Modelo de reconocimiento y traducción de voz multilingüe de NVIDIA'
description: 'Modelo de reconocimiento y traducción de voz multilingüe de NVIDIA'
company: 'nvidia'
model_type: 'Audio Generation'
logo_url: ''
product_url: 'https://huggingface.co/nvidia/canary-1b'
price: 'Free'
rank: 5
release_date: '2024-04-18'
param_count: '1B'
modality: [audio, text]
open_weight: true
license: 'CC-BY-NC 4.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['NVIDIA NIM', 'Hugging Face']
date: '2026-07-16'
tags: [speech-recognition, open-weight, multilingual]
i18n_source: 'ad7707d7cc9a'
---

Canary es una familia de modelos de voz del equipo NeMo de NVIDIA, con el modelo principal Canary-1B publicado en abril de 2024. A diferencia de un modelo de ASR típico, que solo transcribe audio, Canary cubre tanto el reconocimiento de voz como la traducción de voz entre inglés, francés, alemán y español: convierte el audio hablado en texto en el mismo idioma o lo traduce a otro. Combina un encoder FastConformer con un decoder transformer, una arquitectura que NVIDIA ajustó para sacar buena precisión de un modelo comparativamente pequeño, y al lanzarse encabezó el Open ASR Leaderboard de Hugging Face frente a competidores varias veces más grandes.

NVIDIA distribuye Canary-1B a través de Hugging Face y de su framework NeMo para uso autoalojado, y también a través de NVIDIA NIM como API alojada. El Canary-1B original se distribuye bajo licencia CC-BY-NC 4.0, que lo restringe al uso no comercial, aunque NVIDIA ha publicado después variantes más nuevas de Canary, entre ellas Canary-1B-Flash y Canary-1B-v2, bajo la licencia más permisiva CC-BY-4.0, con autorización comercial explícita e inferencia más rápida.
