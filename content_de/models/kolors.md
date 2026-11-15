---
title: 'Kolors'
name: 'Kolors'
slug: 'kolors'
subtitle: 'Offenes Text-zu-Bild-Modell von Kuaishou mit besonderer Stärke bei chinesischen Eingaben'
description: 'Offenes Text-zu-Bild-Modell von Kuaishou mit besonderer Stärke bei chinesischen Eingaben'
company: 'kuaishou'
model_type: 'Image Generation'
logo_url: ''
product_url: 'https://github.com/Kwai-Kolors/Kolors'
price: 'Free'
rank: 5
release_date: '2024-07-06'
param_count: '2.6B'
modality: [text, image]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Kuaishou API']
date: '2026-07-16'
tags: [image-generation, open-weight, api]
i18n_source: 'b566c88c4748'
---
Kolors ist das Text-zu-Bild-Modell von Kuaishou mit offenen Gewichten und wurde im Juli 2024 veröffentlicht. Es ist ein latentes Diffusionsmodell mit etwa 2,6 Milliarden Parametern auf Basis einer U-Net-Architektur. Als Text-Encoder nutzt es ChatGLM statt eines CLIP-ähnlichen Encoders. Dadurch kann es chinesischsprachige Eingaben und chinesische Schrift in Bildern besonders gut lesen und darstellen. Das Modell generiert Bilder nativ mit einer Auflösung von 1024 × 1024 Pixeln und unterstützt verschiedene Seitenverhältnisse. Kuaishou trainierte es mit Milliarden von Text-Bild-Paaren und veröffentlichte die Gewichte kostenlos für Forschungszwecke auf GitHub und Hugging Face. Für den kommerziellen Einsatz ist ein separates Registrierungsverfahren erforderlich. Neben Modellen wie Flux und Stable Diffusion 3 zählt Kolors zu den wenigen weit verbreiteten offenen Bildmodellen, die nicht-lateinische Schriftsysteme gut verarbeiten.
