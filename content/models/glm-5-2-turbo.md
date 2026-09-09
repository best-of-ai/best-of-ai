---
title: 'GLM-5.2 Turbo'
name: 'GLM-5.2 Turbo'
slug: 'glm-5-2-turbo'
subtitle: 'Zhipu''s faster GLM-5.2 variant tuned for long-running agent workflows'
description: 'Zhipu''s faster GLM-5.2 variant tuned for long-running agent workflows'
company: 'zhipu-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.zhipuai.cn/'
price: 'Paid'
rank: 6
release_date: '2026-08-17'
param_count: 'Undisclosed'
context_window_tokens: 202752
input_price_usd_per_m: 1.2
output_price_usd_per_m: 4
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['API']
date: '2026-08-31'
tags: [llm, agentic, api, tool-use]
extra_model_types: ['Reasoning']
---

Zhipu AI released GLM-5.2 Turbo on August 17, 2026 as a faster sibling to GLM-5.2, built specifically for agent-driven workloads rather than general chat or one-off queries. It carries a smaller context window than the base model, about 200,000 tokens versus GLM-5.2's full 1-million-token capacity, in exchange for lower latency on the long execution chains typical of coding agents and automation tools. Zhipu says it improved complex instruction decomposition and tool use, along with stability across scheduled and persistent tasks that run for extended periods without human supervision.

Pricing sits above the base GLM-5.2 rate, at $1.20 per million input tokens and $4 per million output tokens, reflecting the tradeoff toward speed over raw context length. It's aimed at the same agent-framework crowd already using GLM-5.2 and GLM-5.3, giving developers a cheaper-context, faster-response option when a task doesn't need the full million-token window.
