---
title: 'GLM-5.2'
name: 'GLM-5.2'
slug: 'glm-5-2'
subtitle: 'Offenes Flaggschiffmodell von Zhipu, Mitte 2026 zeitgleich mit Kimi K2.7 veröffentlicht'
description: 'Offenes Flaggschiffmodell von Zhipu, Mitte 2026 zeitgleich mit Kimi K2.7 veröffentlicht'
company: 'zhipu-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.zhipuai.cn/'
price: 'Free'
rank: 7
release_date: '2026-06-13'
param_count: '~744B (MoE, ~40B active)'
context_window_tokens: 1000000
modality: [text, code]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 1.4
output_price_usd_per_m: 4.4
api_available: true
mmlu_score: 91.72
humaneval_score: 88.0
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, coding, self-hosted]
extra_model_types: ['Code']
i18n_source: 'd5b4b307c39a'
---

GLM-5.2 ist das Spitzenmodell mit offenen Gewichten von Zhipu AI. Es erschien am 13. Juni 2026 unter MIT-Lizenz. Das Mixture-of-Experts-Modell umfasst rund 744 Milliarden Parameter, davon etwa 40 Milliarden aktiv pro Token. Sein Kontextfenster von einer Million Tokens übertrifft die 128.000 Tokens des Vorgängers GLM-4.6 deutlich. Zhipu entwickelte es speziell für Programmieragenten mit langem Zeithorizont und trainierte es monatelang mit Szenarien agentischer Softwareentwicklung statt allgemeinem Chat.

Bei Benchmarks erzielt das Modell 91,72 Prozent bei MMLU, 80,3 Prozent bei GPQA Diamond und 62,1 Prozent bei SWE-bench Pro. Letzterer Wert liegt über den gemeldeten 58,6 Prozent von GPT-5.5. Der API-Zugriff kostet 1,40 US-Dollar pro Million Eingabetokens und 4,40 US-Dollar pro Million Ausgabetokens – einen Bruchteil vergleichbarer proprietärer Modelle. Zhipu bewirbt die Kombination aus offenen Gewichten und Programmierleistung als direkte Herausforderung für geschlossene Spitzenmodelle von OpenAI und Anthropic.
