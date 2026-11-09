---
title: 'DeepSeek-Coder-33B'
name: 'DeepSeek-Coder-33B'
slug: 'deepseek-coder-33b'
subtitle: 'Modelo de código principal anterior de DeepSeek, previo a DeepSeek-Coder-V2'
description: 'Modelo de código principal anterior de DeepSeek, previo a DeepSeek-Coder-V2'
company: 'deepseek'
model_type: 'Code'
logo_url: ''
product_url: 'https://github.com/deepseek-ai/DeepSeek-Coder'
price: 'Free'
rank: 6
release_date: '2023-11-02'
param_count: '33B'
context_window_tokens: 16384
modality: [text, code]
open_weight: true
license: 'DeepSeek License'
api_available: true
humaneval_score: 79.3
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'DeepSeek API']
date: '2026-07-16'
tags: [code, open-weight, api, legacy]
i18n_source: 'e1d443d0e69c'
---

DeepSeek-Coder-33B es un modelo de lenguaje centrado en código que DeepSeek publicó en noviembre de 2023, antes de que la empresa se hiciera muy conocida por sus modelos de razonamiento posteriores. Se entrenó desde cero con 2 billones de tokens repartidos sobre todo entre código y lenguaje natural, con una ventana de contexto de 16 000 tokens y un entrenamiento a nivel de proyecto que le permite razonar a través de varios archivos y no solo de fragmentos aislados. La versión ajustada para instrucciones obtuvo un 79,3 % de pass@1 en HumanEval en la publicación, por delante de la mayoría de los modelos de código abiertos de entonces y a distancia de alcance de GPT-3.5 en benchmarks de programación. Admite el completado fill-in-the-middle para usarlo en editores de código y cubre un amplio abanico de lenguajes de programación. DeepSeek lo ha sustituido desde entonces por DeepSeek-Coder-V2, un modelo de mezcla de expertos más grande y con una ventana de contexto más larga, pero el modelo de 33B sigue disponible en Hugging Face para autoalojarlo.
