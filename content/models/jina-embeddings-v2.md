---
title: 'Jina Embeddings v2'
name: 'Jina Embeddings v2'
slug: 'jina-embeddings-v2'
subtitle: 'Jina AI''s embedding model, notable for an 8k-token context window at launch'
description: 'Jina AI''s embedding model, notable for an 8k-token context window at launch'
company: 'jina-ai'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://jina.ai/news/jina-embeddings-2-the-best-solution-for-embedding-long-documents/'
price: 'Free'
rank: 5
release_date: '2023-10-30'
param_count: '137M'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Jina API']
date: '2026-07-16'
tags: [embedding, open-weight, api, legacy]
---

Jina Embeddings v2 is a text embedding model from Jina AI, released in October 2023. It came in two main sizes, a 33 million parameter small version and a 137 million parameter base version, both built on a modified BERT architecture using ALiBi position encoding instead of standard positional embeddings. That choice let it handle sequences up to 8,192 tokens, which was unusual for an open embedding model at the time and let it compete with OpenAI's proprietary text-embedding-ada-002 on long document retrieval while being far smaller. The model is released under an Apache 2.0 license and can be run locally or accessed through Jina's API. It has since been superseded by jina-embeddings-v3, which adds multilingual support and task-specific adapters, but v2 remains in use for English-language retrieval tasks where its smaller size is an advantage.
