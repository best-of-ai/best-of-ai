---
title: 'Chameleon'
name: 'Chameleon'
slug: 'chameleon'
subtitle: 'Modelo de fusión temprana de Meta que mezcla de forma nativa tokens de texto y de imagen'
description: 'Modelo de fusión temprana de Meta que mezcla de forma nativa tokens de texto y de imagen'
company: 'meta-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://ai.meta.com/blog/meta-fair-research-new-releases/'
price: 'Free'
rank: 6
release_date: '2024-05-16'
param_count: '34B'
context_window_tokens: 4096
modality: [text, image]
open_weight: true
license: 'Research-only'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Research']
date: '2026-07-16'
tags: [multimodal, research, open-weight]
extra_model_types: ['Image Generation']
i18n_source: '6e820e7a5edb'
---

Chameleon es un modelo multimodal de Meta FAIR, descrito en un artículo de mayo de 2024, que mezcla texto e imágenes desde el principio en lugar de acoplar un encoder de visión a un modelo de lenguaje. La mayoría de los sistemas multimodales usan fusión tardía: un encoder de imagen aparte alimenta rasgos visuales a un modelo de lenguaje que se preentrenó solo con texto. Chameleon, en cambio, cuantiza las imágenes en tokens discretos y entrena desde cero con secuencias de tokens de texto e imagen intercalados, de modo que el mismo transformer aprende a razonar sobre las dos modalidades y también puede generar imágenes como salida, no solo describirlas.

Meta publicó dos tamaños, Chameleon-7B y Chameleon-34B, e informó de que la versión de 34B superaba a modelos como Flamingo e IDEFICS en descripción de imágenes y en respuesta a preguntas visuales, y se mantenía frente a GPT-4V y Gemini Pro en pruebas de preferencia humana por pares en tareas de generación de modalidad mixta. Los pesos están en GitHub bajo una licencia solo de investigación, así que Chameleon no se puede usar de forma comercial, y Meta lo situó sobre todo como demostración del entrenamiento de fusión temprana y no como producto. Ideas de Chameleon pasaron a los modelos Llama multimodales posteriores de Meta, que extendieron un entrenamiento al estilo de la fusión temprana a una línea de modelos más amplia y con licencia comercial.
