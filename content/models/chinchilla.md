---
title: 'Chinchilla'
name: 'Chinchilla'
slug: 'chinchilla'
subtitle: 'DeepMind''s 2022 research model that reset scaling-law assumptions for LLM training'
description: 'DeepMind''s 2022 research model that reset scaling-law assumptions for LLM training'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://deepmind.google/discover/blog/an-empirical-analysis-of-compute-optimal-large-language-model-training/'
price: 'Paid'
rank: 4
release_date: '2022-03-29'
param_count: '70B'
context_window_tokens: 2048
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: false
mmlu_score: 67.5
access_methods: [Self-hosted]
platforms: []
date: '2026-07-16'
tags: [llm, research, legacy]
---

Chinchilla is a research language model that DeepMind described in a March 2022 paper on compute-optimal training. At 70 billion parameters, it is much smaller than DeepMind's earlier 280 billion parameter Gopher model, yet Chinchilla was trained on roughly four times more data and beat Gopher, GPT-3, and other larger models of the era on a wide range of benchmarks, including an average MMLU score around 67.5%. The paper's core finding was that most large language models up to that point were undertrained relative to their size: for a fixed compute budget, model size and training data should scale together, not just model size alone.

That result, now widely known as the Chinchilla scaling law, reshaped how labs planned training runs afterward, pushing the field toward smaller models trained on much larger datasets instead of simply growing parameter counts. DeepMind never released Chinchilla's weights or offered any public access to it; it exists only as a research artifact described in the paper. Its influence shows up indirectly in nearly every major model trained since, from LLaMA to GPT-4, all of which cite compute-optimal scaling as part of their training methodology.
