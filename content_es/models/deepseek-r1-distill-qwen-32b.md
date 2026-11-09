---
title: 'DeepSeek-R1-Distill-Qwen-32B'
name: 'DeepSeek-R1-Distill-Qwen-32B'
slug: 'deepseek-r1-distill-qwen-32b'
subtitle: 'Destilación basada en Qwen de las trazas de razonamiento de DeepSeek-R1, en un modelo abierto más pequeño'
description: 'Destilación basada en Qwen de las trazas de razonamiento de DeepSeek-R1, en un modelo abierto más pequeño'
company: 'deepseek'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://github.com/deepseek-ai/DeepSeek-R1'
price: 'Free'
rank: 6
release_date: '2025-01-20'
param_count: '32B'
context_window_tokens: 131072
modality: [text]
open_weight: true
license: 'MIT'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Together AI']
date: '2026-07-16'
tags: [llm, reasoning, open-weight, api]
i18n_source: '3cf96c55115c'
---

DeepSeek-R1-Distill-Qwen-32B es un modelo denso de 32 000 millones de parámetros que DeepSeek construyó mediante fine-tuning de Qwen2.5-32B con trazas de razonamiento generadas por el modelo DeepSeek-R1 completo. En lugar de entrenar un modelo más pequeño desde cero, DeepSeek destiló las salidas de cadena de pensamiento de R1 en varios modelos base, y la versión Qwen de 32B resultó ser la más sólida del grupo. Superó al o1-mini de OpenAI en benchmarks de matemáticas, programación y ciencia a pesar de su tamaño comparativamente modesto, lo que lo convirtió en uno de los primeros modelos abiertos lo bastante pequeños para correr en una sola GPU de gama alta y, aun así, mostrar capacidad real de razonamiento. Los pesos se publican bajo licencia MIT junto al resto de la familia R1, y el modelo está muy replicado en Hugging Face y lo sirven proveedores de inferencia como Together AI y Groq.

Encaja en un hueco concreto: equipos que quieren un razonamiento paso a paso al estilo de R1 sin pagar ni alojar el modelo completo de 671B. Como es un transformer denso estándar y no un modelo de mezcla de expertos, también es más sencillo de ajustar con fine-tuning y de desplegar que las publicaciones principales de DeepSeek.
