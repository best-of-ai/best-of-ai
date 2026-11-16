---
title: 'Kimi-VL'
name: 'Kimi-VL'
slug: 'kimi-vl'
subtitle: 'Open-Weight-Vision-Language-Modell von Moonshot.'
description: 'Open-Weight-Vision-Language-Modell von Moonshot.'
company: 'moonshot-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.moonshot.ai/'
price: 'Free'
rank: 4
release_date: '2025-04-10'
param_count: '16B (2.8B active)'
context_window_tokens: 128000
modality: [text, image]
open_weight: true
license: 'MIT'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, multimodal, vision]
extra_model_types: ['Reasoning']
i18n_source: 'edae211c40fc'
---

Kimi-VL ist Moonshot AIs Vision-Language-Modell mit offenen Gewichten und erschien im April 2025. Es nutzt eine Mixture-of-Experts-Architektur mit 16 Milliarden Parametern insgesamt, aber nur rund 2,8 Milliarden aktiven im Sprachdecoder. Dadurch bleiben die Inferenzkosten im Verhältnis zu den Fähigkeiten niedrig. Der Decoder ist mit MoonViT verbunden, einem nativen Vision-Encoder, der Bilder mit sehr hoher Auflösung lesen kann, ohne sie vorher zu verkleinern. Das Modell verarbeitet lange Dokumente und Videos mit einem Kontextfenster von 128.000 Tokens. Es richtet sich auf agentische Aufgaben wie die Bedienung von Computerbildschirmen aus und schneidet bei OSWorld gut ab. Weitere Anwendungen umfassen OCR, Schlussfolgern zu Bildern und Bildvergleiche. Moonshot veröffentlichte außerdem Kimi-VL-Thinking, eine mit Reinforcement Learning auf Schlussfolgerungsdaten trainierte Variante, die die Problemlösung des Basismodells auf längere Aufgaben ausdehnt.
