---
title: 'Llama 3.1 405B'
name: 'Llama 3.1 405B'
slug: 'llama-3-1-405b'
subtitle: 'Meta''s largest dense open-weight model, competitive with closed frontier models'
description: 'Meta''s largest dense open-weight model, competitive with closed frontier models'
company: 'meta-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 7
release_date: '2024-07-23'
param_count: '405B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Llama 3.1 Community License'
api_available: true
mmlu_score: 88.6
humaneval_score: 89.0
lmarena_score: 1265
access_methods: [API, Self-hosted]
runs_at_home: false
platforms: ['Hugging Face', 'Together AI', 'AWS Bedrock']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted, foundation-model]
extra_model_types: ['Code']
---

Llama 3.1 405B is Meta's largest Llama 3.1 model, released July 23, 2024 as a dense 405-billion-parameter transformer, not a mixture-of-experts design. It supports a 128,000-token context window and scored 88.6 on MMLU and 89.0 on HumanEval, putting it in the same range as GPT-4 on both knowledge and coding benchmarks. That made it the first open-weight model to genuinely match a closed frontier model rather than trail a generation behind, and Meta released it alongside smaller 70B and 8B versions trained the same way so developers could pick a tradeoff between quality and cost. It's available for self-hosting through Hugging Face, and through hosted inference from Together AI, Fireworks, AWS Bedrock, Azure, and Google Cloud, with providers pricing it well below equivalent closed models since Meta charges nothing for the weights themselves. Llama 3.1 405B pushed Meta's argument that an open model could sit at the frontier rather than just be a cheaper, weaker alternative to one.
