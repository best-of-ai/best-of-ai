---
title: 'Jamba 1.5 Mini'
name: 'Jamba 1.5 Mini'
slug: 'jamba-1-5-mini'
subtitle: 'AI21''s compact hybrid transformer-Mamba model'
description: 'AI21''s compact hybrid transformer-Mamba model'
company: 'ai21-labs'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.ai21.com/jamba/'
price: 'Free'
rank: 4
release_date: '2024-08-22'
param_count: '52B (12B active)'
context_window_tokens: 256000
modality: [text]
open_weight: true
license: 'Jamba Open Model License'
input_price_usd_per_m: 0.2
output_price_usd_per_m: 0.4
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'AWS Bedrock']
date: '2026-07-16'
tags: [llm, open-weight, long-context, hybrid-architecture]
---

Jamba 1.5 Mini is the smaller model in AI21 Labs' Jamba 1.5 family, released alongside Jamba 1.5 Large on August 22, 2024. It shares the same hybrid Transformer-Mamba mixture-of-experts architecture, scaled down to 52 billion total parameters with 12 billion active, and it keeps the same 256,000-token context window as its larger sibling. On the Arena Hard benchmark it scored 46.1, ahead of similarly sized models such as Claude 3 Haiku, Mixtral 8x22B, and Command R+. AI21 built it for latency-sensitive business use cases like function calling, structured JSON output, and grounded generation, and prices it at $0.20 per million input tokens and $0.40 per million output tokens through its API. Like Jamba 1.5 Large, it's released under AI21's Jamba Open Model License with weights on Hugging Face and availability on AWS Bedrock.
