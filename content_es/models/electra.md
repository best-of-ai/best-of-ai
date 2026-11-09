---
title: 'ELECTRA'
name: 'ELECTRA'
slug: 'electra'
subtitle: 'Enfoque de preentrenamiento de Google, más eficiente en muestras, con un objetivo de detección de tokens reemplazados'
description: 'Enfoque de preentrenamiento de Google, más eficiente en muestras, con un objetivo de detección de tokens reemplazados'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://arxiv.org/abs/2003.10555'
price: 'Free'
rank: 6
release_date: '2020-03-23'
param_count: '335M'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, legacy, foundation-model]
i18n_source: 'f5cba0d29eb6'
---

ELECTRA es un método de preentrenamiento de codificadores de texto que investigadores de Google y Stanford presentaron en un artículo publicado para ICLR 2020, junto a una familia de modelos preentrenados hechos con ese método. En lugar del objetivo de modelado de lenguaje enmascarado de BERT, en el que el modelo predice palabras ocultas al azar, ELECTRA entrena un generador pequeño para sustituir algunos tokens por alternativas plausibles y un discriminador que detecta qué tokens se cambiaron. Ese objetivo de «detección de tokens reemplazados» da al modelo una señal de aprendizaje en cada token de la secuencia, en lugar de solo en los enmascarados, y el preentrenamiento resulta mucho más eficiente en el uso de muestras.

La versión publicada más grande, ELECTRA-Large, tiene 335 millones de parámetros y alcanzó puntuaciones en GLUE competitivas con RoBERTa y XLNet usando una cuarta parte de su cómputo de preentrenamiento. Con el mismo presupuesto de cómputo, los superó de forma clara. Google publicó el código y los pesos bajo la licencia Apache 2.0, y las variantes más pequeñas ELECTRA-Small y ELECTRA-Base se hicieron opciones habituales para equipos que querían precisión al nivel de BERT sin el coste de entrenamiento de BERT.
