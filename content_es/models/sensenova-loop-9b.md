---
title: 'SenseNova Loop-9B'
name: 'SenseNova Loop-9B'
slug: 'sensenova-loop-9b'
subtitle: 'Modelo multimodal de pesos abiertos de 9B de SenseTime que reutiliza sus capas en bucle'
description: 'Modelo multimodal de pesos abiertos de 9B de SenseTime que reutiliza sus capas en bucle'
company: 'sensetime'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.sensetime.com/en/news/sensenova-loop-9b-release-20261118-1435'
price: 'Free'
rank: 5
release_date: '2026-11-17'
param_count: '9B (about 14.6B inference-equivalent)'
context_window_tokens: 512000
modality: [text, image]
open_weight: true
license: 'Open weights'
api_available: true
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'GitHub']
date: '2026-11-24'
tags: [llm, open-weight, multimodal, small-model, self-hosted]
i18n_source: '842af8c2e04b'
---

SenseNova Loop-9B es la versión oficial del modelo multimodal de pesos abiertos de SenseTime, publicada el 17 de noviembre de 2026 tras una vista previa. Tiene unos 9B de parámetros repartidos en 32 capas de decodificador distintas, que se ejecutan como 56 cálculos de capa por pasada, lo que da unos 14,6B de parámetros equivalentes en inferencia. Acepta texto e imágenes, devuelve texto y maneja hasta 512.000 tokens de contexto.

Los pesos de 4 bits ocupan unos 4,9 GB, así que cabe en hardware de consumo, y el día del lanzamiento salió una versión AWQ oficial. SenseTime lo considera comparable a Qwen3.8-27B: 41,36 frente a 44,60 en NL2Repo y 65,31 frente a 65,01 en AIDABench. Los pesos están en Hugging Face como sensenova/sensenova-loop, y el código en GitHub.
