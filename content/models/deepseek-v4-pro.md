---
title: 'DeepSeek V4-Pro'
name: 'DeepSeek V4-Pro'
slug: 'deepseek-v4-pro'
subtitle: 'The top open-weight model of 2026, leading on agentic coding and graduate reasoning'
description: 'The top open-weight model of 2026, leading on agentic coding and graduate reasoning'
company: 'deepseek'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 9
release_date: '2026-04-24'
param_count: '1.6T (49B active)'
context_window_tokens: 1000000
modality: [text, code]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 0.43
output_price_usd_per_m: 0.87
api_available: true
mmlu_score: 90.0
humaneval_score: 91.0
lmarena_score: 1390
access_methods: [API, Self-hosted]
platforms: ['Hugging Face', 'API', 'Together AI']
date: '2026-07-16'
tags: [llm, open-weight, reasoning, coding, mixture-of-experts]
---

DeepSeek V4-Pro is DeepSeek's flagship model, released on April 24, 2026 alongside a smaller sibling, V4-Flash. It's a mixture-of-experts model with 1.6 trillion total parameters and 49 billion active per token, and it introduces a hybrid attention design combining Compressed Sparse Attention and Heavily Compressed Attention that cuts inference compute and KV-cache size sharply compared to V3.2, letting it handle a 1-million-token context window. The model runs in both a "thinking" mode for step-by-step reasoning and a non-thinking mode for fast responses, and DeepSeek reports it leading open-weight models on math, science, and agentic coding benchmarks, with a SWE-bench Verified score above 80%.

Like the rest of the DeepSeek lineup, V4-Pro ships with open weights under the MIT license and API pricing well below comparable closed models from OpenAI, Anthropic, and Google. It's positioned as DeepSeek's answer to the frontier reasoning models released by Western labs in early 2026, and its release was covered widely as evidence that the gap between open and closed frontier models keeps narrowing.
