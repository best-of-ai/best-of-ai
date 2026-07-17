---
title: 'CLIP (LAION variant)'
name: 'CLIP (LAION variant)'
slug: 'clip-laion-variant'
subtitle: 'LAION''s open-weight retrained CLIP vision-language embedding model'
description: 'LAION''s open-weight retrained CLIP vision-language embedding model'
company: 'laion'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://laion.ai/'
price: 'Free'
rank: 4
release_date: '2022-09-15'
param_count: '428M'
modality: [text, image]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [embedding, open-weight, vision, self-hosted]
---

This CLIP variant is an open-weight retraining of OpenAI's original CLIP architecture, produced by LAION and distributed through the open_clip project rather than by OpenAI itself. It uses the ViT-L/14 vision transformer backbone, has about 428 million parameters, and was trained on LAION-2B, the English-language 2 billion image-text pair subset of the larger LAION-5B dataset, using 384 A100 GPUs on the JUWELS supercomputer. Like the original CLIP, it maps images and text into a shared embedding space so you can do zero-shot image classification, image-text retrieval, and similarity search without any task-specific fine-tuning, and it reaches about 75.3 percent zero-shot accuracy on ImageNet-1k. Because the weights are released under an open license and hosted on Hugging Face, it has become a common drop-in replacement for OpenAI's closed CLIP checkpoints in open-source image search, captioning, and generative art pipelines, including as a text encoder inside several Stable Diffusion variants.
