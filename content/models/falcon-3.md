---
title: 'Falcon 3'
name: 'Falcon 3'
slug: 'falcon-3'
subtitle: 'TII''s efficient small-model open-weight family'
description: 'TII''s efficient small-model open-weight family'
company: 'technology-innovation-institute'
model_type: 'Language'
logo_url: ''
product_url: 'https://falconllm.tii.ae/'
price: 'Free'
rank: 4
release_date: '2024-12-17'
param_count: '10B'
context_window_tokens: 32000
modality: [text]
open_weight: true
license: 'Falcon License'
api_available: false
mmlu_score: 73.1
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, small-model, self-hosted]
---

Falcon 3 is a family of open-weight language models from the Technology Innovation Institute in Abu Dhabi, released in December 2024 in four sizes: 1B, 3B, 7B, and 10B parameters, each with base and instruct versions. TII built the line to run on modest hardware, including a single GPU or a laptop, while still competing with larger open models. The 10B model topped Hugging Face's leaderboard for models under 13B parameters at launch, scoring 73.1 on MMLU and 83.1 on GSM8K, ahead of comparable Llama and Gemma variants at the time. Most sizes support a 32K token context window (the 1B model is limited to 8K), and TII distributes the weights on Hugging Face under its own Falcon License for self-hosted use. Falcon 3 followed the earlier Falcon and Falcon Mamba releases and reflects TII's shift toward smaller, cheaper-to-run models rather than chasing frontier parameter counts.
