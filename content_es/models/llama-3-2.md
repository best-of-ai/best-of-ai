---
title: 'Llama 3.2'
name: 'Llama 3.2'
slug: 'llama-3-2'
subtitle: 'La primera generación Llama de Meta con niveles de visión y para el dispositivo'
description: 'La primera generación Llama de Meta con niveles de visión y para el dispositivo'
company: 'meta-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 6
release_date: '2024-09-25'
param_count: '90B'
context_window_tokens: 128000
modality: [text, image]
open_weight: true
license: 'Llama 3.2 Community License'
api_available: true
mmlu_score: 86.0
lmarena_score: 1250
access_methods: [Self-hosted, API]
runs_at_home: false
platforms: ['Hugging Face', 'Ollama']
date: '2026-07-16'
tags: [llm, open-weight, multimodal, self-hosted]
extra_model_types: ['Reasoning']
i18n_source: '70c7f383bbf6'
---

Llama 3.2 es la publicación de Meta de septiembre de 2024 que llevó la visión a la línea Llama por primera vez, junto a un conjunto de modelos pequeños solo de texto pensados para teléfonos y dispositivos edge. La variante insignia de visión, de 90B, une un backbone de texto Llama 3.1 con un codificador de imagen entrenado con unos 6000 millones de pares imagen-texto, de modo que puede leer gráficos, describir fotos y responder preguntas sobre una imagen, además de prompts de texto. Meta también publicó modelos ligeros de 1B y 3B en la misma familia, orientados a ejecutarse en local en hardware móvil y no en un centro de datos. En benchmarks de razonamiento, el modelo de 90B rinde cerca de Llama 3.1 70B y añade entrada multimodal. Se distribuye bajo la Llama 3.2 Community License, con los pesos en Hugging Face.
