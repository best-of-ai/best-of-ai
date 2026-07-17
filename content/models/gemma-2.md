---
title: 'Gemma 2'
name: 'Gemma 2'
slug: 'gemma-2'
subtitle: 'Google''s prior-generation open-weight model family'
description: 'Google''s prior-generation open-weight model family'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.google.dev/gemma'
price: 'Free'
rank: 6
release_date: '2024-06-27'
param_count: '27B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Gemma License'
api_available: true
mmlu_score: 75.2
humaneval_score: 51.8
access_methods: [Self-hosted, API]
platforms: ['Hugging Face', 'Google Vertex AI']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted]
---

Gemma 2 is the second generation of Google's open-weight model family, built from the same research as Gemini but released for anyone to download and run themselves. Google launched the 9 billion and 27 billion parameter versions on June 27, 2024, followed later by a smaller 2 billion parameter version aimed at running on laptops and phones. The 27B model was tuned to compete with models more than twice its size, and the 9B version beat Llama 3 8B and other similarly sized open models on several benchmarks at launch, scoring 75.2 on MMLU and 51.8 on HumanEval.

Google distributes Gemma 2 weights through Hugging Face and Kaggle for self-hosting, and also offers it through Google AI Studio and Vertex AI for people who'd rather not run it themselves. It ships under Google's own Gemma license, which permits commercial use but carries some usage restrictions rather than being a fully permissive license like Apache 2.0. Google has since released Gemma 3 as the newer generation, so Gemma 2 is now the prior-generation option in the lineup, kept around for compatibility and for teams already built on it.
