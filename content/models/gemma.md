---
title: 'Gemma'
name: 'Gemma'
slug: 'gemma'
subtitle: 'Google''s original open-weight Gemma release, built from the same research as Gemini'
description: 'Google''s original open-weight Gemma release, built from the same research as Gemini'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://blog.google/technology/developers/gemma-open-models/'
price: 'Free'
rank: 7
release_date: '2024-02-21'
param_count: '7B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Gemma License'
api_available: true
mmlu_score: 64.3
humaneval_score: 32.3
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Google AI Studio']
date: '2026-07-16'
tags: [llm, open-weight, legacy]
---

Gemma is Google's first family of open-weight language models, released in February 2024 and built from the same research used inside Gemini. It came out in two sizes, 2B and 7B parameters, each with a base and an instruction-tuned checkpoint, trained on 2 trillion and 6 trillion tokens of web text, math, and code respectively. The context window is a modest 8,192 tokens, in line with other models of that era.

The release mattered because it gave developers a genuinely usable small model they could run on a single consumer GPU or even a laptop, rather than relying on an API. Its license permits commercial use but blocks a list of harmful applications that Google specifies, a middle ground between fully open licenses like Apache 2.0 and the closed terms of most proprietary models. Gemma was later superseded by Gemma 2 and Gemma 3, but it established the naming and licensing pattern Google has followed since.
