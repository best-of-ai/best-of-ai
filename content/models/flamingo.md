---
title: 'Flamingo'
name: 'Flamingo'
slug: 'flamingo'
subtitle: 'DeepMind''s vision-language model that pioneered few-shot multimodal reasoning'
description: 'DeepMind''s vision-language model that pioneered few-shot multimodal reasoning'
company: 'google-deepmind'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://deepmind.google/discover/blog/tackling-multiple-tasks-with-a-single-visual-language-model/'
price: 'Paid'
rank: 6
release_date: '2022-04-29'
param_count: '80B'
modality: [text, image]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
platforms: ['Research']
date: '2026-07-16'
tags: [multimodal, vision, research]
---

Flamingo is a vision-language model DeepMind published in April 2022, built to handle images, videos, and text together and answer open-ended questions about them after seeing only a handful of examples. It starts from Chinchilla, DeepMind's 70B parameter language model, and adds vision encoders and cross-attention layers that let it condition text generation on visual input, bringing the full model to roughly 80B parameters. The key idea was few-shot learning for vision-language tasks: rather than fine-tuning on each new dataset, Flamingo could be shown a small number of examples in its prompt and generalize from there, similar to how GPT-3 did for text. At release it beat every prior few-shot approach on 16 vision-language benchmarks, including captioning, visual question answering, and visual dialogue. DeepMind never released Flamingo as a product or public API; it stayed a research model, but its architecture influenced later multimodal systems, including open reimplementations like OpenFlamingo and design choices in Google's subsequent multimodal models.
