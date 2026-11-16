---
title: 'InternLM2'
name: 'InternLM2'
slug: 'internlm2'
subtitle: 'El modelo fundacional de pesos abiertos del Shanghai AI Lab, con buen contexto largo y razonamiento'
description: 'El modelo fundacional de pesos abiertos del Shanghai AI Lab, con buen contexto largo y razonamiento'
company: 'shanghai-ai-lab'
model_type: 'Language'
logo_url: ''
product_url: 'https://github.com/InternLM/InternLM'
price: 'Free'
rank: 5
release_date: '2024-01-17'
param_count: '20B'
context_window_tokens: 200000
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
mmlu_score: 67.7
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, long-context]
i18n_source: 'e91b498370ff'
---

InternLM2 es un modelo de lenguaje de pesos abiertos del Shanghai AI Laboratory, publicado el 17 de enero de 2024 en tamaños de 7B y 20B, junto a variantes de chat equivalentes. Ambos tamaños admiten una ventana de contexto de 200 000 tokens, alcanzada con un proceso de entrenamiento que empieza en secuencias de 4K tokens y se extiende de forma gradual a 32K y más allá, y el modelo se mantiene bien en pruebas de aguja en un pajar sobre documentos largos a esa longitud. La variante de chat de 20B obtiene 67,7 en MMLU, por delante de varios modelos abiertos de tamaño parecido en el momento del lanzamiento. InternLM2 se entrenó con un corpus multilingüe grande, con fuerza particular en inglés y chino, y se situó como modelo fundacional de propósito general para razonamiento, programación y tareas de contexto largo, antes de que el Shanghai AI Lab lo sustituyera por InternLM2.5 más adelante ese año. Se publica bajo la licencia Apache 2.0 y se distribuye por Hugging Face y el repositorio de GitHub de InternLM.
