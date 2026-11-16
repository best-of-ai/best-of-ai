---
title: 'Hunyuan DiT'
name: 'Hunyuan DiT'
slug: 'hunyuan-dit'
subtitle: 'Offener Diffusion-Transformer von Tencent für Text-zu-Bild auf Chinesisch und Englisch'
description: 'Offener Diffusion-Transformer von Tencent für Text-zu-Bild auf Chinesisch und Englisch'
company: 'tencent'
model_type: 'Image Generation'
logo_url: ''
product_url: 'https://github.com/Tencent/HunyuanDiT'
price: 'Free'
rank: 5
release_date: '2024-05-14'
param_count: '1.5B'
modality: [text, image]
open_weight: true
license: 'Tencent Hunyuan License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Tencent Cloud']
date: '2026-07-16'
tags: [image-generation, open-weight, api]
i18n_source: '7a104e51d815'
---
Hunyuan-DiT ist das Modell von Tencent mit offenen Gewichten zur Bildgenerierung aus Text. Es basiert auf einer Diffusion-Transformer-Architektur statt auf dem U-Net-Entwurf, den viele frühere Diffusionsmodelle nutzten. Tencent veröffentlichte es im Mai 2024. Es kombiniert einen Entrauschungs-Transformer mit 1,5 Milliarden Parametern mit zweisprachigen CLIP- und mehrsprachigen T5-Text-Encodern. So kann es Eingaben auf Chinesisch und Englisch ähnlich gut umsetzen. Der Schwerpunkt auf beiden Sprachen ist das zentrale Merkmal des Modells: Die meisten offenen Text-zu-Bild-Modelle jener Zeit verarbeiteten chinesische Eingaben nur schlecht. Hunyuan-DiT wurde gezielt trainiert, um diese Lücke zu schließen. Es generiert Bilder mit 1024 × 1024 Pixeln und enthält eine multimodale Chat-Komponente, mit der Nutzer ein Bild über mehrere Dialogrunden verfeinern können, statt die gesamte Eingabe jedes Mal neu zu schreiben. Tencent veröffentlichte die Gewichte auf Hugging Face und GitHub unter der Hunyuan-Lizenz. Ein späteres Update auf Version 1.1 behob übermäßige Sättigung und Wasserzeichenartefakte des ursprünglichen Checkpoints.
