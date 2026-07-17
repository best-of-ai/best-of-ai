---
title: 'Claude 3.5 Haiku'
name: 'Claude 3.5 Haiku'
slug: 'claude-3-5-haiku'
subtitle: 'Anthropic''s fast, affordable model matching the prior Claude 3 Opus on some benchmarks'
description: 'Anthropic''s fast, affordable model matching the prior Claude 3 Opus on some benchmarks'
company: 'anthropic'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.anthropic.com/claude/haiku'
price: 'Paid'
rank: 6
release_date: '2024-11-04'
param_count: 'Undisclosed'
context_window_tokens: 200000
modality: [text]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.8
output_price_usd_per_m: 4
api_available: true
humaneval_score: 88.1
lmarena_score: 1240
access_methods: [API, Chat UI]
platforms: ['Claude.ai', 'AWS Bedrock', 'API']
date: '2026-07-16'
tags: [llm, low-latency, foundation-model, api]
---

Claude 3.5 Haiku is Anthropic's fast, low-cost model in the Claude 3.5 family, released in October 2024 alongside an upgraded Claude 3.5 Sonnet. Anthropic built it to replace Claude 3 Haiku as the cheapest, quickest option in the lineup while closing much of the capability gap with larger models: on coding evaluations such as SWE-bench Verified, Claude 3.5 Haiku scored competitively with the original Claude 3.5 Sonnet and outperformed several larger models available at launch, and Anthropic reported an 88.1% score on HumanEval for code generation.

The model keeps the 200,000-token context window standard across the Claude 3.5 line and is priced at $0.80 per million input tokens and $4 per million output tokens, making it one of the cheaper frontier-adjacent models on the market when it shipped. It is aimed at high-volume, latency-sensitive use cases like customer support, content moderation, and data extraction, where response speed and cost per call matter more than squeezing out the last bit of reasoning quality, and it is available through Anthropic's API, claude.ai, and cloud platforms including AWS Bedrock.
