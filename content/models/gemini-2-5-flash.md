---
title: 'Gemini 2.5 Flash'
name: 'Gemini 2.5 Flash'
slug: 'gemini-2-5-flash'
subtitle: 'Google''s low-latency, cost-efficient Gemini tier'
description: 'Google''s low-latency, cost-efficient Gemini tier'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://deepmind.google/technologies/gemini/'
price: 'Paid'
rank: 7
release_date: '2025-04-17'
param_count: 'Undisclosed'
context_window_tokens: 1000000
modality: [text, image, audio]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.3
output_price_usd_per_m: 2.5
api_available: true
mmlu_score: 84.0
humaneval_score: 82.0
lmarena_score: 1290
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['Gemini app', 'Google Vertex AI', 'API']
date: '2026-07-16'
tags: [llm, low-latency, multimodal, api]
---

Gemini 2.5 Flash is Google's cost-efficient tier of the 2.5 generation, released as a preview in April 2025 and moved to general availability the following month. It's the first Flash model built with visible thinking built in from the start: it can reason step by step through a problem before answering, and developers can set a "thinking budget" to trade off answer quality against latency and cost. It takes text, image, and audio input and handles the same million-token context window as its Pro sibling.

Google prices it at $0.30 per million input tokens and $2.50 per million output tokens, with thinking tokens billed at the output rate, and offers a further stripped-down Flash-Lite variant for even cheaper, simpler workloads. It scores around 83% on MMLU-Pro and performs well on coding and math benchmarks relative to its price, making it Google's default recommendation for high-volume applications that don't need Pro-level reasoning depth.
