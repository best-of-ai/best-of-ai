---
title: 'Granite Vision'
name: 'Granite Vision'
slug: 'granite-vision'
subtitle: 'El modelo compacto de visión y lenguaje de IBM para entender documentos y gráficos'
description: 'El modelo compacto de visión y lenguaje de IBM para entender documentos y gráficos'
company: 'ibm'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.ibm.com/granite'
price: 'Free'
rank: 5
release_date: '2025-02-26'
param_count: '2B'
context_window_tokens: 16384
modality: [text, image]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['IBM watsonx', 'Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, vision, enterprise]
i18n_source: 'a32ea768a093'
---

Granite Vision es el modelo compacto de visión y lenguaje de IBM, publicado como parte de la actualización Granite 3.2 en febrero de 2025 y construido de forma específica para entender documentos visuales, no para el chat general con imágenes. Con 2000 millones de parámetros, lee tablas, gráficos, infografías, diagramas y documentos escaneados y los convierte en texto estructurado. Apunta a benchmarks como DocVQA y ChartQA, donde IBM dice que iguala a modelos abiertos varias veces más grandes. El tamaño reducido es deliberado: IBM lo diseñó para cargas empresariales cotidianas, como leer facturas o extraer datos de informes, donde ejecutar un modelo multimodal grande no es práctico ni asequible. Admite una ventana de contexto de 16K tokens, es de pesos abiertos bajo Apache 2.0 y se distribuye por Hugging Face e IBM watsonx. Versiones posteriores (3.3 y las variantes de visión de Granite 4.0) siguen el mismo diseño centrado en documentos.
