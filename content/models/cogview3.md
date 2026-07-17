---
title: 'CogView3'
name: 'CogView3'
slug: 'cogview3'
subtitle: 'Zhipu''s relay-diffusion text-to-image model'
description: 'Zhipu''s relay-diffusion text-to-image model'
company: 'zhipu-ai'
model_type: 'Image Generation'
logo_url: ''
product_url: 'https://github.com/THUDM/CogView3'
price: 'Free'
rank: 5
release_date: '2024-09-29'
param_count: '3B'
modality: [text, image]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
platforms: ['Hugging Face', 'Zhipu API']
date: '2026-07-16'
tags: [image-generation, open-weight, api]
---

CogView3 is a text-to-image model from Zhipu AI and Tsinghua University, described in a March 2024 research paper and open-sourced on Hugging Face in September 2024. It is built around relay diffusion, a cascaded approach where a 3-billion-parameter base stage generates a low-resolution 512x512 image and a second stage adds noise back into that image before running a shorter super-resolution diffusion pass on top of it, rather than conditioning the second stage directly on the low-res output like older cascaded models did. Zhipu reports that CogView3 beats Stable Diffusion XL in human evaluations by a wide margin while needing only about half the inference time, and a distilled version matches that quality using roughly a tenth of SDXL's inference steps. The model and code are released under Apache 2.0, and Zhipu followed it with CogView-3Plus, a larger diffusion transformer variant in the same family, plus a hosted version through the Zhipu API for developers who don't want to run it themselves.
