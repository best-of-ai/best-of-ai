---
title: 'DALL-E'
name: 'DALL-E'
slug: 'dall-e'
subtitle: 'OpenAI''s original 2021 text-to-image model'
description: 'OpenAI''s original 2021 text-to-image model'
company: 'openai'
model_type: 'Image Generation'
logo_url: ''
product_url: 'https://openai.com/index/dall-e/'
price: 'Paid'
rank: 5
release_date: '2021-01-05'
param_count: '12B'
modality: [text, image]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [image-generation, legacy]
---

DALL-E is OpenAI's original text-to-image model, introduced in January 2021 as a 12-billion-parameter variant of GPT-3 trained to generate images from text captions. It worked by treating image generation as a sequence prediction problem: a discrete variational autoencoder converted images into tokens, and an autoregressive transformer learned to predict those tokens from a text prompt, with a CLIP model used afterward to rank the resulting images. It was trained on around 250 million text-image pairs scraped from the internet and could produce plausible images for combinations of concepts it had never seen paired together, like an armchair shaped like an avocado. DALL-E was never released as a public product; OpenAI kept it as a research preview and later replaced it with the diffusion-based DALL-E 2, which produced sharper images at a fraction of the parameter count.
