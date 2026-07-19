---
title: 'BGE-M3'
name: 'BGE-M3'
slug: 'bge-m3'
subtitle: 'BAAI''s open-weight multilingual, multi-granularity embedding model'
description: 'BAAI''s open-weight multilingual, multi-granularity embedding model'
company: 'baai'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://huggingface.co/BAAI/bge-m3'
price: 'Free'
rank: 4
release_date: '2024-02-06'
param_count: '568M'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'MIT'
api_available: true
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [embedding, open-weight, multilingual, retrieval]
---

BGE-M3 is a text embedding model from BAAI, described in a paper published in February 2024, and the name refers to three things it does at once: multi-linguality across more than 100 languages, multi-granularity handling of inputs up to 8192 tokens, and multi-functionality in that it produces dense vectors, sparse lexical weights, and ColBERT-style token vectors from a single forward pass. It has 568 million parameters, which is modest next to large LLMs but is trained specifically for retrieval rather than generation. That combination let it post state-of-the-art results at the time on the multilingual MIRACL benchmark and the cross-lingual MKQA benchmark, since a single model could substitute for what previously required separate dense and sparse retrieval systems. BAAI released it under the MIT license on Hugging Face, and it's widely used in retrieval-augmented generation pipelines that need to search across documents in multiple languages or documents longer than the 512-token limit typical of earlier BERT-based embedding models.
