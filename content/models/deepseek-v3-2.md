---
title: 'DeepSeek V3.2'
name: 'DeepSeek V3.2'
slug: 'deepseek-v3-2'
subtitle: 'DeepSeek''s V3.1 update, built around a new sparse attention mechanism'
description: 'DeepSeek''s V3.1 update, built around a new sparse attention mechanism'
company: 'deepseek'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 8
release_date: '2025-12-01'
param_count: '685B (MoE)'
context_window_tokens: 163840
modality: [text, code]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 0.21
output_price_usd_per_m: 0.32
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-25'
tags: [llm, open-weight, reasoning, coding, mixture-of-experts]
extra_model_types: ['Code']
---

DeepSeek V3.2 is DeepSeek's update to V3.1, publicly detailed on December 1, 2025 after an experimental preview in September. It introduces DeepSeek Sparse Attention, a fine-grained sparse attention mechanism that cuts training and inference cost while preserving quality on long-context tasks, and the flagship Speciale variant carries roughly 685 billion parameters in a mixture-of-experts layout. The context window sits at 163,840 tokens with up to 64,000 tokens of output, and DeepSeek reports gold-medal-level results on 2025 International Mathematical Olympiad and International Olympiad in Informatics problem sets. API pricing runs around $0.21 per million input tokens and $0.32 per million output tokens, roughly half of what V3.1-Terminus cost, particularly for long-context decoding. Like the rest of the DeepSeek lineup it ships under the MIT license with weights on Hugging Face, and it served as the base DeepSeek built V4-Pro on the following spring.
