---
title: 'GTE-large'
name: 'GTE-large'
slug: 'gte-large'
subtitle: 'Alibaba''s general text embedding model for retrieval and semantic similarity'
description: 'Alibaba''s general text embedding model for retrieval and semantic similarity'
company: 'alibaba'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://huggingface.co/thenlper/gte-large'
price: 'Free'
rank: 5
release_date: '2023-08-07'
param_count: '335M'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
platforms: ['Hugging Face', 'Alibaba Cloud']
date: '2026-07-16'
tags: [embedding, open-weight, api]
---

GTE-large is a text embedding model from Alibaba DAMO Academy, published on Hugging Face in mid-2023 as part of the General Text Embeddings (GTE) family alongside smaller GTE-base and GTE-small variants. It's a 335-million-parameter BERT-style encoder trained with multi-stage contrastive learning on a broad mix of web and domain text, producing 1024-dimension vectors from inputs up to 512 tokens. The model is meant for retrieval, semantic search, clustering, and reranking, and at release it scored well on the MTEB benchmark leaderboard relative to other open embedding models of similar size, competing directly with BGE and E5 style models from other Chinese labs. GTE-large is open-weighted under Apache 2.0, runs easily on a single GPU or CPU for inference, and is distributed through Hugging Face and Alibaba Cloud, making it a common default choice for teams building RAG pipelines who want a compact embedding model without an API dependency.
