---
title: 'Gemini 1.5 Flash'
name: 'Gemini 1.5 Flash'
slug: 'gemini-1-5-flash'
subtitle: 'El nivel Gemini 1.5 de Google, rápido y de bajo coste, destilado a partir de Gemini 1.5 Pro'
description: 'El nivel Gemini 1.5 de Google, rápido y de bajo coste, destilado a partir de Gemini 1.5 Pro'
company: 'google-deepmind'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://deepmind.google/technologies/gemini/flash/'
price: 'Paid'
rank: 7
release_date: '2024-05-14'
param_count: 'Undisclosed'
context_window_tokens: 1000000
modality: [text, image, audio, video]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.075
output_price_usd_per_m: 0.3
api_available: true
mmlu_score: 78.9
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['Google AI Studio', 'Vertex AI', 'Gemini app']
date: '2026-07-16'
tags: [llm, multimodal, api, low-cost]
i18n_source: '33dfe5878945'
---

Gemini 1.5 Flash es el nivel rápido y de bajo coste de la generación Gemini 1.5 de Google, publicado en mayo de 2024 como versión destilada de Gemini 1.5 Pro. Google lo construyó enseñando a un modelo más pequeño a imitar las salidas de Pro, lo que conservó gran parte de la capacidad de razonamiento de Pro y recortó con claridad la latencia y el coste. Lleva la misma ventana de contexto de un millón de tokens que Pro y trabaja texto, imágenes, audio y vídeo, así que es una opción práctica para tareas de alto volumen, como resumir documentos largos o describir vídeo, donde el precio de Pro se acumularía rápido.

En el lanzamiento, Google lo puso a 0,075 $ por millón de tokens de entrada y 0,30 $ por millón de tokens de salida para prompts por debajo de 128 000 tokens, entre los precios de API de clase de frontera más baratos de entonces. Está en Google AI Studio, Vertex AI y la app Gemini, y se convirtió en el nivel gratuito por defecto para muchos usuarios de la app. Google ha movido la mayor parte del desarrollo nuevo a las generaciones Flash 2.0 y 2.5, así que 1.5 Flash se mantiene sobre todo por compatibilidad de la API con versiones anteriores.
