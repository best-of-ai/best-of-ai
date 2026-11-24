---
title: 'Gemini Decision 1'
name: 'Gemini Decision 1'
slug: 'gemini-decision-1'
subtitle: 'Google''s non-generative model that scores options and returns confidence instead of text'
description: 'Google''s non-generative model that scores options and returns confidence instead of text'
company: 'google-deepmind'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/'
price: 'Paid'
rank: 6
release_date: '2026-11-11'
param_count: 'Undisclosed'
context_window_tokens: 256000
modality: [text, image, audio, video]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.1
output_price_usd_per_m: 0
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['Gemini API', 'Google AI Studio']
date: '2026-11-24'
tags: [classification, decision-model, multimodal, api]
---

Gemini Decision 1 is a model behind Google's Decisions API, launched November 11, 2026, that does not write text. It scores options in a single forward pass and returns a probability and confidence for each. It handles yes/no questions, multiple choice with 2 to 255 options, and ordered rubric scoring, with up to 1,000 questions in one request. Inputs can be text, images, audio, video and PDFs, up to 256,000 tokens.

Google quotes end-to-end latency of 150 to 250 milliseconds. Pricing is $0.10 per million input tokens and nothing for output, and AI Studio has a no-cost tier for prototyping. Google says it is nearly five times cheaper than Gemini 3.5 Flash-Lite on the same suite. The model ID is gemini-decision-1, and integrations are rolling out on OpenRouter, LangChain, Vercel and LiteLLM.
