---
title: 'Flan-T5'
name: 'Flan-T5'
slug: 'flan-t5'
subtitle: 'Google''s instruction-tuned, open-weight successor to T5'
description: 'Google''s instruction-tuned, open-weight successor to T5'
company: 'google'
model_type: 'Language'
logo_url: ''
product_url: 'https://huggingface.co/google/flan-t5-xxl'
price: 'Free'
rank: 4
release_date: '2022-10-20'
param_count: '11B'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, instruction-tuned, legacy]
---

Flan-T5 is Google's instruction-tuned version of T5, its earlier text-to-text transformer, released in October 2022. Rather than changing the base architecture, Google fine-tuned T5 on more than a thousand tasks phrased as instructions, spanning translation, summarization, reasoning, and classification across many languages. That fine-tuning made it far more usable out of the box than plain T5, which needed task-specific tuning to perform well. Google released the family in several sizes, from an 80 million parameter small version up to Flan-T5-XXL at 11 billion parameters, all under the Apache 2.0 license and freely downloadable on Hugging Face. Its 512-token context window is short by current standards, which limits it to shorter documents and prompts. It remains a common baseline for research on instruction tuning and a lightweight option for teams that want an open, self-hosted model for straightforward NLP tasks without the compute cost of a larger decoder-only LLM.
