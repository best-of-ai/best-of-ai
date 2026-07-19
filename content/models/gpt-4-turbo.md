---
title: 'GPT-4 Turbo'
name: 'GPT-4 Turbo'
slug: 'gpt-4-turbo'
subtitle: 'Faster, cheaper successor to GPT-4 with a larger context window'
description: 'Faster, cheaper successor to GPT-4 with a larger context window'
company: 'openai'
model_type: 'Language'
logo_url: ''
product_url: 'https://openai.com/index/new-models-and-developer-products-announced-at-devday/'
price: 'Paid'
rank: 6
release_date: '2023-11-06'
param_count: 'Undisclosed'
context_window_tokens: 128000
modality: [text, image]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 10
output_price_usd_per_m: 30
api_available: true
mmlu_score: 86.5
humaneval_score: 87.1
lmarena_score: 1250
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['ChatGPT', 'Azure OpenAI', 'API']
date: '2026-07-16'
tags: [llm, foundation-model, api]
extra_model_types: ['Code']
---

GPT-4 Turbo is OpenAI's November 2023 update to GPT-4, announced at the company's first developer conference. It kept GPT-4's underlying capability level but expanded the context window to 128,000 tokens, added a knowledge cutoff of April 2023, and cut pricing to $10 per million input tokens and $30 per million output tokens, well below original GPT-4 rates. It scores 86.5% on MMLU and 87.1% on HumanEval, and it added vision input, letting developers send images alongside text in the same request.

The larger context window came with a practical caveat: independent testing found that attention quality degraded noticeably past roughly 32,000 tokens, so the full 128K window worked better in theory than in dense, long-document use. Even so, GPT-4 Turbo became the default GPT-4-class model for API developers through much of 2024, available directly through OpenAI, through Azure OpenAI, and in ChatGPT, until GPT-4o replaced it as the recommended option later that year.
