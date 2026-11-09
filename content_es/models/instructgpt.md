---
title: 'InstructGPT'
name: 'InstructGPT'
slug: 'instructgpt'
subtitle: 'El modelo de OpenAI de 2022 que introdujo el ajuste por instrucciones con RLHF a escala'
description: 'El modelo de OpenAI de 2022 que introdujo el ajuste por instrucciones con RLHF a escala'
company: 'openai'
model_type: 'Language'
logo_url: ''
product_url: 'https://openai.com/index/instruction-following/'
price: 'Paid'
rank: 5
release_date: '2022-01-27'
param_count: '175B'
context_window_tokens: 2048
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [API]
runs_at_home: false
platforms: ['API']
date: '2026-07-16'
tags: [llm, foundation-model, legacy, rlhf]
i18n_source: 'e5b0714c6a82'
---

InstructGPT es la versión con fine-tuning de GPT-3 de OpenAI, descrita en el artículo «Training Language Models to Follow Instructions with Human Feedback», de Ouyang et al. OpenAI lo anunció en enero de 2022 y publicó el artículo completo en arXiv en marzo. El equipo lo construyó en tres etapas: recoger demostraciones de buenas respuestas escritas por personas etiquetadoras y hacer fine-tuning de GPT-3 con ellas, reunir clasificaciones humanas de varias salidas del modelo y usar esas clasificaciones para entrenar un modelo de recompensa que guía un fine-tuning adicional mediante aprendizaje por refuerzo. OpenAI entrenó tres tamaños, de 1300 millones, 6000 millones y 175 000 millones de parámetros, todos con la ventana de contexto de 2048 tokens de GPT-3.

El resultado más citado del artículo es que quienes evaluaban preferían las salidas del modelo InstructGPT de 1300 millones a las del GPT-3 base de 175 000 millones, a pesar de que el modelo más pequeño tenía cien veces menos parámetros. Esa brecha mostró que el ajuste con feedback humano importaba más que la escala bruta para producir respuestas que la gente de verdad quería, y redujo las salidas tóxicas y falsas con poco coste para la capacidad general. La técnica que OpenAI desarrolló aquí, el aprendizaje por refuerzo a partir de feedback humano, pasó a ser el método estándar para convertir un modelo de lenguaje en bruto en un asistente usable, y llevó de forma directa a ChatGPT menos de un año después.
