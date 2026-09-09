---
title: 'Qwen3.8-27B'
name: 'Qwen3.8-27B'
slug: 'qwen3-8-27b'
subtitle: 'Alibaba''s open-weight multimodal model sized to run on a single local GPU'
description: 'Alibaba''s open-weight multimodal model sized to run on a single local GPU'
company: 'alibaba'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://qwen.ai/'
price: 'Free'
rank: 7
release_date: '2026-08-14'
param_count: '27B'
context_window_tokens: 262144
modality: [text, image, video]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Alibaba Cloud', 'API']
date: '2026-08-17'
tags: [llm, open-weight, multimodal, single-gpu, apache-2.0, local]
---

Alibaba's Qwen team released Qwen3.8-27B on August 14, 2026, with open weights available immediately under the Apache 2.0 license. It's a dense 27 billion parameter model rather than a mixture-of-experts design, and it handles text, images, and video, including diagrams, documents, and multi-hour footage. Context runs to 262,000 tokens natively and can stretch to a million using the YaRN scaling method. Alibaba says it beats the larger Qwen3.7-Plus on coding and office tasks and has sharpened its agentic planning, letting it complete multi-step tasks with less supervision.

The release was aimed squarely at developers who want a capable model that fits on a single consumer or workstation GPU rather than a datacenter cluster, positioning it against similarly local-first releases from Meta and Google. Alibaba paired the launch with open weights for Qwen3.8-2.4T-A95B, the Max-class model from the same generation, giving developers a choice between this lightweight version and a frontier-scale model built for heavier agentic workloads.
