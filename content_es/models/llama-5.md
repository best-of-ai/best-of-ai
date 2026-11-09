---
title: 'Llama 5'
name: 'Llama 5'
slug: 'llama-5'
subtitle: 'El siguiente modelo insignia multimodal de pesos abiertos de Meta, para el dispositivo y para el centro de datos'
description: 'El siguiente modelo insignia multimodal de pesos abiertos de Meta, para el dispositivo y para el centro de datos'
company: 'meta-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 9
release_date: '2026-07-14'
param_count: '520B (24B active)'
context_window_tokens: 2000000
modality: [text, image, audio]
open_weight: true
license: 'Llama 4 Community License'
api_available: true
mmlu_score: 89.5
humaneval_score: 90.0
lmarena_score: 1381
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Together AI', 'AWS Bedrock', 'Azure AI Foundry']
date: '2026-07-19'
tags: [llm, open-weight, multimodal, self-hosted, mixture-of-experts]
i18n_source: '47cdfc96510e'
---

Llama 5 es la continuación de Meta de la línea Llama 4 del año pasado. Otra vez sale como modelo de mezcla de expertos, pero escalado a 520 000 millones de parámetros en total, con 24 000 millones activos por token. El salto mayor es la ventana de contexto de 2 millones de tokens, el doble de lo que ofrecía Llama 4 Maverick, y Meta la propone para tareas como ingerir bases de código enteras o transcripciones largas de vídeo de una sola pasada. Trata de forma nativa la entrada de texto, imagen y audio, en lugar de acoplar codificadores a una base solo de texto, y Meta dice que queda ligeramente por encima de Gemini 3.5 Pro y de GPT-5.6 en varios benchmarks abiertos, y que sigue ejecutándose con eficiencia gracias al enrutado disperso de expertos.

Como en las publicaciones anteriores de Llama, los pesos son abiertos bajo la Llama 4 Community License y están disponibles de inmediato en Hugging Face. Socios de alojamiento como Together AI, AWS Bedrock y Azure AI Foundry ofrecen inferencia gestionada para los equipos que no quieren ejecutarlo ellos mismos. Meta sigue sin conceder plenos derechos comerciales a las empresas que superan cierto umbral de usuarios, la misma excepción que aplica desde Llama 2.
