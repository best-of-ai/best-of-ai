---
title: 'InternLM2.5'
name: 'InternLM2.5'
slug: 'internlm2-5'
subtitle: 'Aktualisierte InternLM-Generation des Shanghai AI Lab mit verbessertem Tool-Einsatz und Schlussfolgern'
description: 'Aktualisierte InternLM-Generation des Shanghai AI Lab mit verbessertem Tool-Einsatz und Schlussfolgern'
company: 'shanghai-ai-lab'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://github.com/InternLM/InternLM'
price: 'Free'
rank: 5
release_date: '2024-07-03'
param_count: '7B (1.8B and 20B variants also released)'
context_window_tokens: 1000000
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
mmlu_score: 72.8
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, reasoning, open-weight, long-context]
i18n_source: '4f1fc404afae'
---
InternLM2.5 ist der Nachfolger von InternLM2 des Shanghai AI Laboratory und erschien ab dem 3. Juli 2024 in Größen mit 7B und 1,8B Parametern. Eine Version mit 20B Parametern folgte am 1. August 2024. Das 7B-Chatmodell erreicht laut den OpenCompass-Auswertungen des Entwicklers 72,8 Punkte bei MMLU und übertrifft Llama 3 8B Instruct sowie Gemma 2 9B in mehreren Reasoning- und Mathematik-Benchmarks. Ein eigener 7B-Chat-1M-Checkpoint erweitert das Kontextfenster auf eine Million Tokens und kann in Needle-in-a-Haystack-Tests gezielte Fakten in Dokumenten dieser Länge finden. Das Standardmodell mit 20B Parametern erreicht bis zu 200K Tokens. Gegenüber InternLM2 bietet die Reihe auch verbessertes Function Calling und agentische Tool-Nutzung. Alle Gewichte stehen unter Apache 2.0 auf Hugging Face und im InternLM-GitHub-Repository.
