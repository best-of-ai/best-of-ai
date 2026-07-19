---
title: 'BLIP'
name: 'BLIP'
slug: 'blip'
subtitle: 'Salesforce''s vision-language pretraining model for captioning and retrieval'
description: 'Salesforce''s vision-language pretraining model for captioning and retrieval'
company: 'salesforce'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://github.com/salesforce/BLIP'
price: 'Free'
rank: 6
release_date: '2022-01-28'
param_count: '223M'
modality: [text, image]
open_weight: true
license: 'BSD-3-Clause'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, vision, legacy]
---

BLIP (Bootstrapping Language-Image Pre-training) is a vision-language model that Salesforce Research introduced in early 2022. It handles both understanding tasks, like image captioning and visual question answering, and retrieval tasks, like matching images to text. The model was trained with a bootstrapping method that cleans up noisy web-scraped captions by generating synthetic ones and filtering out the bad matches, which let it reach strong results without relying purely on massive uncurated datasets. At around 223 million parameters, BLIP is small next to later multimodal systems, but it was influential in showing that caption quality matters as much as caption quantity for pretraining.

Salesforce released BLIP's weights and code openly under a BSD license, and it became a common baseline in vision-language research and a building block in other projects, including early versions of tools like Stable Diffusion's interrogator features. Its successor, BLIP-2, improved efficiency by pairing frozen image encoders with frozen language models through a lightweight bridging module, but the original BLIP is still used in academic work and self-hosted pipelines where a compact, well-documented captioning model is enough.
