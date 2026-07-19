---
title: 'Jamba Large 1.6'
name: 'Jamba Large 1.6'
slug: 'jamba-large-1-6'
subtitle: 'AI21''s updated flagship hybrid transformer-Mamba model'
description: 'AI21''s updated flagship hybrid transformer-Mamba model'
company: 'ai21-labs'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.ai21.com/jamba/'
price: 'Free'
rank: 4
release_date: '2025-03-06'
param_count: '398B (94B active)'
context_window_tokens: 256000
modality: [text]
open_weight: true
license: 'Jamba Open Model License'
input_price_usd_per_m: 2
output_price_usd_per_m: 8
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: false
platforms: ['Hugging Face', 'AWS Bedrock']
date: '2026-07-16'
tags: [llm, open-weight, long-context, hybrid-architecture]
---

Jamba Large 1.6 is AI21 Labs' flagship language model, built on a hybrid architecture that combines transformer attention layers with Mamba state-space model layers. AI21 released it in March 2025 as part of the Jamba 1.6 family, alongside a smaller Jamba Mini 1.6. The model has 398 billion total parameters, with only 94 billion active at inference time thanks to a mixture-of-experts design, which keeps compute costs down while supporting a 256,000-token context window. AI21 markets it toward enterprise customers who need to process long documents, contracts, or codebases without sending data to a third party, since the model is available for self-hosted deployment as well as through an API. In AI21's own benchmarking, Jamba Large 1.6 beat open models from Meta, Mistral, and Cohere on a range of tasks, and it runs notably faster than similarly sized dense transformers because of the Mamba layers' more efficient handling of long sequences.
