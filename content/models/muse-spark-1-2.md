---
title: 'Muse Spark 1.2'
name: 'Muse Spark 1.2'
slug: 'muse-spark-1-2'
subtitle: 'Meta''s coding-focused update to Muse Spark, shipped alongside its first terminal coding agent'
description: 'Meta''s coding-focused update to Muse Spark, shipped alongside its first terminal coding agent'
company: 'meta-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://ai.meta.com/'
price: 'Paid'
rank: 6
release_date: '2026-08-05'
param_count: 'Undisclosed'
context_window_tokens: 1048576
modality: [text, code]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 1.25
output_price_usd_per_m: 4.25
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['Meta API']
date: '2026-08-09'
tags: [code, agentic, api, coding-assistant]
---

Muse Spark 1.2 is a coding-focused point release of Muse Spark 1.1 rather than a new base model, shipped August 5, 2026 alongside Muse Code, Meta's first terminal coding agent. It keeps the 1,048,576 token context window and roughly 131,072 max output tokens from 1.1, and was co-trained with the new agent using rejection-sampled harness trajectories plus a self-improvement loop. Meta reports a jump from 76.2 to 82.9 percent on Terminal-Bench 2.1 and from 53.0 to 59.3 percent on DeepSWE v1.1 over the previous version. Standard API pricing holds at $1.25 per million input tokens and $4.25 per million output tokens, and Meta added a separate contributor tier at $0.10 input and $0.20 output in exchange for permission to train future models on submitted prompts and completions.
