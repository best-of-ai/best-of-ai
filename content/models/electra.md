---
title: 'ELECTRA'
name: 'ELECTRA'
slug: 'electra'
subtitle: 'Google''s more sample-efficient pretraining approach using a replaced-token-detection objective'
description: 'Google''s more sample-efficient pretraining approach using a replaced-token-detection objective'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://arxiv.org/abs/2003.10555'
price: 'Free'
rank: 6
release_date: '2020-03-23'
param_count: '335M'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, legacy, foundation-model]
---

ELECTRA is a text-encoder pretraining method that researchers at Google and Stanford introduced in a paper published for ICLR 2020, along with a family of pretrained models built with it. Instead of BERT's masked-language-modeling objective, where the model predicts randomly hidden words, ELECTRA trains a small generator to replace some tokens with plausible alternatives and a discriminator to spot which tokens were swapped. That "replaced token detection" objective gives the model a learning signal from every token in a sequence rather than just the masked ones, which makes pretraining far more sample-efficient.

The largest released version, ELECTRA-Large, has 335 million parameters and reached GLUE scores competitive with RoBERTa and XLNet while using a quarter of their pretraining compute. Given equal compute budgets, it outperformed those models outright. Google released the code and weights under the Apache 2.0 license, and the smaller ELECTRA-Small and ELECTRA-Base variants became popular choices for teams that wanted BERT-level accuracy without BERT-level training cost.
