---
title: 'InternVL2'
name: 'InternVL2'
slug: 'internvl2'
subtitle: 'Shanghai AI Lab''s open vision-language model family, competitive with proprietary multimodal models'
description: 'Shanghai AI Lab''s open vision-language model family, competitive with proprietary multimodal models'
company: 'shanghai-ai-lab'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://github.com/OpenGVLab/InternVL'
price: 'Free'
rank: 6
release_date: '2024-07-04'
param_count: '76B (flagship; family spans 1B-108B)'
context_window_tokens: 8192
modality: [text, image, video]
open_weight: true
license: 'MIT'
api_available: true
access_methods: [Self-hosted, API]
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, vision]
---

InternVL2 is a family of open vision-language models from Shanghai AI Laboratory's OpenGVLab, released July 4, 2024, spanning sizes from 1B up to a 108B (76B InternViT + Llama 3 70B) flagship configuration. The models pair the InternViT vision encoder with a language model backbone, and the largest configuration, InternVL2-Llama3-76B, scored 62.0% on the MMMU benchmark, matching GPT-4o at the time and topping other open multimodal models on document and chart understanding tasks like DocVQA and ChartQA. Beyond static images, InternVL2 can process video by sampling frames and reasoning across them, and it supports multi-image inputs for document and comparison tasks. It was released under the MIT license with weights on Hugging Face, and at the time it was one of the strongest open alternatives to closed systems like GPT-4o and Gemini. Shanghai AI Lab followed it up with InternVL2.5 in December 2024, which pushed the largest model past 70% on MMMU.
