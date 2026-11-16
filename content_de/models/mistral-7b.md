---
title: 'Mistral 7B'
name: 'Mistral 7B'
slug: 'mistral-7b'
subtitle: 'Ursprüngliches kompaktes Open-Weight-Modell von Mistral, das größere Konkurrenzmodelle übertraf'
description: 'Ursprüngliches kompaktes Open-Weight-Modell von Mistral, das größere Konkurrenzmodelle übertraf'
company: 'mistral-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://mistral.ai/news/announcing-mistral-7b/'
price: 'Free'
rank: 6
release_date: '2023-09-27'
param_count: '7B'
context_window_tokens: 32000
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
mmlu_score: 60.1
humaneval_score: 30.5
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Ollama']
date: '2026-07-16'
tags: [llm, open-weight, small-model, self-hosted]
extra_model_types: ['Code']
i18n_source: 'c7cb93d8e531'
---

Mistral 7B machte Mistral AI bekannt und war das erste öffentliche Modell des französischen Start-ups. Es erschien am 27. September 2023. Mit sieben Milliarden Parametern lief es auf einer einzelnen Consumer-GPU, übertraf aber Llama 2 13B bei allen von Mistral getesteten Benchmarks und schlug Llama 2 34B bei mehreren Aufgaben zum Schlussfolgern und Programmieren. Es erreichte 60,1 Prozent bei MMLU und 30,5 Prozent bei HumanEval. Grouped-Query-Attention und Sliding-Window-Attention sorgen beim Kontextfenster von 32.000 Tokens für schnelle, speichereffiziente Inferenz.

Mistral veröffentlichte das Modell unter Apache 2.0 ohne Nutzungsbeschränkungen. Für ein Modell dieser Qualität war das damals ungewöhnlich und trug dazu bei, dass es sich über Hugging Face und Werkzeuge wie Ollama und llama.cpp schnell in der Open-Source-Community verbreitete. Es wurde zu einer verbreiteten Grundlage für Fine-Tunes und Modellmischungen. Sein Erfolg machte Mistral AI innerhalb weniger Monate zu einem ernsthaften Wettbewerber von Meta und OpenAI.
