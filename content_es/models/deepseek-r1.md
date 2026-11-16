---
title: 'DeepSeek R1'
name: 'DeepSeek R1'
slug: 'deepseek-r1'
subtitle: 'Modelo de razonamiento de DeepSeek que igualó a modelos de frontera cerrados en matemáticas y código'
description: 'Modelo de razonamiento de DeepSeek que igualó a modelos de frontera cerrados en matemáticas y código'
company: 'deepseek'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 8
release_date: '2025-01-20'
param_count: '671B (37B active)'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 0.55
output_price_usd_per_m: 2.19
api_available: true
mmlu_score: 90.8
humaneval_score: 92.0
lmarena_score: 1360
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, reasoning, chain-of-thought]
i18n_source: 'fa3b02ee20e3'
---

DeepSeek R1 es un modelo de razonamiento que el laboratorio chino DeepSeek publicó el 20 de enero de 2025. Usa una arquitectura de mezcla de expertos de 671 000 millones de parámetros, con 37 000 millones activos por token, y parte del entrenamiento fue aprendizaje por refuerzo a gran escala, en lugar de depender solo del fine-tuning supervisado, lo que lo empujó a resolver los problemas paso a paso antes de responder. En el lanzamiento igualó al o1 de OpenAI en benchmarks de matemáticas, programación y ciencias (90,8 en MMLU y cerca de lo más alto entre los modelos de entonces en problemas al estilo de AIME y Codeforces), con pesos abiertos bajo la licencia MIT y un precio de API muy por debajo del de o1.

El lanzamiento armó revuelo bastante más allá de los círculos habituales de investigación en IA: la app de DeepSeek llegó un momento a encabezar la lista del App Store de EE. UU., y la noticia de que un laboratorio chino relativamente pequeño había entrenado un modelo de razonamiento de clase de frontera por una fracción del coste habitual sacudió las acciones del sector. R1 está en la API y en la interfaz de chat de DeepSeek, y con los pesos abiertos también se puede autoalojar: hay muchas copias en Hugging Face y lo sirven proveedores de inferencia de terceros.
