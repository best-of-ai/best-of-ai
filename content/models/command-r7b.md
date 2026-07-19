---
title: 'Command R7B'
name: 'Command R7B'
slug: 'command-r7b'
subtitle: 'Cohere''s smallest current-generation Command model'
description: 'Cohere''s smallest current-generation Command model'
company: 'cohere'
model_type: 'Language'
logo_url: ''
product_url: 'https://cohere.com/command'
price: 'Free'
rank: 3
release_date: '2024-12-13'
param_count: '7B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'CC-BY-NC 4.0'
input_price_usd_per_m: 0.0375
output_price_usd_per_m: 0.15
api_available: true
mmlu_score: 70.4
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Cohere Platform', 'Hugging Face']
date: '2026-07-16'
tags: [llm, small-model, open-weight, low-latency]
---

Command R7B is the smallest model in Cohere's R series, released in December 2024 as what the company called the final entry in that lineup. At 7 billion parameters it is built to run on cheap hardware, including CPUs and single GPUs, while still handling retrieval-augmented generation, tool use, and reasoning tasks that Cohere's larger models were designed for. It topped the Hugging Face Open LLM Leaderboard among similarly sized open-weight models at launch, beating Gemma 2 9B, Ministral 8B, and Llama 3.1 8B on average across benchmarks including MMLU, IFEval, and GPQA. The model keeps the same 128,000-token context window as its bigger siblings and is priced far below them, making it a fit for high-volume, latency-sensitive applications rather than frontier-level tasks.
