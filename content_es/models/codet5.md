---
title: 'CodeT5+'
name: 'CodeT5+'
slug: 'codet5'
subtitle: 'Familia de modelos de código encoder-decoder de pesos abiertos de Salesforce'
description: 'Familia de modelos de código encoder-decoder de pesos abiertos de Salesforce'
company: 'salesforce'
model_type: 'Code'
logo_url: ''
product_url: 'https://github.com/salesforce/CodeT5'
price: 'Free'
rank: 3
release_date: '2023-05-13'
param_count: '16B'
context_window_tokens: 2048
modality: [text, code]
open_weight: true
license: 'BSD-3-Clause'
api_available: false
humaneval_score: 30.9
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, code, self-hosted]
i18n_source: '20777365e144'
---

CodeT5+ es una familia de modelos de código de pesos abiertos construida por Salesforce Research, publicada en mayo de 2023 como continuación del modelo encoder-decoder CodeT5 original. Llega en varios tamaños, de 220 millones hasta 16 000 millones de parámetros, y puede ejecutarse en modo solo encoder, solo decoder o encoder-decoder completo, lo que permite que una sola arquitectura cubra tareas de comprensión de código, como la detección de defectos, junto a tareas de generación, como el completado de código y la síntesis de texto a código. El entrenamiento combina eliminación de ruido por tramos, modelado causal de lenguaje, aprendizaje contrastivo y objetivos de emparejamiento texto-código, un enfoque que, según Salesforce, le da ventaja sobre los modelos de código solo decoder de tamaño parecido en tareas de generación aumentada por recuperación. La variante de 16B obtiene alrededor de un 30,9 % de pass@1 en HumanEval, y una versión ajustada para instrucciones del mismo checkpoint supera el 35 %, por delante del modelo antiguo code-cushman-001 de OpenAI en el mismo benchmark. Los pesos están alojados en Hugging Face bajo licencia BSD-3-Clause, lo que convierte a CodeT5+ en una de las primeras alternativas completamente abiertas a los modelos de código propietarios de la época de Codex.
