---
title: 'Gemini Nano'
name: 'Gemini Nano'
slug: 'gemini-nano'
subtitle: 'El nivel Gemini en el dispositivo de Google, integrado en Pixel y Android'
description: 'El nivel Gemini en el dispositivo de Google, integrado en Pixel y Android'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://deepmind.google/technologies/gemini/'
price: 'Paid'
rank: 4
release_date: '2023-12-06'
param_count: '3.25B'
context_window_tokens: 8192
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Self-hosted]
runs_at_home: false
platforms: ['Android', 'Chrome']
date: '2026-07-16'
tags: [llm, on-device, small-model]
i18n_source: '6991c4c972f9'
---

Gemini Nano es el nivel más pequeño de la familia Gemini de Google, diseñado para correr del todo en un teléfono en lugar de llamar a un servidor. Google lo anunció junto a Gemini Pro y Ultra el 6 de diciembre de 2023 y lo envió primero en el Pixel 8 Pro, donde impulsa funciones en el dispositivo como Smart Reply en apps de mensajería, resúmenes de llamadas y los resúmenes de la app Recorder. Sale en un par de tamaños, de unos 1800 millones y 3250 millones de parámetros, cuantizado para correr con eficiencia dentro de los límites de memoria y de NPU de un teléfono, y funciona del todo sin conexión, sin que los datos salgan del dispositivo.

Como corre en local, Nano cambia capacidad bruta por velocidad, privacidad y coste marginal cero por consulta, y su ventana de contexto usable es mucho más pequeña que la de los modelos de servidor de Google. Desde el lanzamiento, Google ha ampliado el soporte de dispositivos a más modelos Pixel y, mediante acuerdos, a dispositivos Samsung Galaxy, y expone Nano a desarrolladores de Android de terceros a través del sistema AICore y de las API de ML Kit GenAI, no por una API pública en la nube.
