---
title: 'Granite Embedding'
name: 'Granite Embedding'
slug: 'granite-embedding'
subtitle: 'IBM''s enterprise text embedding model family for retrieval'
description: 'IBM''s enterprise text embedding model family for retrieval'
company: 'ibm'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://www.ibm.com/granite'
price: 'Free'
rank: 4
release_date: '2024-12-18'
param_count: '278M'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
platforms: ['IBM watsonx', 'Hugging Face']
date: '2026-07-16'
tags: [embedding, open-weight, enterprise]
---

Granite Embedding is IBM's family of text embedding models for retrieval and semantic search, built to plug into enterprise RAG systems on watsonx or self-hosted infrastructure. The 278M-parameter multilingual variant covers twelve languages including English, German, Japanese, Arabic, and Chinese, and it produces 768-dimension vectors from inputs up to 512 tokens. IBM trained it with contrastive fine-tuning, knowledge distillation, and model merging over a mix of open relevance-pair datasets and IBM's own curated data, favoring sources with permissive, enterprise-friendly licensing. Like the rest of the Granite line, the embedding models ship under Apache 2.0 and are distributed through Hugging Face, Ollama, and IBM watsonx, competing with other open embedding families like BGE and GTE on retrieval benchmarks while emphasizing compliance and traceable training data for regulated customers.
