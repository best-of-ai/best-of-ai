---
title: 'Inkling'
name: 'Inkling'
slug: 'inkling'
subtitle: 'Erstes Open-Weight-Modell aus Mira Muratis Thinking Machines Lab'
description: 'Erstes Open-Weight-Modell aus Mira Muratis Thinking Machines Lab'
company: 'thinking-machines'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://thinkingmachines.ai/model-card/inkling/'
price: 'Free'
rank: 6
release_date: '2026-07-15'
param_count: '975B (41B active)'
context_window_tokens: 1000000
modality: [text, image, audio]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Tinker']
date: '2026-07-25'
tags: [llm, open-weight, multimodal, self-hosted]
i18n_source: '010a5c004d85'
---

Inkling ist das erste Produktivmodell von Thinking Machines Lab, dem von der früheren OpenAI-CTO Mira Murati gegründeten KI-Start-up. Es erschien am 15. Juli 2026 als nativ multimodales Mixture-of-Experts-Modell mit 975 Milliarden Parametern insgesamt und 41 Milliarden aktiven pro Token. Trainiert wurde es mit 45 Billionen Tokens aus Text, Bildern, Audio und Video auf Nvidia-GB300-NVL72-Systemen. Die Gewichte stehen auf Hugging Face bereit und unterstützen ein Kontextfenster von einer Million Tokens. Über die Fine-Tuning-Plattform Tinker des Unternehmens ist das Kontextfenster auf 256.000 Tokens begrenzt. Die Apache-2.0-Lizenz erlaubt freie Feinabstimmung und Weiterverbreitung. Im Artificial Analysis Intelligence Index startete es mit 41 Punkten als damals stärkstes offenes Modell aus einem US-Labor. Es entspricht dem erklärten Ziel von Thinking Machines, Modelle für einzelne Nutzer:innen statt ein einziges System für alle zu entwickeln.
