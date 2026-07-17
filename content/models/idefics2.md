---
title: 'IDEFICS2'
name: 'IDEFICS2'
slug: 'idefics2'
subtitle: 'Hugging Face''s open vision-language model built for document and chart QA'
description: 'Hugging Face''s open vision-language model built for document and chart QA'
company: 'hugging-face'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://huggingface.co/blog/idefics2'
price: 'Free'
rank: 5
release_date: '2024-04-15'
param_count: '8B'
context_window_tokens: 32768
modality: [text, image]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, vision]
---

IDEFICS2 is Hugging Face's open vision-language model, released in April 2024 as a follow-up to its earlier IDEFICS model. It has 8 billion parameters, built by combining Mistral-7B as the language backbone with a SigLIP vision encoder, and it processes images at their native resolution and aspect ratio instead of forcing everything into a fixed square crop. That choice, plus training on a more efficient mix of image tokens, gives it a strong edge on document understanding, chart reading, and OCR-heavy tasks compared to models several times its size, including LLaVA-NeXT-34B. Hugging Face released the weights under Apache 2.0, making it fully open for commercial use and fine-tuning without licensing restrictions. It's meant to run self-hosted rather than through a hosted API, fitting Hugging Face's broader push to keep strong open vision-language baselines available to researchers and developers.
