---
title: 'Codestral Mamba'
name: 'Codestral Mamba'
slug: 'codestral-mamba'
subtitle: 'Mistral''s code model built on the Mamba state-space architecture instead of a transformer'
description: 'Mistral''s code model built on the Mamba state-space architecture instead of a transformer'
company: 'mistral-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://mistral.ai/news/codestral-mamba/'
price: 'Free'
rank: 6
release_date: '2024-07-16'
param_count: '7B'
context_window_tokens: 256000
modality: [text, code]
open_weight: true
license: 'Apache 2.0'
input_price_usd_per_m: 0.25
output_price_usd_per_m: 0.25
api_available: true
humaneval_score: 75.0
access_methods: [Self-hosted, API]
platforms: ['Hugging Face', 'Mistral API']
date: '2026-07-16'
tags: [code, open-weight, api]
---

Codestral Mamba is a code generation model Mistral AI released in July 2024, notable mainly for its architecture: instead of the transformer design used by nearly every other code model, it's built on Mamba, a state-space model architecture. State-space models process sequences with linear rather than quadratic scaling in sequence length, which means inference speed does not degrade as sharply as context grows. Mistral sized it at roughly 7 billion parameters and gave it a 256,000-token context window, with the company reporting reliable in-context retrieval performance even at that length.

On HumanEval, Codestral Mamba scores around 75 percent pass@1, competitive with much larger transformer-based code models. It's released under the Apache 2.0 license, so the weights can be freely downloaded, fine-tuned, and used commercially, and it's also available through Mistral's API at $0.25 per million input and output tokens. Mistral pitched it as a proof of concept that state-space architectures can match transformers on real coding tasks while offering faster and cheaper inference for long-context use cases like reasoning over large repositories.
