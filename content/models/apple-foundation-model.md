---
title: 'Apple Foundation Model'
name: 'Apple Foundation Model'
slug: 'apple-foundation-model'
subtitle: 'Apple''s on-device and server foundation models powering Apple Intelligence'
description: 'Apple''s on-device and server foundation models powering Apple Intelligence'
company: 'apple'
model_type: 'Language'
logo_url: ''
product_url: 'https://machinelearning.apple.com/research/introducing-apple-foundation-models'
price: 'Paid'
rank: 6
release_date: '2024-06-10'
param_count: '3B (on-device)'
context_window_tokens: 32000
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Self-hosted]
runs_at_home: false
platforms: ['iOS', 'macOS']
date: '2026-07-16'
tags: [llm, on-device, foundation-model]
---

Apple's Foundation Models are the pair of language models behind Apple Intelligence, introduced in June 2024 at WWDC: a roughly 3-billion-parameter model that runs directly on iPhone, iPad, and Mac hardware, and a larger model that runs on Apple's own Private Cloud Compute servers for tasks the on-device model can't handle alone. The on-device model relies on techniques like KV-cache sharing and 2-bit quantization-aware training to fit within a phone's memory and power budget, while the server model uses a mixture-of-experts transformer design. The on-device model's usable context window is limited to 4,096 tokens, while the server model handles up to 32,000 tokens.

Apple doesn't sell API access to these models the way OpenAI or Anthropic do; instead, they power built-in system features like writing tools, notification summaries, and Siri's revamped capabilities, and since WWDC 2025 they're exposed to third-party developers through the Foundation Models framework so apps can call the on-device model directly, for free and without a network connection. Apple has since updated the lineup at WWDC 2025 and introduced a third generation at WWDC 2026, generally focused on quality and efficiency gains rather than dramatic size increases, reflecting Apple's preference for privacy and on-device inference over sending user data to cloud-hosted frontier models.
