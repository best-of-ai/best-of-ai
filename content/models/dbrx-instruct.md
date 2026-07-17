---
title: 'DBRX Instruct'
name: 'DBRX Instruct'
slug: 'dbrx-instruct'
subtitle: 'Instruction-tuned variant of Databricks'' open-weight DBRX model'
description: 'Instruction-tuned variant of Databricks'' open-weight DBRX model'
company: 'databricks'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm'
price: 'Free'
rank: 4
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
tags: [llm, open-weight, instruction-tuned, self-hosted]
---

DBRX Instruct is the fine-tuned, chat-ready version of Databricks' DBRX model, released in March 2024 alongside the DBRX base model. It uses a fine-grained mixture-of-experts architecture with 132 billion total parameters, of which only 36 billion are active for any given token, and it was trained on 12 trillion tokens of text and code. Databricks tuned it specifically for instruction following and multi-turn conversation, and at launch the company reported it beating GPT-3.5 on MMLU (73.7% versus 70.0%) and on HumanEval (70.1% versus 48.1%). It supports a 32,000-token context window and is distributed under the Databricks Open Model License, which permits commercial use with some restrictions for very large deployments. Organizations run it through Databricks' own platform or self-host the weights from Hugging Face.
