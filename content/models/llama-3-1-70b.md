---
title: 'Llama 3.1 70B'
name: 'Llama 3.1 70B'
slug: 'llama-3-1-70b'
subtitle: 'The mid-sized tier of Meta''s Llama 3.1 release, between the 8B and 405B models'
description: 'The mid-sized tier of Meta''s Llama 3.1 release, between the 8B and 405B models'
company: 'meta-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.meta.com/blog/meta-llama-3-1/'
price: 'Free'
rank: 7
release_date: '2024-07-23'
param_count: '70B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Llama 3.1 Community License'
input_price_usd_per_m: 0.35
output_price_usd_per_m: 0.4
api_available: true
mmlu_score: 83.6
humaneval_score: 80.5
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Together AI', 'AWS Bedrock']
date: '2026-07-16'
tags: [llm, open-weight, foundation-model, api]
extra_model_types: ['Code']
---

Llama 3.1 70B is the middle tier of Meta's July 2024 Llama 3.1 release, sitting between the 8 billion parameter version and the 405 billion parameter flagship. Meta trained the whole family on more than 15 trillion tokens and extended the context window to 128,000 tokens, a big jump from the 8,192 tokens of the original Llama 3. The 70B model added multilingual support and better tool use, and on benchmarks like MMLU and HumanEval it lands close to the far larger 405B model at a fraction of the compute cost. Because Meta released the weights openly under the Llama 3.1 Community License, the 70B tier became a common choice for companies that wanted strong quality they could self-host or run through third-party API providers such as Together AI and AWS Bedrock.
