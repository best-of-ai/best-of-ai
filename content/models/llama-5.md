---
title: 'Llama 5'
name: 'Llama 5'
slug: 'llama-5'
subtitle: 'Meta''s next flagship open-weight multimodal model, built for on-device and datacenter use alike'
description: 'Meta''s next flagship open-weight multimodal model, built for on-device and datacenter use alike'
company: 'meta-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 9
release_date: '2026-07-14'
param_count: '520B (24B active)'
context_window_tokens: 2000000
modality: [text, image, audio]
open_weight: true
license: 'Llama 4 Community License'
api_available: true
mmlu_score: 89.5
humaneval_score: 90.0
lmarena_score: 1381
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Together AI', 'AWS Bedrock', 'Azure AI Foundry']
date: '2026-07-19'
tags: [llm, open-weight, multimodal, self-hosted, mixture-of-experts]
---

Llama 5 is Meta's follow-up to last year's Llama 4 line, again shipped as a mixture-of-experts model but scaled up to 520 billion total parameters with 24 billion active per token. The bigger jump is the 2 million token context window, double what Llama 4 Maverick offered, which Meta is pitching for tasks like ingesting entire codebases or long video transcripts in one pass. It handles text, image, and audio input natively rather than bolting encoders onto a text-only base, and Meta says it edges out Gemini 3.5 Pro and GPT-5.6 on several open benchmarks while still running efficiently thanks to the sparse expert routing.

As with prior Llama releases, the weights are open under the Llama 4 Community License and available immediately on Hugging Face, with hosting partners like Together AI, AWS Bedrock, and Azure AI Foundry offering managed inference for teams that don't want to run it themselves. Meta continues to withhold full commercial rights from companies above a certain user threshold, the same carve-out that's applied since Llama 2.
