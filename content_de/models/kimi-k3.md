---
title: 'Kimi K3'
name: 'Kimi K3'
slug: 'kimi-k3'
subtitle: 'Offenes Modell von Moonshot mit 2,8 Billionen Parametern, das bislang größte veröffentlichte offene Modell'
description: 'Offenes Modell von Moonshot mit 2,8 Billionen Parametern, das bislang größte veröffentlichte offene Modell'
company: 'moonshot-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.moonshot.ai/'
price: 'Free'
rank: 8
release_date: '2026-07-16'
param_count: '2.8T (MoE)'
context_window_tokens: 1000000
modality: [text, image, video]
open_weight: true
license: 'Modified MIT'
input_price_usd_per_m: 3
output_price_usd_per_m: 15
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-08-09'
tags: [llm, open-weight, multimodal, reasoning, mixture-of-experts]
extra_model_types: ['Reasoning']
i18n_source: 'bf5cebe9bf5c'
---

Kimi K3 ist Moonshot AIs bislang größte Veröffentlichung. Das Mixture-of-Experts-Modell umfasst 2,8 Billionen Parameter und ist laut Unternehmen das größte offene Modell, das bisher veröffentlicht wurde. Es verarbeitet nativ Text, Bilder und Videos, bietet ein Kontextfenster von einer Million Tokens und arbeitet dauerhaft im Thinking-Modus statt einen separaten Schnellmodus anzubieten. Über die API kostet es drei US-Dollar pro Million Eingabetokens (bei Cache-Treffer sinkt der Preis auf 0,30 US-Dollar) und 15 US-Dollar pro Million Ausgabetokens. Damit unterbietet es geschlossene Spitzenmodelle westlicher Labore deutlich. Kurz nach der Ankündigung vom 16. Juli wurden die vollständigen Gewichte auf Hugging Face veröffentlicht. Die MXFP4-Quantisierung reduziert den Download auf etwa 1,4 TB – klein genug für leistungsfähige selbst gehostete Systeme ohne dedizierten Cluster.
