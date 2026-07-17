---
title: 'DeepSeek R1'
name: 'DeepSeek R1'
slug: 'deepseek-r1'
subtitle: 'DeepSeek''s reasoning model that matched closed frontier models on math and code'
description: 'DeepSeek''s reasoning model that matched closed frontier models on math and code'
company: 'deepseek'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 8
release_date: '2025-01-20'
param_count: '671B (37B active)'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 0.55
output_price_usd_per_m: 2.19
api_available: true
mmlu_score: 90.8
humaneval_score: 92.0
lmarena_score: 1360
access_methods: [API, Self-hosted]
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, reasoning, chain-of-thought]
---

DeepSeek R1 is a reasoning model released by the Chinese lab DeepSeek on January 20, 2025. It uses a 671-billion-parameter mixture-of-experts architecture with 37 billion parameters active per token, and it was trained in part with large-scale reinforcement learning rather than relying only on supervised fine-tuning, which pushed it to work through problems step by step before answering. On launch, it matched OpenAI's o1 on math, coding, and science benchmarks (scoring 90.8 on MMLU and performing near the top of contemporary models on AIME and Codeforces-style problems) while being released with open weights under the MIT license and API pricing far below o1's.

The release caused a stir well beyond the usual AI research circles: DeepSeek's app briefly topped the U.S. App Store charts, and the news that a comparatively small Chinese lab had trained a frontier-class reasoning model at a fraction of the usual cost rattled AI stocks. R1 is available through DeepSeek's own API and chat interface, and its open weights mean it's also self-hostable and widely mirrored on Hugging Face and served by third-party inference providers.
