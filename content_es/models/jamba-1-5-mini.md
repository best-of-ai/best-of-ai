---
title: 'Jamba 1.5 Mini'
name: 'Jamba 1.5 Mini'
slug: 'jamba-1-5-mini'
subtitle: 'El modelo híbrido compacto transformer-Mamba de AI21'
description: 'El modelo híbrido compacto transformer-Mamba de AI21'
company: 'ai21-labs'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.ai21.com/jamba/'
price: 'Free'
rank: 4
release_date: '2024-08-22'
param_count: '52B (12B active)'
context_window_tokens: 256000
modality: [text]
open_weight: true
license: 'Jamba Open Model License'
input_price_usd_per_m: 0.2
output_price_usd_per_m: 0.4
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'AWS Bedrock']
date: '2026-07-16'
tags: [llm, open-weight, long-context, hybrid-architecture]
i18n_source: 'e0243c637f6d'
---

Jamba 1.5 Mini es el modelo más pequeño de la familia Jamba 1.5 de AI21 Labs, publicado junto a Jamba 1.5 Large el 22 de agosto de 2024. Comparte la misma arquitectura híbrida de mezcla de expertos Transformer-Mamba, reducida a 52 000 millones de parámetros en total con 12 000 millones activos, y mantiene la misma ventana de contexto de 256 000 tokens que su hermano mayor. En el benchmark Arena Hard obtuvo 46,1, por delante de modelos de tamaño parecido como Claude 3 Haiku, Mixtral 8x22B y Command R+. AI21 lo construyó para usos de negocio sensibles a la latencia, como llamadas a funciones, salida JSON estructurada y generación anclada a fuentes, y lo cobra a 0,20 $ por millón de tokens de entrada y 0,40 $ por millón de tokens de salida por su API. Como Jamba 1.5 Large, se publica bajo la Jamba Open Model License de AI21, con pesos en Hugging Face y disponibilidad en AWS Bedrock.
