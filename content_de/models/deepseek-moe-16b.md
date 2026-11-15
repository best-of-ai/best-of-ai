---
title: 'DeepSeek-MoE-16B'
name: 'DeepSeek-MoE-16B'
slug: 'deepseek-moe-16b'
subtitle: 'DeepSeeks frühes fein abgestimmtes Mixture-of-Experts-Modell, das spätere MoE-Architekturen prägte'
description: 'DeepSeeks frühes fein abgestimmtes Mixture-of-Experts-Modell, das spätere MoE-Architekturen prägte'
company: 'deepseek'
model_type: 'Language'
logo_url: ''
product_url: 'https://github.com/deepseek-ai/DeepSeek-MoE'
price: 'Free'
rank: 5
release_date: '2024-01-11'
param_count: '16.4B'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'DeepSeek License'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, mixture-of-experts, legacy]
i18n_source: '61ec60299e14'
---
DeepSeek-MoE-16B erschien im Januar 2024 als früher Versuch von DeepSeek mit einer fein abgestimmten Mixture-of-Experts-Architektur. Seine Designentscheidungen flossen in die späteren Modelle V2 und V3 ein. Das Modell umfasst insgesamt 16,4 Milliarden Parameter, aktiviert pro Token jedoch nur etwa 2,8 Milliarden. Der Forschungsbeitrag beschreibt dafür zwei Techniken: Experten werden in kleinere, stärker spezialisierte Einheiten aufgeteilt und eine Gruppe gemeinsam genutzter Experten wird stets aktiviert, um allgemeines Wissen abzudecken. Das Modell wurde von Grund auf mit zwei Billionen englischen und chinesischen Tokens trainiert. Es erreichte eine mit den dichten Modellen DeepSeek 7B und Llama 2 7B vergleichbare Leistung und benötigte bei der Inferenz nur etwa 40 Prozent des Rechenaufwands. Das Kontextfenster umfasst 4096 Tokens. Die Veröffentlichung unter DeepSeeks offener Lizenz diente vor allem dazu, die Spezialisierung von Experten zu demonstrieren, und weniger als produktionsorientiertes Angebot.
