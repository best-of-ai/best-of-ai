---
title: 'GLM-5.2'
name: 'GLM-5.2'
slug: 'glm-5-2'
subtitle: 'Zhipu''s flagship open-weight model, shipped alongside Kimi K2.7 in mid-2026'
description: 'Zhipu''s flagship open-weight model, shipped alongside Kimi K2.7 in mid-2026'
company: 'zhipu-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.zhipuai.cn/'
price: 'Free'
rank: 7
release_date: '2026-06-13'
param_count: '~744B (MoE, ~40B active)'
context_window_tokens: 1000000
modality: [text, code]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 1.4
output_price_usd_per_m: 4.4
api_available: true
mmlu_score: 91.72
humaneval_score: 88.0
access_methods: [API, Self-hosted]
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, coding, self-hosted]
---

GLM-5.2 is Zhipu AI's flagship open-weight model, released on June 13, 2026 under the MIT license. It's a mixture-of-experts model with roughly 744 billion total parameters and about 40 billion active per token, and it ships with a context window of 1 million tokens, far beyond the 128,000-token window of its GLM-4.6 predecessor. Zhipu built it specifically for long-horizon coding agents, training it for months on agentic software engineering scenarios rather than general chat.

On benchmarks it scores 91.72% on MMLU, 80.3% on GPQA Diamond, and 62.1% on SWE-bench Pro, the last of which beats GPT-5.5's reported 58.6%. Zhipu prices API access at $1.40 per million input tokens and $4.40 per million output tokens, a fraction of what comparable proprietary models charge, and the company markets the combination of open weights and coding performance as a direct challenge to closed frontier models from OpenAI and Anthropic.
