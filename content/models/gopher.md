---
title: 'Gopher'
name: 'Gopher'
slug: 'gopher'
subtitle: 'DeepMind''s 280B-parameter research model that informed the Chinchilla scaling laws'
description: 'DeepMind''s 280B-parameter research model that informed the Chinchilla scaling laws'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://deepmind.google/discover/blog/language-modelling-at-scale-gopher-ethical-considerations-and-retrieval/'
price: 'Paid'
rank: 6
release_date: '2021-12-08'
param_count: '280B'
context_window_tokens: 2048
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: false
mmlu_score: 60.0
access_methods: [Research]
platforms: ['Research']
date: '2026-07-16'
tags: [llm, research, legacy]
---

Gopher is a 280-billion-parameter language model that DeepMind trained and described in a December 2021 paper as part of a study on how model performance scales with size. It was trained on MassiveText, a 10.5-terabyte corpus, and evaluated alongside five smaller models ranging from 44 million to 7 billion parameters to see how capability improved with scale. On the MMLU benchmark, Gopher scored 60% under a five-shot setup, a marked jump over prior models at the time.

DeepMind never released Gopher publicly or through an API; it existed purely as a research vehicle. Its main legacy came from the follow-up analysis, published as the Chinchilla paper, which used Gopher and its siblings to show that most large language models of that period were undertrained relative to their parameter counts. That finding reshaped how labs allocated compute between model size and training data for years afterward.
