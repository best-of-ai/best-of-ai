---
title: 'Aya 23'
name: 'Aya 23'
slug: 'aya-23'
subtitle: 'Cohere For AI''s open-weight multilingual model covering 23 languages'
description: 'Cohere For AI''s open-weight multilingual model covering 23 languages'
company: 'cohere'
model_type: 'Language'
logo_url: ''
product_url: 'https://cohere.com/research/aya'
price: 'Free'
rank: 5
release_date: '2024-05-27'
param_count: '35B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'CC-BY-NC 4.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, multilingual]
---

Aya 23 is a family of multilingual language models that Cohere For AI, Cohere's research lab, released in May 2024, covering 23 languages including Arabic, Chinese, Hindi, Japanese, Russian, and Spanish alongside English. It shipped in two sizes, 8B and 35B parameters, both built on Cohere's Command architecture and initialized from a pretrained checkpoint before further multilingual training. The 35B version is the one tracked here, with an 8192-token context window aimed at retrieval and instruction-following tasks across languages that are usually underserved by English-centric open models. Cohere released the weights under a CC-BY-NC 4.0 license with an acceptable-use addendum, so it's free for research and non-commercial use but requires a separate commercial agreement for production deployment. It followed the original Aya project, which had focused on data and evaluation for 101 languages, by narrowing scope to a smaller set of languages in exchange for stronger per-language quality.
