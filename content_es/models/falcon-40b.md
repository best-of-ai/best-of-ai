---
title: 'Falcon 40B'
name: 'Falcon 40B'
slug: 'falcon-40b'
subtitle: 'Modelo de pesos abiertos anterior de TII, que encabezó rankings antes de Falcon 180B'
description: 'Modelo de pesos abiertos anterior de TII, que encabezó rankings antes de Falcon 180B'
company: 'technology-innovation-institute'
model_type: 'Language'
logo_url: ''
product_url: 'https://falconllm.tii.ae/'
price: 'Free'
rank: 4
release_date: '2023-05-25'
param_count: '40B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
mmlu_score: 82.7
humaneval_score: 76.3
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted, legacy]
extra_model_types: ['Code']
i18n_source: '109766ee6da4'
---

Falcon 40B es un modelo de lenguaje causal solo decodificador de 40 000 millones de parámetros que el Technology Innovation Institute publicó en mayo de 2023. Se entrenó con cerca de 1 billón de tokens de RefinedWeb, un gran conjunto de datos web que TII seleccionó y filtró por su cuenta, combinado con otros corpus escogidos. En el lanzamiento encabezó el Open LLM Leaderboard de Hugging Face entre los modelos de código abierto, con 82,7 en MMLU y 76,3 en HumanEval, por delante de contemporáneos como MPT y RedPajama y a un nivel competitivo con el Llama 2 70B de Meta, más grande, en varios benchmarks. La arquitectura usa multiquery attention y FlashAttention para mantener el coste de inferencia bajo respecto a su tamaño. TII lo publicó bajo una licencia Apache 2.0 sin regalías, una elección poco habitual entonces para un modelo de esa escala, lo que ayudó a una adopción temprana en empresas, incluida la disponibilidad en AWS SageMaker JumpStart. Falcon 40B ha quedado superado por Falcon 180B y por la familia Falcon 3, y su ventana de contexto de 2048 tokens queda corta al lado de los modelos actuales.
