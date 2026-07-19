---
title: 'Kimi-VL'
name: 'Kimi-VL'
slug: 'kimi-vl'
subtitle: 'Moonshot''s open-weight vision-language model'
description: 'Moonshot''s open-weight vision-language model'
company: 'moonshot-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.moonshot.ai/'
price: 'Free'
rank: 4
release_date: '2025-04-10'
param_count: '16B (2.8B active)'
context_window_tokens: 128000
modality: [text, image]
open_weight: true
license: 'MIT'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, multimodal, vision]
extra_model_types: ['Reasoning']
---

Kimi-VL is Moonshot AI's open-weight vision-language model, released in April 2025. It uses a mixture-of-experts design with 16 billion total parameters but only about 2.8 billion active in its language decoder, which keeps inference cheap relative to its capability. The model pairs that decoder with MoonViT, a native-resolution vision encoder that can read ultra-high-resolution images without downscaling them first, and it handles a 128,000-token context window for long documents and videos. Kimi-VL is aimed at agent-style tasks such as navigating a computer screen (it performs well on OSWorld), along with OCR, math reasoning from images, and multi-image comparison. Moonshot also released a Kimi-VL-Thinking variant trained with reinforcement learning on chain-of-thought data, which extends the base model's reasoning over longer horizons.
