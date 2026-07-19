---
title: 'Gemini 1.5 Pro'
name: 'Gemini 1.5 Pro'
slug: 'gemini-1-5-pro'
subtitle: 'Google''s 2024 model that introduced the 1M-token context window'
description: 'Google''s 2024 model that introduced the 1M-token context window'
company: 'google-deepmind'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://deepmind.google/technologies/gemini/'
price: 'Paid'
rank: 6
release_date: '2024-02-15'
param_count: 'Undisclosed'
context_window_tokens: 1000000
modality: [text, image, audio, video]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 1.25
output_price_usd_per_m: 5
api_available: true
mmlu_score: 85.9
humaneval_score: 71.9
lmarena_score: 1260
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['Gemini app', 'Google Vertex AI', 'API']
date: '2026-07-16'
tags: [llm, multimodal, long-context, api, legacy]
extra_model_types: ['Code']
---

Gemini 1.5 Pro is the model that introduced million-token context windows to a mainstream API, released by Google in February 2024 and moved to general availability that May. It reads text, images, audio, and video in a single prompt, and Google demonstrated it holding an entire hour of video or hundreds of pages of documents in context at once, well beyond what GPT-4 or Claude offered at the time. It uses a mixture-of-experts architecture, which Google said let it match or beat the larger Gemini 1.0 Ultra on most benchmarks while running cheaper.

Google cut 1.5 Pro's price twice during 2024, eventually settling near $1.25 per million input tokens and $5 per million output tokens for prompts under 128,000 tokens. It scored around 85.9 on MMLU and 71.9 on HumanEval, and became Google's default production model through most of 2024 via the Gemini app, Vertex AI, and the Gemini API. Google replaced it as the flagship with Gemini 2.5 Pro in 2025, though 1.5 Pro remains available through the API for existing integrations.
