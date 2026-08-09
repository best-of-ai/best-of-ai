---
title: 'DeepSeek-V4-Flash-0731'
name: 'DeepSeek-V4-Flash-0731'
slug: 'deepseek-v4-flash-0731'
subtitle: 'DeepSeek''s MIT-licensed 284B MoE model, retrained for stronger agentic coding'
description: 'DeepSeek''s MIT-licensed 284B MoE model, retrained for stronger agentic coding'
company: 'deepseek'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 6
release_date: '2026-07-31'
param_count: '284B (13B active)'
context_window_tokens: 1000000
modality: [text, code]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 0.14
output_price_usd_per_m: 0.28
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'DeepSeek API']
date: '2026-08-09'
tags: [llm, open-weight, code, agentic, mixture-of-experts]
extra_model_types: ['Code']
---

DeepSeek-V4-Flash-0731 moves DeepSeek-V4-Flash out of preview and into public beta as a re-post-trained checkpoint, announced July 31, 2026 in the company's API changelog. The architecture is unchanged from the model's April debut, a 284 billion parameter mixture-of-experts design with 13 billion active parameters per token, a shared expert plus 256 routed experts, and a 1 million token context window. What changed is the post-training pipeline: DeepSeek retuned it specifically for coding, agentic tool use, and reasoning, and the API now natively supports the Responses format and works with Codex out of the box. It remains MIT-licensed and ungated, so teams can self-host it commercially without restriction, with roughly 110 GB of memory needed at 3-bit quantization or a 4x GB300 node for full precision. API pricing stayed low at $0.14 per million input tokens and $0.28 per million output tokens.
