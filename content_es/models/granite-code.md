---
title: 'Granite Code'
name: 'Granite Code'
slug: 'granite-code'
subtitle: 'La familia de modelos de generación de código de pesos abiertos de IBM'
description: 'La familia de modelos de generación de código de pesos abiertos de IBM'
company: 'ibm'
model_type: 'Code'
logo_url: ''
product_url: 'https://www.ibm.com/granite'
price: 'Free'
rank: 4
release_date: '2024-05-06'
param_count: '3B, 8B, 20B, 34B'
context_window_tokens: 8192
modality: [text, code]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'IBM watsonx']
date: '2026-07-16'
tags: [llm, open-weight, code, self-hosted]
i18n_source: '10f0aa565ad0'
---

Granite Code es la familia de modelos de código abiertos de IBM, publicada en mayo de 2024 en cuatro tamaños: 3B, 8B, 20B y 34B parámetros, cada uno en versión base y en versión ajustada a instrucciones. IBM Research entrenó los modelos con unos 3 a 4 billones de tokens de 116 lenguajes de programación, mezclando código en bruto con texto en lenguaje natural sobre código, de modo que los modelos cubren en el mismo sistema tareas como generación de código, corrección de errores y explicación de código. Los modelos salen bajo Apache 2.0, lo que permite a las empresas hacer fine-tuning y volver a desplegarlos sin fricción de licencias, el objetivo de IBM con empresas recelosas de los asistentes de código cerrados. Los benchmarks del lanzamiento mostraron que los modelos Granite Code igualaban o superaban a otros modelos de código abiertos de tamaño parecido en HumanEval y suites relacionadas. La línea está en Hugging Face, en Ollama y en AWS vía Bedrock y SageMaker, y un trabajo posterior de escala llevó algunas variantes a una ventana de contexto de 128K.
