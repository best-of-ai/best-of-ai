---
title: 'GLM-4.6'
name: 'GLM-4.6'
slug: 'glm-4-6'
subtitle: 'Zhipu''s value-tier open-weight model for day-to-day coding'
description: 'Zhipu''s value-tier open-weight model for day-to-day coding'
company: 'zhipu-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://www.zhipuai.cn/'
price: 'Free'
rank: 7
release_date: '2025-09-30'
param_count: '355B (MoE, ~32B active)'
context_window_tokens: 200000
modality: [text, image, code]
open_weight: true
license: 'Apache 2.0'
input_price_usd_per_m: 0.43
output_price_usd_per_m: 1.75
api_available: true
humaneval_score: 85.0
lmarena_score: 1320
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, code, self-hosted]
---

GLM-4.6 is Zhipu's (Z.ai's) value-tier open-weight model, released on September 30, 2025 as an upgrade to GLM-4.5. It uses a mixture-of-experts design with roughly 355 billion total parameters and about 32 billion active per token, and its context window grew from 128,000 to 200,000 tokens to support longer agentic sessions. The model handles text, images, and code, and Zhipu tuned it specifically for tool use inside coding assistants like Claude Code, Cline, and Roo Code.

On coding benchmarks the model performs near the top of the open-weight field, leading LiveCodeBench v6 and scoring competitively against DeepSeek-V3.1-Terminus and Claude Sonnet 4 on several agentic tasks. Its main selling point is price: at well under a dollar per million input tokens, it undercuts most proprietary flagship models by a wide margin while remaining usable for real coding work, which is why it shows up often in self-hosted and API-based developer tooling.
