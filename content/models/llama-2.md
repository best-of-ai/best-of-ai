---
title: 'Llama 2'
name: 'Llama 2'
slug: 'llama-2'
subtitle: 'Meta''s 2023 open-weight release that jump-started the open LLM ecosystem'
description: 'Meta''s 2023 open-weight release that jump-started the open LLM ecosystem'
company: 'meta-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 6
release_date: '2023-07-18'
param_count: '70B'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'Llama 2 Community License'
api_available: true
mmlu_score: 68.9
humaneval_score: 29.9
access_methods: [Self-hosted]
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted, legacy]
---

Llama 2 is Meta's second-generation open-weight language model line, released July 18, 2023 in 7B, 13B, and 70B sizes, along with chat-tuned versions of each. It was trained on 2 trillion tokens and supports a 4,096-token context window, modest by later standards but competitive when it launched. The 70B model scored 68.9 on MMLU, close to GPT-3.5, though it lagged well behind on code generation, reaching only 29.9 on HumanEval against GPT-3.5's 48.1. What mattered more than the raw scores was the license: Meta allowed commercial use for most companies, which made Llama 2 the first genuinely open-weight model good enough to build products on, and it kicked off the wave of fine-tunes, quantized variants, and derivative models that now populate Hugging Face. The weights are still freely downloadable years later, even though Meta has since released Llama 3 and Llama 4.
