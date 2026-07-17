---
title: 'Hunyuan DiT'
name: 'Hunyuan DiT'
slug: 'hunyuan-dit'
subtitle: 'Tencent''s open-weight diffusion transformer for Chinese and English text-to-image'
description: 'Tencent''s open-weight diffusion transformer for Chinese and English text-to-image'
company: 'tencent'
model_type: 'Image Generation'
logo_url: ''
product_url: 'https://github.com/Tencent/HunyuanDiT'
price: 'Free'
rank: 5
release_date: '2024-05-14'
param_count: '1.5B'
modality: [text, image]
open_weight: true
license: 'Tencent Hunyuan License'
api_available: true
access_methods: [Self-hosted, API]
platforms: ['Hugging Face', 'Tencent Cloud']
date: '2026-07-16'
tags: [image-generation, open-weight, api]
---

Hunyuan-DiT is Tencent's open-weight text-to-image model, built on a diffusion transformer architecture rather than the U-Net design most earlier diffusion models used. Tencent published it in May 2024, pairing a 1.5B-parameter denoising transformer with bilingual CLIP and multilingual T5 text encoders so it can follow prompts written in Chinese or English with similar fidelity. That bilingual focus is the model's main selling point: most open text-to-image models of the time handled Chinese prompts poorly, and Hunyuan-DiT was trained specifically to close that gap. It generates 1024x1024 images and includes a built-in multimodal chat component that lets users refine an image across several turns of dialogue instead of rewriting the whole prompt each time. Tencent released the weights on Hugging Face and GitHub under its Hunyuan license, and later shipped a 1.1 update that fixed oversaturation and watermark artifacts present in the original checkpoint.
