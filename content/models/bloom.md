---
title: 'BLOOM'
name: 'BLOOM'
slug: 'bloom'
subtitle: 'The open, multilingual model built by the BigScience collaboration'
description: 'The open, multilingual model built by the BigScience collaboration'
company: 'hugging-face'
model_type: 'Language'
logo_url: ''
product_url: 'https://huggingface.co/bigscience/bloom'
price: 'Free'
rank: 4
release_date: '2022-07-06'
param_count: '176B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'RAIL License'
api_available: false
access_methods: [Self-hosted]
runs_at_home: false
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, multilingual, legacy]
---

BLOOM is a 176 billion parameter language model built by BigScience, a year-long collaboration of over a thousand researchers coordinated through Hugging Face with compute donated by the French government's Jean Zay supercomputer. It launched in July 2022 as an answer to closed models like GPT-3, trained on the ROOTS corpus covering 46 natural languages and 13 programming languages, with a deliberate emphasis on underrepresented languages that most large labs ignored at the time. The project published its training data, code, and a full technical report alongside the weights, which was rare for a model at that scale.

BLOOM is released under the RAIL License, a permissive-but-restricted license that allows commercial use while banning specific harmful applications, an approach BigScience helped popularize. Its 2,048-token context window and dense architecture look dated next to current frontier models, and it has largely been superseded by more efficient open-weight families such as Llama and Mistral, but it remains a reference point in discussions of multilingual coverage and open, community-governed model development.
