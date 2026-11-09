---
title: 'GPT-J'
name: 'GPT-J'
slug: 'gpt-j'
subtitle: 'El primer modelo de pesos abiertos al estilo GPT-3 de EleutherAI'
description: 'El primer modelo de pesos abiertos al estilo GPT-3 de EleutherAI'
company: 'eleuther-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.eleuther.ai/'
price: 'Free'
rank: 3
release_date: '2021-06-04'
param_count: '6B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted, legacy]
extra_model_types: ['Code']
i18n_source: '3c03d602f92a'
---

GPT-J es un modelo de lenguaje de 6000 millones de parámetros que EleutherAI publicó el 9 de junio de 2021, como una de las primeras réplicas abiertas creíbles de la arquitectura de GPT-3, en un momento en que OpenAI mantenía el propio GPT-3 cerrado tras una API de pago. Se entrenó en the Pile, el conjunto de textos de 825 GB de EleutherAI, usando la biblioteca Mesh Transformer JAX para paralelizar el entrenamiento en pods de TPU en lugar de GPU. Con 28 capas y una ventana de contexto de 2048 tokens, era bastante más pequeño que la configuración más grande de GPT-3, pero aun así cubría generación de texto general, respuesta a preguntas y completado de código lo bastante bien como para convertirse en una referencia habitual de la investigación de PLN de código abierto. Salió bajo la licencia Apache 2.0, así que cualquiera podía descargarlo, hacer fine-tuning y desplegarlo sin las restricciones de uso de OpenAI, lo que lo convirtió en una base habitual de los primeros proyectos de chatbots abiertos. GPT-J quedó después por detrás de GPT-NeoX-20B y de modelos abiertos posteriores, pero sigue citándose como referencia de cómo la comunidad de código abierto alcanzó a los laboratorios cerrados en la época de GPT-3.
