---
title: 'Llama 3.3'
name: 'Llama 3.3'
slug: 'llama-3-3'
subtitle: 'El modelo de 70B y pesos abiertos de Meta, eficiente y a la altura de predecesores más grandes'
description: 'El modelo de 70B y pesos abiertos de Meta, eficiente y a la altura de predecesores más grandes'
company: 'meta-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 7
release_date: '2024-12-06'
param_count: '70B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Llama 3.3 Community License'
api_available: true
mmlu_score: 86.0
humaneval_score: 88.4
lmarena_score: 1270
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Together AI', 'Ollama']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted, foundation-model]
extra_model_types: ['Code']
i18n_source: '00af49010fb3'
---

Llama 3.3 es un modelo solo de texto de 70B que Meta publicó en diciembre de 2024 como sustituto directo de Llama 3.1 70B. Meta lo ajustó con técnicas nuevas de post-entrenamiento, sin añadir parámetros, y acaba igualando o superando al modelo de 405B de la misma familia en seguimiento de instrucciones y matemáticas, pese a ser unas seis veces más pequeño. Las puntuaciones de HumanEval y MMLU mejoraron respecto a Llama 3.1 70B, y los benchmarks independientes muestran que aguanta bien frente a modelos contemporáneos de otros laboratorios en tareas cotidianas. Como cuesta mucho menos de ejecutar que un modelo de 405B, Llama 3.3 70B pasó pronto a ser una opción habitual en plataformas de inferencia como Together AI y Groq, para equipos que quieren una calidad cercana a la del modelo insignia a un precio más bajo.
