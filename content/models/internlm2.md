---
title: 'InternLM2'
name: 'InternLM2'
slug: 'internlm2'
subtitle: 'Shanghai AI Lab''s open-weight foundation model with strong long-context and reasoning ability'
description: 'Shanghai AI Lab''s open-weight foundation model with strong long-context and reasoning ability'
company: 'shanghai-ai-lab'
model_type: 'Language'
logo_url: ''
product_url: 'https://github.com/InternLM/InternLM'
price: 'Free'
rank: 5
release_date: '2024-01-17'
param_count: '20B'
context_window_tokens: 200000
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
mmlu_score: 67.7
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, long-context]
---

InternLM2 is an open-weight language model from the Shanghai AI Laboratory, released January 17, 2024 in 7B and 20B sizes alongside matching chat variants. Both sizes support a 200,000-token context window, reached through a training process that starts on 4K-token sequences and extends gradually to 32K and beyond, and the model holds up well on long-document needle-in-a-haystack tests at that length. The 20B chat variant scores 67.7 on MMLU, putting it ahead of several open models of similar size at the time of release. InternLM2 was trained on a large multilingual corpus with particular strength in English and Chinese, and it was positioned as a general-purpose foundation model for reasoning, coding, and long-context tasks before Shanghai AI Lab replaced it with InternLM2.5 later that year. It's released under the Apache 2.0 license and distributed through Hugging Face and the InternLM GitHub repository.
