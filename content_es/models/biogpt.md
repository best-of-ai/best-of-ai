---
title: 'BioGPT'
name: 'BioGPT'
slug: 'biogpt'
subtitle: 'Modelo generativo de Microsoft, específico de dominio, preentrenado con literatura biomédica'
description: 'Modelo generativo de Microsoft, específico de dominio, preentrenado con literatura biomédica'
company: 'microsoft'
model_type: 'Language'
logo_url: ''
product_url: 'https://github.com/microsoft/BioGPT'
price: 'Free'
rank: 5
release_date: '2022-09-24'
param_count: '347M (base), 1.5B (Large)'
context_window_tokens: 1024
modality: [text]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [healthcare, open-weight, legacy]
i18n_source: 'b08c07fb9738'
---

BioGPT es un modelo de lenguaje que Microsoft Research presentó en octubre de 2022, construido de forma específica para texto biomédico y no adaptado a posteriori a partir de un modelo de uso general. Usa una arquitectura de decoder al estilo de GPT-2, entrenada desde cero con unos 15 millones de resúmenes de PubMed, y llega en una versión base de 347 millones de parámetros y una versión BioGPT-Large de 1500 millones. Como se entrenó con texto biomédico desde el principio, y no con un fine-tuning posterior sobre ese dominio, superó a modelos de lenguaje de uso general anteriores en tareas como la extracción de relaciones biomédicas, la respuesta a preguntas sobre literatura médica y la clasificación de documentos. Microsoft publicó ambos checkpoints bajo licencia MIT en Hugging Face y GitHub, y se convirtió en un punto de partida habitual para grupos de investigación que construyen herramientas de NLP biomédico sin tener que entrenar un modelo de dominio desde cero. Es anterior a la oleada de modelos de chat de uso general ajustados para instrucciones y no se ha actualizado desde entonces, así que hoy se usa sobre todo como opción ligera y autoalojable para tareas estrechas de texto biomédico, y no como asistente general.
