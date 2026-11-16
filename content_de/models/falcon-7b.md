---
title: 'Falcon 7B'
name: 'Falcon 7B'
slug: 'falcon-7b'
subtitle: 'Die kompakte Falcon-Stufe von TII, die zur Verbreitung der ursprünglichen Falcon-Veröffentlichung beitrug'
description: 'Die kompakte Falcon-Stufe von TII, die zur Verbreitung der ursprünglichen Falcon-Veröffentlichung beitrug'
company: 'technology-innovation-institute'
model_type: 'Language'
logo_url: ''
product_url: 'https://falconllm.tii.ae/'
price: 'Free'
rank: 5
release_date: '2023-05-25'
param_count: '7B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, small-model, legacy]
i18n_source: '61f475ea6988'
---
Falcon 7B ist das kleinere Schwestermodell der ursprünglichen Falcon-Veröffentlichung von TII. Es wurde mit demselben RefinedWeb-Datensatz wie Falcon 40B trainiert, ist jedoch für eine günstigere Bereitstellung auf einer einzelnen GPU ausgelegt. TII trainierte es Anfang 2023 über etwa zwei Wochen und veröffentlichte es unter der freizügigen Apache-2.0-Lizenz. Entwickler konnten es damit gebührenfrei kommerziell nutzen, verändern und bereitstellen. Diese Lizenzierung war damals bemerkenswert, da viele ähnlich leistungsfähige offene Modelle nur für Forschungszwecke freigegeben waren. Falcon 7B teilt mit dem 40B-Modell eine reine Decoder-Transformer-Architektur mit Multiquery-Attention, hat jedoch ein Kontextfenster von 2048 Tokens und geringere Rechenanforderungen. Dadurch war es 2023 und Anfang 2024 eine verbreitete Wahl für Fine-Tuning-Experimente und Anwendungen auf Geräten. TII ist inzwischen zu den Familien Falcon 3 und Falcon Mamba übergegangen. Falcon 7B bleibt als älteres Modell auf Hugging Face weit verbreitet verfügbar.
