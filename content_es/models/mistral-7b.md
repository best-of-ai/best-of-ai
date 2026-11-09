---
title: 'Mistral 7B'
name: 'Mistral 7B'
slug: 'mistral-7b'
subtitle: 'El modelo compacto original de pesos abiertos de Mistral, que superó a rivales más grandes'
description: 'El modelo compacto original de pesos abiertos de Mistral, que superó a rivales más grandes'
company: 'mistral-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://mistral.ai/news/announcing-mistral-7b/'
price: 'Free'
rank: 6
release_date: '2023-09-27'
param_count: '7B'
context_window_tokens: 32000
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
mmlu_score: 60.1
humaneval_score: 30.5
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Ollama']
date: '2026-07-16'
tags: [llm, open-weight, small-model, self-hosted]
extra_model_types: ['Code']
i18n_source: 'c7cb93d8e531'
---

Mistral 7B es el modelo que dio a conocer a Mistral AI. Se publicó el 27 de septiembre de 2023 como el primer modelo público de la startup francesa. Con 7000 millones de parámetros cabía en una sola GPU de consumo, y aun así superó a Llama 2 13B en todos los benchmarks que probó Mistral, e incluso a Llama 2 34B en varias tareas de razonamiento y de código, con un 60,1 % en MMLU y un 30,5 % en HumanEval. Usa atención de consultas agrupadas (grouped-query attention) y atención de ventana deslizante para que la inferencia sea rápida y gaste poca memoria, con una longitud de contexto de 32 000 tokens.

Mistral lo publicó bajo licencia Apache 2.0, sin restricciones de uso, algo poco habitual entonces para un modelo de esa calidad. Eso ayudó a que se extendiera deprisa por la comunidad de código abierto, a través de Hugging Face y de herramientas como Ollama y llama.cpp. Se convirtió en una base habitual de fine-tunes y merges, y con ese resultado Mistral AI quedó como competidor serio de Meta y de OpenAI a los pocos meses de fundarse la empresa.
