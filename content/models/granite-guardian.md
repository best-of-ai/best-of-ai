---
title: 'Granite Guardian'
name: 'Granite Guardian'
slug: 'granite-guardian'
subtitle: 'IBM''s safety and risk-detection model for filtering harmful LLM inputs and outputs'
description: 'IBM''s safety and risk-detection model for filtering harmful LLM inputs and outputs'
company: 'ibm'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.ibm.com/granite'
price: 'Free'
rank: 5
release_date: '2024-10-21'
param_count: '8B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
platforms: ['IBM watsonx', 'Hugging Face']
date: '2026-07-16'
tags: [safety, open-weight, enterprise]
---

Granite Guardian is IBM's family of safety models, built to sit alongside a primary LLM and flag risky prompts or responses before they reach a user or an application. It launched with Granite 3.0 in October 2024 in 2B and 8B sizes, both fine-tuned from the base Granite instruct models rather than trained from scratch, and it checks for harms cataloged in IBM's AI Risk Atlas: things like jailbreak attempts, profanity, social bias, violence, and hallucinated tool calls or retrieval results in agentic workflows. IBM also ships a much smaller 38M-parameter HAP (hate, abuse, profanity) variant for teams that need guardrailing under tighter latency or cost budgets. Granite Guardian is open-weighted under Apache 2.0 and distributed through Hugging Face, Ollama, NVIDIA, and watsonx, and later updates, including a 3.3 release and a 4.1 release with support for user-defined judging criteria, extended the same approach to newer Granite base models.
