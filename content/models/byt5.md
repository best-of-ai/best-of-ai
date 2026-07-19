---
title: 'ByT5'
name: 'ByT5'
slug: 'byt5'
subtitle: 'Google''s token-free variant of T5 that operates directly on raw bytes'
description: 'Google''s token-free variant of T5 that operates directly on raw bytes'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://arxiv.org/abs/2105.13626'
price: 'Free'
rank: 4
release_date: '2021-05-28'
param_count: '13B'
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, legacy, research]
---

ByT5 is a variant of Google's T5 text-to-text model that Google Research published in mid-2021, notable for dropping tokenization altogether and operating directly on raw UTF-8 bytes. Standard language models split text into subword tokens using a fixed vocabulary built by a tokenizer, which works well for the languages and scripts that vocabulary was built around but tends to handle rare words, misspellings, and less common languages poorly. ByT5 sidesteps that by treating every input as a sequence of bytes, giving it a vocabulary of only a few hundred possible values instead of tens of thousands of subword tokens.

The tradeoff is that byte sequences are much longer than token sequences for the same text, so ByT5 needs deeper encoders and more compute per input to match token-based models on standard benchmarks. Google released a family of ByT5 sizes up to ByT5-XXL at around 13 billion parameters, with all checkpoints open on Hugging Face under Apache 2.0. It performed especially well on noisy text, transliteration, and multilingual tasks involving low-resource scripts, which made it a useful reference point in research on tokenization-free and character-level modeling, even though most production language models have stuck with token-based approaches for their efficiency.
