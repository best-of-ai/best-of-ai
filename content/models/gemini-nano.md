---
title: 'Gemini Nano'
name: 'Gemini Nano'
slug: 'gemini-nano'
subtitle: 'Google''s on-device Gemini tier built into Pixel and Android'
description: 'Google''s on-device Gemini tier built into Pixel and Android'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://deepmind.google/technologies/gemini/'
price: 'Paid'
rank: 4
release_date: '2023-12-06'
param_count: '3.25B'
context_window_tokens: 8192
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Self-hosted]
platforms: ['Android', 'Chrome']
date: '2026-07-16'
tags: [llm, on-device, small-model]
---

Gemini Nano is the smallest tier of Google's Gemini family, designed to run entirely on a phone rather than calling out to a server. Google announced it alongside Gemini Pro and Ultra on December 6, 2023 and shipped it first on the Pixel 8 Pro, where it powers on-device features like Smart Reply in messaging apps, call summarization, and the Recorder app's summaries. It comes in a couple of sizes, roughly 1.8 billion and 3.25 billion parameters, quantized to run efficiently within a phone's memory and NPU limits, and works fully offline with no data leaving the device.

Because it runs locally, Nano trades raw capability for speed, privacy, and zero marginal cost per query, and its usable context window is far smaller than Google's server-side models. Google has expanded device support since launch to more Pixel models and, through partnerships, to Samsung Galaxy devices, and it exposes Nano to third-party Android developers through the AICore system and ML Kit GenAI APIs rather than a public cloud API.
