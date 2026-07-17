---
title: 'GPT-J'
name: 'GPT-J'
slug: 'gpt-j'
subtitle: 'EleutherAI''s early open-weight GPT-3-style model'
description: 'EleutherAI''s early open-weight GPT-3-style model'
company: 'eleuther-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.eleuther.ai/'
price: 'Free'
rank: 3
release_date: '2021-06-04'
param_count: '6B'
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

GPT-J is a 6 billion parameter language model that EleutherAI released on June 9, 2021, as one of the first credible open replications of GPT-3's architecture at a time when OpenAI kept GPT-3 itself locked behind a paid API. It was trained on the Pile, EleutherAI's own 825GB text dataset, using the Mesh Transformer JAX library to parallelize training across TPU pods rather than GPUs. With 28 layers and a 2048 token context window, it was noticeably smaller than GPT-3's largest configuration but still handled general text generation, question answering, and code completion well enough to become a standard baseline for open-source NLP research. It shipped under the Apache 2.0 license, so anyone could download, fine-tune, and deploy it without OpenAI's usage restrictions, which made it a popular backbone for early open chatbot projects. GPT-J has since been superseded by GPT-NeoX-20B and later open models, but it remains a commonly cited reference point for how the open-source community caught up to closed labs during the GPT-3 era.
