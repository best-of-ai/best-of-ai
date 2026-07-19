---
title: 'Cerebras-GPT'
name: 'Cerebras-GPT'
slug: 'cerebras-gpt'
subtitle: 'Cerebras'' fully open family of models trained on its wafer-scale chips'
description: 'Cerebras'' fully open family of models trained on its wafer-scale chips'
company: 'cerebras'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.cerebras.ai/blog/cerebras-gpt-a-family-of-open-compute-efficient-large-language-models'
price: 'Free'
rank: 3
release_date: '2023-03-28'
param_count: '13B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, fully-open, self-hosted]
---

Cerebras-GPT is a family of language models, ranging from 111 million to 13 billion parameters, that Cerebras trained on its own CS-2 wafer-scale systems and released in March 2023. The point of the project was less about beating benchmarks and more about openness: Cerebras published the weights, training code, and a detailed technical report describing hyperparameters and scaling behavior for every size in the family, following compute-optimal training recipes similar to those behind Chinchilla. That made Cerebras-GPT one of the more fully documented open model families of its time, useful to researchers who wanted a clean, reproducible baseline for studying scaling laws.

All Cerebras-GPT checkpoints are released under Apache 2.0 and hosted on Hugging Face, free for commercial and research use. The models use a fairly standard GPT-style architecture with a 2,048-token context window, and by 2023 standards their raw capability was modest next to models like LLaMA, since Cerebras prioritized transparent, reproducible training over squeezing out maximum benchmark performance. The family is mainly cited today in scaling-law research and as an example of an AI hardware company demonstrating its own chips by training and open-sourcing a full model lineup.
