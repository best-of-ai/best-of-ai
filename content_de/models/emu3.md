---
title: 'Emu3'
name: 'Emu3'
slug: 'emu3'
subtitle: 'BAAIs Next-Token-Prediction-Modell für die gemeinsame Generierung und das Verständnis von Text, Bildern und Videos'
description: 'BAAIs Next-Token-Prediction-Modell für die gemeinsame Generierung und das Verständnis von Text, Bildern und Videos'
company: 'baai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://baai-agents.github.io/Emu3/'
price: 'Free'
rank: 5
release_date: '2024-09-27'
param_count: '8B'
modality: [text, image, video]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, research]
extra_model_types: ['Image Generation']
i18n_source: '6fd97391d2f7'
---
Emu3 ist ein multimodales Modell mit offenen Gewichten, das die Beijing Academy of Artificial Intelligence im September 2024 veröffentlichte. Es beruht auf der Idee, Text, Bilder und Videos als Folgen diskreter Tokens zu behandeln und einen einzelnen Transformer darauf zu trainieren, für alle drei Modalitäten das nächste Token vorherzusagen – ohne separate Diffusions- oder CLIP-Komponente. BAAI veröffentlichte es als Modell mit 8B Parametern in den Varianten Chat und Gen: Die eine ist auf das Verständnis von Vision und Sprache abgestimmt, die andere auf Generierung. Trotz des vereinfachten, einheitlichen Trainingsziels berichtete BAAI, dass Emu3 etablierte offene Modelle für einzelne Aufgaben übertraf, darunter SDXL bei der Bildgenerierung und LLaVA-1.6 beim Verständnis von Vision und Sprache. Das Projekt ist ein Vorläufer des größeren Modells Emu3.5 von BAAI, das Ende 2025 erschien und denselben Next-Token-Prediction-Ansatz auf 34 Milliarden Parameter skaliert.
