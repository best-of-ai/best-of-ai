---
title: 'Codex'
name: 'Codex'
slug: 'codex'
subtitle: 'OpenAI''s original code-completion model that powered early GitHub Copilot'
description: 'OpenAI''s original code-completion model that powered early GitHub Copilot'
company: 'openai'
model_type: 'Code'
logo_url: ''
product_url: 'https://openai.com/index/openai-codex/'
price: 'Paid'
rank: 6
release_date: '2021-08-10'
param_count: '12B'
context_window_tokens: 4096
modality: [text, code]
open_weight: false
license: 'Proprietary'
api_available: false
humaneval_score: 28.8
access_methods: [Research]
runs_at_home: false
platforms: ['API (deprecated)']
date: '2026-07-16'
tags: [code, legacy, foundation-model]
---

Codex is OpenAI's first dedicated code-generation model, announced in August 2021 as a GPT-3 descendant fine-tuned on billions of lines of public source code from GitHub. The largest published version had 12 billion parameters and a 4,096-token context window, and it solved 28.8% of problems on OpenAI's HumanEval benchmark on the first try, rising to 77.5% when allowed 100 sampled attempts per problem. Codex is what powered the original GitHub Copilot when Copilot launched in technical preview in 2021, marking one of the first large-scale deployments of an LLM as a coding assistant rather than a chat or completion demo. OpenAI made it available through a private beta API for a few years before retiring the standalone Codex API in March 2023, folding its capabilities into successor GPT-3.5 and GPT-4 family models. The name lives on today as the brand for OpenAI's newer agentic coding products, but the original Codex model itself is no longer accessible through the API.
