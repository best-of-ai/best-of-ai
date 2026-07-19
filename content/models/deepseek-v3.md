---
title: 'DeepSeek V3'
name: 'DeepSeek V3'
slug: 'deepseek-v3'
subtitle: 'DeepSeek''s efficient mixture-of-experts model trained at a fraction of rival costs'
description: 'DeepSeek''s efficient mixture-of-experts model trained at a fraction of rival costs'
company: 'deepseek'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 8
release_date: '2024-12-26'
param_count: '671B (37B active)'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 0.27
output_price_usd_per_m: 1.1
api_available: true
mmlu_score: 88.5
humaneval_score: 82.6
lmarena_score: 1330
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, mixture-of-experts, self-hosted]
extra_model_types: ['Code']
---

DeepSeek V3 is a 671-billion-parameter mixture-of-experts model, with 37 billion parameters active per token, that DeepSeek released on December 26, 2024. It's a non-reasoning base model built on the same Multi-head Latent Attention and DeepSeekMoE architecture as V2, and DeepSeek reported training it for about $5.6 million in GPU time, a figure far lower than what Western labs were spending on comparable models. It scored 88.5 on MMLU and 82.6 on HumanEval, putting it roughly on par with GPT-4o and Claude 3.5 Sonnet on many benchmarks despite the low training cost.

V3 is released under the MIT license with open weights, and DeepSeek priced its API well below competing frontier models. It later served as the base model that R1's reasoning-focused reinforcement learning was built on top of, and its cost efficiency became a talking point across the industry about how much compute is actually required to reach frontier-level performance.
