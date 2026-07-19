---
title: 'Hunyuan3D'
name: 'Hunyuan3D'
slug: 'hunyuan3d'
subtitle: 'Tencent''s open-weight model for generating 3D assets from text or images'
description: 'Tencent''s open-weight model for generating 3D assets from text or images'
company: 'tencent'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://github.com/Tencent/Hunyuan3D-2'
price: 'Free'
rank: 5
release_date: '2025-01-21'
param_count: '2.6B (shape) + 1.3B (texture)'
modality: [text, image]
open_weight: true
license: 'Tencent Hunyuan License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Tencent Cloud']
date: '2026-07-16'
tags: [3d-generation, open-weight, api]
---

Hunyuan3D is Tencent's open-weight system for turning text prompts or reference images into 3D assets, with the widely used 2.0 release published in January 2025. It splits the job into two models: a 2.6B-parameter shape generator built on a flow-based diffusion transformer that produces an untextured mesh, and a 1.3B-parameter texture model that paints high-resolution PBR materials onto that mesh afterward. That two-stage split lets each part specialize, so the shape model focuses purely on geometry while the texture model handles color, lighting response, and surface detail. Tencent released the weights on Hugging Face and GitHub under its Hunyuan license, giving game studios and 3D artists a way to run asset generation locally instead of through a paid API. It competes with other open and semi-open 3D generators such as TripoSR and Stability AI's TripoSG, and later Hunyuan3D versions (2.1, 2.5) pushed texture fidelity and geometry detail further.
