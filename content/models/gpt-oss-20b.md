---
title: 'GPT-OSS-20B'
name: 'GPT-OSS-20B'
slug: 'gpt-oss-20b'
subtitle: 'The smaller, single-GPU-friendly tier of OpenAI''s open-weight model release'
description: 'The smaller, single-GPU-friendly tier of OpenAI''s open-weight model release'
company: 'openai'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://openai.com/index/introducing-gpt-oss/'
price: 'Free'
rank: 7
release_date: '2025-08-05'
param_count: '21B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
mmlu_score: 85.3
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Together AI']
date: '2026-07-16'
tags: [llm, reasoning, open-weight, small-model, api]
---

GPT-OSS-20B is the smaller of the two open-weight models OpenAI released on August 5, 2025, alongside the larger GPT-OSS-120B, in its first open model release since GPT-2. It uses a mixture-of-experts design with about 21 billion total parameters and roughly 3.6 billion active per token, light enough to run on a single consumer GPU with 16GB or more of memory, which was the point: OpenAI built it for developers and hobbyists who wanted a capable reasoning model without server-grade hardware. It scored 85.3 on MMLU at launch, a strong result for its size class, and handles coding, math, and general reasoning tasks reasonably close to its bigger sibling despite the much smaller footprint. Released under the Apache 2.0 license, it can be fine-tuned and redistributed freely, and it is available through Hugging Face, Together AI, and OpenAI's API for teams that want a managed option instead of self-hosting.
