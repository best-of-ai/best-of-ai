---
title: 'Llama Guard 2'
name: 'Llama Guard 2'
slug: 'llama-guard-2'
subtitle: 'Meta''s earlier content-safety classifier model, preceding Llama Guard 3'
description: 'Meta''s earlier content-safety classifier model, preceding Llama Guard 3'
company: 'meta-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.meta.com/blog/meta-llama-3/'
price: 'Free'
rank: 5
release_date: '2024-04-18'
param_count: '8B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Llama 3 Community License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Together AI']
date: '2026-07-16'
tags: [safety, open-weight, legacy]
---

Llama Guard 2 is a content-safety classifier Meta released alongside Llama 3 in April 2024, built on an 8B Llama 3 base rather than as a general-purpose chat model. It checks both prompts going into a language model and responses coming out, flagging content across 11 hazard categories drawn from the MLCommons taxonomy, covering things like violence, hate speech, and sexual content. Developers run it as a guardrail in front of or behind another LLM in a pipeline, rather than using it to generate answers directly. Meta has since replaced it with Llama Guard 3, but it remains available on Hugging Face under the Llama 3 Community License for teams already running it in production.
