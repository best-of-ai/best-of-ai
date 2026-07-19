---
title: 'CLIP'
name: 'CLIP'
slug: 'clip'
subtitle: 'OpenAI''s foundational image-text contrastive model that underlies much of modern multimodal AI'
description: 'OpenAI''s foundational image-text contrastive model that underlies much of modern multimodal AI'
company: 'openai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://openai.com/index/clip/'
price: 'Free'
rank: 8
release_date: '2021-01-05'
param_count: '428M'
modality: [text, image]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'GitHub']
date: '2026-07-16'
tags: [multimodal, open-weight, vision, legacy, foundation-model]
---

CLIP (Contrastive Language-Image Pre-training) is a model OpenAI released in January 2021 that learns to match images with text descriptions. It was trained on 400 million image-text pairs scraped from the internet, using a contrastive objective that pulls matching image and text embeddings together while pushing mismatched pairs apart. The largest released variant, built on a ViT-L/14 vision transformer paired with a 63M-parameter text transformer, totals roughly 428 million parameters. Instead of being trained for one narrow task, CLIP learns a general-purpose joint embedding space for images and text, which lets it perform zero-shot image classification by comparing an image against a set of text labels with no task-specific fine-tuning.

CLIP's real impact came after release, not from headline benchmark numbers. Its image and text encoders became the backbone for a wave of later systems, including DALL-E 2's image generation pipeline, Stable Diffusion's text conditioning, and countless image search and retrieval tools. Meta, Salesforce, and other labs have released their own CLIP variants and fine-tunes, but OpenAI's original weights, published under an MIT license on GitHub and Hugging Face, remain a common default starting point for multimodal projects even years after release.
