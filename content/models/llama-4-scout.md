---
title: 'Llama 4 Scout'
name: 'Llama 4 Scout'
slug: 'llama-4-scout'
subtitle: 'Meta''s smaller, faster Llama 4 tier with a 10M-token context window'
description: 'Meta''s smaller, faster Llama 4 tier with a 10M-token context window'
company: 'meta-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 7
release_date: '2025-04-05'
param_count: '109B (17B active)'
context_window_tokens: 10000000
modality: [text, image]
open_weight: true
license: 'Llama 4 Community License'
api_available: true
mmlu_score: 80.5
lmarena_score: 1290
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Together AI']
date: '2026-07-16'
tags: [llm, open-weight, multimodal, long-context, self-hosted]
---

Llama 4 Scout is the smaller sibling in Meta's April 2025 Llama 4 release, a mixture-of-experts model with 109 billion total parameters and 17 billion active per token spread across 16 experts. Its standout feature is context length: Scout supports up to 10 million tokens, far beyond what other openly available models offered at launch, which suits tasks like summarizing an entire codebase or a long document collection in a single pass. Like Maverick, it is natively multimodal and trained to process text and images together. Meta positioned Scout as a faster, cheaper option that still beats models like Gemma 3 and Gemini 2.0 Flash-Lite on public benchmarks, and it runs on a single H100 GPU when quantized, which made it popular for self-hosted deployments.
