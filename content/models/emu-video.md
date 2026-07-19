---
title: 'Emu Video'
name: 'Emu Video'
slug: 'emu-video'
subtitle: 'Meta''s text-to-video model built on the Emu image generator'
description: 'Meta''s text-to-video model built on the Emu image generator'
company: 'meta-ai'
model_type: 'Video Generation'
logo_url: ''
product_url: 'https://ai.meta.com/blog/emu-text-to-video-generation-image-editing-research/'
price: 'Paid'
rank: 5
release_date: '2023-11-16'
param_count: 'Undisclosed'
modality: [text, video]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [video-generation, research, legacy]
---

Emu Video is a text-to-video research model Meta introduced in November 2023, built on top of Meta's Emu image generator. Rather than generating video directly from a text prompt in one step, it splits the job in two: first it uses Emu to generate a still image from the prompt, then it generates a video conditioned on both the text and that image. Meta reported that this factored approach let it skip the deep cascade of separate models that earlier systems like Google's Imagen Video and Meta's own Make-A-Video relied on, while still producing higher-resolution output. In human preference evaluations, Meta said raters favored Emu Video's clips over Imagen Video's and Make-A-Video's the large majority of the time. It was released as a research paper and demo rather than a public product, and its techniques fed into later Meta video features rather than shipping as a standalone model.
