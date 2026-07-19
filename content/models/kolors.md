---
title: 'Kolors'
name: 'Kolors'
slug: 'kolors'
subtitle: 'Kuaishou''s open-weight text-to-image model, strong on Chinese-language prompts'
description: 'Kuaishou''s open-weight text-to-image model, strong on Chinese-language prompts'
company: 'kuaishou'
model_type: 'Image Generation'
logo_url: ''
product_url: 'https://github.com/Kwai-Kolors/Kolors'
price: 'Free'
rank: 5
release_date: '2024-07-06'
param_count: '2.6B'
modality: [text, image]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Kuaishou API']
date: '2026-07-16'
tags: [image-generation, open-weight, api]
---

Kolors is Kuaishou's open-weight text-to-image model, released in July 2024. It is a latent diffusion model with about 2.6 billion parameters, built on a U-Net architecture, and it uses ChatGLM as its text encoder instead of a CLIP-style encoder, which gives it a notable edge at reading and rendering Chinese-language prompts and Chinese text within images. It generates at a native 1024x1024 resolution and supports multiple aspect ratios. Kuaishou trained it on billions of text-image pairs and released the weights on GitHub and Hugging Face, free for research use, with a separate registration process required for commercial deployment. Alongside models like Flux and Stable Diffusion 3, Kolors is one of the few widely-used open image models that handles non-Latin scripts well.
