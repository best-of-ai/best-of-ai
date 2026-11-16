---
title: 'Claude 3.5 Haiku'
name: 'Claude 3.5 Haiku'
slug: 'claude-3-5-haiku'
subtitle: 'Modelo rápido y asequible de Anthropic que iguala al Claude 3 Opus anterior en algunos benchmarks'
description: 'Modelo rápido y asequible de Anthropic que iguala al Claude 3 Opus anterior en algunos benchmarks'
company: 'anthropic'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.anthropic.com/claude/haiku'
price: 'Paid'
rank: 6
release_date: '2024-11-04'
param_count: 'Undisclosed'
context_window_tokens: 200000
modality: [text]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.8
output_price_usd_per_m: 4
api_available: true
humaneval_score: 88.1
lmarena_score: 1240
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['Claude.ai', 'AWS Bedrock', 'API']
date: '2026-07-16'
tags: [llm, low-latency, foundation-model, api]
extra_model_types: ['Code']
i18n_source: '43df5415f16a'
---

Claude 3.5 Haiku es el modelo rápido y de bajo coste de Anthropic en la familia Claude 3.5, publicado en octubre de 2024 junto a un Claude 3.5 Sonnet actualizado. Anthropic lo construyó para sustituir a Claude 3 Haiku como la opción más barata y rápida de la gama, a la vez que cerraba gran parte de la distancia de capacidad con los modelos más grandes: en evaluaciones de programación como SWE-bench Verified, Claude 3.5 Haiku puntuó de forma competitiva con el Claude 3.5 Sonnet original y superó a varios modelos más grandes disponibles en el lanzamiento, y Anthropic informó de un 88,1 % en HumanEval para generación de código.

El modelo conserva la ventana de contexto de 200 000 tokens, estándar en la línea Claude 3.5, y cuesta 0,80 $ por millón de tokens de entrada y 4 $ por millón de tokens de salida, lo que lo situó entre los modelos cercanos a la frontera más baratos del mercado cuando salió. Se dirige a usos de mucho volumen y sensibles a la latencia, como atención al cliente, moderación de contenido y extracción de datos, donde la velocidad de respuesta y el coste por llamada importan más que arañar el último punto de calidad de razonamiento, y está disponible a través de la API de Anthropic, de claude.ai y de plataformas en la nube que incluyen AWS Bedrock.
