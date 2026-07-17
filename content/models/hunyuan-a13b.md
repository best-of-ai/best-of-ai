---
title: 'Hunyuan-A13B'
name: 'Hunyuan-A13B'
slug: 'hunyuan-a13b'
subtitle: 'Tencent''s open-weight mixture-of-experts reasoning model'
description: 'Tencent''s open-weight mixture-of-experts reasoning model'
company: 'tencent'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://llm.hunyuan.tencent.com/'
price: 'Free'
rank: 4
release_date: '2025-06-27'
param_count: '80B (13B active)'
context_window_tokens: 256000
modality: [text]
open_weight: true
license: 'Tencent Hunyuan License'
api_available: true
access_methods: [Self-hosted, API]
platforms: ['Hugging Face', 'Tencent Cloud']
date: '2026-07-16'
tags: [llm, open-weight, reasoning, mixture-of-experts]
---

Hunyuan-A13B is Tencent's open-weight mixture-of-experts language model, released in June 2025 with 80 billion total parameters but only 13 billion active per token, which keeps inference cost close to a much smaller dense model. It natively supports a 256K context window, though many self-hosted setups cap it lower to fit GPU memory. The model offers a dual-mode design that lets users toggle between a fast response mode and a slower step-by-step reasoning mode for harder math, science, and coding problems. Tencent released the weights on Hugging Face under its own Hunyuan license, and the model is also available through Tencent Cloud's API for teams that don't want to run it themselves. It positions itself against other efficient open MoE reasoning models like DeepSeek's smaller releases and Alibaba's Qwen, competing more on active-parameter efficiency than raw parameter count.
