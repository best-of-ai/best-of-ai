---
title: 'BTLM-3B'
name: 'BTLM-3B'
slug: 'btlm-3b'
subtitle: 'Cerebras'' compact open-weight model tuned to punch above its parameter count'
description: 'Cerebras'' compact open-weight model tuned to punch above its parameter count'
company: 'cerebras'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.cerebras.ai/blog/btlm-3b-8b-7b-parameter-performance-in-a-3-billion-parameter-model'
price: 'Free'
rank: 4
release_date: '2023-07-24'
param_count: '3B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, small-model]
---

BTLM-3B-8K is a 3 billion parameter language model that Cerebras built with the Opentensor Foundation and trained on Cerebras' wafer-scale CS-2 systems. Announced in the summer of 2023, it was designed for a specific goal: match the quality of 7 billion parameter models while staying small enough to run on phones and low-memory devices. Cerebras reports that BTLM-3B, once quantized, fits in around 3GB of memory and runs on hardware like the iPhone, Google Pixel, and even a Raspberry Pi, while performing in line with contemporary 7B models such as RedPajama-INCITE-7B on common benchmarks.

The model was trained on 627 billion tokens from the SlimPajama dataset, fewer than several competing 3B models used at the time, and it uses ALiBi position embeddings to support a native 8,192-token context window with reasonable extrapolation beyond that. Cerebras released BTLM-3B under Apache 2.0, making it free for commercial use, and it briefly held the title of best-performing open 3B model before newer small models from Microsoft, Google, and others moved past it.
