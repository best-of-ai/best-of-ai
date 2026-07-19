---
title: 'Dolly 2.0'
name: 'Dolly 2.0'
slug: 'dolly-2-0'
subtitle: 'Databricks'' first fully open, commercially-usable instruction-following model'
description: 'Databricks'' first fully open, commercially-usable instruction-following model'
company: 'databricks'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.databricks.com/blog/2023/04/12/dolly-first-open-commercially-viable-instruction-tuned-llm'
price: 'Free'
rank: 5
release_date: '2023-04-12'
param_count: '12B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, legacy]
---

Dolly 2.0 is a 12-billion-parameter instruction-following language model that Databricks released on April 12, 2023, built on top of EleutherAI's Pythia model. What made it notable wasn't its raw capability, which trailed well behind GPT-3.5 at the time, but its licensing: Databricks open-sourced the model weights, training code, and a fresh instruction dataset called databricks-dolly-15k, all cleared for commercial use. That 15,000-example dataset was written from scratch by roughly 5,000 Databricks employees, specifically to avoid the licensing restrictions attached to datasets built from OpenAI outputs, which earlier open instruction-tuned models had relied on.

Databricks positioned Dolly 2.0 as proof that a useful instruction-following model could be built and shared without restrictive terms, at a time when most comparably capable open models carried research-only licenses. It's no longer competitive with modern instruction-tuned models, but it was an early, influential example of a fully open alternative to closed commercial chatbots.
