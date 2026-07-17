---
title: 'Kimi K2.6'
name: 'Kimi K2.6'
slug: 'kimi-k2-6'
subtitle: 'Moonshot''s open-weight model built for long-running agentic and tool-use tasks'
description: 'Moonshot''s open-weight model built for long-running agentic and tool-use tasks'
company: 'moonshot-ai'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.moonshot.ai/'
price: 'Free'
rank: 8
release_date: '2026-04-20'
param_count: '1T (32B active)'
context_window_tokens: 256000
modality: [text]
open_weight: true
license: 'Modified MIT'
input_price_usd_per_m: 0.6
output_price_usd_per_m: 2.5
api_available: true
mmlu_score: 88.0
humaneval_score: 87.0
lmarena_score: 1355
access_methods: [API, Self-hosted]
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, agentic, reasoning, mixture-of-experts]
---

Kimi K2.6 is Moonshot AI's open-weight flagship model, released in April 2026 as the successor to the original Kimi K2. It is a 1-trillion-parameter mixture-of-experts model that activates about 32 billion parameters per token, ships natively in INT4 for cheaper inference, and handles a 262,144-token context window. The model is built for long-running agentic work: Moonshot designed it around multi-agent orchestration, coding sessions that run for hours without human intervention, and native multimodal input rather than bolted-on vision. Independent evaluations from Artificial Analysis rank it as the strongest open-weight model available, putting it within a few points of closed frontier systems from OpenAI and Anthropic on tasks like SWE-Bench Pro and Humanity's Last Exam, while charging a fraction of their per-token price. Moonshot releases the weights under a modified MIT license, so anyone can download and self-host the model rather than relying on Moonshot's own API.
