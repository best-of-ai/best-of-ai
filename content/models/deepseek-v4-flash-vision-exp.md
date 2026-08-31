---
title: 'DeepSeek-V4-Flash-Vision-Exp'
name: 'DeepSeek-V4-Flash-Vision-Exp'
slug: 'deepseek-v4-flash-vision-exp'
subtitle: 'DeepSeek''s experimental multimodal variant of V4-Flash for document and chart understanding'
description: 'DeepSeek''s experimental multimodal variant of V4-Flash for document and chart understanding'
company: 'deepseek'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://api-docs.deepseek.com/news/news260821/'
price: 'Paid'
rank: 6
release_date: '2026-08-21'
param_count: '284B (MoE, 13B active)'
context_window_tokens: 1048576
modality: [text, image]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.22
output_price_usd_per_m: 0.66
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['DeepSeek API']
date: '2026-08-31'
tags: [multimodal, vision, api, document-understanding, mixture-of-experts]
---

DeepSeek released DeepSeek-V4-Flash-Vision-Exp on August 21, 2026 as an experimental image-input variant of DeepSeek-V4-Flash, the sparse mixture-of-experts model with 284 billion total parameters and 13 billion active per token. It matches the text-only V4-Flash on agentic and reasoning tasks while adding image understanding, aimed at document and chart reading, visual question answering, and agent workflows that mix text and images. Images can be passed as inline base64 data, URLs, or through DeepSeek's Files API, and the model tokenizes each image at 384 tokens, well below what GPT and Claude models typically use per image.

On DeepSeek's internal multimodal agent benchmarks, the company reports V4-Flash-Vision-Exp closing much of the gap to Anthropic's Opus-4.8 on tasks that require reasoning over visual input, a notable jump from the text-only V4-Flash. It's priced at $0.22 per million input tokens and $0.66 per million output tokens, with a separate lower rate for cached input, and remains available only through the DeepSeek API while the company gathers feedback ahead of a non-experimental release.
