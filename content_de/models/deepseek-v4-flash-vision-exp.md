---
title: 'DeepSeek-V4-Flash-Vision-Exp'
name: 'DeepSeek-V4-Flash-Vision-Exp'
slug: 'deepseek-v4-flash-vision-exp'
subtitle: 'Experimentelle multimodale Variante von V4-Flash für das Verständnis von Dokumenten und Diagrammen'
description: 'Experimentelle multimodale Variante von V4-Flash für das Verständnis von Dokumenten und Diagrammen'
company: 'deepseek'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://api-docs.deepseek.com/news/news260821/'
price: 'Paid'
rank: 6
release_date: '2026-08-21'
param_count: '284B (MoE, 13B active)'
context_window_tokens: 1048576
modality: [text, image]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.22
output_price_usd_per_m: 0.66
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['DeepSeek API']
date: '2026-08-31'
tags: [multimodal, vision, api, document-understanding, mixture-of-experts]
i18n_source: '1264f839812e'
---

DeepSeek veröffentlichte DeepSeek-V4-Flash-Vision-Exp am 21. August 2026 als experimentelle Variante von DeepSeek-V4-Flash mit Bildeingabe. Das zugrunde liegende sparse Mixture-of-Experts-Modell hat 284 Milliarden Parameter insgesamt und 13 Milliarden aktive pro Token. Die Vision-Variante soll bei agentischen und Schlussfolgerungsaufgaben mit dem reinen Textmodell mithalten und ergänzt Bildverständnis für das Lesen von Dokumenten und Diagrammen, visuelle Fragenbeantwortung und Agentenabläufe mit Text und Bildern. Bilder lassen sich als eingebettete Base64-Daten, URL oder über DeepSeeks Files-API übermitteln. Jedes Bild wird in 384 Tokens umgewandelt – deutlich weniger als bei GPT- und Claude-Modellen üblich.

Bei internen multimodalen Agenten-Benchmarks soll V4-Flash-Vision-Exp laut DeepSeek bei Aufgaben mit visueller Schlussfolgerung einen großen Teil des Abstands zu Anthropics Opus 4.8 schließen – eine deutliche Verbesserung gegenüber dem reinen Textmodell. Der Preis beträgt 0,22 US-Dollar pro Million Eingabetokens und 0,66 US-Dollar pro Million Ausgabetokens; zwischengespeicherte Eingaben sind günstiger. Bis zur regulären Veröffentlichung ist das Modell nur über die DeepSeek-API verfügbar, während das Unternehmen Rückmeldungen sammelt.
