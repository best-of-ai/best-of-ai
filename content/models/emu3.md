---
title: 'Emu3'
name: 'Emu3'
slug: 'emu3'
subtitle: 'BAAI''s next-token-prediction model unifying text, image, and video generation and understanding'
description: 'BAAI''s next-token-prediction model unifying text, image, and video generation and understanding'
company: 'baai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://baai-agents.github.io/Emu3/'
price: 'Free'
rank: 5
release_date: '2024-09-27'
param_count: '8B'
modality: [text, image, video]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, research]
extra_model_types: ['Image Generation']
---

Emu3 is an open-weight multimodal model from the Beijing Academy of Artificial Intelligence, released in September 2024, built around a single idea: treat text, images, and video all as sequences of discrete tokens and train one transformer to predict the next token across all three, with no separate diffusion or CLIP-style component. BAAI released it as an 8B-parameter model in Chat and Gen variants, one tuned for vision-language understanding and one for generation. Despite the simplified single-objective design, BAAI reported that Emu3 outperformed established task-specific open models of the time, including SDXL for image generation and LLaVA-1.6 for vision-language understanding. The project is a predecessor to BAAI's larger Emu3.5 model, released in late 2025, which scales the same next-token-prediction approach up to 34 billion parameters.
