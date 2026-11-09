---
title: 'GPT-OSS-120B'
name: 'GPT-OSS-120B'
slug: 'gpt-oss-120b'
subtitle: 'El primer modelo de pesos abiertos de OpenAI desde GPT-2, a la altura de o4-mini en muchos benchmarks de razonamiento'
description: 'El primer modelo de pesos abiertos de OpenAI desde GPT-2, a la altura de o4-mini en muchos benchmarks de razonamiento'
company: 'openai'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://openai.com/index/introducing-gpt-oss/'
price: 'Free'
rank: 8
release_date: '2025-08-05'
param_count: '117B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
mmlu_score: 90.0
access_methods: [Self-hosted, API]
runs_at_home: false
platforms: ['Hugging Face', 'Together AI', 'Azure AI Foundry']
date: '2026-07-16'
tags: [llm, reasoning, open-weight, api]
i18n_source: 'caa1902f73b4'
---

GPT-OSS-120B es un modelo de razonamiento de pesos abiertos que OpenAI publicó el 5 de agosto de 2025, su primer modelo abierto desde GPT-2 en 2019. Usa una arquitectura transformer de mezcla de expertos con 117 000 millones de parámetros en total, pero solo unos 5100 millones activos por token, lo que permite ejecutar cargas de razonamiento pesadas en una sola GPU de gama alta, en lugar de los clústeres de varias GPU que necesitarían los modelos densos de tamaño parecido. En el lanzamiento obtuvo alrededor de 90 en MMLU, en el mismo rango que el propio o4-mini de OpenAI en muchos benchmarks de razonamiento y programación, y sale bajo la licencia Apache 2.0, de modo que las empresas pueden alojarlo ellas mismas, hacer fine-tuning y ejecutarlo sin restricciones de uso. OpenAI lo construyó para competir con los lanzamientos abiertos de Meta, Mistral y laboratorios chinos como DeepSeek y el equipo Qwen de Alibaba, que marcaban el ritmo en modelos de pesos abiertos mientras OpenAI seguía cerrado. Está disponible en Hugging Face, Together AI, Azure AI Foundry y la propia API de OpenAI, para organizaciones que quieren tanto el autoalojamiento abierto como un alojamiento gestionado.
