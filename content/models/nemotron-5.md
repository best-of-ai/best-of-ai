---
title: 'Nemotron 5'
name: 'Nemotron 5'
slug: 'nemotron-5'
subtitle: 'NVIDIA''s open-weight model tuned for efficient inference on its own hardware'
description: 'NVIDIA''s open-weight model tuned for efficient inference on its own hardware'
company: 'nvidia'
model_type: 'Language'
logo_url: ''
product_url: 'https://developer.nvidia.com/nemotron'
price: 'Free'
rank: 6
release_date: '2026-07-10'
param_count: '70B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'NVIDIA Open Model License'
api_available: true
mmlu_score: 82.0
humaneval_score: 80.0
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'NVIDIA NIM', 'NGC']
date: '2026-07-19'
tags: [llm, open-weight, self-hosted, efficiency]
---

Nemotron 5 continues NVIDIA's line of open-weight models built less to top leaderboards and more to showcase how well models run on the company's own GPUs and inference stack. It's a 70 billion parameter dense model with a 128,000 token context window, distributed under the NVIDIA Open Model License and packaged for one-click deployment through NVIDIA NIM microservices as well as plain Hugging Face downloads.

NVIDIA has used the Nemotron line since Nemotron-4 340B to demonstrate techniques like pruning and distillation that shrink models without gutting quality, and Nemotron 5 keeps that focus. The 70B size was chosen specifically to fit on a single H100 or a pair of consumer GPUs at reasonable quantization. NVIDIA's real pitch here is the hardware and software stack underneath the model, not the model itself.
