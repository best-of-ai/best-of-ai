---
title: 'Amazon Nova Lite'
name: 'Amazon Nova Lite'
slug: 'amazon-nova-lite'
subtitle: 'Amazon''s low-cost multimodal Bedrock model tier'
description: 'Amazon''s low-cost multimodal Bedrock model tier'
company: 'amazon'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://aws.amazon.com/ai/generative-ai/nova/'
price: 'Paid'
rank: 4
release_date: '2024-12-03'
param_count: 'Undisclosed'
context_window_tokens: 300000
modality: [text, image, video]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.06
output_price_usd_per_m: 0.24
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['AWS Bedrock']
date: '2026-07-16'
tags: [llm, multimodal, low-latency, api]
---

Amazon Nova Lite is a multimodal model in Amazon's Nova family, announced in December 2024 at AWS re:Invent and available through Amazon Bedrock. It accepts text, image, and video input and returns text output, with a 300,000-token context window, and is priced at $0.06 per million input tokens and $0.24 per million output tokens. Amazon built it as the mid-tier option between the text-only Nova Micro and the more capable Nova Pro, aimed at applications that need to handle images or video but still want fast response times and low cost.

Nova Lite competes with similarly sized multimodal models from OpenAI and Google, and Amazon has marketed the Nova line mainly on price-to-performance rather than topping benchmark leaderboards. It supports fine-tuning and distillation on Bedrock, so customers can adapt it to specific tasks like document understanding or visual question answering without paying for a larger model at inference time.
