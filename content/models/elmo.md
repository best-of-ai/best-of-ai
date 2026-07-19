---
title: 'ELMo'
name: 'ELMo'
slug: 'elmo'
subtitle: 'AI2''s deep contextualized word representation model that predated the transformer era'
description: 'AI2''s deep contextualized word representation model that predated the transformer era'
company: 'allen-institute-for-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://allenai.org/allennlp/software/elmo'
price: 'Free'
rank: 5
release_date: '2018-02-15'
param_count: '93.6M'
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['AllenNLP']
date: '2026-07-16'
tags: [llm, open-weight, legacy, foundation-model]
---

ELMo, short for Embeddings from Language Models, came out of the Allen Institute for AI and the University of Washington in February 2018, described in the paper "Deep Contextualized Word Representations" by Matthew Peters, Mark Neumann, and coauthors. Instead of assigning each word a single fixed vector the way earlier embeddings like word2vec and GloVe did, ELMo runs a bidirectional LSTM over a sentence and produces a representation for each word that depends on its surrounding context, so the same word gets a different vector depending on how it's used. Trained on roughly a billion words, it improved results across six NLP tasks at the time, including question answering and named entity recognition, when plugged into existing models as a feature. ELMo predates the transformer architecture and was largely superseded by BERT and its successors within about a year of release, but it's still cited as one of the models that established contextual word representations as the standard approach in NLP.
