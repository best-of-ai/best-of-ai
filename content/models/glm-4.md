---
title: 'GLM-4'
name: 'GLM-4'
slug: 'glm-4'
subtitle: 'Zhipu''s 2024 general-purpose open-weight model'
description: 'Zhipu''s 2024 general-purpose open-weight model'
company: 'zhipu-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.zhipuai.cn/'
price: 'Free'
rank: 5
release_date: '2024-06-05'
param_count: '9B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
mmlu_score: 72.4
humaneval_score: 71.8
access_methods: [Self-hosted]
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted]
---

GLM-4 is Zhipu AI's open-weight release from June 2024, distributed as GLM-4-9B with base, chat, and long-context variants. At 9 billion parameters it's small enough to run on a single high-end GPU, yet Zhipu reported it beating Meta's Llama 3 8B across semantic, math, reasoning, and code evaluations. The chat variant also supports web browsing, code execution, and custom tool calls through function calling, plus a context window that stretches to 128,000 tokens.

The model added support for 26 languages beyond Chinese and English, including Japanese, Korean, and German, which broadened its use outside Zhipu's home market. Released under Apache 2.0, GLM-4 became one of the more widely adopted small open-weight models on Hugging Face and set the base architecture that Zhipu later scaled up into GLM-4-Plus, GLM-4.5, and GLM-4.6.
