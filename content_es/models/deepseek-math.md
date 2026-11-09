---
title: 'DeepSeek-Math'
name: 'DeepSeek-Math'
slug: 'deepseek-math'
subtitle: 'Modelo de pesos abiertos de DeepSeek especializado en razonamiento matemático'
description: 'Modelo de pesos abiertos de DeepSeek especializado en razonamiento matemático'
company: 'deepseek'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 4
release_date: '2024-02-05'
param_count: '7B'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'DeepSeek License'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, math, reasoning]
i18n_source: 'f4c27d033105'
---

DeepSeekMath es un modelo de 7000 millones de parámetros que DeepSeek construyó de forma específica para el razonamiento matemático, publicado en febrero de 2024 e inicializado a partir de DeepSeek-Coder-Base. Se entrenó con 120 000 millones de tokens relacionados con matemáticas, extraídos de datos web, junto a lenguaje natural y código, y obtuvo un 51,7 % en el benchmark MATH de nivel de competición sin apoyarse en calculadoras ni herramientas externas, un resultado que entonces se acercaba al rendimiento de modelos cerrados mucho más grandes, como Gemini-Ultra y GPT-4. DeepSeek lo publicó en variantes base, ajustada para instrucciones y ajustada con aprendizaje por refuerzo; la versión de RL se entrenó con Group Relative Policy Optimization, un algoritmo que la empresa introdujo en este artículo y reutilizó después en DeepSeek-R1. El modelo tiene una ventana de contexto de 4096 tokens y se dirige a investigadores y desarrolladores que trabajan en tutoría de matemáticas, demostración de teoremas y tareas de razonamiento cuantitativo, y no al chat de propósito general.
