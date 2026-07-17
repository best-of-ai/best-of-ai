---
title: 'Code Llama'
name: 'Code Llama'
slug: 'code-llama'
subtitle: 'Meta''s open-weight code-specialized Llama variant'
description: 'Meta''s open-weight code-specialized Llama variant'
company: 'meta-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://ai.meta.com/blog/code-llama-large-language-model-coding/'
price: 'Free'
rank: 6
release_date: '2023-08-24'
param_count: '34B'
context_window_tokens: 100000
modality: [text, code]
open_weight: true
license: 'Llama 2 Community License'
api_available: true
humaneval_score: 53.7
access_methods: [Self-hosted]
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, code, self-hosted]
---

Code Llama is Meta's code-focused version of Llama 2, released in August 2023. It was trained further on code-heavy data on top of the base Llama 2 weights and shipped in three foundation sizes (7B, 13B, and 34B parameters), each with a base version, a Python-specialized version, and an instruction-tuned version for chat-style coding help. Meta later added a 70B variant. A key change from the base Llama 2 model was extending the context window from 4,096 tokens up to 100,000 tokens, achieved by adjusting the RoPE positional embeddings, which made the model far more useful for reading and editing long files or entire codebases in one pass.

On the HumanEval benchmark, the 34B model scored 53.7 percent pass@1, putting it roughly on par with GPT-3.5 at the time of release, though well behind GPT-4. Code Llama is released under the same Llama 2 Community License as its parent model, permitting commercial use for most companies, and its weights are freely downloadable from Hugging Face. It was one of the first widely adopted open-weight coding models and set a template that later open code models, including Codestral and DeepSeek Coder, would compete against.
