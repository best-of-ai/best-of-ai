---
title: 'Gato'
name: 'Gato'
slug: 'gato'
subtitle: 'Agente generalista único de DeepMind, entrenado con texto, imágenes y control robótico'
description: 'Agente generalista único de DeepMind, entrenado con texto, imágenes y control robótico'
company: 'google-deepmind'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://deepmind.google/discover/blog/a-generalist-agent/'
price: 'Paid'
rank: 5
release_date: '2022-05-12'
param_count: '1.18B'
modality: [text, image]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [multimodal, research, generalist-agent]
i18n_source: '7358d84afc22'
---

Gato es una sola red neuronal que DeepMind presentó en mayo de 2022, y el mismo conjunto de pesos puede encargarse de más de 600 tareas distintas: jugar a juegos de Atari, describir imágenes, mantener una conversación de texto y controlar un brazo robótico real para apilar bloques. En lugar de entrenar un modelo distinto por tarea, DeepMind serializó cada entrada, fuera texto, imágenes, pares de las articulaciones o pulsaciones de botones, en una secuencia plana de tokens, y entrenó un solo transformer con todo ello a la vez, con una arquitectura parecida a la de un modelo de lenguaje grande, pero con tokens que representan acciones y datos de sensores además de las palabras.

Con 1180 millones de parámetros, Gato es pequeño al lado de los 175 000 millones de GPT-3, y su rendimiento en cualquier tarea concreta va por detrás de especialistas hechos solo para esa tarea. Lo que lo hizo relevante fue demostrar que una sola red podía hacer un trabajo razonable en modalidades y problemas de control tan distintos. DeepMind lo describió como un paso de investigación hacia agentes de uso más general, no como un producto, y Gato nunca se publicó ni se ofreció por API.
