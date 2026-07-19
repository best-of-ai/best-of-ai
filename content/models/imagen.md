---
title: 'Imagen'
name: 'Imagen'
slug: 'imagen'
subtitle: 'Google''s original text-to-image diffusion model, introduced alongside Parti as a research preview'
description: 'Google''s original text-to-image diffusion model, introduced alongside Parti as a research preview'
company: 'google-deepmind'
model_type: 'Image Generation'
logo_url: ''
product_url: 'https://imagen.research.google/'
price: 'Paid'
rank: 6
release_date: '2022-05-24'
param_count: 'Undisclosed'
modality: [text, image]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [image-generation, research, legacy]
---

Imagen is Google Research's original text-to-image diffusion model, described in a paper titled "Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding" and posted to arXiv in May 2022. It pairs a large frozen language model, T5, with a cascade of diffusion models: a base model that generates a small 64x64 image, followed by two super-resolution stages that upsample it to 256x256 and then 1024x1024. The paper's central finding was that scaling up the text encoder improved image quality and prompt alignment more than scaling up the image diffusion network itself, a result that influenced later text-to-image systems across the industry. Imagen reported a state-of-the-art FID score of 7.27 on the COCO benchmark despite never training on COCO data.

Google never released Imagen as a public product. It stayed a research preview, shown off alongside the autoregressive Parti model and compared against OpenAI's DALL-E 2, which had launched a few months earlier. The name and lineage carried forward into Google's later commercial image models, Imagen 2, 3, and 4, which built on the same diffusion approach but added production infrastructure, safety filtering, and API access that the original research model lacked.
