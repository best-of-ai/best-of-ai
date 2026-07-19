---
title: 'Ministral 8B'
name: 'Ministral 8B'
slug: 'ministral-8b'
subtitle: 'Mistral''s compact model built for on-device and edge deployment'
description: 'Mistral''s compact model built for on-device and edge deployment'
company: 'mistral-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://mistral.ai/news/ministraux/'
price: 'Free'
rank: 4
release_date: '2024-10-16'
param_count: '8B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Mistral Research License'
input_price_usd_per_m: 0.1
output_price_usd_per_m: 0.1
api_available: true
mmlu_score: 65.0
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, small-model, on-device]
---

Ministral 8B is an 8 billion parameter model that Mistral AI released in October 2024 as part of "Les Ministraux," a pair of small models aimed at on-device and edge deployment alongside the smaller Ministral 3B. It uses interleaved sliding-window attention to support a 128,000-token context window despite its small size, and Mistral positioned it against similarly sized models like Llama 3.1 8B and Gemma 2 9B, claiming better results on knowledge, reasoning, and multilingual benchmarks within that class.

Mistral released it under the Mistral Research License, which allows free use for research and testing but requires a commercial license for production deployment, unlike the fully open Apache 2.0 terms of Mistral 7B. It targets developers building applications for phones, laptops, and other constrained hardware, such as local assistants, translation, and lightweight agents, where running a full-size model isn't practical.
