---
title: 'Apple Foundation Model'
name: 'Apple Foundation Model'
slug: 'apple-foundation-model'
subtitle: 'Modelos fundacionales de Apple, en el dispositivo y en servidor, detrás de Apple Intelligence'
description: 'Modelos fundacionales de Apple, en el dispositivo y en servidor, detrás de Apple Intelligence'
company: 'apple'
model_type: 'Language'
logo_url: ''
product_url: 'https://machinelearning.apple.com/research/introducing-apple-foundation-models'
price: 'Paid'
rank: 6
release_date: '2024-06-10'
param_count: '3B (on-device)'
context_window_tokens: 32000
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Self-hosted]
runs_at_home: false
platforms: ['iOS', 'macOS']
date: '2026-07-16'
tags: [llm, on-device, foundation-model]
i18n_source: '7fbb8197cfde'
---

Los Foundation Models de Apple son el par de modelos de lenguaje detrás de Apple Intelligence, presentados en junio de 2024 en la WWDC: un modelo de unos 3000 millones de parámetros que se ejecuta directamente en el hardware de iPhone, iPad y Mac, y un modelo más grande que corre en los servidores Private Cloud Compute de Apple para las tareas que el modelo del dispositivo no puede resolver solo. El modelo en el dispositivo se apoya en técnicas como el uso compartido de la KV-cache y el entrenamiento consciente de la cuantización a 2 bits para caber en la memoria y el consumo de un teléfono, mientras que el modelo de servidor usa un transformer de mezcla de expertos. La ventana de contexto útil del modelo en el dispositivo se limita a 4096 tokens; el de servidor llega hasta 32 000.

Apple no vende acceso por API a estos modelos como hacen OpenAI o Anthropic. En su lugar, alimentan funciones del sistema como las herramientas de escritura, los resúmenes de notificaciones y las capacidades renovadas de Siri y, desde la WWDC 2025, se exponen a desarrolladores externos a través del framework Foundation Models, para que las apps llamen al modelo del dispositivo de forma directa, gratis y sin conexión de red. Apple ha actualizado después la gama en la WWDC 2025 y presentó una tercera generación en la WWDC 2026, en general centrada en ganancias de calidad y de eficiencia más que en aumentos grandes de tamaño, en línea con la preferencia de Apple por la privacidad y la inferencia en el dispositivo frente a enviar datos de quien usa el producto a modelos de frontera alojados en la nube.
