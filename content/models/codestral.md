---
title: 'Codestral'
name: 'Codestral'
slug: 'codestral'
subtitle: 'Mistral''s code-generation and completion model'
description: 'Mistral''s code-generation and completion model'
company: 'mistral-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://mistral.ai/news/codestral/'
price: 'Free'
rank: 6
release_date: '2024-05-29'
param_count: '22B'
context_window_tokens: 256000
modality: [text, code]
open_weight: true
license: 'Apache 2.0'
input_price_usd_per_m: 0.3
output_price_usd_per_m: 0.9
api_available: true
humaneval_score: 81.1
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, code, open-weight, api]
---

Codestral is Mistral AI's dedicated code generation model, first released in May 2024 with 22 billion parameters. It's built for fill-in-the-middle completion and multi-language code generation, and it launched with an 81.1 percent pass@1 score on HumanEval, ahead of larger code models like Code Llama 70B and DeepSeek Coder 33B at the time. The original release used a 32,000-token context window and shipped under the Mistral AI Non-Production License, which limited free use to research and testing and required a separate commercial license for production deployment.

Mistral later extended Codestral's context window to 256,000 tokens and, in April 2026, relicensed the model under Apache 2.0, removing the earlier commercial-use restriction and making it freely usable in IDEs, coding assistants, and CI pipelines. Codestral is available both as downloadable weights on Hugging Face and through Mistral's API, currently priced at $0.30 per million input tokens and $0.90 per million output tokens. It competes directly with other mid-size open code models such as Codestral Mamba and Code Llama, and its move to a permissive license was widely seen as a significant shift in the open-source coding model space.
