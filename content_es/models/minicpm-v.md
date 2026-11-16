---
title: 'MiniCPM-V'
name: 'MiniCPM-V'
slug: 'minicpm-v'
subtitle: 'El modelo multimodal para el edge de OpenBMB, capaz de tareas de visión al nivel de GPT-4V en un teléfono'
description: 'El modelo multimodal para el edge de OpenBMB, capaz de tareas de visión al nivel de GPT-4V en un teléfono'
company: 'openbmb'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://github.com/OpenBMB/MiniCPM-V'
price: 'Free'
rank: 5
release_date: '2024-05-20'
param_count: '8B'
context_window_tokens: 32768
modality: [text, image, video]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, small-model, on-device]
i18n_source: '83a16a62bccc'
---

MiniCPM-V es una línea de modelos de visión-lenguaje de pesos abiertos de OpenBMB, un laboratorio de investigación salido de la Universidad de Tsinghua, hechos para ejecutar comprensión de imagen y de vídeo en teléfonos y otros dispositivos con pocos recursos, sin una GPU de servidor. La publicación de mayo de 2024, MiniCPM-Llama3-V 2.5, une un backbone Llama3 de 8000 millones de parámetros con un codificador de visión SigLip, y afirma un rendimiento en OCR, razonamiento con varias imágenes y respuesta a preguntas visuales que iguala o supera a GPT-4V en varios benchmarks públicos, pese a ejecutarse del todo sin conexión en un teléfono.

Desde entonces OpenBMB ha seguido con la serie. Versiones posteriores, como MiniCPM-V 4.5 y 4.6, bajan aún más el número de parámetros y suben la precisión, en la línea de una tendencia más amplia: cerrar la distancia entre los modelos multimodales pequeños en el dispositivo y otros mucho más grandes alojados en la nube. Los modelos se publican bajo licencia Apache 2.0 en Hugging Face y GitHub, para desarrolladores que necesitan IA multimodal sin conexión y que cuide la privacidad, en hardware de consumo.
