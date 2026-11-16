---
title: 'CodeGen2'
name: 'CodeGen2'
slug: 'codegen2'
subtitle: 'Modelo de código de pesos abiertos de Salesforce, pensado para rellenar huecos y síntesis de programas en varios turnos'
description: 'Modelo de código de pesos abiertos de Salesforce, pensado para rellenar huecos y síntesis de programas en varios turnos'
company: 'salesforce'
model_type: 'Code'
logo_url: ''
product_url: 'https://github.com/salesforce/CodeGen2'
price: 'Free'
rank: 5
release_date: '2023-05-03'
param_count: '16B'
context_window_tokens: 2048
modality: [text, code]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [code, open-weight]
i18n_source: '19442e527069'
---

CodeGen2 es la familia de segunda generación de modelos de código abiertos de Salesforce Research, publicada en mayo de 2023 como continuación del CodeGen original. Llega en cuatro tamaños: 1B, 3,7B, 7B y 16B de parámetros. La mejora principal respecto al primer CodeGen es el soporte de infilling: el modelo puede rellenar un fragmento de código que falta a partir del contexto que lo rodea por los dos lados, en lugar de generar texto solo de izquierda a derecha. Eso lo hace más adecuado para flujos reales de un editor, como el autocompletado y la reparación de código, donde el modelo tiene que escribir código en medio de un archivo que ya existe.

Los modelos se entrenan con una mezcla de lenguaje natural y código fuente de muchos lenguajes de programación, y se publican bajo la licencia permisiva Apache 2.0 a través de Hugging Face y GitHub. CodeGen2 se probó con un contexto de trabajo de unos 2000 tokens, modesto para los estándares de hoy pero típico de los modelos de código de aquella época. Salesforce lo situó como alternativa amable para la investigación frente a modelos de código cerrados como Codex, y después llegó CodeGen2.5, un modelo más pequeño ajustado para igualar el rendimiento de predecesores más grandes.
