---
title: 'Gemma 3'
name: 'Gemma 3'
slug: 'gemma-3'
subtitle: 'Google''s open-weight model family built from Gemini research'
description: 'Google''s open-weight model family built from Gemini research'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.google.dev/gemma'
price: 'Free'
rank: 7
release_date: '2025-03-12'
param_count: '27B'
context_window_tokens: 128000
modality: [text, image]
open_weight: true
license: 'Gemma License'
api_available: true
mmlu_score: 78.0
access_methods: [API, Self-hosted]
platforms: ['Hugging Face', 'Google Vertex AI']
date: '2026-07-16'
tags: [llm, open-weight, small-model, self-hosted]
---

Gemma 3 is Google's third generation of open-weight models, built with research and technology from the Gemini 2.0 project. It ships in four sizes, 1B, 4B, 12B, and 27B parameters, each available as a base checkpoint and an instruction-tuned version. The 4B, 12B, and 27B models accept both text and images, while the 1B model is text only, and all sizes handle over 140 languages with strong out-of-the-box support for more than 35 of them. Context length runs to 128,000 tokens for the larger models, a big jump from the 8,192 tokens in Gemma 2.

Google positions Gemma 3 as small enough to run on a single GPU or TPU host while still competing with much larger closed models on standard benchmarks. The 27B variant reportedly outperforms Gemini 1.5 Pro on several evaluations, and independent testing puts it well ahead of the earlier Gemma 2 27B. Because the weights are downloadable under the Gemma license, developers use it for local deployment, fine-tuning, and edge applications where sending data to a hosted API isn't an option.
