---
title: 'MiniCPM-V'
name: 'MiniCPM-V'
slug: 'minicpm-v'
subtitle: 'OpenBMB''s multimodal edge model, capable of GPT-4V-level vision tasks on a phone'
description: 'OpenBMB''s multimodal edge model, capable of GPT-4V-level vision tasks on a phone'
company: 'openbmb'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://github.com/OpenBMB/MiniCPM-V'
price: 'Free'
rank: 5
release_date: '2024-05-20'
param_count: '8B'
context_window_tokens: 32768
modality: [text, image, video]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, small-model, on-device]
---

MiniCPM-V is a line of open-weight vision-language models from OpenBMB, a research lab spun out of Tsinghua University, built to run vision and video understanding on phones and other resource-limited devices rather than requiring a server GPU. The May 2024 release, MiniCPM-Llama3-V 2.5, pairs an 8B parameter Llama3 backbone with a SigLip vision encoder and claims performance on OCR, multi-image reasoning, and general visual question answering that matches or beats GPT-4V on several public benchmarks, despite running fully offline on a phone.

OpenBMB has kept iterating on the series since, with later versions such as MiniCPM-V 4.5 and 4.6 shrinking the parameter count further while improving accuracy, reflecting a broader trend of closing the gap between small on-device multimodal models and much larger cloud-hosted ones. The models are released under an Apache 2.0 license on Hugging Face and GitHub, aimed at developers who need offline, privacy-preserving multimodal AI on consumer hardware.
