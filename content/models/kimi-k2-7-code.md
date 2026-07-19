---
title: 'Kimi K2.7 Code'
name: 'Kimi K2.7 Code'
slug: 'kimi-k2-7-code'
subtitle: 'Moonshot''s open-weight agentic coding model, tuned for tool-use and long-running tasks'
description: 'Moonshot''s open-weight agentic coding model, tuned for tool-use and long-running tasks'
company: 'moonshot-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://www.moonshot.ai/'
price: 'Free'
rank: 8
release_date: '2026-06-12'
param_count: '1T (32B active)'
context_window_tokens: 256000
modality: [text, code]
open_weight: true
license: 'Modified MIT'
input_price_usd_per_m: 0.95
output_price_usd_per_m: 4.0
api_available: true
humaneval_score: 90.0
lmarena_score: 1360
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, code, agentic, mixture-of-experts]
extra_model_types: ['Reasoning']
---

Kimi K2.7 Code is Moonshot AI's coding-focused model, released in June 2026 as a specialized build on top of Kimi K2.6. It keeps the same 1-trillion-parameter mixture-of-experts architecture with about 32 billion active parameters and a 256,000-token context window, but tunes the model specifically for long-horizon coding and agentic task decomposition. Moonshot reports gains of roughly 22% on its Kimi Code Bench v2, 11% on Program Bench, and 31.5% on MLS Bench Lite over K2.6, along with about 30% fewer reasoning tokens spent per task, which lowers the effective cost of running it in an agent loop. The model always runs in thinking mode and does not support a non-thinking fallback, and it accepts text, image, and video input alongside code. Weights are open on Hugging Face, and Moonshot's own API prices it well below closed competitors like Claude Opus and GPT-5.5 on both input and output tokens.
