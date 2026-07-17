---
title: 'DBRX'
name: 'DBRX'
slug: 'dbrx'
subtitle: 'Databricks'' open-weight mixture-of-experts model'
description: 'Databricks'' open-weight mixture-of-experts model'
company: 'databricks'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm'
price: 'Free'
rank: 5
release_date: '2024-03-27'
param_count: '132B (36B active)'
context_window_tokens: 32000
modality: [text]
open_weight: true
license: 'Databricks Open Model License'
api_available: true
mmlu_score: 73.7
humaneval_score: 70.1
access_methods: [Self-hosted, API]
platforms: ['Hugging Face', 'Databricks']
date: '2026-07-16'
tags: [llm, open-weight, mixture-of-experts, self-hosted]
---

DBRX is Databricks' open-weight large language model, released in March 2024 as the base model behind the instruction-tuned DBRX Instruct. It is a fine-grained mixture-of-experts model with 132 billion total parameters and 36 billion active parameters per token, trained from scratch on 12 trillion tokens of text and code using Databricks' own Mosaic AI training stack. At release, Databricks reported it outperforming other open models of the time, including Llama 2 70B and Mixtral, on benchmarks such as MMLU and HumanEval, and it was pitched as evidence that an enterprise-focused company could train a competitive foundation model without relying on a big-lab research budget. It has a 32,000-token context window and is released under the Databricks Open Model License, with weights available on Hugging Face for self-hosting or through Databricks' own serving infrastructure.
