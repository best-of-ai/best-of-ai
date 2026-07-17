---
title: 'Llama 3.2'
name: 'Llama 3.2'
slug: 'llama-3-2'
subtitle: 'Meta''s first Llama generation with vision-capable and on-device tiers'
description: 'Meta''s first Llama generation with vision-capable and on-device tiers'
company: 'meta-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 6
release_date: '2024-09-25'
param_count: '90B'
context_window_tokens: 128000
modality: [text, image]
open_weight: true
license: 'Llama 3.2 Community License'
api_available: true
mmlu_score: 86.0
lmarena_score: 1250
access_methods: [Self-hosted, API]
platforms: ['Hugging Face', 'Ollama']
date: '2026-07-16'
tags: [llm, open-weight, multimodal, self-hosted]
---

Llama 3.2 is the Meta release from September 2024 that first brought vision into the Llama line, alongside a set of small text-only models built for phones and edge devices. The flagship 90B vision variant pairs a Llama 3.1 text backbone with an image encoder trained on roughly six billion image-text pairs, so it can read charts, caption photos, and answer questions about an image alongside plain text prompts. Meta also shipped lightweight 1B and 3B models in the same family, aimed at running locally on mobile hardware rather than in a data center. On reasoning benchmarks the 90B model performs close to Llama 3.1 70B while adding multimodal input, and it is distributed under the Llama 3.2 Community License with weights on Hugging Face.
