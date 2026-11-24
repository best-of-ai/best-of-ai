---
title: 'SenseNova Loop-9B'
name: 'SenseNova Loop-9B'
slug: 'sensenova-loop-9b'
subtitle: 'Open-Weight-Multimodalmodell von SenseTime mit 9B Parametern, das seine Schichten in einer Schleife wiederverwendet'
description: 'Open-Weight-Multimodalmodell von SenseTime mit 9B Parametern, das seine Schichten in einer Schleife wiederverwendet'
company: 'sensetime'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.sensetime.com/en/news/sensenova-loop-9b-release-20261118-1435'
price: 'Free'
rank: 5
release_date: '2026-11-17'
param_count: '9B (about 14.6B inference-equivalent)'
context_window_tokens: 512000
modality: [text, image]
open_weight: true
license: 'Open weights'
api_available: true
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'GitHub']
date: '2026-11-24'
tags: [llm, open-weight, multimodal, small-model, self-hosted]
i18n_source: '842af8c2e04b'
---
SenseNova Loop-9B ist die offizielle Version des Open-Weight-Multimodalmodells von SenseTime, veröffentlicht am 17. November 2026 nach einer Vorschau. Es hat etwa 9B Parameter in 32 verschiedenen Decoder-Schichten, die pro Durchlauf als 56 Schichtberechnungen laufen, was rund 14,6B Inferenz-äquivalente Parameter ergibt. Es nimmt Text und Bilder entgegen, gibt Text aus und verarbeitet bis zu 512.000 Tokens Kontext.

Die 4-Bit-Gewichte sind etwa 4,9 GB groß, sodass es auf Consumer-Hardware passt, und ein offizieller AWQ-Build erschien am Starttag. SenseTime nennt es vergleichbar mit Qwen3.8-27B: 41,36 gegenüber 44,60 bei NL2Repo und 65,31 gegenüber 65,01 bei AIDABench. Die Gewichte liegen auf Hugging Face unter sensenova/sensenova-loop, der Code auf GitHub.
