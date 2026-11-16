---
title: 'Gemini 1.5 Pro'
name: 'Gemini 1.5 Pro'
slug: 'gemini-1-5-pro'
subtitle: 'El modelo de Google de 2024 que introdujo la ventana de contexto de 1 millón de tokens'
description: 'El modelo de Google de 2024 que introdujo la ventana de contexto de 1 millón de tokens'
company: 'google-deepmind'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://deepmind.google/technologies/gemini/'
price: 'Paid'
rank: 6
release_date: '2024-02-15'
param_count: 'Undisclosed'
context_window_tokens: 1000000
modality: [text, image, audio, video]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 1.25
output_price_usd_per_m: 5
api_available: true
mmlu_score: 85.9
humaneval_score: 71.9
lmarena_score: 1260
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['Gemini app', 'Google Vertex AI', 'API']
date: '2026-07-16'
tags: [llm, multimodal, long-context, api, legacy]
extra_model_types: ['Code']
i18n_source: 'eceffcd944e2'
---

Gemini 1.5 Pro es el modelo que llevó las ventanas de contexto de un millón de tokens a una API de uso generalizado. Google lo publicó en febrero de 2024 y lo pasó a disponibilidad general en mayo de ese año. Lee texto, imágenes, audio y vídeo en un solo prompt, y Google mostró que podía tener en contexto una hora entera de vídeo o cientos de páginas de documentos a la vez, bastante más allá de lo que ofrecían entonces GPT-4 o Claude. Usa una arquitectura de mezcla de expertos que, según Google, le permitía igualar o superar al Gemini 1.0 Ultra, más grande, en la mayoría de benchmarks, y correr más barato.

Google bajó el precio de 1.5 Pro dos veces durante 2024, hasta quedar cerca de 1,25 $ por millón de tokens de entrada y 5 $ por millón de tokens de salida para prompts por debajo de 128 000 tokens. Sacó alrededor de 85,9 en MMLU y 71,9 en HumanEval, y fue el modelo de producción por defecto de Google durante la mayor parte de 2024, a través de la app Gemini, Vertex AI y la API de Gemini. Google lo sustituyó como insignia por Gemini 2.5 Pro en 2025, aunque 1.5 Pro sigue disponible en la API para integraciones ya existentes.
