---
title: 'BERT'
name: 'BERT'
slug: 'bert'
subtitle: 'Google''s 2018 bidirectional encoder that reshaped NLP research'
description: 'Google''s 2018 bidirectional encoder that reshaped NLP research'
company: 'google'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://github.com/google-research/bert'
price: 'Free'
rank: 6
release_date: '2018-10-11'
param_count: '340M'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [embedding, open-weight, nlp, legacy]
---

BERT (Bidirectional Encoder Representations from Transformers) is a language model that Google Research published in October 2018, and it changed how the field approached pretraining for NLP tasks. Unlike earlier models that read text left to right, BERT trains on masked-word prediction and next-sentence prediction, letting it build representations that draw on context from both directions at once. Google released two main sizes: BERT-base at 110 million parameters and BERT-large at 340 million, both with a 512-token limit, and made the weights freely available under Apache 2.0 on GitHub and later Hugging Face. Fine-tuned versions of BERT set new records on eleven different NLP benchmarks at launch, including question answering and natural language inference, and it quickly became the standard base model to fine-tune for tasks like classification, named entity recognition, and search ranking. It's mostly been superseded by newer encoder models like RoBERTa and DeBERTa and by the embedding models that followed it, but it's still one of the most cited papers in NLP and its architecture underlies a large share of later encoder-based systems.
