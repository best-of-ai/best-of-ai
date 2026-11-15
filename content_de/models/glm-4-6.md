---
title: 'GLM-4.6'
name: 'GLM-4.6'
slug: 'glm-4-6'
subtitle: 'Preisgünstiges offenes Modell von Zhipu für alltägliche Programmieraufgaben'
description: 'Preisgünstiges offenes Modell von Zhipu für alltägliche Programmieraufgaben'
company: 'zhipu-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://www.zhipuai.cn/'
price: 'Free'
rank: 7
release_date: '2025-09-30'
param_count: '355B (MoE, ~32B active)'
context_window_tokens: 200000
modality: [text, image, code]
open_weight: true
license: 'Apache 2.0'
input_price_usd_per_m: 0.43
output_price_usd_per_m: 1.75
api_available: true
humaneval_score: 85.0
lmarena_score: 1320
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, code, self-hosted]
i18n_source: '89b99962ef6e'
---

GLM-4.6 ist das preisgünstig ausgerichtete Modell mit offenen Gewichten von Zhipu (Z.ai). Es erschien am 30. September 2025 als Weiterentwicklung von GLM-4.5. Das Mixture-of-Experts-Modell umfasst rund 355 Milliarden Parameter, davon etwa 32 Milliarden aktiv pro Token. Sein Kontextfenster wurde von 128.000 auf 200.000 Tokens erweitert, um längere agentische Sitzungen zu unterstützen. Es verarbeitet Text, Bilder und Code und wurde gezielt für den Einsatz von Werkzeugen in Programmierassistenten wie Claude Code, Cline und Roo Code abgestimmt.

Bei Programmier-Benchmarks gehört es zur Spitzengruppe offener Modelle. Es führt LiveCodeBench v6 an und konkurriert bei mehreren agentischen Aufgaben mit DeepSeek-V3.1-Terminus und Claude Sonnet 4. Der wichtigste Vorteil ist der Preis: Weniger als ein US-Dollar pro Million Eingabetokens unterbietet die meisten proprietären Spitzenmodelle deutlich und reicht dennoch für praktische Programmierarbeit. Deshalb findet es sich häufig in selbst gehosteten und API-basierten Entwicklerwerkzeugen.
