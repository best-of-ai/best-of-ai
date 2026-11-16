---
title: 'CogView3'
name: 'CogView3'
slug: 'cogview3'
subtitle: 'Zhipus Text-zu-Bild-Modell auf Basis von Relay-Diffusion'
description: 'Zhipus Text-zu-Bild-Modell auf Basis von Relay-Diffusion'
company: 'zhipu-ai'
model_type: 'Image Generation'
logo_url: ''
product_url: 'https://github.com/THUDM/CogView3'
price: 'Free'
rank: 5
release_date: '2024-09-29'
param_count: '3B'
modality: [text, image]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Zhipu API']
date: '2026-07-16'
tags: [image-generation, open-weight, api]
i18n_source: 'e06af9d7cbba'
---
CogView3 ist ein Text-zu-Bild-Modell von Zhipu AI und der Tsinghua-Universität. Es wurde in einer Forschungsarbeit vom März 2024 beschrieben und im September 2024 auf Hugging Face als Open Source veröffentlicht. Im Zentrum steht Relay-Diffusion, ein kaskadierter Ansatz: Eine Basisstufe mit drei Milliarden Parametern erzeugt zunächst ein Bild mit niedriger Auflösung von 512 × 512 Pixeln. Anschließend wird dem Bild in einer zweiten Stufe Rauschen hinzugefügt, bevor ein kürzerer Diffusionsdurchlauf zur Superauflösung erfolgt. Ältere kaskadierte Modelle konditionierten die zweite Stufe stattdessen direkt mit der niedrig aufgelösten Ausgabe. Zhipu berichtet, dass CogView3 in menschlichen Bewertungen Stable Diffusion XL mit deutlichem Abstand übertrifft und dabei nur etwa die Hälfte der Inferenzzeit benötigt. Eine destillierte Version erreicht eine vergleichbare Qualität mit ungefähr einem Zehntel der SDXL-Inferenzschritte. Modell und Code stehen unter Apache 2.0. Später ergänzte Zhipu die Familie um CogView-3Plus, eine größere Diffusion-Transformer-Variante, sowie eine gehostete Version über die Zhipu-API.
