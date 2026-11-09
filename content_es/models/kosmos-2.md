---
title: 'Kosmos-2'
name: 'Kosmos-2'
slug: 'kosmos-2'
subtitle: 'El modelo multimodal con anclaje de Microsoft, que vincula el lenguaje a regiones concretas de la imagen'
description: 'El modelo multimodal con anclaje de Microsoft, que vincula el lenguaje a regiones concretas de la imagen'
company: 'microsoft'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://github.com/microsoft/unilm/tree/master/kosmos-2'
price: 'Free'
rank: 5
release_date: '2023-06-26'
param_count: '1.6B'
modality: [text, image]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, vision]
i18n_source: '327b99415fef'
---

Kosmos-2 es un modelo multimodal de Microsoft Research, publicado en junio de 2023, con unos 1600 millones de parámetros. Su rasgo distintivo es el anclaje: en lugar de limitarse a describir una imagen en texto, vincula frases de su salida a cajas delimitadoras concretas de la imagen, de modo que una oración sobre «un perro» o «la silla de la izquierda» señala los píxeles exactos a los que se refiere. Microsoft lo entrenó en GrIT, un conjunto grande de pares imagen-texto anclados que construyeron para este fin, combinado con corpus multimodales generales, y lo evaluó en comprensión de expresiones de referencia, anclaje de frases y tareas estándar de visión y lenguaje. Kosmos-2 fue un lanzamiento de investigación, no un producto, pensado para mostrar que el anclaje se podía aprender de extremo a extremo dentro de un modelo de lenguaje, y no añadirlo con un detector aparte. El código y los pesos están abiertos en GitHub y Hugging Face bajo licencia MIT, y el trabajo alimentó la investigación multimodal posterior de Microsoft, incluidas partes de las líneas de visión y lenguaje Florence y Phi.
