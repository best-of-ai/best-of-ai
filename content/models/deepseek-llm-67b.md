---
title: 'DeepSeek LLM 67B'
name: 'DeepSeek LLM 67B'
slug: 'deepseek-llm-67b'
subtitle: 'DeepSeek''s first dense open-weight foundation model'
description: 'DeepSeek''s first dense open-weight foundation model'
company: 'deepseek'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 4
release_date: '2023-11-29'
param_count: '67B'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'DeepSeek License'
api_available: false
mmlu_score: 71.9
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted, legacy]
---

DeepSeek LLM 67B is DeepSeek's first dense foundation model, released in November 2023 before the company pivoted toward the mixture-of-experts architectures used in its later V2 and V3 lines. It is a 67-billion-parameter dense transformer trained on 2 trillion tokens of English and Chinese text, and it scored around 71.9 on MMLU, putting it roughly in line with Llama 2 70B on general knowledge benchmarks while beating it on several Chinese-language tasks. The model has a comparatively short 4,096-token context window by later standards, reflecting the norms of late 2023 training runs. It was released with both base and chat variants under a permissive DeepSeek license allowing commercial use, and it served as the foundation DeepSeek built on for its subsequent, more widely used models.
