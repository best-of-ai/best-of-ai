---
title: 'CogVideoX'
name: 'CogVideoX'
slug: 'cogvideox'
subtitle: 'Zhipu''s open-weight text-to-video model family'
description: 'Zhipu''s open-weight text-to-video model family'
company: 'zhipu-ai'
model_type: 'Video Generation'
logo_url: ''
product_url: 'https://github.com/THUDM/CogVideo'
price: 'Free'
rank: 6
release_date: '2024-08-27'
param_count: '5B'
modality: [text, video]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
platforms: ['Hugging Face', 'Zhipu API']
date: '2026-07-16'
tags: [video-generation, open-weight, api]
---

CogVideoX is Zhipu AI's open-weight text-to-video model, built with Tsinghua University's KEG lab and released in August 2024 as a successor to the original CogVideo project. It ships in 2B and 5B parameter variants using a 3D causal VAE for spatial and temporal compression alongside an expert adaptive LayerNorm transformer, and it supports text-to-video, image-to-video, and video continuation from a single frame or prompt. The 5B model generates clips up to 10 seconds long at up to 768p resolution and 16 frames per second, and Zhipu later shipped a CogVideoX-1.5 update in November 2024 with longer, higher-resolution output. Weights are released under Apache 2.0 and hosted on Hugging Face, and Zhipu also serves the models through its own API, so CogVideoX works both as a self-hosted open model and as a hosted service, similar to how Stability AI and Runway position their video generators.
