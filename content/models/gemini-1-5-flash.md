---
title: 'Gemini 1.5 Flash'
name: 'Gemini 1.5 Flash'
slug: 'gemini-1-5-flash'
subtitle: 'Google''s fast, low-cost Gemini 1.5 tier, distilled from Gemini 1.5 Pro'
description: 'Google''s fast, low-cost Gemini 1.5 tier, distilled from Gemini 1.5 Pro'
company: 'google-deepmind'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://deepmind.google/technologies/gemini/flash/'
price: 'Paid'
rank: 7
release_date: '2024-05-14'
param_count: 'Undisclosed'
context_window_tokens: 1000000
modality: [text, image, audio, video]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.075
output_price_usd_per_m: 0.3
api_available: true
mmlu_score: 78.9
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['Google AI Studio', 'Vertex AI', 'Gemini app']
date: '2026-07-16'
tags: [llm, multimodal, api, low-cost]
---

Gemini 1.5 Flash is Google's fast, low-cost tier of the Gemini 1.5 generation, released in May 2024 as a distilled version of Gemini 1.5 Pro. Google built it by teaching a smaller model to imitate Pro's outputs, which kept much of Pro's reasoning ability while cutting latency and cost sharply. It carries the same million-token context window as Pro and handles text, images, audio, and video, making it a practical choice for high-volume tasks like summarizing long documents or captioning video where Pro's price would add up quickly.

At launch, Google priced it at $0.075 per million input tokens and $0.30 per million output tokens for prompts under 128,000 tokens, among the cheapest frontier-class API pricing at the time. It's available through Google AI Studio, Vertex AI, and the Gemini app, and it became the default free tier for many Gemini app users. Google has since moved most new development to the 2.0 and 2.5 Flash generations, so 1.5 Flash is now mainly kept around for API backward compatibility.
