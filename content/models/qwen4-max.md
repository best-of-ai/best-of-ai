---
title: 'Qwen4-Max'
name: 'Qwen4-Max'
slug: 'qwen4-max'
subtitle: 'Alibaba''s flagship proprietary model for its Qwen API and cloud platform'
description: 'Alibaba''s flagship proprietary model for its Qwen API and cloud platform'
company: 'alibaba'
model_type: 'Language'
logo_url: ''
product_url: 'https://qwen.ai/'
price: 'Paid'
rank: 8
release_date: '2026-07-11'
param_count: 'Undisclosed'
context_window_tokens: 1000000
modality: [text, image]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 1.20
output_price_usd_per_m: 4.80
api_available: true
mmlu_score: 88.0
lmarena_score: 1352
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['Alibaba Cloud', 'Qwen Chat', 'API']
date: '2026-07-19'
tags: [llm, proprietary, api, multimodal]
---

Qwen4-Max is Alibaba's top-tier proprietary model, sitting above the open-weight Qwen3 family the company keeps releasing on Hugging Face. Unlike those, Qwen4-Max is closed and only reachable through Alibaba Cloud's API, Qwen Chat, or partner platforms, priced at $1.20 per million input tokens and $4.80 per million output tokens. It takes text and image input, carries a 1 million token context window, and Alibaba has been positioning it directly against GPT-5.6 and Gemini 3.5 Pro in its own benchmark comparisons.

The split between open Qwen3 models and closed Qwen4-Max mirrors a pattern other labs have settled into: give away capable mid-size weights to build developer mindshare while reserving the largest, most expensive-to-train model for a paid API. Alibaba has leaned on this approach to expand Qwen's footprint well beyond China, particularly with developers on Hugging Face who fine-tune the open releases but still reach for the Max tier in production when they need the extra reasoning headroom.
