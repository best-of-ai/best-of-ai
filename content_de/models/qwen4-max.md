---
title: 'Qwen4-Max'
name: 'Qwen4-Max'
slug: 'qwen4-max'
subtitle: 'Proprietäres Flaggschiffmodell von Alibaba für die Qwen-API und Cloudplattform'
description: 'Proprietäres Flaggschiffmodell von Alibaba für die Qwen-API und Cloudplattform'
company: 'alibaba'
model_type: 'Language'
logo_url: ''
product_url: 'https://qwen.ai/'
price: 'Paid'
rank: 8
release_date: '2026-07-11'
param_count: 'Undisclosed'
context_window_tokens: 1000000
modality: [text, image]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 1.20
output_price_usd_per_m: 4.80
api_available: true
mmlu_score: 88.0
lmarena_score: 1352
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['Alibaba Cloud', 'Qwen Chat', 'API']
date: '2026-07-19'
tags: [llm, proprietary, api, multimodal]
i18n_source: 'd9ca0c4f1096'
---

Qwen4-Max ist Alibabas proprietäres Spitzenmodell und steht über der offenen Qwen3-Familie, die das Unternehmen auf Hugging Face veröffentlicht. Anders als diese Modelle ist Qwen4-Max geschlossen und nur über die API von Alibaba Cloud, Qwen Chat oder Partnerplattformen erreichbar. Der Preis beträgt 1,20 US-Dollar pro Million Eingabetokens und 4,80 US-Dollar pro Million Ausgabetokens. Das Modell verarbeitet Text- und Bildeingaben und bietet ein Kontextfenster mit einer Million Tokens. In Alibabas eigenen Benchmark-Vergleichen wird es direkt mit GPT-5.6 und Gemini 3.5 Pro verglichen.

Die Trennung zwischen offenen Qwen3-Modellen und dem geschlossenen Qwen4-Max folgt einem Muster, das sich bei anderen KI-Laboren etabliert hat: Leistungsfähige mittelgroße Modelle werden freigegeben, um Entwickler zu gewinnen, während das größte und teuerste Modell als kostenpflichtige API angeboten wird. Mit diesem Ansatz hat Alibaba Qwens Verbreitung weit über China hinaus ausgebaut. Besonders Entwickler auf Hugging Face stimmen für offene Modelle, die sie feinabstimmen, greifen im produktiven Einsatz bei Bedarf an zusätzlicher Rechenleistung aber weiterhin auf die Max-Stufe zurück.
