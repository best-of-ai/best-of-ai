---
title: 'GPT-NeoX-20B'
name: 'GPT-NeoX-20B'
slug: 'gpt-neox-20b'
subtitle: 'EleutherAI''s open-weight model, one of the largest public checkpoints of its era'
description: 'EleutherAI''s open-weight model, one of the largest public checkpoints of its era'
company: 'eleuther-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.eleuther.ai/'
price: 'Free'
rank: 4
release_date: '2022-04-14'
param_count: '20B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted, legacy]
---

GPT-NeoX-20B is a 20 billion parameter language model EleutherAI announced in April 2022, after roughly a year of development on its own GPT-NeoX training framework built on Megatron and DeepSpeed. At release it was the largest dense autoregressive language model with publicly downloadable weights, trained on the Pile with a 2048 token context window. On EleutherAI's own evaluation harness it landed between OpenAI's Curie and Davinci models on most standard NLP benchmarks, and its one-shot performance on math word problems beat the full 175B GPT-3 on that particular test, which the team highlighted as evidence that training data quality mattered as much as raw scale. It was released under the Apache 2.0 license through Hugging Face, giving researchers a large, inspectable model to study and fine-tune without needing access to a closed API. GPT-NeoX-20B has since been passed by far larger and more efficient open models, but it stayed influential in open-source LLM research as one of the reference training codebases the field built on.
