---
title: 'Amazon Nova Sonic'
name: 'Amazon Nova Sonic'
slug: 'amazon-nova-sonic'
subtitle: 'Amazon''s speech-to-speech model for real-time conversational voice agents'
description: 'Amazon''s speech-to-speech model for real-time conversational voice agents'
company: 'amazon'
model_type: 'Audio Generation'
logo_url: ''
product_url: 'https://aws.amazon.com/ai/generative-ai/nova/speech/'
price: 'Freemium'
rank: 6
release_date: '2025-04-08'
param_count: 'Undisclosed'
context_window_tokens: 300000
modality: [audio, text]
open_weight: false
license: 'Proprietary'
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['AWS Bedrock']
date: '2026-07-16'
tags: [voice, audio, api, real-time]
---

Amazon Nova Sonic is a speech-to-speech model that Amazon announced in April 2025, unifying speech understanding and speech generation into a single model rather than chaining separate speech-to-text, language, and text-to-speech systems together. It's accessed through a bidirectional streaming API on Amazon Bedrock, supports a 300,000-token context window, and is built for real-time voice agents that need to listen, reason, and respond with natural-sounding speech and low latency. It also supports tool use and knowledge grounding, so a voice agent built on Sonic can call external functions or retrieve information mid-conversation.

Amazon pitched Sonic as a lower-cost alternative to combining separate ASR, LLM, and TTS pipelines, and as a competitor to OpenAI's Realtime API and Google's native audio models for voice assistants and customer service bots. Amazon later followed it with Nova 2 Sonic, which added support for more languages and an expanded context window, but the original Sonic model remains available on Bedrock for existing voice-agent workloads.
