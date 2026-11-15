---
title: 'GPT-OSS-20B'
name: 'GPT-OSS-20B'
slug: 'gpt-oss-20b'
subtitle: 'Kleinere Variante des offenen Modells von OpenAI, geeignet für eine einzelne GPU'
description: 'Kleinere Variante des offenen Modells von OpenAI, geeignet für eine einzelne GPU'
company: 'openai'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://openai.com/index/introducing-gpt-oss/'
price: 'Free'
rank: 7
release_date: '2025-08-05'
param_count: '21B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
mmlu_score: 85.3
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Together AI']
date: '2026-07-16'
tags: [llm, reasoning, open-weight, small-model, api]
i18n_source: '7a4a62f3cc31'
---

GPT-OSS-20B ist das kleinere der beiden Modelle mit offenen Gewichten, die OpenAI am 5. August 2025 zusammen mit GPT-OSS-120B veröffentlichte – die erste offene Modellveröffentlichung seit GPT-2. Es nutzt ein Mixture-of-Experts-Design mit rund 21 Milliarden Parametern insgesamt und etwa 3,6 Milliarden aktiven pro Token. Das ist leicht genug für eine einzelne Consumer-GPU mit mindestens 16 GB Speicher. OpenAI entwickelte es für Entwickler:innen und Hobbyanwender:innen, die ein leistungsfähiges Schlussfolgerungsmodell ohne Serverhardware einsetzen möchten. Bei der Veröffentlichung erzielte es 85,3 Punkte bei MMLU, ein starker Wert für diese Größenklasse. Programmier-, Mathematik- und allgemeine Schlussfolgerungsaufgaben bewältigt es trotz der deutlich geringeren Größe annähernd so gut wie sein größeres Geschwistermodell. Unter Apache 2.0 kann es kostenlos feinabgestimmt und weitergegeben werden. Es ist über Hugging Face, Together AI und OpenAIs API für Teams verfügbar, die eine verwaltete Lösung statt Selbsthosting bevorzugen.
