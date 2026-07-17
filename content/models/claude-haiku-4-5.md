---
title: 'Claude Haiku 4.5'
name: 'Claude Haiku 4.5'
slug: 'claude-haiku-4-5'
subtitle: 'Anthropic''s fastest and cheapest current-generation model'
description: 'Anthropic''s fastest and cheapest current-generation model'
company: 'anthropic'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.anthropic.com/news/claude-haiku-4-5'
price: 'Paid'
rank: 7
release_date: '2025-10-15'
param_count: 'Undisclosed'
context_window_tokens: 200000
modality: [text, image]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 1
output_price_usd_per_m: 5
api_available: true
mmlu_score: 85.0
humaneval_score: 84.0
lmarena_score: 1310
access_methods: [API, Chat UI]
platforms: ['Claude.ai', 'AWS Bedrock', 'API']
date: '2026-07-16'
tags: [llm, foundation-model, low-latency, api]
---

Claude Haiku 4.5 is Anthropic's fastest and cheapest current-generation model, released on October 15, 2025. It is the first Haiku model to include extended thinking, computer use, and context awareness, features that had previously only shipped in Anthropic's larger Sonnet and Opus models. On SWE-bench Verified it scores about 73.3 percent, which puts it within a few points of Claude Sonnet 4.5's 77.2 percent despite costing a third as much: $1 per million input tokens and $5 per million output tokens versus Sonnet's $3/$15. That makes it a practical choice for running many agents in parallel or handling high-volume tasks where Sonnet or Opus would be needlessly expensive. It reads both text and images and shares the 200,000 token context window used across the rest of the current Claude lineup.
