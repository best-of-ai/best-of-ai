---
title: 'InternLM2.5'
name: 'InternLM2.5'
slug: 'internlm2-5'
subtitle: 'La generación InternLM actualizada del Shanghai AI Lab, con más fuerza en uso de herramientas y razonamiento'
description: 'La generación InternLM actualizada del Shanghai AI Lab, con más fuerza en uso de herramientas y razonamiento'
company: 'shanghai-ai-lab'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://github.com/InternLM/InternLM'
price: 'Free'
rank: 5
release_date: '2024-07-03'
param_count: '7B (1.8B and 20B variants also released)'
context_window_tokens: 1000000
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
mmlu_score: 72.8
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, reasoning, open-weight, long-context]
i18n_source: '4f1fc404afae'
---

InternLM2.5 es la continuación de InternLM2 del Shanghai AI Laboratory, publicada a partir del 3 de julio de 2024 en tamaños de 7B y 1,8B, con una versión de 20B añadida el 1 de agosto de 2024. El modelo de chat de 7B obtiene 72,8 en MMLU y supera a Llama 3 8B Instruct y a Gemma 2 9B en varios benchmarks de razonamiento y matemáticas, según las propias evaluaciones OpenCompass de quien lo desarrolla. Un checkpoint dedicado, 7B-Chat-1M, extiende la ventana de contexto a un millón de tokens y puede localizar hechos concretos dentro de documentos de un millón de tokens en pruebas de aguja en un pajar, mientras que el modelo estándar de 20B llega como máximo a 200K tokens. La serie también añade llamadas a funciones y uso de herramientas al estilo de agentes más fuertes que el InternLM2 original, y todos los pesos se publican bajo la licencia Apache 2.0 en Hugging Face y en el repositorio de GitHub de InternLM.
