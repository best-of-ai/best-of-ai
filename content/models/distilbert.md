---
title: 'DistilBERT'
name: 'DistilBERT'
slug: 'distilbert'
subtitle: 'Hugging Face''s distilled, 40%-smaller version of BERT that retains most of its performance'
description: 'Hugging Face''s distilled, 40%-smaller version of BERT that retains most of its performance'
company: 'hugging-face'
model_type: 'Language'
logo_url: ''
product_url: 'https://arxiv.org/abs/1910.01108'
price: 'Free'
rank: 7
release_date: '2019-10-02'
param_count: '66M'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, legacy, small-model]
---

DistilBERT is a compressed version of Google's BERT that Hugging Face released in October 2019, using a technique called knowledge distillation to train a smaller student model to mimic the outputs of the larger BERT teacher during pretraining. At 66 million parameters, it's 40% smaller than the original BERT-base and runs about 60% faster, while retaining around 97% of BERT's performance on the GLUE benchmark suite. On tasks like SQuAD question answering and IMDb sentiment classification, it comes within a few points of full BERT despite the size cut.

The paper, "DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter," became one of the most cited papers in NLP, and the model itself became a default choice for teams that needed BERT-level language understanding on constrained hardware, including mobile devices. It's released under the Apache 2.0 license and remains one of the most downloaded models on Hugging Face years after its release.
