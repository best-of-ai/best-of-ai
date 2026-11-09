---
title: 'Fuyu-8B'
name: 'Fuyu-8B'
slug: 'fuyu-8b'
subtitle: 'Modelo multimodal de pesos abiertos de Adept, construido para la percepción de agentes digitales'
description: 'Modelo multimodal de pesos abiertos de Adept, construido para la percepción de agentes digitales'
company: 'adept-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.adept.ai/blog/fuyu-8b'
price: 'Free'
rank: 3
release_date: '2023-10-17'
param_count: '8B'
context_window_tokens: 16000
modality: [text, image]
open_weight: true
license: 'CC-BY-NC 4.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, multimodal, open-weight, agentic]
i18n_source: 'f65d9839efe1'
---

Fuyu-8B es un modelo multimodal que Adept AI publicó en octubre de 2023, construido en concreto para apoyar a agentes digitales que tienen que ver pantallas y actuar sobre ellas, no para servir de chatbot de uso general. Adept lo diseñó en torno a una arquitectura simplificada: mete parches de imagen directamente en un transformador solo decodificador estándar, sin un codificador de imagen aparte, lo que le permite aceptar imágenes en la resolución en la que llegan en lugar de redimensionarlo todo a un tamaño fijo. Eso importa para el uso de Adept, porque necesita leer elementos de interfaz, botones y texto a resolución nativa para responder preguntas sobre capturas de pantalla, gráficos y diagramas, y para localizar elementos concretos en una pantalla. Adept publicó el modelo de 8000 millones de parámetros en Hugging Face bajo una licencia CC-BY-NC: se puede usar y modificar gratis, pero no con fines comerciales, y lo situó como una vista previa pública más pequeña del modelo que impulsa el producto propio de Adept, no como una oferta del todo aparte. Admite una ventana de contexto de 16K tokens, y Adept fue adquirida después, con gran parte del equipo pasando a Amazon en 2024, de modo que Fuyu-8B queda como una foto de aquella línea de investigación centrada en agentes.
