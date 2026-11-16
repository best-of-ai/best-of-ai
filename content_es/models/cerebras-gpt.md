---
title: 'Cerebras-GPT'
name: 'Cerebras-GPT'
slug: 'cerebras-gpt'
subtitle: 'Familia de modelos completamente abierta de Cerebras, entrenada en sus chips de escala de oblea'
description: 'Familia de modelos completamente abierta de Cerebras, entrenada en sus chips de escala de oblea'
company: 'cerebras'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.cerebras.ai/blog/cerebras-gpt-a-family-of-open-compute-efficient-large-language-models'
price: 'Free'
rank: 3
release_date: '2023-03-28'
param_count: '13B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, fully-open, self-hosted]
i18n_source: 'ff8674011b4e'
---

Cerebras-GPT es una familia de modelos de lenguaje, de 111 millones a 13 000 millones de parámetros, que Cerebras entrenó en sus propios sistemas CS-2 de escala de oblea y publicó en marzo de 2023. El sentido del proyecto era menos ganar benchmarks que la apertura: Cerebras publicó los pesos, el código de entrenamiento y un informe técnico detallado que describe hiperparámetros y el comportamiento de escalado de cada tamaño de la familia, siguiendo recetas de entrenamiento óptimas en cómputo parecidas a las que hay detrás de Chinchilla. Eso convirtió a Cerebras-GPT en una de las familias de modelos abiertos mejor documentadas de su momento, útil para quien investiga y quiere una referencia limpia y reproducible para estudiar leyes de escalado.

Todos los checkpoints de Cerebras-GPT se publican bajo Apache 2.0 y están alojados en Hugging Face, de uso gratuito en comercio y en investigación. Los modelos usan una arquitectura bastante estándar al estilo de GPT, con una ventana de contexto de 2048 tokens, y para los estándares de 2023 su capacidad bruta era modesta al lado de modelos como LLaMA, porque Cerebras priorizó un entrenamiento transparente y reproducible frente a exprimir el máximo rendimiento en benchmarks. Hoy la familia se cita sobre todo en la investigación de leyes de escalado y como ejemplo de una empresa de hardware de IA que demuestra sus propios chips entrenando y publicando en abierto una gama completa de modelos.
