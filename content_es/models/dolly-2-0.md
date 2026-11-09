---
title: 'Dolly 2.0'
name: 'Dolly 2.0'
slug: 'dolly-2-0'
subtitle: 'El primer modelo de seguimiento de instrucciones de Databricks totalmente abierto y usable con fines comerciales'
description: 'El primer modelo de seguimiento de instrucciones de Databricks totalmente abierto y usable con fines comerciales'
company: 'databricks'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.databricks.com/blog/2023/04/12/dolly-first-open-commercially-viable-instruction-tuned-llm'
price: 'Free'
rank: 5
release_date: '2023-04-12'
param_count: '12B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, legacy]
i18n_source: '24b60e23db79'
---

Dolly 2.0 es un modelo de lenguaje de seguimiento de instrucciones de 12 000 millones de parámetros que Databricks publicó el 12 de abril de 2023, construido sobre el modelo Pythia de EleutherAI. Lo que lo hizo relevante no fue su capacidad bruta, que en aquel momento iba muy por detrás de GPT-3.5, sino la licencia: Databricks publicó en abierto los pesos, el código de entrenamiento y un conjunto de datos de instrucciones nuevo llamado databricks-dolly-15k, todos autorizados para uso comercial. Esas 15 000 muestras las escribieron desde cero unos 5000 empleados de Databricks, precisamente para evitar las restricciones de licencia de los conjuntos de datos hechos a partir de salidas de OpenAI, de los que dependían modelos abiertos anteriores ajustados con instrucciones.

Databricks presentó Dolly 2.0 como la prueba de que se podía construir y compartir un modelo útil de seguimiento de instrucciones sin condiciones restrictivas, en un momento en que la mayoría de modelos abiertos de capacidad parecida llevaban licencias solo para investigación. Ya no compite con los modelos actuales ajustados con instrucciones, pero fue un ejemplo temprano e influyente de una alternativa totalmente abierta a los chatbots comerciales cerrados.
