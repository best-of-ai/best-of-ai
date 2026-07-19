---
title: 'GPT-1'
name: 'GPT-1'
slug: 'gpt-1'
subtitle: 'OpenAI''s original 2018 paper model that introduced the GPT architecture'
description: 'OpenAI''s original 2018 paper model that introduced the GPT architecture'
company: 'openai'
model_type: 'Language'
logo_url: ''
product_url: 'https://openai.com/index/language-unsupervised/'
price: 'Free'
rank: 5
release_date: '2018-06-11'
param_count: '117M'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Research']
date: '2026-07-16'
tags: [llm, legacy, foundation-model]
---

GPT-1 is OpenAI's first Generative Pre-trained Transformer, introduced in a June 2018 paper titled "Improving Language Understanding by Generative Pre-Training." It had 117 million parameters and was trained on BookCorpus, a collection of unpublished novels, using a 512-token context window. The core idea was simple: pretrain a Transformer on raw text without labels, then fine-tune the same model on specific tasks like question answering or textual entailment.

That approach outperformed task-specific architectures on 9 of the 12 benchmarks OpenAI tested it against, which was the real point of the paper. GPT-1 itself was never a product; it was proof that generative pretraining followed by fine-tuning could beat models built and trained separately for each task. That result set the template OpenAI scaled up through GPT-2, GPT-3, and everything that followed.
