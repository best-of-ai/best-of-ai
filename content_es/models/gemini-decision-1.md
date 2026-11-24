---
title: 'Gemini Decision 1'
name: 'Gemini Decision 1'
slug: 'gemini-decision-1'
subtitle: 'Modelo no generativo de Google que puntúa opciones y devuelve confianza en lugar de texto'
description: 'Modelo no generativo de Google que puntúa opciones y devuelve confianza en lugar de texto'
company: 'google-deepmind'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/'
price: 'Paid'
rank: 6
release_date: '2026-11-11'
param_count: 'Undisclosed'
context_window_tokens: 256000
modality: [text, image, audio, video]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.1
output_price_usd_per_m: 0
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['Gemini API', 'Google AI Studio']
date: '2026-11-24'
tags: [classification, decision-model, multimodal, api]
i18n_source: '1bbd28f7737a'
---

Gemini Decision 1 es un modelo de la Decisions API de Google, lanzada el 11 de noviembre de 2026, que no escribe texto. Puntúa opciones en una sola pasada y devuelve una probabilidad y una confianza para cada una. Resuelve preguntas de sí o no, de opción múltiple con de 2 a 255 opciones y puntuación ordenada con rúbrica, con hasta 1.000 preguntas en una sola solicitud. Las entradas pueden ser texto, imágenes, audio, vídeo y PDF, hasta 256.000 tokens.

Google cita una latencia de extremo a extremo de 150 a 250 milisegundos. Cuesta 0,10 $ por millón de tokens de entrada y nada por la salida, y AI Studio tiene un nivel sin coste para prototipos. Google dice que es casi cinco veces más barato que Gemini 3.5 Flash-Lite en el mismo conjunto de pruebas. El ID del modelo es gemini-decision-1, y las integraciones se están desplegando en OpenRouter, LangChain, Vercel y LiteLLM.
