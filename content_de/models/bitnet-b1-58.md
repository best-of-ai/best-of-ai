---
title: 'BitNet b1.58'
name: 'BitNet b1.58'
slug: 'bitnet-b1-58'
subtitle: 'Forschungsmodell von Microsoft, das konkurrenzfähige LLM-Leistung mit ternären Gewichten von 1,58 Bit demonstriert'
description: 'Forschungsmodell von Microsoft, das konkurrenzfähige LLM-Leistung mit ternären Gewichten von 1,58 Bit demonstriert'
company: 'microsoft'
model_type: 'Language'
logo_url: ''
product_url: 'https://github.com/microsoft/BitNet'
price: 'Free'
rank: 6
release_date: '2024-02-27'
param_count: '2B (2B4T release)'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'GitHub']
date: '2026-07-16'
tags: [llm, open-weight, research, efficiency]
i18n_source: '4d1b2822f6ff'
---

BitNet b1.58 ist eine Forschungsreihe von Microsoft zu Sprachmodellen mit ternären Gewichten. Jeder Gewichtswert ist auf -1, 0 oder 1 beschränkt, statt wie üblich als 16- oder 32-Bit-Gleitkommazahl vorzuliegen. Die ursprüngliche Arbeit „The Era of 1-bit LLMs“ erschien im Februar 2024. Sie zeigte, dass Modelle, die nativ auf diese Weise trainiert – statt nachträglich quantisiert – werden, bei vergleichbarer Größe mit Modellen wie Llama 2 mithalten und zugleich Speicherbedarf und Inferenzenergie deutlich senken können. Im April 2025 folgte BitNet b1.58 2B4T: ein offen veröffentlichtes Modell mit zwei Milliarden Parametern, trainiert auf vier Billionen Tokens. Sein Speicherbedarf außerhalb der Embeddings beträgt etwa 0,4 GB und liegt damit deutlich unter ähnlich großen Modellen wie Gemma 3 1B oder MiniCPM 2B. Gewichte und Inferenzcode stehen unter MIT-Lizenz auf GitHub und Hugging Face bereit. Das Projekt ist weniger wegen Benchmark-Siegen bemerkenswert als dafür, dass es 1-Bit-Training ohne große Leistungseinbußen demonstriert – wichtig für leistungsfähige Modelle auf Smartphones und Edge-Geräten.
