---
title: 'Llama 3.3'
name: 'Llama 3.3'
slug: 'llama-3-3'
subtitle: 'Meta''s efficient 70B open-weight model matching larger predecessors'
description: 'Meta''s efficient 70B open-weight model matching larger predecessors'
company: 'meta-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 7
release_date: '2024-12-06'
param_count: '70B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Llama 3.3 Community License'
api_available: true
mmlu_score: 86.0
humaneval_score: 88.4
lmarena_score: 1270
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Together AI', 'Ollama']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted, foundation-model]
extra_model_types: ['Code']
---

Llama 3.3 is a 70B text-only model Meta released in December 2024 as a drop-in upgrade to Llama 3.1 70B. Meta tuned it with new post-training techniques rather than adding parameters, and it ends up matching or beating the 405B model from the same family on instruction following and math despite being about six times smaller. HumanEval and MMLU scores both improved over Llama 3.1 70B, and independent benchmarks show it holding up well against contemporary models from other labs on everyday tasks. Because it costs far less to run than a 405B model, Llama 3.3 70B quickly became a common choice on inference platforms like Together AI and Groq for teams that want near-flagship quality at a lower price.
