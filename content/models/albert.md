---
title: 'ALBERT'
name: 'ALBERT'
slug: 'albert'
subtitle: 'Google''s parameter-sharing variant of BERT designed for efficiency at scale'
description: 'Google''s parameter-sharing variant of BERT designed for efficiency at scale'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://arxiv.org/abs/1909.11942'
price: 'Free'
rank: 6
release_date: '2019-09-26'
param_count: '223M'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, legacy, foundation-model]
---

ALBERT (A Lite BERT) is a language representation model that Google Research and Toyota Technological Institute published in September 2019 as a follow-up to BERT. It uses two parameter-reduction tricks, factorized embedding parameterization and cross-layer parameter sharing, to cut the parameter count sharply while keeping accuracy competitive with much larger models. The largest configuration, ALBERT-xxlarge at around 223 million parameters, has roughly 18 times fewer parameters than BERT-large yet trains faster and set new state-of-the-art scores on GLUE, SQuAD 2.0, and RACE at the time of release.

Like BERT, ALBERT is an encoder-only model meant for understanding tasks such as classification, question answering, and reading comprehension rather than open-ended text generation, and it caps input at 512 tokens per sequence. Google released the code and pretrained weights openly, and the model became a common baseline for NLP research and production systems in the early 2020s before decoder-only generative models took over most attention in the field.
