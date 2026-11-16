---
title: 'Megatron-Turing NLG'
name: 'Megatron-Turing NLG'
slug: 'megatron-turing-nlg'
subtitle: 'El modelo de investigación de 530 000 millones de parámetros de NVIDIA y Microsoft, de los LLM densos más grandes de su momento'
description: 'El modelo de investigación de 530 000 millones de parámetros de NVIDIA y Microsoft, de los LLM densos más grandes de su momento'
company: 'nvidia'
model_type: 'Language'
logo_url: ''
product_url: 'https://developer.nvidia.com/megatron-turing-natural-language-generation'
price: 'Paid'
rank: 5
release_date: '2021-10-11'
param_count: '530B'
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [llm, research, legacy]
extra_model_types: ['Reasoning']
i18n_source: '06b0502910e0'
---

Megatron-Turing NLG es un modelo de lenguaje transformer denso, de 530 000 millones de parámetros, que NVIDIA y Microsoft entrenaron juntos y anunciaron en octubre de 2021. En aquel momento era el mayor modelo de lenguaje monolítico (no de mezcla de expertos) jamás entrenado. Se construyó al combinar el paralelismo de tensores de Megatron-LM, de NVIDIA, con el paralelismo de pipeline y el optimizador ZeRO de DeepSpeed, de Microsoft, en cientos de GPU A100. El modelo tiene 105 capas transformer y se entrenó con un corpus de 270 000 millones de tokens, tomado de texto web, libros y otras fuentes seleccionadas.

Sirvió sobre todo como demostración de investigación e ingeniería: hasta dónde podían llegar el escalado de modelos densos y el software de entrenamiento distribuido, antes de que las arquitecturas de mezcla de expertos fueran el camino más práctico hacia modelos más grandes. NVIDIA y Microsoft publicaron resultados en benchmarks de completado, comprensión lectora y razonamiento, donde superaba a predecesores más pequeños como GPT-3 y Turing-NLG, pero el modelo en sí nunca se abrió como producto público ni como API.
