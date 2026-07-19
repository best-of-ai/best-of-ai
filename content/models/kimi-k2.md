---
title: 'Kimi K2'
name: 'Kimi K2'
slug: 'kimi-k2'
subtitle: 'Moonshot''s original K2-generation open-weight base model'
description: 'Moonshot''s original K2-generation open-weight base model'
company: 'moonshot-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.moonshot.ai/'
price: 'Free'
rank: 7
release_date: '2025-07-11'
param_count: '1T (32B active)'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Modified MIT'
input_price_usd_per_m: 0.55
output_price_usd_per_m: 2.2
api_available: true
humaneval_score: 85.0
lmarena_score: 1340
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, mixture-of-experts, self-hosted]
extra_model_types: ['Code']
---

Kimi K2 is Moonshot AI's original K2-generation base model, released in July 2025 as one of the largest open-weight language models available at the time. It uses a mixture-of-experts design with about 1 trillion total parameters and 32 billion active per token, and it supports a 128,000-token context window. Moonshot built it around agentic use cases such as tool calling and multi-step task execution rather than pure chat, and on coding benchmarks like the multilingual HumanEval variant MultiPL-E it scored close to the best closed models available that summer. The weights are released under a modified MIT license, so companies can download, fine-tune, and self-host it instead of going through Moonshot's API, and it became the base that later Moonshot releases, including K2.5, K2.6, and K2.7 Code, built on top of.
