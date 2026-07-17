---
title: 'DeepSeek Coder V2'
name: 'DeepSeek Coder V2'
slug: 'deepseek-coder-v2'
subtitle: 'DeepSeek''s open-weight code-specialized mixture-of-experts model'
description: 'DeepSeek''s open-weight code-specialized mixture-of-experts model'
company: 'deepseek'
model_type: 'Code'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 6
release_date: '2024-06-17'
param_count: '236B (21B active)'
context_window_tokens: 128000
modality: [text, code]
open_weight: true
license: 'MIT'
api_available: true
humaneval_score: 90.2
access_methods: [Self-hosted, API]
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, code, self-hosted]
---

DeepSeek-Coder-V2 is DeepSeek's second-generation code model, released in June 2024 as a mixture-of-experts model with 236 billion total parameters and 21 billion active per token. It extended the context window to 128,000 tokens, up sharply from the 16,000-token window of the original DeepSeek-Coder, and expanded language coverage from 86 to 338 programming languages. On HumanEval it scored 90.2%, a result DeepSeek billed at the time as closing the gap with closed models like GPT-4 Turbo on coding tasks, and it also improved on general reasoning and math benchmarks compared to its predecessor. Unlike the original DeepSeek-Coder's more restrictive license, DeepSeek-Coder-V2 is released under the MIT license, making it freely usable for commercial projects, and weights are available on Hugging Face alongside API access through DeepSeek's own platform.
