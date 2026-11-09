---
title: 'BLIP-2'
name: 'BLIP-2'
slug: 'blip-2'
subtitle: 'Sucesor más eficiente de BLIP, de Salesforce, que arranca el preentrenamiento de visión y lenguaje a partir de encoders congelados'
description: 'Sucesor más eficiente de BLIP, de Salesforce, que arranca el preentrenamiento de visión y lenguaje a partir de encoders congelados'
company: 'salesforce'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://github.com/salesforce/LAVIS/tree/main/projects/blip2'
price: 'Free'
rank: 6
release_date: '2023-01-30'
param_count: '3.7B'
modality: [text, image]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, vision]
i18n_source: '8456e2d29321'
---

BLIP-2 es un modelo de visión y lenguaje que Salesforce Research publicó en enero de 2023, y se construye en torno a un truco concreto de eficiencia: en lugar de entrenar juntos desde cero un encoder de imagen grande y un modelo de lenguaje, congela un encoder de imagen preentrenado y un modelo de lenguaje preentrenado, y entrena solo un conector ligero entre ambos, llamado Q-Former. Ese Q-Former tiene unos 188 millones de parámetros entrenables, menos del 2 % del modelo total, lo que hizo que entrenar BLIP-2 fuera mucho más barato que los modelos de visión y lenguaje comparables de la época, sin dejar de ir bien en descripción de imágenes y en respuesta a preguntas visuales. Salesforce publicó varias variantes que emparejan el Q-Former con distintos modelos de lenguaje congelados, incluidas versiones construidas sobre OPT (2,7B y 6,7B de parámetros) y Flan-T5 (hasta 11B de parámetros), de modo que se puede cambiar capacidad por coste de cómputo. El código y los pesos están en GitHub y Hugging Face bajo licencia MIT, como parte de la biblioteca LAVIS de Salesforce, y el enfoque de encoder congelado con conector ligero que popularizó influyó en modelos multimodales posteriores que, del mismo modo, acoplan capacidad de visión a modelos de lenguaje ya existentes en lugar de entrenarlo todo de forma conjunta.
