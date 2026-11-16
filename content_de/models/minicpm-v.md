---
title: 'MiniCPM-V'
name: 'MiniCPM-V'
slug: 'minicpm-v'
subtitle: 'Das multimodale Edge-Modell von OpenBMB, das auf einem Smartphone Vision-Aufgaben auf GPT-4V-Niveau bewältigen kann'
description: 'Das multimodale Edge-Modell von OpenBMB, das auf einem Smartphone Vision-Aufgaben auf GPT-4V-Niveau bewältigen kann'
company: 'openbmb'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://github.com/OpenBMB/MiniCPM-V'
price: 'Free'
rank: 5
release_date: '2024-05-20'
param_count: '8B'
context_window_tokens: 32768
modality: [text, image, video]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, small-model, on-device]
i18n_source: '83a16a62bccc'
---
MiniCPM-V ist eine Reihe offener Vision-Language-Modelle von OpenBMB, einem aus der Tsinghua-Universität hervorgegangenen Forschungslabor. Sie wurden so entwickelt, dass sie Bild- und Videoverständnis auf Smartphones und anderen Geräten mit begrenzten Ressourcen ermöglichen, ohne eine Server-GPU zu benötigen. Die im Mai 2024 veröffentlichte Version MiniCPM-Llama3-V 2.5 kombiniert ein Llama-3-Modell mit 8B Parametern und einen SigLIP-Vision-Encoder. Laut OpenBMB erreicht oder übertrifft sie GPT-4V in mehreren öffentlichen Benchmarks zu OCR, Schlussfolgern über mehrere Bilder und allgemeiner visueller Fragebeantwortung – und läuft dabei vollständig offline auf einem Smartphone.

OpenBMB hat die Reihe weiterentwickelt. Spätere Versionen wie MiniCPM-V 4.5 und 4.6 verringerten die Parameterzahl weiter und verbesserten zugleich die Genauigkeit. Das spiegelt den allgemeinen Trend wider, den Abstand zwischen kleinen multimodalen Modellen auf Geräten und deutlich größeren Cloud-Modellen zu verringern. Die Modelle stehen unter Apache 2.0 auf Hugging Face und GitHub bereit und richten sich an Entwickler, die multimodale KI offline und datenschutzfreundlich auf Geräten für Verbraucher benötigen.
