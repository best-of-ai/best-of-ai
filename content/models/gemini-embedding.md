---
title: 'Gemini Embedding'
name: 'Gemini Embedding'
slug: 'gemini-embedding'
subtitle: 'Google''s unified text embedding model built from Gemini'
description: 'Google''s unified text embedding model built from Gemini'
company: 'google-deepmind'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://ai.google.dev/gemini-api/docs/embeddings'
price: 'Freemium'
rank: 5
release_date: '2025-03-07'
param_count: 'Undisclosed'
context_window_tokens: 2048
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: true
access_methods: [API]
platforms: ['Google Vertex AI']
date: '2026-07-16'
tags: [embedding, retrieval, api]
---

Gemini Embedding is Google's text embedding model, built from the Gemini family and made generally available through the Gemini API starting in March 2025. It converts text into a single vector representation that developers use for search, clustering, classification, and retrieval-augmented generation, replacing Google's earlier separate embedding models with one unified model trained across over 100 languages plus code. It supports Matryoshka Representation Learning, so a developer can truncate the default embedding down to smaller sizes like 768 or 256 dimensions to save storage without retraining anything.

At release, it topped the MTEB multilingual leaderboard by a wide margin over the next-best model. Google has continued extending the line since, including a newer version that adds native support for images, audio, and video alongside text in the same vector space. It's accessed through the Gemini API and Vertex AI and is priced per input token like Google's other Gemini models.
