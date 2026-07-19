---
title: 'Amazon Nova Micro'
name: 'Amazon Nova Micro'
slug: 'amazon-nova-micro'
subtitle: 'Amazon''s fastest, lowest-cost Nova tier for simple text tasks'
description: 'Amazon''s fastest, lowest-cost Nova tier for simple text tasks'
company: 'amazon'
model_type: 'Language'
logo_url: ''
product_url: 'https://aws.amazon.com/ai/generative-ai/nova/'
price: 'Paid'
rank: 5
release_date: '2024-12-03'
param_count: 'Undisclosed'
context_window_tokens: 128000
modality: [text]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.035
output_price_usd_per_m: 0.14
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['AWS Bedrock']
date: '2026-07-16'
tags: [llm, low-cost, api]
---

Amazon Nova Micro is the smallest and cheapest model in Amazon's Nova lineup, announced in December 2024 alongside the rest of the family and available through Amazon Bedrock. It handles text only, in and out, with a 128,000-token context window, and is priced at $0.035 per million input tokens and $0.14 per million output tokens, making it Amazon's answer to lightweight models like GPT-4o mini and Gemini Flash-Lite. Amazon built it for high-volume, latency-sensitive workloads such as text classification, simple extraction, and routing logic inside larger agent pipelines.

Because it skips image and video understanding entirely, Nova Micro runs faster and cheaper than its multimodal Nova siblings, Lite and Pro, at the cost of not being able to process visual input. It supports fine-tuning and model distillation on Bedrock, letting customers train it on a larger model's outputs to get closer to that model's quality for narrow tasks at a fraction of the cost.
