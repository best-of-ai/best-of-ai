---
title: 'Stable Diffusion 4'
name: 'Stable Diffusion 4'
slug: 'stable-diffusion-4'
subtitle: 'Stability AI''s next open-weight text-to-image diffusion model'
description: 'Stability AI''s next open-weight text-to-image diffusion model'
company: 'stability-ai'
model_type: 'Image Generation'
logo_url: ''
product_url: 'https://stability.ai/'
price: 'Free'
rank: 7
release_date: '2026-07-15'
param_count: '12B'
modality: [text, image]
open_weight: true
license: 'Stability AI Community License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Stability API']
date: '2026-07-19'
tags: [image-generation, open-weight, text-to-image, diffusion, self-hosted]
---

Stable Diffusion 4 is Stability AI's first major update to the line since SD 3.5 in late 2024, growing the model to 12 billion parameters and sharpening prompt adherence and text rendering inside images, both long-standing weak points against closed competitors like Midjourney and Imagen. It's released under the same Stability AI Community License as SD 3.5, free for individuals and small companies, with paid licensing required above a revenue threshold.

The weights are on Hugging Face as usual, quantized versions run on a single consumer GPU, and Stability also offers hosted inference through its own API for teams that don't want to manage the infrastructure. SD4 arrives at a point where Stability faces real pressure from FLUX and other open image models that have chipped away at its lead, and the release leans heavily on the community fine-tuning ecosystem (LoRAs, ControlNets, custom checkpoints) that's kept Stable Diffusion the default choice for open-weight image generation despite the fiercer competition.
