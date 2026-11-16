---
title: 'Jamba Large 1.6'
name: 'Jamba Large 1.6'
slug: 'jamba-large-1-6'
subtitle: 'El modelo principal híbrido transformer-Mamba actualizado de AI21'
description: 'El modelo principal híbrido transformer-Mamba actualizado de AI21'
company: 'ai21-labs'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.ai21.com/jamba/'
price: 'Free'
rank: 4
release_date: '2025-03-06'
param_count: '398B (94B active)'
context_window_tokens: 256000
modality: [text]
open_weight: true
license: 'Jamba Open Model License'
input_price_usd_per_m: 2
output_price_usd_per_m: 8
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: false
platforms: ['Hugging Face', 'AWS Bedrock']
date: '2026-07-16'
tags: [llm, open-weight, long-context, hybrid-architecture]
i18n_source: '7f46269a09c0'
---

Jamba Large 1.6 es el modelo de lenguaje principal de AI21 Labs, construido sobre una arquitectura híbrida que combina capas de atención transformer con capas del modelo de espacio de estados Mamba. AI21 lo publicó en marzo de 2025 como parte de la familia Jamba 1.6, junto a un Jamba Mini 1.6 más pequeño. El modelo tiene 398 000 millones de parámetros en total, con solo 94 000 millones activos en inferencia gracias a un diseño de mezcla de expertos, lo que contiene el coste de cómputo y admite una ventana de contexto de 256 000 tokens. AI21 lo dirige a clientes de empresa que necesitan procesar documentos largos, contratos o bases de código sin enviar datos a un tercero, ya que el modelo está disponible para despliegue autoalojado y también por API. En los propios benchmarks de AI21, Jamba Large 1.6 superó a modelos abiertos de Meta, Mistral y Cohere en un abanico de tareas, y corre de forma claramente más rápida que los transformers densos de tamaño parecido, por el tratamiento más eficiente de las secuencias largas que dan las capas Mamba.
