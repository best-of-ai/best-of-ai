---
title: 'CosyVoice'
name: 'CosyVoice'
slug: 'cosyvoice'
subtitle: 'Alibaba''s open-weight zero-shot voice-cloning and text-to-speech model'
description: 'Alibaba''s open-weight zero-shot voice-cloning and text-to-speech model'
company: 'alibaba'
model_type: 'Audio Generation'
logo_url: ''
product_url: 'https://github.com/FunAudioLLM/CosyVoice'
price: 'Free'
rank: 5
release_date: '2024-07-09'
param_count: 'Undisclosed'
modality: [audio, text]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: false
platforms: ['Hugging Face', 'Alibaba Cloud']
date: '2026-07-16'
tags: [text-to-speech, open-weight, voice-cloning, api]
---

CosyVoice is a text-to-speech and voice-cloning model from Alibaba's FunAudioLLM team, released as open weights in July 2024. It generates speech from short reference audio clips, so it can clone a voice from just a few seconds of sample and then speak arbitrary text in that voice across multiple languages, including Chinese, English, Japanese, and Korean. The model builds on supervised semantic speech tokens paired with a language-model-style generation approach, which lets it handle cross-lingual and zero-shot voice cloning without speaker-specific fine-tuning. Alibaba has continued to update the line, later releasing CosyVoice 2 and CosyVoice 3 with larger underlying models and lower latency, and the original release remains available on Hugging Face and through Alibaba Cloud's Model Studio API under an Apache 2.0 license.
