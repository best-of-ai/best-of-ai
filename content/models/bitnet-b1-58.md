---
title: 'BitNet b1.58'
name: 'BitNet b1.58'
slug: 'bitnet-b1-58'
subtitle: 'Microsoft''s research model demonstrating competitive LLM performance with 1.58-bit ternary weights'
description: 'Microsoft''s research model demonstrating competitive LLM performance with 1.58-bit ternary weights'
company: 'microsoft'
model_type: 'Language'
logo_url: ''
product_url: 'https://github.com/microsoft/BitNet'
price: 'Free'
rank: 6
release_date: '2024-02-27'
param_count: '2B (2B4T release)'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'GitHub']
date: '2026-07-16'
tags: [llm, open-weight, research, efficiency]
---

BitNet b1.58 is a line of research from Microsoft exploring language models built from ternary weights, meaning every weight is restricted to -1, 0, or 1 instead of the usual 16- or 32-bit floating point values. The original paper, "The Era of 1-bit LLMs," came out in February 2024 and showed that models trained natively this way, rather than quantized after the fact, could match full-precision models like Llama 2 at comparable sizes while cutting memory use and inference energy substantially. Microsoft followed up in April 2025 with BitNet b1.58 2B4T, an openly released 2-billion-parameter checkpoint trained on 4 trillion tokens, whose non-embedding memory footprint runs about 0.4GB, well under similarly sized models like Gemma 3 1B or MiniCPM 2B. The weights and inference code are on GitHub and Hugging Face under the MIT license, and the project is notable less for beating other models on benchmarks than for proving that 1-bit training works at all without a big performance penalty, which matters for running capable models on phones or edge devices.
