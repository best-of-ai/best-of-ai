---
title: 'BioGPT'
name: 'BioGPT'
slug: 'biogpt'
subtitle: 'Microsoft''s domain-specific generative model pre-trained on biomedical literature'
description: 'Microsoft''s domain-specific generative model pre-trained on biomedical literature'
company: 'microsoft'
model_type: 'Language'
logo_url: ''
product_url: 'https://github.com/microsoft/BioGPT'
price: 'Free'
rank: 5
release_date: '2022-09-24'
param_count: '347M (base), 1.5B (Large)'
context_window_tokens: 1024
modality: [text]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [healthcare, open-weight, legacy]
---

BioGPT is a language model that Microsoft Research introduced in October 2022, built specifically for biomedical text rather than adapted from a general-purpose model after the fact. It uses a GPT-2-style decoder architecture trained from scratch on roughly 15 million PubMed abstracts, and it comes in a 347-million-parameter base version and a 1.5-billion-parameter BioGPT-Large version. Because it was trained on biomedical text from the start rather than fine-tuned onto it, it outperformed earlier general-purpose language models on tasks like biomedical relation extraction, question answering over medical literature, and document classification. Microsoft released both checkpoints under the MIT license on Hugging Face and GitHub, making it a common starting point for research groups building biomedical NLP tools without needing to train a domain-specific model from scratch. It predates the wave of general-purpose instruction-tuned chat models and hasn't been updated since, so it's mostly used now as a lightweight, self-hostable option for narrow biomedical text tasks rather than as an general assistant.
