---
title: 'Amazon Nova Lite'
name: 'Amazon Nova Lite'
slug: 'amazon-nova-lite'
subtitle: 'Nivel multimodal de bajo coste de Amazon en Bedrock'
description: 'Nivel multimodal de bajo coste de Amazon en Bedrock'
company: 'amazon'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://aws.amazon.com/ai/generative-ai/nova/'
price: 'Paid'
rank: 4
release_date: '2024-12-03'
param_count: 'Undisclosed'
context_window_tokens: 300000
modality: [text, image, video]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.06
output_price_usd_per_m: 0.24
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['AWS Bedrock']
date: '2026-07-16'
tags: [llm, multimodal, low-latency, api]
i18n_source: 'e235a3a5281e'
---

Amazon Nova Lite es un modelo multimodal de la familia Nova de Amazon, anunciado en diciembre de 2024 en AWS re:Invent y disponible a través de Amazon Bedrock. Acepta texto, imagen y vídeo y devuelve texto, con una ventana de contexto de 300 000 tokens, y cuesta 0,06 $ por millón de tokens de entrada y 0,24 $ por millón de tokens de salida. Amazon lo construyó como la opción intermedia entre el Nova Micro, solo de texto, y el Nova Pro, más capaz, para aplicaciones que tienen que tratar imágenes o vídeo y aun así quieren respuestas rápidas y un coste bajo.

Nova Lite compite con modelos multimodales de tamaño parecido de OpenAI y Google, y Amazon ha vendido la línea Nova sobre todo por la relación entre precio y rendimiento, no por encabezar rankings de benchmarks. Admite fine-tuning y destilación en Bedrock, así que se puede adaptar a tareas concretas, como entender documentos o responder preguntas visuales, sin pagar un modelo más grande en el momento de la inferencia.
