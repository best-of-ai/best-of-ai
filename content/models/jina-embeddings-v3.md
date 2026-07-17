---
title: 'jina-embeddings-v3'
name: 'jina-embeddings-v3'
slug: 'jina-embeddings-v3'
subtitle: 'Jina AI''s open-weight multilingual embedding model'
description: 'Jina AI''s open-weight multilingual embedding model'
company: 'jina-ai'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://jina.ai/embeddings/'
price: 'Free'
rank: 4
release_date: '2024-09-18'
param_count: '570M'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'CC-BY-NC 4.0'
api_available: true
access_methods: [API, Self-hosted]
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [embedding, open-weight, retrieval, multilingual]
---

jina-embeddings-v3 is Jina AI's multilingual text embedding model, released in September 2024. It has 570 million parameters and supports 89 languages, with a context window of 8,192 tokens using rotary position embeddings. The model uses task-specific LoRA adapters for different use cases such as query-document retrieval, clustering, classification, and text matching, so a single set of weights can be adapted to different jobs without full retraining. It also supports Matryoshka representation learning, which lets users truncate the output embedding down from its default 1024 dimensions to as low as 32 while keeping most of the retrieval quality. On the MTEB benchmark, Jina AI reported that v3 outperformed proprietary embeddings from OpenAI and Cohere on English tasks and beat multilingual-e5-large-instruct across multilingual tasks. It is released under a CC BY-NC 4.0 license, which permits free use for research and evaluation but requires a commercial license for production use at scale.
