---
title: 'Llama 3.1 8B'
name: 'Llama 3.1 8B'
slug: 'llama-3-1-8b'
subtitle: 'Meta''s compact tier of the Llama 3.1 generation'
description: 'Meta''s compact tier of the Llama 3.1 generation'
company: 'meta-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 6
release_date: '2024-07-23'
param_count: '8B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Llama 3.1 Community License'
api_available: true
mmlu_score: 69.4
humaneval_score: 72.6
lmarena_score: 1180
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Ollama']
date: '2026-07-16'
tags: [llm, open-weight, small-model, self-hosted]
extra_model_types: ['Code']
---

Llama 3.1 8B is the small tier of the same July 2024 release, built for people who want to run a capable model on a single GPU or even a high-end laptop. It shares the 128,000-token context window and multilingual training of its larger siblings, and it scores higher than the original Llama 3 8B on MMLU and HumanEval thanks to more training data and refined post-training. Developers use it for on-device assistants, cheap batch processing, and fine-tuning experiments where the 70B or 405B models would be overkill or too expensive to serve. It runs easily through tools like Ollama and is one of the most downloaded models on Hugging Face.
