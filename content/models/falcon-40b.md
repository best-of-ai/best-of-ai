---
title: 'Falcon 40B'
name: 'Falcon 40B'
slug: 'falcon-40b'
subtitle: 'TII''s earlier open-weight model that led leaderboards before Falcon 180B'
description: 'TII''s earlier open-weight model that led leaderboards before Falcon 180B'
company: 'technology-innovation-institute'
model_type: 'Language'
logo_url: ''
product_url: 'https://falconllm.tii.ae/'
price: 'Free'
rank: 4
release_date: '2023-05-25'
param_count: '40B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
mmlu_score: 82.7
humaneval_score: 76.3
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted, legacy]
extra_model_types: ['Code']
---

Falcon 40B is a 40 billion parameter causal decoder-only language model released by the Technology Innovation Institute in May 2023. It was trained on roughly 1 trillion tokens of RefinedWeb, a large web dataset TII curated and filtered itself, combined with select additional corpora. At launch it topped the Hugging Face Open LLM Leaderboard among open-source models, scoring 82.7 on MMLU and 76.3 on HumanEval, ahead of contemporaries like MPT and RedPajama and competitive with Meta's larger Llama 2 70B on several benchmarks. The architecture uses multiquery attention and FlashAttention to keep inference costs down relative to its size. TII released it under an Apache 2.0 license with no royalties, an unusually permissive choice for a model of its scale at the time, which helped drive early enterprise adoption including availability on AWS SageMaker JumpStart. Falcon 40B has since been superseded by Falcon 180B and the Falcon 3 family, and its 2,048 token context window looks small next to current models.
