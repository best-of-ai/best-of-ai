---
title: 'DBRX Instruct'
name: 'DBRX Instruct'
slug: 'dbrx-instruct'
subtitle: 'Variante ajustada para instrucciones del modelo DBRX de pesos abiertos de Databricks'
description: 'Variante ajustada para instrucciones del modelo DBRX de pesos abiertos de Databricks'
company: 'databricks'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm'
price: 'Free'
rank: 4
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
tags: [llm, open-weight, instruction-tuned, self-hosted]
extra_model_types: ['Code']
i18n_source: '2f1996df20fb'
---

DBRX Instruct es la versión con fine-tuning y lista para chat del modelo DBRX de Databricks, publicada en marzo de 2024 junto al modelo base DBRX. Usa una arquitectura de mezcla de expertos de grano fino, con 132 000 millones de parámetros en total, de los que solo 36 000 millones están activos para un token dado, y se entrenó con 12 billones de tokens de texto y código. Databricks lo ajustó de forma específica para el seguimiento de instrucciones y la conversación de varios turnos, y en el lanzamiento la empresa informó de que superaba a GPT-3.5 en MMLU (73,7 % frente a 70,0 %) y en HumanEval (70,1 % frente a 48,1 %). Admite una ventana de contexto de 32 000 tokens y se distribuye bajo la Databricks Open Model License, que permite el uso comercial con algunas restricciones para despliegues muy grandes. Las organizaciones lo ejecutan a través de la propia plataforma de Databricks o autoalojan los pesos desde Hugging Face.
