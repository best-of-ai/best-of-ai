---
title: 'Nemotron 5'
name: 'Nemotron 5'
slug: 'nemotron-5'
subtitle: 'Open-Weight-Modell von NVIDIA, optimiert für effiziente Inferenz auf eigener Hardware'
description: 'Open-Weight-Modell von NVIDIA, optimiert für effiziente Inferenz auf eigener Hardware'
company: 'nvidia'
model_type: 'Language'
logo_url: ''
product_url: 'https://developer.nvidia.com/nemotron'
price: 'Free'
rank: 6
release_date: '2026-07-10'
param_count: '70B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'NVIDIA Open Model License'
api_available: true
mmlu_score: 82.0
humaneval_score: 80.0
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'NVIDIA NIM', 'NGC']
date: '2026-07-19'
tags: [llm, open-weight, self-hosted, efficiency]
i18n_source: '528d47e90cc1'
---

Nemotron 5 setzt NVIDIAs Reihe offener Modelle fort. Im Mittelpunkt stehen weniger Spitzenplätze in Ranglisten als der Nachweis, wie gut Modelle auf den GPUs und dem Inferenz-Stack des Unternehmens laufen. Das dichte Modell mit 70 Milliarden Parametern hat ein Kontextfenster von 128.000 Tokens. Es wird unter der NVIDIA Open Model License angeboten und ist sowohl für die Bereitstellung mit einem Klick über NVIDIA-NIM-Microservices als auch als normaler Download bei Hugging Face verpackt.

Seit Nemotron-4 340B nutzt NVIDIA die Reihe, um Techniken wie Pruning und Destillation zu demonstrieren, die Modelle verkleinern, ohne ihre Qualität stark zu beeinträchtigen. Nemotron 5 führt diesen Schwerpunkt fort. Die Größe von 70 Milliarden Parametern wurde gewählt, damit das Modell auf eine einzelne H100 oder zwei Consumer-GPUs mit angemessener Quantisierung passt. NVIDIAs eigentliches Verkaufsargument ist die darunterliegende Hard- und Softwareplattform, nicht das Modell allein.
