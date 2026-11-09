---
title: 'DBRX'
name: 'DBRX'
slug: 'dbrx'
subtitle: 'Modelo de mezcla de expertos de pesos abiertos de Databricks'
description: 'Modelo de mezcla de expertos de pesos abiertos de Databricks'
company: 'databricks'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm'
price: 'Free'
rank: 5
release_date: '2024-03-27'
param_count: '132B (36B active)'
context_window_tokens: 32000
modality: [text]
open_weight: true
license: 'Databricks Open Model License'
api_available: true
mmlu_score: 73.7
humaneval_score: 70.1
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Databricks']
date: '2026-07-16'
tags: [llm, open-weight, mixture-of-experts, self-hosted]
extra_model_types: ['Code']
i18n_source: 'c49f11ecc44d'
---

DBRX es el gran modelo de lenguaje de pesos abiertos de Databricks, publicado en marzo de 2024 como modelo base detrás del DBRX Instruct ajustado para instrucciones. Es un modelo de mezcla de expertos de grano fino, con 132 000 millones de parámetros en total y 36 000 millones de parámetros activos por token, entrenado desde cero con 12 billones de tokens de texto y código usando la propia pila de entrenamiento Mosaic AI de Databricks. En la publicación, Databricks informó de que superaba a otros modelos abiertos de la época, entre ellos Llama 2 70B y Mixtral, en benchmarks como MMLU y HumanEval, y se presentó como prueba de que una empresa centrada en el mercado empresarial podía entrenar un modelo fundacional competitivo sin depender del presupuesto de investigación de un gran laboratorio. Tiene una ventana de contexto de 32 000 tokens y se publica bajo la Databricks Open Model License, con pesos disponibles en Hugging Face para autoalojarlos o a través de la propia infraestructura de servicio de Databricks.
