---
title: 'Cohere Embed Multilingual v3'
name: 'Cohere Embed Multilingual v3'
slug: 'cohere-embed-multilingual-v3'
subtitle: 'Cohere''s embedding model tuned for retrieval across 100+ languages'
description: 'Cohere''s embedding model tuned for retrieval across 100+ languages'
company: 'cohere'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://cohere.com/blog/introducing-embed-v3'
price: 'Paid'
rank: 6
release_date: '2023-11-02'
param_count: 'Undisclosed'
context_window_tokens: 512
modality: [text]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.1
api_available: true
access_methods: [API]
platforms: ['Cohere API']
date: '2026-07-16'
tags: [embedding, api, multilingual]
---

Cohere Embed Multilingual v3 is a text embedding model Cohere released in November 2023 for search, retrieval-augmented generation, and semantic similarity tasks across more than 100 languages. It takes input text up to 512 tokens and outputs a 1024-dimension vector by default, with support for shorter 384 or 768 dimension embeddings when a team wants faster search or lower storage cost. Cohere trained it alongside an English-only sibling, Embed English v3, and pitched both as an upgrade over v2 because they weight passages by how relevant they are likely to be, not just how similar they are, which cuts down on noisy retrieval results in RAG pipelines. It's priced at $0.10 per million tokens through the Cohere API and is also distributed through AWS, Azure, and Oracle Cloud marketplaces. Cohere has since released newer Embed v4 models, and some cloud providers such as Oracle now list v3 as a legacy or deprecated option, though it remains available through Cohere's own API and Hugging Face.
