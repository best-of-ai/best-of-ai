---
title: 'Kimi K2.6'
name: 'Kimi K2.6'
slug: 'kimi-k2-6'
subtitle: 'El modelo de pesos abiertos de Moonshot para tareas agénticas y de uso de herramientas de larga duración'
description: 'El modelo de pesos abiertos de Moonshot para tareas agénticas y de uso de herramientas de larga duración'
company: 'moonshot-ai'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.moonshot.ai/'
price: 'Free'
rank: 8
release_date: '2026-04-20'
param_count: '1T (32B active)'
context_window_tokens: 256000
modality: [text]
open_weight: true
license: 'Modified MIT'
input_price_usd_per_m: 0.6
output_price_usd_per_m: 2.5
api_available: true
mmlu_score: 88.0
humaneval_score: 87.0
lmarena_score: 1355
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, agentic, reasoning, mixture-of-experts]
extra_model_types: ['Code']
i18n_source: 'f4220c32edb6'
---

Kimi K2.6 es el modelo principal de pesos abiertos de Moonshot AI, publicado en abril de 2026 como sucesor del Kimi K2 original. Es un modelo de mezcla de expertos de un billón de parámetros que activa unos 32 000 millones de parámetros por token, sale de forma nativa en INT4 para una inferencia más barata y trata una ventana de contexto de 262 144 tokens. El modelo está pensado para trabajo agéntico de larga duración: Moonshot lo diseñó alrededor de la orquestación multiagente, sesiones de programación que corren durante horas sin intervención humana y entrada multimodal nativa, no una visión añadida después. Evaluaciones independientes de Artificial Analysis lo sitúan como el modelo de pesos abiertos más fuerte disponible, a pocos puntos de los sistemas cerrados de frontera de OpenAI y Anthropic en tareas como SWE-Bench Pro y Humanity's Last Exam, y a una fracción de su precio por token. Moonshot publica los pesos bajo una licencia MIT modificada, así que cualquiera puede descargar y autoalojar el modelo en lugar de depender de la propia API de Moonshot.
