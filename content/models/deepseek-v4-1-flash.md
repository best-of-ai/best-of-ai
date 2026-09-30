---
title: 'DeepSeek-V4.1-Flash'
name: 'DeepSeek-V4.1-Flash'
slug: 'deepseek-v4-1-flash'
subtitle: 'DeepSeek''s cheaper, vision-capable follow-up to V4-Flash with tiered peak pricing'
description: 'DeepSeek''s cheaper, vision-capable follow-up to V4-Flash with tiered peak pricing'
company: 'deepseek'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://api-docs.deepseek.com/quick_start/pricing/'
price: 'Paid'
rank: 7
release_date: '2026-09-10'
param_count: '552B (MoE)'
context_window_tokens: 1048576
modality: [text, image]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.15
output_price_usd_per_m: 0.60
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['DeepSeek API']
date: '2026-09-18'
tags: [llm, multimodal, api, cost-efficient, moe]
---

DeepSeek shipped V4.1-Flash on September 10, 2026, a 552-billion-parameter mixture-of-experts model with native vision support and a 1,048,576 token context window that extends to 393,216 tokens of output. Pricing runs on a peak/off-peak split: off-peak rates are $0.003 per million input tokens on a cache hit, $0.15 on a cache miss, and $0.60 per million output tokens, with peak-hour rates (weekday mornings UTC) exactly double.

The tiered pricing is DeepSeek leaning into its usual playbook: undercut Western API pricing hard during low-demand windows to pull in batch and non-latency-sensitive workloads, while still charging enough at peak to manage capacity.
