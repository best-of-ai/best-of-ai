---
title: 'AudioCraft'
name: 'AudioCraft'
slug: 'audiocraft'
subtitle: 'Meta''s open-source framework spanning music and sound-effect generation'
description: 'Meta''s open-source framework spanning music and sound-effect generation'
company: 'meta-ai'
model_type: 'Audio Generation'
logo_url: ''
product_url: 'https://ai.meta.com/blog/audiocraft-musicgen-audiogen-encodec-generative-ai-audio/'
price: 'Free'
rank: 6
release_date: '2023-08-02'
param_count: '300M-3.3B (MusicGen), 1.5B (AudioGen)'
modality: [audio, text]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
platforms: ['GitHub']
date: '2026-07-16'
tags: [audio, open-weight, music-generation]
---

AudioCraft is a code library that Meta released in August 2023, bundling three generative audio models: MusicGen for text-to-music generation, AudioGen for environmental sound effects, and EnCodec, the neural audio codec both rely on for tokenizing waveforms. MusicGen comes in several sizes (300M, 1.5B, and 3.3B parameters), with variants that can also follow a melody alongside a text prompt, while AudioGen ships as a 1.5B-parameter model trained on sound effects rather than music. Meta released the code and weights under the MIT license, which made AudioCraft one of the first fully open toolkits for text-to-audio generation, in contrast to closed systems from companies like Google. It runs on a single consumer GPU for the smaller checkpoints, and it's become a common base for open-source music generation projects and research on controllable audio synthesis.
