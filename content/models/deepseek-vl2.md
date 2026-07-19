---
title: 'DeepSeek-VL2'
name: 'DeepSeek-VL2'
slug: 'deepseek-vl2'
subtitle: 'DeepSeek''s open-weight vision-language mixture-of-experts model'
description: 'DeepSeek''s open-weight vision-language mixture-of-experts model'
company: 'deepseek'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 5
release_date: '2024-12-13'
param_count: '27B (4.5B active)'
context_window_tokens: 4096
modality: [text, image]
open_weight: true
license: 'DeepSeek License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, multimodal, vision]
---

DeepSeek-VL2 is a family of vision-language models that DeepSeek released on December 13, 2024, following up on the original DeepSeek-VL from earlier that year. It comes in three sizes, Tiny, Small, and the full VL2, with 3B, 16B, and 27B total parameters and 1B, 2.8B, and 4.5B active parameters respectively, using the same DeepSeekMoE and Multi-head Latent Attention architecture that powers DeepSeek's language models. A dynamic tiling method lets it process high-resolution images of varying aspect ratios without losing detail, which helps on tasks like reading dense documents, charts, and screenshots.

The mixture-of-experts design means DeepSeek-VL2 gets strong performance on visual question answering, OCR, and visual grounding benchmarks while keeping inference cheap relative to its total parameter count, since only a small fraction of experts activate for any given input. All three sizes were released with open weights, making DeepSeek-VL2 one of the more capable open multimodal model families available at the time.
