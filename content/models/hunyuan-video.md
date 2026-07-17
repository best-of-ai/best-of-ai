---
title: 'Hunyuan Video'
name: 'Hunyuan Video'
slug: 'hunyuan-video'
subtitle: 'Tencent''s open-weight text-to-video generation model'
description: 'Tencent''s open-weight text-to-video generation model'
company: 'tencent'
model_type: 'Video Generation'
logo_url: ''
product_url: 'https://aivideo.hunyuan.tencent.com/'
price: 'Free'
rank: 6
release_date: '2024-12-03'
param_count: '13B'
modality: [text, video]
open_weight: true
license: 'Tencent Hunyuan License'
api_available: true
access_methods: [Self-hosted]
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [video-generation, open-weight, text-to-video]
---

HunyuanVideo is Tencent's open-weight video generation model, released in December 2024 with roughly 13 billion parameters, which made it the largest open video model available at the time. It generates text-to-video and image-to-video clips up to about 720p and five seconds long, with prompt adherence and motion quality that reviewers compared favorably to closed models like Runway Gen-3 and Kling. Tencent released the full training and inference code along with pretrained weights on GitHub and Hugging Face under a license that permits commercial use in most jurisdictions, which was unusual for a model of this scale at release. The open weights let researchers and studios fine-tune it for specific styles or subjects rather than working only through an API. Tencent later followed up with HunyuanVideo-1.5, a smaller 8.3B-parameter model that reaches comparable quality with less compute.
