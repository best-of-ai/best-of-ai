---
title: 'Llama Guard 3'
name: 'Llama Guard 3'
slug: 'llama-guard-3'
subtitle: 'Meta''s open-weight safety classifier model for moderating LLM input and output'
description: 'Meta''s open-weight safety classifier model for moderating LLM input and output'
company: 'meta-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 4
release_date: '2024-07-23'
param_count: '8B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Llama 3.1 Community License'
api_available: true
access_methods: [Self-hosted, API]
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, safety, self-hosted]
---

Llama Guard 3 is Meta's safety classifier released in July 2024 alongside Llama 3.1, and it replaced Llama Guard 2 as Meta's recommended moderation model. Built on an 8B Llama 3.1 base, it expands on its predecessor by adding three new hazard categories, bringing the total taxonomy to 14, and it improves multilingual moderation coverage. Like Llama Guard 2, it sits in a pipeline rather than serving as a standalone assistant: it reads a prompt or a model's response and returns a safe or unsafe label plus the violated category. It is open-weight under the Llama 3.1 Community License and widely used by companies deploying open-source LLMs that need a moderation layer without relying on a third-party API.
