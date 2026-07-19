---
title: 'MiniCPM'
name: 'MiniCPM'
slug: 'minicpm'
subtitle: 'OpenBMB''s efficient small model designed to run well on phones and edge devices'
description: 'OpenBMB''s efficient small model designed to run well on phones and edge devices'
company: 'openbmb'
model_type: 'Language'
logo_url: ''
product_url: 'https://github.com/OpenBMB/MiniCPM'
price: 'Free'
rank: 5
release_date: '2024-02-01'
param_count: '2.4B'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, small-model, on-device]
---

MiniCPM is a 2.4B parameter language model that OpenBMB released in February 2024, built to run well on phones and other edge devices where a full-size 7B or 13B model would be too heavy. Despite its small size, OpenBMB reported that it performs close to Mistral 7B on general benchmarks and ahead of larger models like Llama 2 13B and Falcon 40B on several tasks, particularly in Chinese language understanding, math, and code. A separate long-context variant, MiniCPM-2B-128k, extends the context window to 128,000 tokens for document-heavy use cases.

The model is open-weight under an Apache 2.0 license and distributed through Hugging Face, aimed at developers building offline or low-cost applications who need a capable model that fits within tight memory and compute budgets. It became the base for OpenBMB's later MiniCPM-V multimodal models and helped establish the lab's focus on efficient, on-device AI as an alternative to scaling everything up.
