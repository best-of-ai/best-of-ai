---
title: 'Falcon Mamba 7B'
name: 'Falcon Mamba 7B'
slug: 'falcon-mamba-7b'
subtitle: 'Open-Weight-Modell des TII auf Basis der Mamba-State-Space-Architektur.'
description: 'Open-Weight-Modell des TII auf Basis der Mamba-State-Space-Architektur.'
company: 'technology-innovation-institute'
model_type: 'Language'
logo_url: ''
product_url: 'https://falconllm.tii.ae/'
price: 'Free'
rank: 3
release_date: '2024-08-12'
param_count: '7B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'TII Falcon Mamba 7B License 1.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, hybrid-architecture, self-hosted]
i18n_source: '117aa18c3953'
---

Falcon Mamba 7B erschien im August 2024 beim Technology Innovation Institute und war das erste leistungsfähige offene Sprachmodell mit sieben Milliarden Parametern, das vollständig auf der Mamba-Zustandsraumarchitektur statt auf Transformer-Attention beruhte. Da es keinen Attention-Mechanismus hat, bleiben Speicherbedarf und Inferenzgeschwindigkeit auch bei längeren generierten Sequenzen konstant. Bei Transformern wächst der Rechenaufwand dagegen mit der Kontextlänge. Das TII trainierte das Modell in mehreren Stufen und erhöhte die effektive Kontextverarbeitung von 2.048 auf 8.192 Tokens. In Benchmarks erreichte oder übertraf es ähnlich große Transformer wie Mistral 7B und Meta Llama 3.1 8B sowie andere Nicht-Transformer wie RecurrentGemma 9B und RWKV-v6. Das TII stellt die Gewichte auf Hugging Face unter seiner Falcon-Mamba-Lizenz bereit. Das Modell richtet sich an Forschende und Entwickler:innen, die für lange Sequenzen eine Alternative zu Attention-Architekturen suchen.
