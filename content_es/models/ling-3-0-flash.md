---
title: 'Ling-3.0-Flash'
name: 'Ling-3.0-Flash'
slug: 'ling-3-0-flash'
subtitle: 'El modelo de razonamiento de pesos abiertos y eficiente de Ant Group, pensado para agentes de IA en producción'
description: 'El modelo de razonamiento de pesos abiertos y eficiente de Ant Group, pensado para agentes de IA en producción'
company: 'ant-group'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.antgroup.com'
price: 'Free'
rank: 6
release_date: '2026-07-23'
param_count: '124B (5.1B active)'
context_window_tokens: 262144
modality: [text]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 0.075
output_price_usd_per_m: 0.22
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'OpenRouter']
date: '2026-08-09'
tags: [llm, open-weight, reasoning, agentic, mixture-of-experts, efficiency]
extra_model_types: ['Code']
i18n_source: '368f5f371b66'
---

Ling-3.0-Flash es la entrada más reciente de la línea Ling de Ant Group, centrada en la eficiencia. Lo construyó su laboratorio inclusionAI y se presentó el 23 de julio de 2026 como modelo fundacional de razonamiento híbrido para cargas de agentes de IA en producción. Es un modelo de mezcla de expertos de 124 000 millones de parámetros que activa solo unos 5100 millones de parámetros por token, admite de forma nativa una ventana de contexto de 256 000 tokens que puede escalar hasta 1 millón, y Ant dice que iguala o supera a modelos con dos o tres veces su número de parámetros en benchmarks de razonamiento, seguimiento de instrucciones y contexto largo. Un sistema de caché jerárquica a nivel de clúster recorta el tiempo hasta el primer token en conversaciones largas entre un 60 y un 80 %. Ant fijó la API de primera parte en 0,075 $ por millón de tokens de entrada y 0,22 $ por millón de tokens de salida, entre las tarifas más baratas medidas para un modelo que puntúa 38 o más en el Artificial Analysis Intelligence Index, y publicó los pesos en Hugging Face bajo la licencia MIT.
