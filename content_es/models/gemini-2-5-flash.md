---
title: 'Gemini 2.5 Flash'
name: 'Gemini 2.5 Flash'
slug: 'gemini-2-5-flash'
subtitle: 'El nivel Gemini de Google de baja latencia y coste ajustado'
description: 'El nivel Gemini de Google de baja latencia y coste ajustado'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://deepmind.google/technologies/gemini/'
price: 'Paid'
rank: 7
release_date: '2025-04-17'
param_count: 'Undisclosed'
context_window_tokens: 1000000
modality: [text, image, audio]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.3
output_price_usd_per_m: 2.5
api_available: true
mmlu_score: 84.0
humaneval_score: 82.0
lmarena_score: 1290
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['Gemini app', 'Google Vertex AI', 'API']
date: '2026-07-16'
tags: [llm, low-latency, multimodal, api]
i18n_source: 'd2ed515fd5c9'
---

Gemini 2.5 Flash es el nivel de coste ajustado de la generación 2.5 de Google, publicado en vista previa en abril de 2025 y pasado a disponibilidad general al mes siguiente. Es el primer modelo Flash construido con pensamiento visible desde el principio: puede razonar paso a paso sobre un problema antes de responder, y los desarrolladores pueden fijar un «thinking budget» para equilibrar la calidad de la respuesta con la latencia y el coste. Toma entrada de texto, imagen y audio, y trabaja la misma ventana de contexto de un millón de tokens que su hermano Pro.

Google lo cobra a 0,30 $ por millón de tokens de entrada y 2,50 $ por millón de tokens de salida, con los tokens de pensamiento facturados a la tarifa de salida, y ofrece una variante Flash-Lite aún más recortada para cargas más baratas y sencillas. Ronda el 83 % en MMLU-Pro y rinde bien en benchmarks de programación y matemáticas respecto a su precio, así que es la recomendación por defecto de Google para aplicaciones de alto volumen que no necesitan la profundidad de razonamiento de Pro.
