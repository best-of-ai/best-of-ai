---
title: 'Flamingo'
name: 'Flamingo'
slug: 'flamingo'
subtitle: 'Modelo de visión-lenguaje de DeepMind que abrió el razonamiento multimodal few-shot'
description: 'Modelo de visión-lenguaje de DeepMind que abrió el razonamiento multimodal few-shot'
company: 'google-deepmind'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://deepmind.google/discover/blog/tackling-multiple-tasks-with-a-single-visual-language-model/'
price: 'Paid'
rank: 6
release_date: '2022-04-29'
param_count: '80B'
modality: [text, image]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [multimodal, vision, research]
i18n_source: '98bf1c585f2e'
---

Flamingo es un modelo de visión-lenguaje que DeepMind publicó en abril de 2022, construido para trabajar con imágenes, vídeos y texto a la vez y responder a preguntas abiertas sobre ellos tras ver solo un puñado de ejemplos. Parte de Chinchilla, el modelo de lenguaje de 70B de DeepMind, y añade codificadores de visión y capas de atención cruzada que le permiten condicionar la generación de texto a la entrada visual, con lo que el modelo completo llega a unos 80B de parámetros. La idea central era el aprendizaje few-shot para tareas de visión-lenguaje: en lugar de hacer fine-tuning en cada conjunto de datos nuevo, a Flamingo se le podían mostrar unos pocos ejemplos en el prompt y generalizar a partir de ahí, de forma parecida a lo que GPT-3 hacía con el texto. En el lanzamiento superó a todos los enfoques few-shot anteriores en 16 benchmarks de visión-lenguaje, entre ellos la descripción de imágenes, la respuesta a preguntas visuales y el diálogo visual. DeepMind nunca publicó Flamingo como producto ni como API pública; se quedó como modelo de investigación, pero su arquitectura influyó en sistemas multimodales posteriores, incluidas reimplementaciones abiertas como OpenFlamingo y decisiones de diseño en los modelos multimodales posteriores de Google.
