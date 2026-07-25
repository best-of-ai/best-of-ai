---
title: 'Claude Sonnet 4.6'
name: 'Claude Sonnet 4.6'
slug: 'claude-sonnet-4-6'
subtitle: 'Anthropic''s default Sonnet model, built to approach Opus-class results at a fifth of the price'
description: 'Anthropic''s default Sonnet model, built to approach Opus-class results at a fifth of the price'
company: 'anthropic'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.anthropic.com/news/claude-sonnet-4-6'
price: 'Paid'
rank: 9
release_date: '2026-02-17'
param_count: 'Undisclosed'
context_window_tokens: 1000000
modality: [text, image]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 3
output_price_usd_per_m: 15
api_available: true
lmarena_score: 1380
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['Claude.ai', 'AWS Bedrock', 'Google Vertex AI', 'API']
date: '2026-07-25'
tags: [llm, reasoning, frontier-model, api, agentic]
extra_model_types: ['Code']
---

Claude Sonnet 4.6 shipped on February 17, 2026 and became the default model in claude.ai and Claude Cowork, Anthropic's workspace product. It matches Opus 4.6's 1 million token context window and 128,000 token output limit while pricing in at $3 per million input tokens and $15 per million output tokens, roughly a fifth of Opus 4.6's rate. On SWE-bench Verified it scored 79.6 percent, within a few points of the Opus model despite the price gap, and it posted 59.1 percent on Terminal-Bench 2.0 and 72.5 percent on OSWorld-Verified, benchmarks that test agentic terminal and computer-use tasks. Anthropic built in extended reasoning chains that can run up to 100 steps, aimed at developers who want Opus-level reliability without paying Opus prices.
