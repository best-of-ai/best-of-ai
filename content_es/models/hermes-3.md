---
title: 'Hermes 3'
name: 'Hermes 3'
slug: 'hermes-3'
subtitle: 'El fine-tune de pesos abiertos de Nous Research, centrado en el control por instrucciones y el razonamiento'
description: 'El fine-tune de pesos abiertos de Nous Research, centrado en el control por instrucciones y el razonamiento'
company: 'nous-research'
model_type: 'Language'
logo_url: ''
product_url: 'https://nousresearch.com/hermes3/'
price: 'Free'
rank: 4
release_date: '2024-08-27'
param_count: '405B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Llama 3.1 Community License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: false
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, fine-tune, self-hosted]
i18n_source: 'b20d0dae77b1'
---

Hermes 3 es un modelo de lenguaje de pesos abiertos que Nous Research construyó sobre la base Llama 3.1 405B de Meta. Nous lo publicó en agosto de 2024 como un fine-tune de todos los parámetros, no como un adaptador ligero, con la idea de devolver más control a quien lo usa mediante la dirección por el prompt de sistema, el uso de herramientas de agentes y cadenas largas de razonamiento. Sale en tres tamaños (8B, 70B y 405B), entrenados sobre todo con datos sintéticos seleccionados por Nous, y admite salida estructurada y llamadas a funciones lo bastante bien como para funcionar como backend de agentes listo para usar. En benchmarks públicos iguala o supera al propio ajuste Llama 3.1 Instruct de Meta en tareas como ARC, HellaSwag e IFEval, algo notable porque es un fine-tune de la comunidad que compite con el lanzamiento oficial del proveedor. Como los pesos están abiertos bajo la licencia de Llama 3.1, se puede autoalojar el modelo completo de 405B o ejecutarlo a través de proveedores de inferencia de terceros, en lugar de una API propietaria.
