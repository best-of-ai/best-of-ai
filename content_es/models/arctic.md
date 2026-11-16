---
title: 'Arctic'
name: 'Arctic'
slug: 'arctic'
subtitle: 'Modelo de pesos abiertos de Snowflake, orientado a empresas y afinado para SQL y RAG'
description: 'Modelo de pesos abiertos de Snowflake, orientado a empresas y afinado para SQL y RAG'
company: 'snowflake-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.snowflake.com/en/blog/arctic-open-efficient-foundation-language-models-snowflake/'
price: 'Free'
rank: 4
release_date: '2024-04-24'
param_count: '480B (17B active)'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
mmlu_score: 67.3
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Snowflake Cortex']
date: '2026-07-16'
tags: [llm, open-weight, enterprise, self-hosted]
i18n_source: '083cf9082048'
---

Arctic es un gran modelo de lenguaje que Snowflake publicó en abril de 2024, pensado para trabajo de empresa como generación de SQL, programación y seguimiento de instrucciones, y no para el chat general. Usa un diseño de mezcla de expertos con 480 000 millones de parámetros en total, repartidos en 128 expertos, pero solo unos 17 000 millones están activos para un token dado, lo que mantiene el coste de inferencia por debajo del de los modelos densos de escala parecida. Snowflake publicó los checkpoints base e instruct bajo licencia Apache 2.0, así que los pesos se pueden autoalojar o ejecutar a través de Snowflake Cortex. En el benchmark de texto a SQL Spider obtuvo alrededor de un 79 % de precisión, y Snowflake lo presentó como forma de llevar modelos abiertos capaces a los almacenes de datos sin enviar las consultas a la API de un tercero. A cambio de una ventana de contexto corta, de 4K, y de un chat general más flojo, rinde bien en las tareas de empresa estrechas para las que se construyó.
