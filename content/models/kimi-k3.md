---
title: 'Kimi K3'
name: 'Kimi K3'
slug: 'kimi-k3'
subtitle: 'Moonshot''s 2.8 trillion parameter open-weight model, the largest open model shipped to date'
description: 'Moonshot''s 2.8 trillion parameter open-weight model, the largest open model shipped to date'
company: 'moonshot-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.moonshot.ai/'
price: 'Free'
rank: 8
release_date: '2026-07-16'
param_count: '2.8T (MoE)'
context_window_tokens: 1000000
modality: [text, image, video]
open_weight: true
license: 'Modified MIT'
input_price_usd_per_m: 3
output_price_usd_per_m: 15
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-08-09'
tags: [llm, open-weight, multimodal, reasoning, mixture-of-experts]
extra_model_types: ['Reasoning']
---

Kimi K3 is Moonshot AI's largest release yet, a 2.8 trillion parameter mixture-of-experts model that the company says is the biggest open-weight model shipped by anyone so far. It reads text, images, and video natively, carries a 1 million token context window, and runs in an always-on thinking mode rather than offering a separate fast path. Moonshot priced API access at $3 per million input tokens (dropping to $0.30 on a cache hit) and $15 per million output tokens, undercutting closed frontier models from Western labs by a wide margin. Full weights landed on Hugging Face shortly after the July 16 announcement, using MXFP4 quantization to bring the download to roughly 1.4 TB, small enough for serious self-hosting setups to run without a dedicated cluster.
