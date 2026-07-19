---
title: 'DeepSeek-MoE-16B'
name: 'DeepSeek-MoE-16B'
slug: 'deepseek-moe-16b'
subtitle: 'DeepSeek''s early fine-grained mixture-of-experts model that informed its later MoE architectures'
description: 'DeepSeek''s early fine-grained mixture-of-experts model that informed its later MoE architectures'
company: 'deepseek'
model_type: 'Language'
logo_url: ''
product_url: 'https://github.com/deepseek-ai/DeepSeek-MoE'
price: 'Free'
rank: 5
release_date: '2024-01-11'
param_count: '16.4B'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'DeepSeek License'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, mixture-of-experts, legacy]
---

DeepSeek-MoE-16B, released in January 2024, was DeepSeek's early attempt at a fine-grained mixture-of-experts architecture, and its design choices carried forward into the company's later V2 and V3 models. It has 16.4 billion total parameters but only about 2.8 billion active per token, achieved through two techniques described in its paper: splitting experts into smaller, more specialized units, and isolating a set of shared experts that always fire to capture common knowledge. Trained from scratch on 2 trillion English and Chinese tokens, it reached performance comparable to the dense DeepSeek 7B and Llama 2 7B models while using only around 40% of the compute those models require at inference. It has a 4,096-token context window and was released under DeepSeek's open license for self-hosted use, mainly as a research demonstration of expert specialization rather than a production-focused release.
