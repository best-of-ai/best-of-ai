---
title: 'InternLM2.5'
name: 'InternLM2.5'
slug: 'internlm2-5'
subtitle: 'Shanghai AI Lab''s updated InternLM generation with stronger tool-use and reasoning'
description: 'Shanghai AI Lab''s updated InternLM generation with stronger tool-use and reasoning'
company: 'shanghai-ai-lab'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://github.com/InternLM/InternLM'
price: 'Free'
rank: 5
release_date: '2024-07-03'
param_count: '7B (1.8B and 20B variants also released)'
context_window_tokens: 1000000
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
mmlu_score: 72.8
access_methods: [Self-hosted, API]
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, reasoning, open-weight, long-context]
---

InternLM2.5 is Shanghai AI Laboratory's follow-up to InternLM2, released starting July 3, 2024 in 7B and 1.8B sizes, with a 20B version added on August 1, 2024. The 7B chat model scores 72.8 on MMLU and beats Llama 3 8B Instruct and Gemma 2 9B on several reasoning and math benchmarks, according to the developer's own OpenCompass evaluations. A dedicated 7B-Chat-1M checkpoint extends the context window to one million tokens and can locate specific facts inside million-token documents in needle-in-a-haystack tests, while the standard 20B model tops out at 200K tokens. The series also adds stronger function calling and agent-style tool use compared to the original InternLM2, and all weights are released under the Apache 2.0 license through Hugging Face and the InternLM GitHub repository.
