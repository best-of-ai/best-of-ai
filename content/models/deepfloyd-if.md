---
title: 'DeepFloyd IF'
name: 'DeepFloyd IF'
slug: 'deepfloyd-if'
subtitle: 'A pixel-space (non-latent) text-to-image model developed by the Stability-backed DeepFloyd lab'
description: 'A pixel-space (non-latent) text-to-image model developed by the Stability-backed DeepFloyd lab'
company: 'stability-ai'
model_type: 'Image Generation'
logo_url: ''
product_url: 'https://stability.ai/news/deepfloyd-if-text-to-image-model'
price: 'Free'
rank: 5
release_date: '2023-04-28'
param_count: '4.3B'
modality: [text, image]
open_weight: true
license: 'Stability Community License'
api_available: false
access_methods: [Self-hosted]
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [image-generation, open-weight, legacy]
---

DeepFloyd IF is a text-to-image model released in April 2023 by DeepFloyd, a research lab backed by Stability AI. It takes a different approach from Stable Diffusion's latent-space diffusion: it operates directly in pixel space across a cascade of three modules, first generating a low-resolution 64x64 image and then upsampling it in stages to 1024x1024, which gives it a strong reputation for rendering legible text inside images, a task that latent diffusion models of that era often botched. DeepFloyd trained three sizes of the base module, the largest with 4.3 billion parameters, and the full pipeline was released as a non-commercial research preview under a Stability Community License rather than a fully open license. It never became a mainstream product the way Stable Diffusion did, but its text-rendering results influenced later commercial models that improved on the same weakness.
