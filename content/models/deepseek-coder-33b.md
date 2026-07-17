---
title: 'DeepSeek-Coder-33B'
name: 'DeepSeek-Coder-33B'
slug: 'deepseek-coder-33b'
subtitle: 'DeepSeek''s earlier flagship code model, preceding DeepSeek-Coder-V2'
description: 'DeepSeek''s earlier flagship code model, preceding DeepSeek-Coder-V2'
company: 'deepseek'
model_type: 'Code'
logo_url: ''
product_url: 'https://github.com/deepseek-ai/DeepSeek-Coder'
price: 'Free'
rank: 6
release_date: '2023-11-02'
param_count: '33B'
context_window_tokens: 16384
modality: [text, code]
open_weight: true
license: 'DeepSeek License'
api_available: true
humaneval_score: 79.3
access_methods: [Self-hosted, API]
platforms: ['Hugging Face', 'DeepSeek API']
date: '2026-07-16'
tags: [code, open-weight, api, legacy]
---

DeepSeek-Coder-33B is a code-focused language model that DeepSeek released in November 2023, before the company became widely known for its later reasoning models. It was trained from scratch on 2 trillion tokens split mostly between code and natural language, with a 16,000-token context window and project-level training that lets it reason across multiple files rather than isolated snippets. The instruction-tuned version scored 79.3% pass@1 on HumanEval at release, putting it ahead of most open code models of the time and within striking distance of GPT-3.5 on coding benchmarks. It supports fill-in-the-middle completion for use in code editors and covers a wide range of programming languages. DeepSeek has since superseded it with DeepSeek-Coder-V2, a larger mixture-of-experts model with a longer context window, but the 33B model is still available on Hugging Face for self-hosting.
