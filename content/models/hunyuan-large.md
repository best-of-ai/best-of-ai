---
title: 'Hunyuan Large'
name: 'Hunyuan Large'
slug: 'hunyuan-large'
subtitle: 'Tencent''s open-weight mixture-of-experts model'
description: 'Tencent''s open-weight mixture-of-experts model'
company: 'tencent'
model_type: 'Language'
logo_url: ''
product_url: 'https://llm.hunyuan.tencent.com/'
price: 'Free'
rank: 5
release_date: '2024-11-05'
param_count: '389B (52B active)'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Tencent Hunyuan License'
api_available: true
access_methods: [Self-hosted, API]
platforms: ['Hugging Face', 'Tencent Cloud']
date: '2026-07-16'
tags: [llm, open-weight, mixture-of-experts]
---

Hunyuan-Large is Tencent's open-weight mixture-of-experts language model, released in November 2024 with 389 billion total parameters and 52 billion activated per token, which Tencent described at launch as the largest open Transformer-based MoE model available at the time. It supports a 256K context window and was trained with a mix of synthetic and real data aimed at improving reasoning, coding, and long-context recall over Tencent's earlier dense Hunyuan models. The company published a technical report alongside the weights detailing its expert-routing and data-scaling choices, and released the model on Hugging Face under the Hunyuan license for self-hosting alongside API access through Tencent Cloud. It competes directly with other large open MoE releases from that period, including DeepSeek-V2 and Mistral's Mixtral family, on the strength of its very large expert pool relative to its active-parameter cost.
