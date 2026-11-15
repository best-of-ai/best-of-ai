---
title: 'CogVideoX'
name: 'CogVideoX'
slug: 'cogvideox'
subtitle: 'Offene Modellfamilie von Zhipu zur Text-zu-Video-Generierung'
description: 'Offene Modellfamilie von Zhipu zur Text-zu-Video-Generierung'
company: 'zhipu-ai'
model_type: 'Video Generation'
logo_url: ''
product_url: 'https://github.com/THUDM/CogVideo'
price: 'Free'
rank: 6
release_date: '2024-08-27'
param_count: '5B'
modality: [text, video]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Zhipu API']
date: '2026-07-16'
tags: [video-generation, open-weight, api]
i18n_source: '892ae410997f'
---

CogVideoX ist ein Text-zu-Video-Modell mit offenen Gewichten von Zhipu AI, entwickelt mit dem KEG-Labor der Tsinghua-Universität. Es erschien im August 2024 als Nachfolger des ursprünglichen CogVideo-Projekts. Varianten mit 2 und 5 Milliarden Parametern verwenden ein kausales 3D-VAE zur räumlichen und zeitlichen Kompression sowie einen Transformer mit adaptiver Experten-LayerNorm. Unterstützt werden Text-zu-Video, Bild-zu-Video und die Fortsetzung eines Videos ausgehend von einem Bild oder Prompt. Das 5B-Modell erzeugt Clips von bis zu zehn Sekunden mit maximal 768p und 16 Bildern pro Sekunde. Im November 2024 folgte CogVideoX-1.5 mit längeren Ausgaben und höherer Auflösung. Die Gewichte stehen unter Apache 2.0 auf Hugging Face bereit; Zhipu bietet die Modelle auch über eine eigene API an. CogVideoX kann selbst gehostet oder als Dienst genutzt werden, ähnlich wie die Videogeneratoren von Stability AI und Runway.
