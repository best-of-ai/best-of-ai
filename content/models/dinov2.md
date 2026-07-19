---
title: 'DINOv2'
name: 'DINOv2'
slug: 'dinov2'
subtitle: 'Meta''s self-supervised vision model producing general-purpose image features without labels'
description: 'Meta''s self-supervised vision model producing general-purpose image features without labels'
company: 'meta-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://ai.meta.com/blog/dino-v2-computer-vision-self-supervised-learning/'
price: 'Free'
rank: 6
release_date: '2023-04-17'
param_count: '1.1B'
modality: [image]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'GitHub']
date: '2026-07-16'
tags: [computer-vision, open-weight, self-supervised]
---

DINOv2 is a computer vision model that Meta AI released in April 2023, trained entirely without labels on a curated dataset of 142 million images called LVD-142M. Rather than learning to classify images into predefined categories, it learns general-purpose visual features through self-supervised distillation, and those features turn out to work well across a wide range of downstream tasks, image classification, depth estimation, segmentation, and retrieval, often without any fine-tuning at all. The largest released model has 1.1 billion parameters.

Because its features transfer so well out of the box, DINOv2 became a common backbone for other computer vision systems, including in fields like medical imaging where labeled data is scarce. Meta released the code and model weights under the Apache 2.0 license, and later followed it with DINOv3, but DINOv2 remains widely used as a general-purpose visual feature extractor.
