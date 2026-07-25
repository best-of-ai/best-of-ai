---
title: 'GLM-5'
name: 'GLM-5'
slug: 'glm-5'
subtitle: 'Zhipu''s frontier open-weight model, trained entirely on domestic Huawei hardware'
description: 'Zhipu''s frontier open-weight model, trained entirely on domestic Huawei hardware'
company: 'zhipu-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.zhipuai.cn/'
price: 'Free'
rank: 7
release_date: '2026-02-11'
param_count: '~744B (MoE, ~40B active)'
context_window_tokens: 203000
modality: [text, code]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 0.57
output_price_usd_per_m: 1.92
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-25'
tags: [llm, open-weight, coding, self-hosted]
extra_model_types: ['Code']
---

GLM-5 is Zhipu AI's frontier open-weight model, released February 11, 2026 as roughly a two-times scale-up from GLM-4.5, growing from 355 billion to about 744 billion total parameters while keeping a similar 40 billion active per token in its mixture-of-experts design. It ships with a 203,000 token context window, well short of the 1 million tokens its GLM-5.2 successor would add four months later, and Zhipu trained it entirely on Huawei Ascend chips using the MindSpore framework rather than Nvidia hardware. API pricing starts at $0.57 per million input tokens and $1.92 per million output tokens through Zhipu's own platform and the WaveSpeed API. It shipped under the MIT license, and coverage at the time framed it as the first frontier-class model from a Chinese lab built on fully domestic hardware.
