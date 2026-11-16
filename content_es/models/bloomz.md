---
title: 'BLOOMZ'
name: 'BLOOMZ'
slug: 'bloomz'
subtitle: 'Variante de BLOOM ajustada para instrucciones, entrenada para seguir instrucciones entre idiomas'
description: 'Variante de BLOOM ajustada para instrucciones, entrenada para seguir instrucciones entre idiomas'
company: 'hugging-face'
model_type: 'Language'
logo_url: ''
product_url: 'https://huggingface.co/bigscience/bloomz'
price: 'Free'
rank: 5
release_date: '2022-11-03'
param_count: '176B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'RAIL License'
api_available: false
access_methods: [Self-hosted]
runs_at_home: false
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, multilingual, legacy]
i18n_source: '9dff7db95770'
---

BLOOMZ es la versión de BLOOM ajustada para instrucciones de BigScience, publicada a finales de 2022 mediante fine-tuning del modelo base de 176 000 millones de parámetros con xP3, una colección grande de tareas multilingües formuladas como instrucciones en lenguaje natural. El sentido del proyecto era la generalización entre idiomas: BLOOMZ se ajustó sobre todo con instrucciones en inglés, pero mostró que podía seguir instrucciones en lenguas que nunca había visto emparejadas con instrucciones durante el fine-tuning, siempre que hubiera encontrado esa lengua en el preentrenamiento original de BLOOM. Fue una de las primeras demostraciones públicas de que la habilidad de seguir instrucciones se transfiere entre idiomas y no exige un ajuste aparte para cada uno.

Como BLOOM, BLOOMZ conserva la ventana de contexto de 2048 tokens y la arquitectura transformer densa del modelo base, y se distribuye bajo la misma licencia RAIL, que permite un uso amplio con una lista de aplicaciones prohibidas. Hoy interesa sobre todo a quien investiga el ajuste de instrucciones multilingüe, y no como modelo de chat de producción, porque los modelos abiertos ajustados para instrucciones más nuevos ofrecen mejor calidad y ventanas de contexto mucho más grandes con un coste de cómputo parecido o menor.
