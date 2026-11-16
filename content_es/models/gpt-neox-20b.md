---
title: 'GPT-NeoX-20B'
name: 'GPT-NeoX-20B'
slug: 'gpt-neox-20b'
subtitle: 'El modelo de pesos abiertos de EleutherAI, uno de los checkpoints públicos más grandes de su época'
description: 'El modelo de pesos abiertos de EleutherAI, uno de los checkpoints públicos más grandes de su época'
company: 'eleuther-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.eleuther.ai/'
price: 'Free'
rank: 4
release_date: '2022-04-14'
param_count: '20B'
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
i18n_source: '3f0cef2ef3c0'
---

GPT-NeoX-20B es un modelo de lenguaje de 20 000 millones de parámetros que EleutherAI anunció en abril de 2022, tras cerca de un año de desarrollo de su propio marco de entrenamiento GPT-NeoX, construido sobre Megatron y DeepSpeed. En el lanzamiento era el modelo de lenguaje autorregresivo denso más grande con pesos descargables de forma pública, entrenado en the Pile con una ventana de contexto de 2048 tokens. En el propio arnés de evaluación de EleutherAI quedó entre los modelos Curie y Davinci de OpenAI en la mayoría de los benchmarks estándar de PLN, y su rendimiento one-shot en problemas matemáticos redactados superó al GPT-3 completo de 175B en esa prueba concreta, algo que el equipo destacó como prueba de que la calidad de los datos de entrenamiento importaba tanto como la escala bruta. Se publicó bajo la licencia Apache 2.0 en Hugging Face, y dio a quienes investigan un modelo grande e inspeccionable para estudiar y ajustar sin necesitar acceso a una API cerrada. GPT-NeoX-20B ha quedado atrás frente a modelos abiertos mucho más grandes y eficientes, pero siguió influyendo en la investigación de LLM de código abierto como una de las bases de código de entrenamiento de referencia sobre las que se construyó el campo.
