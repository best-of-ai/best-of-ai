---
title: 'Florence-2'
name: 'Florence-2'
slug: 'florence-2'
subtitle: 'Modelo fundacional de visión compacto de Microsoft para descripción, detección y segmentación en un solo modelo'
description: 'Modelo fundacional de visión compacto de Microsoft para descripción, detección y segmentación en un solo modelo'
company: 'microsoft'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.microsoft.com/en-us/research/publication/florence-2-advancing-a-unified-representation-for-a-variety-of-vision-tasks/'
price: 'Free'
rank: 6
release_date: '2024-06-15'
param_count: '0.77B'
modality: [text, image]
open_weight: true
license: 'MIT'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Azure AI Foundry']
date: '2026-07-16'
tags: [computer-vision, open-weight, multimodal]
i18n_source: '9791d240cd8e'
---

Florence-2 es un modelo fundacional de visión que Microsoft Research publicó en junio de 2024, construido para encargarse de la descripción de imágenes, la detección de objetos, la segmentación y el grounding visual dentro de un solo modelo, en lugar de exigir un modelo distinto por tarea. Sigue un enfoque basado en prompts: la misma red puede producir una descripción, un conjunto de cajas delimitadoras o una máscara de segmentación según la instrucción de texto que reciba, con una arquitectura unificada de secuencia a secuencia. Microsoft lo publicó en dos tamaños, una base de 230 millones de parámetros y una versión grande de 770 millones, ambos pequeños al lado de los modelos de visión-lenguaje habituales. Se entrenó con FLD-5B, un conjunto de datos interno de Microsoft de unos 126 millones de imágenes con 5400 millones de anotaciones, que es lo que permite a un modelo tan pequeño igualar o superar a modelos especializados más grandes en tareas como la descripción en COCO y la comprensión de expresiones referenciales. Microsoft publicó los pesos bajo la licencia MIT en Hugging Face y también lo ofrece a través de Azure AI Foundry, así que es una opción habitual para equipos que quieren capacidades de visión sin ejecutar un LLM multimodal grande.
