---
title: 'GPT-4o Realtime'
name: 'GPT-4o Realtime'
slug: 'gpt-4o-realtime'
subtitle: 'Variante de voz a voz y baja latencia de GPT-4o para conversación en directo'
description: 'Variante de voz a voz y baja latencia de GPT-4o para conversación en directo'
company: 'openai'
model_type: 'Audio Generation'
logo_url: ''
product_url: 'https://openai.com/index/introducing-the-realtime-api/'
price: 'Paid'
rank: 7
release_date: '2024-10-01'
param_count: 'Undisclosed'
context_window_tokens: 32000
modality: [audio, text]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 5
output_price_usd_per_m: 20
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['API', 'ChatGPT Advanced Voice']
date: '2026-07-16'
tags: [voice, multimodal, api, real-time]
i18n_source: '507fc668616b'
---

GPT-4o Realtime es una variante de voz a voz de GPT-4o que OpenAI presentó con su Realtime API el 1 de octubre de 2024. En lugar del proceso habitual de transcribir el audio a texto, pasarlo por un modelo de lenguaje y sintetizar de nuevo el habla, procesa el audio de extremo a extremo por una conexión WebSocket o WebRTC, lo que reduce el retardo que hacía que los bots de voz anteriores sonaran rígidos. Impulsa el Advanced Voice Mode de ChatGPT y permite construir agentes telefónicos, asistentes de voz y herramientas de traducción en directo que responden en menos de un segundo. El modelo tiene una ventana de contexto de 32K tokens y cobra 5 $ por millón de tokens de texto de entrada y 20 $ por millón de tokens de texto de salida, con tarifas aparte y más altas para los tokens de audio. Compite con la Gemini Live API de Google y con varias startups centradas en voz que apilan transcripción de la clase Whisper con un modelo de lenguaje, pero su argumento es la arquitectura de un solo modelo y baja latencia, no un proceso ensamblado.
