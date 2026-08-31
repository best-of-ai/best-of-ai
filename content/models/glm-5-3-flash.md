---
title: 'GLM-5.3-Flash'
name: 'GLM-5.3-Flash'
slug: 'glm-5-3-flash'
subtitle: 'Zhipu''s first natively multimodal GLM-5 model, revealed after going viral under the name "Ox Alpha"'
description: 'Zhipu''s first natively multimodal GLM-5 model, revealed after going viral under the name "Ox Alpha"'
company: 'zhipu-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.zhipuai.cn/'
price: 'Paid'
rank: 7
release_date: '2026-08-26'
param_count: '320B (MoE, 18B active)'
context_window_tokens: 1000000
modality: [text, image, code]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 0.15
output_price_usd_per_m: 0.5
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: false
platforms: ['Hugging Face', 'API']
date: '2026-08-31'
tags: [llm, multimodal, coding, agentic, mixture-of-experts]
extra_model_types: ['Code']
---

Zhipu AI officially revealed GLM-5.3-Flash on August 26, 2026, confirming it as the model previously seeded anonymously on testing platforms under the name "Ox Alpha," which had drawn over 50 trillion tokens of traffic in five days before anyone knew who built it. It's a 320-billion-parameter mixture-of-experts model with 18 billion active parameters per token, the first natively multimodal release in the GLM-5 line, combining a hybrid sparse-and-linear attention design with a 1-million-token context window. Zhipu pretrained it on a 30-trillion-token multimodal corpus and says it matches Nvidia GPU-based models on efficiency and token cost while running on domestic Chinese chips.

Pricing lands far below Zhipu's own GLM-5.3: $0.15 per million input tokens and $0.50 per million output tokens at list price, with a launch promotion cutting that roughly in half through early September. That works out to about a tenth of GLM-5.3's published rate, positioning GLM-5.3-Flash as a cheaper, faster option for multimodal and agentic workloads rather than a replacement for Zhipu's flagship coding model.
