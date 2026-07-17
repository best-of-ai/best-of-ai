---
title: 'Grok-1'
name: 'Grok-1'
slug: 'grok-1'
subtitle: 'xAI''s first model, later open-weighted under Apache 2.0'
description: 'xAI''s first model, later open-weighted under Apache 2.0'
company: 'xai'
model_type: 'Language'
logo_url: ''
product_url: 'https://x.ai/blog/grok-os'
price: 'Free'
rank: 5
release_date: '2023-11-04'
param_count: '314B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
platforms: ['Hugging Face', 'GitHub']
date: '2026-07-16'
tags: [llm, open-weight, legacy]
---

Grok-1 is xAI's first large language model, built by Elon Musk's AI lab and originally offered to X Premium+ subscribers starting in November 2023. It is a 314 billion parameter mixture-of-experts model with 8 experts and top-2 routing, meaning only about a quarter of its weights activate for any given token, and it uses an 8,192-token context window. xAI open-sourced the base model weights and architecture on March 17, 2024 under the Apache 2.0 license, making Grok-1 the largest open-weight MoE model publicly available at the time. The release included only the raw pretrained weights, not an instruction-tuned or chat-ready version, so the model was mainly picked up by researchers and infrastructure teams rather than end users. xAI trained Grok-1 on a custom JAX and Rust stack instead of PyTorch, and pretraining had concluded by October 2023, before Grok-2 superseded it later in 2024.
