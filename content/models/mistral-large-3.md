---
title: 'Mistral Large 3'
name: 'Mistral Large 3'
slug: 'mistral-large-3'
subtitle: 'Mistral''s flagship frontier-tier language model'
description: 'Mistral''s flagship frontier-tier language model'
company: 'mistral-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://mistral.ai/news/'
price: 'Freemium'
rank: 7
release_date: '2025-12-02'
param_count: '675B (41B active)'
context_window_tokens: 256000
modality: [text, image]
open_weight: true
license: 'Apache 2.0'
input_price_usd_per_m: 0.5
output_price_usd_per_m: 1.5
api_available: true
access_methods: [API, Chat UI, Self-hosted]
runs_at_home: true
platforms: ['Le Chat', 'Azure AI', 'API', 'Hugging Face']
date: '2026-07-16'
tags: [llm, foundation-model, api, open-weight]
---

Mistral Large 3 is Mistral AI's flagship language model, released on December 2, 2025 as part of the broader Mistral 3 lineup. It uses a sparse mixture-of-experts design with 675 billion total parameters but only about 41 billion active per token, so it runs at roughly the compute cost of a much smaller dense model while drawing on a far larger pool of learned weights. It takes both text and images as input, handles a 256,000-token context window, and Mistral released the weights under an Apache 2.0 license, a departure from the closed approach it took with Mistral Large 2.

The model placed near the top of the open-weight field on the LMArena leaderboard at launch and is aimed at developers who want frontier-level reasoning, coding, and multilingual performance without being locked into a closed API. It is available through Mistral's Le Chat assistant, its own API, Azure AI, and as downloadable weights on Hugging Face for anyone who wants to self-host or fine-tune it, with API pricing set well below what Mistral charged for Large 2.
