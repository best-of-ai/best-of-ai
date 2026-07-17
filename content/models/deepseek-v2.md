---
title: 'DeepSeek-V2'
name: 'DeepSeek-V2'
slug: 'deepseek-v2'
subtitle: 'DeepSeek''s 2024 mixture-of-experts model that undercut rivals on API price'
description: 'DeepSeek''s 2024 mixture-of-experts model that undercut rivals on API price'
company: 'deepseek'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 5
release_date: '2024-05-06'
param_count: '236B (21B active)'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'DeepSeek License'
input_price_usd_per_m: 0.14
output_price_usd_per_m: 0.28
api_available: true
mmlu_score: 78.5
access_methods: [Self-hosted, API]
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, mixture-of-experts, legacy]
---

DeepSeek-V2 is a mixture-of-experts language model that DeepSeek released in May 2024, with 236 billion total parameters and 21 billion active per token. Its main technical contribution was Multi-head Latent Attention, a method for compressing the key-value cache that cut memory use dramatically and let the model serve far more tokens per second than DeepSeek's earlier dense 67B model on the same hardware. Trained on 8.1 trillion tokens with a 128K context window, it scored competitively on MMLU and coding benchmarks against other open models of the time.

What made V2 notable wasn't just its architecture but its price: DeepSeek launched its API at a fraction of what Chinese and Western rivals were charging, kicking off a round of price cuts across the industry that commentators at the time called a "price war." The MLA and DeepSeekMoE techniques introduced here carried forward into every subsequent DeepSeek model, including V3 and R1, making V2 the architectural foundation for the company's later frontier releases.
