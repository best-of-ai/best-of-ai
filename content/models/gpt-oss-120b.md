---
title: 'GPT-OSS-120B'
name: 'GPT-OSS-120B'
slug: 'gpt-oss-120b'
subtitle: 'OpenAI''s first open-weight model release since GPT-2, matching o4-mini on many reasoning benchmarks'
description: 'OpenAI''s first open-weight model release since GPT-2, matching o4-mini on many reasoning benchmarks'
company: 'openai'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://openai.com/index/introducing-gpt-oss/'
price: 'Free'
rank: 8
release_date: '2025-08-05'
param_count: '117B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
mmlu_score: 90.0
access_methods: [Self-hosted, API]
platforms: ['Hugging Face', 'Together AI', 'Azure AI Foundry']
date: '2026-07-16'
tags: [llm, reasoning, open-weight, api]
---

GPT-OSS-120B is an open-weight reasoning model OpenAI released on August 5, 2025, marking its first open model release since GPT-2 in 2019. It uses a mixture-of-experts transformer architecture with 117 billion total parameters but only about 5.1 billion active per token, which lets it run reasoning-heavy workloads on a single high-end GPU instead of the multi-GPU clusters dense models of similar size would need. It scored around 90 on MMLU at launch, putting it in the same range as OpenAI's own o4-mini on many reasoning and coding benchmarks, and it ships under the Apache 2.0 license so companies can self-host it, fine-tune it, and run it without usage restrictions. OpenAI built it specifically to compete with open releases from Meta, Mistral, and Chinese labs like DeepSeek and Alibaba's Qwen team, which had been setting the pace in open-weight models while OpenAI stayed closed. It is available through Hugging Face, Together AI, Azure AI Foundry, and OpenAI's own API for organizations that want the option of both open self-hosting and managed hosting.
