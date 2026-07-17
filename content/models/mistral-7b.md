---
title: 'Mistral 7B'
name: 'Mistral 7B'
slug: 'mistral-7b'
subtitle: 'Mistral''s original compact open-weight model that outperformed larger rivals'
description: 'Mistral''s original compact open-weight model that outperformed larger rivals'
company: 'mistral-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://mistral.ai/news/announcing-mistral-7b/'
price: 'Free'
rank: 6
release_date: '2023-09-27'
param_count: '7B'
context_window_tokens: 32000
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
mmlu_score: 60.1
humaneval_score: 30.5
access_methods: [Self-hosted]
platforms: ['Hugging Face', 'Ollama']
date: '2026-07-16'
tags: [llm, open-weight, small-model, self-hosted]
---

Mistral 7B is the model that put Mistral AI on the map, released on September 27, 2023 as the French startup's first public model. At 7 billion parameters it was small enough to run on a single consumer GPU, yet it beat Llama 2 13B on every benchmark Mistral tested and even outperformed Llama 2 34B on several reasoning and code tasks, scoring 60.1% on MMLU and 30.5% on HumanEval. It uses grouped-query attention and sliding-window attention to keep inference fast and memory-efficient at its 32,000-token context length.

Mistral released it under an Apache 2.0 license with no usage restrictions, which was unusual for a model of its quality at the time and helped it spread quickly through the open-source community via Hugging Face and tools like Ollama and llama.cpp. It became a common base for fine-tunes and merges, and its success established Mistral AI as a serious competitor to Meta and OpenAI within months of the company's founding.
