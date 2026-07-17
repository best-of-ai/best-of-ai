---
title: 'BGE-large-en'
name: 'BGE-large-en'
slug: 'bge-large-en'
subtitle: 'BAAI''s widely-used general embedding model for English retrieval'
description: 'BAAI''s widely-used general embedding model for English retrieval'
company: 'baai'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://huggingface.co/BAAI/bge-large-en-v1.5'
price: 'Free'
rank: 6
release_date: '2023-09-15'
param_count: '335M'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'MIT'
api_available: true
access_methods: [Self-hosted, API]
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [embedding, open-weight, api]
---

BGE-large-en-v1.5 is a text embedding model from BAAI, the Beijing Academy of Artificial Intelligence, released in September 2023 as an update to the original BGE-large-en model from a few weeks earlier. It has 335 million parameters, produces 1024-dimension embeddings, and handles sequences up to 512 tokens, putting it in the same size class as other BERT-scale encoder models rather than the larger decoder-based embedding models that came later. The v1.5 update mainly fixed a similarity-score distribution issue in the original release and improved retrieval quality when used without a task-specific instruction prefix, which had been a rough edge in v1. BAAI released it under the MIT license, and it became one of the most widely used open embedding models for English retrieval and RAG pipelines, largely because it was free, fast to run, and scored well on the MTEB benchmark relative to its size. It's since been joined by larger and more capable BAAI models like BGE-M3, but it remains a common default for lightweight self-hosted retrieval.
