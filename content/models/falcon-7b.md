---
title: 'Falcon 7B'
name: 'Falcon 7B'
slug: 'falcon-7b'
subtitle: 'TII''s compact Falcon tier that helped popularize the original Falcon release'
description: 'TII''s compact Falcon tier that helped popularize the original Falcon release'
company: 'technology-innovation-institute'
model_type: 'Language'
logo_url: ''
product_url: 'https://falconllm.tii.ae/'
price: 'Free'
rank: 5
release_date: '2023-05-25'
param_count: '7B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, small-model, legacy]
---

Falcon 7B is the smaller sibling in TII's original Falcon release, trained on the same RefinedWeb dataset as Falcon 40B but sized for cheaper deployment on a single GPU. TII trained it over about two weeks in early 2023 and released it under the permissive Apache 2.0 license, which let developers use, modify, and deploy it commercially without royalties. That licensing move was notable at the time, since many comparable open models carried research-only restrictions. Falcon 7B shares the 40B model's decoder-only transformer architecture with multiquery attention, but with a 2,048 token context window and lower compute requirements, making it a common choice for fine-tuning experiments and on-device use cases in 2023 and early 2024. TII has since moved on to the Falcon 3 and Falcon Mamba families, leaving Falcon 7B as a legacy model still widely mirrored on Hugging Face.
