---
title: 'Mathstral'
name: 'Mathstral'
slug: 'mathstral'
subtitle: 'Mistral''s math-specialised model derived from Mistral 7B'
description: 'Mistral''s math-specialised model derived from Mistral 7B'
company: 'mistral-ai'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://mistral.ai/news/mathstral/'
price: 'Free'
rank: 5
release_date: '2024-07-16'
param_count: '7B'
context_window_tokens: 32768
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [reasoning, math, open-weight]
---

Mathstral is a 7B parameter model that Mistral AI released in July 2024, built on the Mistral 7B base and tuned specifically for math and STEM reasoning. It came out of a collaboration with Project Numina, a group focused on advancing open math models, and was released alongside Codestral Mamba as one of two specialist "miniature" models that week. On the MATH benchmark it scores 56.6%, rising to nearly 69% with majority voting across multiple samples, and it reaches 63.5% on MMLU, putting it ahead of most other models in the 7B class on quantitative reasoning tasks.

Mistral released Mathstral under an Apache 2.0 license, so it can be downloaded, fine-tuned, and run locally without restriction. It targets researchers and developers who need a small, self-hostable model for multi-step math problems, tutoring applications, or as a base for further fine-tuning, rather than general-purpose chat.
