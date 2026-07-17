---
title: 'CodeT5+'
name: 'CodeT5+'
slug: 'codet5'
subtitle: 'Salesforce''s open-weight encoder-decoder code model family'
description: 'Salesforce''s open-weight encoder-decoder code model family'
company: 'salesforce'
model_type: 'Code'
logo_url: ''
product_url: 'https://github.com/salesforce/CodeT5'
price: 'Free'
rank: 3
release_date: '2023-05-13'
param_count: '16B'
context_window_tokens: 2048
modality: [text, code]
open_weight: true
license: 'BSD-3-Clause'
api_available: false
humaneval_score: 30.9
access_methods: [Self-hosted]
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, code, self-hosted]
---

CodeT5+ is a family of open-weight code models built by Salesforce Research, released in May 2023 as a follow-up to the original CodeT5 encoder-decoder model. It comes in several sizes from 220 million up to 16 billion parameters and can run in encoder-only, decoder-only, or full encoder-decoder mode, which lets one architecture cover code understanding tasks like defect detection alongside generation tasks like code completion and text-to-code synthesis. Training combines span denoising, causal language modeling, contrastive learning, and text-code matching objectives, an approach Salesforce says gives it an edge over decoder-only code models of similar size on retrieval-augmented generation tasks. The 16B variant scores around 30.9% pass@1 on HumanEval, and an instruction-tuned version of the same checkpoint pushes past 35%, beating OpenAI's older code-cushman-001 model on the same benchmark. Weights are hosted on Hugging Face under a BSD-3-Clause license, making CodeT5+ one of the earlier fully open alternatives to Codex-era proprietary code models.
