---
title: 'AudioLM'
name: 'AudioLM'
slug: 'audiolm'
subtitle: 'Google''s framework for generating realistic speech and audio continuations'
description: 'Google''s framework for generating realistic speech and audio continuations'
company: 'google-deepmind'
model_type: 'Audio Generation'
logo_url: ''
product_url: 'https://google-research.github.io/seanet/audiolm/examples/'
price: 'Paid'
rank: 5
release_date: '2022-09-07'
param_count: 'Undisclosed'
modality: [audio]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
platforms: ['Research']
date: '2026-07-16'
tags: [audio, research, legacy]
---

AudioLM is a research framework that Google published in September 2022, treating audio generation as a language modeling problem over discrete audio tokens instead of the usual spectrogram or waveform regression approaches. It combines two representations: semantic tokens from w2v-BERT, a self-supervised speech model, that capture long-range structure, and acoustic tokens from the SoundStream neural codec that preserve fine audio detail for high-quality synthesis. Trained only on raw audio with no text transcripts or annotations, it can continue a few seconds of spoken audio or piano music in a way that stays coherent over tens of seconds, something earlier audio generation methods struggled with. Google never released it as a product; it stayed a research paper and demo page, and Google DeepMind used its token-based approach as a building block for later work like MusicLM and parts of Lyria.
