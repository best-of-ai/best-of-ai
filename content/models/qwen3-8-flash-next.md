---
title: 'Qwen3.8-Flash-Next'
name: 'Qwen3.8-Flash-Next'
slug: 'qwen3-8-flash-next'
subtitle: 'Alibaba''s open-weight preview of its next-generation Qwen4 architecture'
description: 'Alibaba''s open-weight preview of its next-generation Qwen4 architecture'
company: 'alibaba'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://qwen.ai/'
price: 'Free'
rank: 7
release_date: '2026-08-26'
param_count: '125B (6B active)'
context_window_tokens: 262144
modality: [text, image, video]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Alibaba Cloud', 'API']
date: '2026-09-05'
tags: [llm, open-weight, multimodal, moe, apache-2.0, cost-efficient]
---

Alibaba open-sourced Qwen3.8-Flash-Next on August 26, 2026, giving developers an early look at the Qwen4 architecture ahead of the full model family. It's a multimodal mixture-of-experts model with a 125 billion parameter backbone but only 6 billion active per token, alongside a 51 billion parameter n-gram embedding table and a 4 billion parameter multi-token prediction module. Context runs natively to 262,144 tokens and extends to a million. Alibaba says it outperforms the older Qwen3.7-Plus, especially on coding and office tasks, while costing roughly one-ninth as much to train and about a twelfth as much to run. Both a standard and an FP8 checkpoint were released at launch.
