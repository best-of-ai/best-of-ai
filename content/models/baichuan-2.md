---
title: 'Baichuan 2'
name: 'Baichuan 2'
slug: 'baichuan-2'
subtitle: 'Baichuan''s open-weight bilingual foundation model'
description: 'Baichuan''s open-weight bilingual foundation model'
company: 'baichuan-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.baichuan-ai.com/'
price: 'Free'
rank: 3
release_date: '2023-09-06'
param_count: '13B'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'Baichuan 2 Community License'
api_available: false
mmlu_score: 59.5
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted, legacy]
---

Baichuan 2 is the second generation of open-weight language models from Baichuan Intelligent Technology, released in September 2023. It came in 7B and 13B parameter sizes, each with base and chat variants, and was trained on 2.6 trillion bilingual Chinese-English tokens, roughly double what the original Baichuan models saw. Baichuan reported that the 7B model gained close to 30% on MMLU over its Baichuan 1 predecessor of the same size, and the family did well on Chinese-language benchmarks like C-Eval and CMMLU relative to other open models available at the time. The weights are distributed under Apache 2.0 for the code plus a separate community license for the model itself, which allows free commercial use as long as the deploying company has under 1 million daily active users and isn't itself a cloud or software service reselling the model. It has since been superseded by Baichuan 3 and Baichuan 4, which moved to closed, API-only access.
