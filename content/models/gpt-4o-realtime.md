---
title: 'GPT-4o Realtime'
name: 'GPT-4o Realtime'
slug: 'gpt-4o-realtime'
subtitle: 'Low-latency speech-to-speech variant of GPT-4o for live voice conversation'
description: 'Low-latency speech-to-speech variant of GPT-4o for live voice conversation'
company: 'openai'
model_type: 'Audio Generation'
logo_url: ''
product_url: 'https://openai.com/index/introducing-the-realtime-api/'
price: 'Paid'
rank: 7
release_date: '2024-10-01'
param_count: 'Undisclosed'
context_window_tokens: 32000
modality: [audio, text]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 5
output_price_usd_per_m: 20
api_available: true
access_methods: [API]
platforms: ['API', 'ChatGPT Advanced Voice']
date: '2026-07-16'
tags: [voice, multimodal, api, real-time]
---

GPT-4o Realtime is a speech-to-speech variant of GPT-4o that OpenAI introduced through its Realtime API on October 1, 2024. Instead of the usual pipeline of transcribing audio to text, running it through a language model, and synthesizing speech back out, it processes audio natively end to end over a WebSocket or WebRTC connection, which cuts the lag that made earlier voice bots feel stilted. It powers ChatGPT's Advanced Voice Mode and lets developers build phone agents, voice assistants, and live translation tools that respond in under a second. The model has a 32K token context window and charges $5 per million input text tokens and $20 per million output text tokens, with separate, higher rates for audio tokens. It competes with Google's Gemini Live API and various speech-focused startups building on top of Whisper-class transcription stacked with a language model, but its selling point is the single-model, low-latency architecture rather than a stitched-together pipeline.
