---
title: 'Llama 4 Maverick'
name: 'Llama 4 Maverick'
slug: 'llama-4-maverick'
subtitle: 'Meta''s flagship open-weight multimodal mixture-of-experts model'
description: 'Meta''s flagship open-weight multimodal mixture-of-experts model'
company: 'meta-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 8
release_date: '2025-04-05'
param_count: '400B (17B active)'
context_window_tokens: 1000000
modality: [text, image]
open_weight: true
license: 'Llama 4 Community License'
api_available: true
mmlu_score: 86.0
humaneval_score: 85.0
lmarena_score: 1330
access_methods: [API, Self-hosted]
platforms: ['Hugging Face', 'Together AI', 'AWS Bedrock']
date: '2026-07-16'
tags: [llm, open-weight, multimodal, self-hosted, mixture-of-experts]
---

Llama 4 Maverick is Meta's flagship model from the April 2025 Llama 4 release, built as a mixture-of-experts model with 400 billion total parameters but only 17 billion active per token, spread across 128 experts. It is natively multimodal, trained to handle text and images together rather than adding a vision encoder onto a text model afterward, and it supports a 1 million token context window. Meta reported that Maverick beats GPT-4o and Gemini 2.0 Flash on a range of public benchmarks, and that it matches DeepSeek V3 on reasoning and coding tasks while using less than half the active parameters. It is distributed under the Llama 4 Community License with weights available on Hugging Face and through cloud providers like AWS Bedrock and Together AI.
