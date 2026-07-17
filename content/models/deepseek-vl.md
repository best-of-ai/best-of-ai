---
title: 'DeepSeek-VL'
name: 'DeepSeek-VL'
slug: 'deepseek-vl'
subtitle: 'DeepSeek''s first vision-language model, preceding DeepSeek-VL2'
description: 'DeepSeek''s first vision-language model, preceding DeepSeek-VL2'
company: 'deepseek'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://github.com/deepseek-ai/DeepSeek-VL'
price: 'Free'
rank: 5
release_date: '2024-03-11'
param_count: '7B'
context_window_tokens: 4096
modality: [text, image]
open_weight: true
license: 'DeepSeek License'
api_available: true
access_methods: [Self-hosted, API]
platforms: ['Hugging Face', 'DeepSeek API']
date: '2026-07-16'
tags: [multimodal, open-weight, vision, legacy]
---

DeepSeek-VL is DeepSeek's first vision-language model, released on March 11, 2024 in 1.3B and 7B parameter versions. It pairs a hybrid vision encoder, tuned to handle high-resolution images up to 1024x1024 pixels without a heavy compute cost, with a language model trained on a mix of web screenshots, OCR data, charts, and documents rather than only captioned photos. That training mix was meant to make it useful for practical tasks like reading a chart or a slide, not just describing generic images, and DeepSeek folded vision-language training in from the start of pretraining so the model kept strong text-only performance alongside its visual grounding.

It was a modest but credible early entry in DeepSeek's push beyond pure language models, and it set up the architecture DeepSeek expanded on later that year with the larger, mixture-of-experts DeepSeek-VL2.
