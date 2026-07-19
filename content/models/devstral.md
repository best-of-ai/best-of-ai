---
title: 'Devstral'
name: 'Devstral'
slug: 'devstral'
subtitle: 'Mistral''s open-weight model tuned for agentic coding and codebase exploration'
description: 'Mistral''s open-weight model tuned for agentic coding and codebase exploration'
company: 'mistral-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://mistral.ai/news/devstral/'
price: 'Free'
rank: 6
release_date: '2025-05-21'
param_count: '24B'
context_window_tokens: 128000
modality: [text, code]
open_weight: true
license: 'Apache 2.0'
input_price_usd_per_m: 0.1
output_price_usd_per_m: 0.3
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Mistral API']
date: '2026-07-16'
tags: [code, open-weight, agentic, api]
---

Devstral is a 24-billion-parameter code model that Mistral AI released on May 21, 2025, built in collaboration with All Hands AI, the team behind the OpenHands agent framework. Unlike most code models, which are tuned mainly for autocomplete or single-turn code generation, Devstral is trained specifically for agentic coding: exploring a codebase across multiple files, using tools, and completing multi-step software engineering tasks. On SWE-bench Verified it scored 46.8%, ahead of every open model available at release and even some larger proprietary ones.

Mistral released the weights under the Apache 2.0 license, and the model is small enough to run on a single high-end consumer GPU, which made it a popular base for local coding agents. Mistral later followed it up with Devstral Small 1.1 and the larger Devstral 2, each pushing SWE-bench scores higher, but the original Devstral remains notable as one of the first open-weight models built specifically around agentic software engineering rather than general-purpose code completion.
