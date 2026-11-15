---
title: 'Qwen3.8-Flash-Next'
name: 'Qwen3.8-Flash-Next'
slug: 'qwen3-8-flash-next'
subtitle: 'Offene Vorschau von Alibaba auf die Qwen4-Architektur der nächsten Generation'
description: 'Offene Vorschau von Alibaba auf die Qwen4-Architektur der nächsten Generation'
company: 'alibaba'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://qwen.ai/'
price: 'Free'
rank: 7
release_date: '2026-08-26'
param_count: '125B (6B active)'
context_window_tokens: 262144
modality: [text, image, video]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Alibaba Cloud', 'API']
date: '2026-09-05'
tags: [llm, open-weight, multimodal, moe, apache-2.0, cost-efficient]
i18n_source: '6dac4a7632ca'
---

Alibaba veröffentlichte Qwen3.8-Flash-Next am 26. August 2026 als Open Source und ermöglichte Entwicklern damit einen frühen Einblick in die Qwen4-Architektur, noch vor der vollständigen Modellfamilie. Das multimodale Mixture-of-Experts-Modell hat ein Backbone mit 125 Milliarden Parametern, von denen pro Token nur 6 Milliarden aktiv sind. Hinzu kommen eine N-Gramm-Einbettungstabelle mit 51 Milliarden Parametern und ein Modul zur Vorhersage mehrerer Tokens mit 4 Milliarden Parametern. Das Kontextfenster umfasst nativ 262.144 Tokens und lässt sich auf eine Million erweitern. Alibaba zufolge übertrifft das Modell das ältere Qwen3.7-Plus besonders bei Programmier- und Büroaufgaben, während Training etwa neunmal und Betrieb etwa zwölfmal günstiger sind. Zum Start wurden sowohl ein Standard- als auch ein FP8-Checkpoint veröffentlicht.
