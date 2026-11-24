---
title: 'SenseNova Loop-9B'
name: 'SenseNova Loop-9B'
slug: 'sensenova-loop-9b'
subtitle: 'SenseTime''s open-weight 9B multimodal model that reuses its layers in a loop'
description: 'SenseTime''s open-weight 9B multimodal model that reuses its layers in a loop'
company: 'sensetime'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.sensetime.com/en/news/sensenova-loop-9b-release-20261118-1435'
price: 'Free'
rank: 5
release_date: '2026-11-17'
param_count: '9B (about 14.6B inference-equivalent)'
context_window_tokens: 512000
modality: [text, image]
open_weight: true
license: 'Open weights'
api_available: true
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'GitHub']
date: '2026-11-24'
tags: [llm, open-weight, multimodal, small-model, self-hosted]
---

SenseNova Loop-9B is the official release of SenseTime's open-weight multimodal model, published on November 17, 2026 after a preview. It has about 9B parameters across 32 distinct decoder layers, which run as 56 layer computations per pass, giving roughly 14.6B inference-equivalent parameters. It accepts text and images, outputs text and handles up to 512,000 tokens of context.

The 4-bit weights are about 4.9 GB, so it fits on consumer hardware, and an official AWQ build shipped on launch day. SenseTime calls it comparable to Qwen3.8-27B: 41.36 against 44.60 on NL2Repo and 65.31 against 65.01 on AIDABench. Weights are on Hugging Face under sensenova/sensenova-loop, with code on GitHub.
