---
title: 'DeepSeek-R1-Distill-Llama-70B'
name: 'DeepSeek-R1-Distill-Llama-70B'
slug: 'deepseek-r1-distill-llama-70b'
subtitle: 'Destilación basada en Llama de las trazas de razonamiento de DeepSeek-R1, la variante destilada más grande'
description: 'Destilación basada en Llama de las trazas de razonamiento de DeepSeek-R1, la variante destilada más grande'
company: 'deepseek'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://github.com/deepseek-ai/DeepSeek-R1'
price: 'Free'
rank: 6
release_date: '2025-01-20'
param_count: '70B'
context_window_tokens: 131072
modality: [text]
open_weight: true
license: 'Llama 3.3 Community License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Together AI']
date: '2026-07-16'
tags: [llm, reasoning, open-weight, api]
i18n_source: '875e7d1cacd9'
---

DeepSeek-R1-Distill-Llama-70B es un modelo de razonamiento destilado que DeepSeek publicó junto a DeepSeek-R1 en enero de 2025. En lugar de entrenar un modelo de razonamiento desde cero, DeepSeek hizo fine-tuning de Llama 3.3 70B Instruct de Meta con trazas de razonamiento generadas por el modelo R1 completo, y trasladó gran parte de la capacidad de resolución de problemas por cadena de pensamiento de R1 a una arquitectura más pequeña y más barata de ejecutar. Es la más grande de las seis variantes destiladas de R1 que publicó DeepSeek, sobre modelos base Qwen y Llama de 1,5B hasta 70B de parámetros, y en la publicación obtuvo un 70,0 % de pass@1 en AIME 2024 y un 94,5 % en MATH-500, muy por delante de modelos de uso general como GPT-4o y Claude 3.5 Sonnet en los mismos benchmarks de matemáticas. Lleva una ventana de contexto de 128 000 tokens, heredada de su base Llama 3.3, y se distribuye bajo la Llama 3.3 Community License, con pesos en Hugging Face y acceso por API alojada a través de proveedores que incluyen Together AI.
