---
title: 'Falcon Mamba 7B'
name: 'Falcon Mamba 7B'
slug: 'falcon-mamba-7b'
subtitle: 'TII''s open-weight model built on the state-space Mamba architecture'
description: 'TII''s open-weight model built on the state-space Mamba architecture'
company: 'technology-innovation-institute'
model_type: 'Language'
logo_url: ''
product_url: 'https://falconllm.tii.ae/'
price: 'Free'
rank: 3
release_date: '2024-08-12'
param_count: '7B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'TII Falcon Mamba 7B License 1.0'
api_available: false
access_methods: [Self-hosted]
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, hybrid-architecture, self-hosted]
---

Falcon Mamba 7B, released by the Technology Innovation Institute in August 2024, was the first strong open 7B language model built entirely on the Mamba state-space architecture instead of transformer attention. Because it has no attention mechanism, memory use and inference speed stay constant as generated sequences get longer, unlike transformers whose compute grows with context length. TII trained it in stages that pushed the effective context handling from 2,048 up to 8,192 tokens. In benchmark comparisons it matched or beat transformer models of similar size, including Mistral 7B and Meta's Llama 3.1 8B, and outperformed other non-transformer models such as RecurrentGemma 9B and RWKV-v6. TII distributes the weights on Hugging Face under its own Falcon Mamba license, aimed at researchers and developers who want an alternative to attention-based architectures for long-sequence workloads.
