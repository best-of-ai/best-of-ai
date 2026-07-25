---
title: 'Inkling'
name: 'Inkling'
slug: 'inkling'
subtitle: 'The first open-weight model from Mira Murati''s Thinking Machines Lab'
description: 'The first open-weight model from Mira Murati''s Thinking Machines Lab'
company: 'thinking-machines'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://thinkingmachines.ai/model-card/inkling/'
price: 'Free'
rank: 6
release_date: '2026-07-15'
param_count: '975B (41B active)'
context_window_tokens: 1000000
modality: [text, image, audio]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Tinker']
date: '2026-07-25'
tags: [llm, open-weight, multimodal, self-hosted]
---

Inkling is the first production model released by Thinking Machines Lab, the AI startup founded by former OpenAI CTO Mira Murati. It shipped July 15, 2026 as a natively multimodal mixture-of-experts model with 975 billion total parameters and 41 billion active per token, pretrained on 45 trillion tokens of text, images, audio, and video using Nvidia GB300 NVL72 systems. Weights are on Hugging Face with a 1 million token context window, while access through the company's Tinker fine-tuning platform is capped at 256,000 tokens, and the model is released under the Apache 2.0 license so it can be fine-tuned and redistributed freely. On the Artificial Analysis Intelligence Index it debuted at a score of 41, making it the strongest open-weight release from a US lab at the time, and it fits Thinking Machines' stated goal of building models tuned to specific users rather than one system meant to serve everyone.
