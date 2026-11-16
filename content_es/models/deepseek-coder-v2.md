---
title: 'DeepSeek Coder V2'
name: 'DeepSeek Coder V2'
slug: 'deepseek-coder-v2'
subtitle: 'Modelo de mezcla de expertos de pesos abiertos de DeepSeek, especializado en código'
description: 'Modelo de mezcla de expertos de pesos abiertos de DeepSeek, especializado en código'
company: 'deepseek'
model_type: 'Code'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 6
release_date: '2024-06-17'
param_count: '236B (21B active)'
context_window_tokens: 128000
modality: [text, code]
open_weight: true
license: 'MIT'
api_available: true
humaneval_score: 90.2
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, code, self-hosted]
i18n_source: '5e8d9823340f'
---

DeepSeek-Coder-V2 es el modelo de código de segunda generación de DeepSeek, publicado en junio de 2024 como modelo de mezcla de expertos con 236 000 millones de parámetros en total y 21 000 millones activos por token. Amplió la ventana de contexto a 128 000 tokens, un salto fuerte respecto a la ventana de 16 000 tokens del DeepSeek-Coder original, y extendió la cobertura de lenguajes de 86 a 338 lenguajes de programación. En HumanEval obtuvo un 90,2 %, un resultado que DeepSeek presentó entonces como el cierre de la distancia con modelos cerrados como GPT-4 Turbo en tareas de programación, y también mejoró en benchmarks de razonamiento general y de matemáticas respecto a su predecesor. A diferencia de la licencia más restrictiva del DeepSeek-Coder original, DeepSeek-Coder-V2 se publica bajo licencia MIT, así que se puede usar con libertad en proyectos comerciales, y los pesos están en Hugging Face junto al acceso por API a través de la propia plataforma de DeepSeek.
