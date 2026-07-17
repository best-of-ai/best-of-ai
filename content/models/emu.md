---
title: 'Emu'
name: 'Emu'
slug: 'emu'
subtitle: 'Meta''s photorealistic text-to-image model behind Meta AI''s image features'
description: 'Meta''s photorealistic text-to-image model behind Meta AI''s image features'
company: 'meta-ai'
model_type: 'Image Generation'
logo_url: ''
product_url: 'https://ai.meta.com/blog/emu-text-to-video-generation-image-editing-research/'
price: 'Paid'
rank: 6
release_date: '2023-09-27'
param_count: 'Undisclosed'
modality: [text, image]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Chat UI]
platforms: ['Meta AI', 'Instagram', 'WhatsApp']
date: '2026-07-16'
tags: [image-generation, legacy]
---

Emu is Meta's text-to-image model, described in a September 2023 paper as a latent diffusion system pretrained on around 1.1 billion image-text pairs and then fine-tuned on a small set of manually selected high-quality images, a technique Meta called quality-tuning. The approach let a relatively standard diffusion architecture produce more consistently photorealistic and aesthetically pleasing output without changing the underlying model much, and Meta used it as the image generator behind Meta AI's sticker and image creation features in Facebook Messenger, Instagram, and WhatsApp. Emu also became the base model for follow-on Meta research projects, including Emu Video and Emu Edit. It isn't offered as a standalone API or product outside Meta's own apps.
