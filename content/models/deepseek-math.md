---
title: 'DeepSeek-Math'
name: 'DeepSeek-Math'
slug: 'deepseek-math'
subtitle: 'DeepSeek''s open-weight model specialized for mathematical reasoning'
description: 'DeepSeek''s open-weight model specialized for mathematical reasoning'
company: 'deepseek'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 4
release_date: '2024-02-05'
param_count: '7B'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'DeepSeek License'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, math, reasoning]
---

DeepSeekMath is a 7-billion-parameter model DeepSeek built specifically for mathematical reasoning, released in February 2024 and initialized from DeepSeek-Coder-Base. It was trained on 120 billion math-related tokens pulled from web data, alongside natural language and code, and scored 51.7% on the competition-level MATH benchmark without relying on external calculators or tools, a result that at the time approached the performance of much larger closed models like Gemini-Ultra and GPT-4. DeepSeek released it in base, instruction-tuned, and reinforcement-learning-tuned variants, with the RL version trained using Group Relative Policy Optimization, an algorithm the company introduced in this paper and later reused for DeepSeek-R1. The model has a 4,096-token context window and is aimed at researchers and developers working on math tutoring, theorem proving, and quantitative reasoning tasks rather than general-purpose chat.
