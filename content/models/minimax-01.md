---
title: 'MiniMax-01'
name: 'MiniMax-01'
slug: 'minimax-01'
subtitle: 'MiniMax''s 2025 open-weight model with a 4M-token context window'
description: 'MiniMax''s 2025 open-weight model with a 4M-token context window'
company: 'minimax-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.minimaxi.com/'
price: 'Free'
rank: 6
release_date: '2025-01-15'
param_count: '456B (45.9B active)'
context_window_tokens: 4000000
modality: [text]
open_weight: true
license: 'Apache 2.0'
input_price_usd_per_m: 0.2
output_price_usd_per_m: 1.1
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, long-context, mixture-of-experts]
extra_model_types: ['Multimodal']
---

MiniMax-01 is an open-weight model family that the Chinese AI lab MiniMax released in January 2025, combining a text model (MiniMax-Text-01) and a vision-language model (MiniMax-VL-01) built on the same hybrid architecture. It uses a mixture-of-experts design with 456 billion total parameters and about 45.9 billion active per token, and mixes Lightning Attention with regular softmax attention to make very long sequences computationally practical. The headline feature is context length: the model can handle inputs up to 4 million tokens, well beyond what most competing models support at the time, while API-hosted versions typically expose a 1 million token window.

MiniMax released the weights under an Apache 2.0 license on Hugging Face and also offers the model through its own API, priced at $0.20 per million input tokens and $1.10 per million output tokens, undercutting most Western frontier-model pricing. It targets use cases like long-document analysis, extended agent workflows, and codebase-level reasoning where context length is the limiting factor rather than raw parameter count.
