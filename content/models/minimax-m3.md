---
title: 'MiniMax M3'
name: 'MiniMax M3'
slug: 'minimax-m3'
subtitle: 'First open-weight model to combine frontier coding, a 1M-token context, and native multimodality'
description: 'First open-weight model to combine frontier coding, a 1M-token context, and native multimodality'
company: 'minimax-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.minimaxi.com/'
price: 'Free'
rank: 8
release_date: '2026-06-01'
param_count: '428B (23B active)'
context_window_tokens: 1000000
modality: [text, image, code]
open_weight: true
license: 'Apache 2.0'
input_price_usd_per_m: 0.3
output_price_usd_per_m: 1.2
api_available: true
lmarena_score: 1340
access_methods: [API, Self-hosted]
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, multimodal, long-context, coding]
---

MiniMax M3 is an open-weight mixture-of-experts model that MiniMax released in June 2026, with weights on Hugging Face by June 7. It has around 428 billion total parameters with roughly 23 billion active per token, spread across 256 fine-grained experts, and MiniMax bills it as the first open-weight model to pair frontier-level coding ability with a 1 million token context window and native multimodal input across text, images, and video. The lab reports 59% on SWE-Bench Pro and 66% on Terminal-Bench 2.1, benchmarks aimed at long-running coding and agent tasks rather than one-off question answering.

Its architecture is built to keep long-context inference cheap: MiniMax says the per-token compute cost at 1 million tokens is a fraction of its prior generation, with prefill and decoding both several times faster. It is released under Apache 2.0 and priced at $0.30 per million input tokens and $1.20 per million output tokens through MiniMax's API, positioning it as a lower-cost open alternative to closed frontier coding models for developers building autonomous coding agents and tools that operate over large codebases.
