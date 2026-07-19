---
title: 'Megatron-Turing NLG'
name: 'Megatron-Turing NLG'
slug: 'megatron-turing-nlg'
subtitle: 'NVIDIA and Microsoft''s 530B-parameter research model, among the largest dense LLMs of its time'
description: 'NVIDIA and Microsoft''s 530B-parameter research model, among the largest dense LLMs of its time'
company: 'nvidia'
model_type: 'Language'
logo_url: ''
product_url: 'https://developer.nvidia.com/megatron-turing-natural-language-generation'
price: 'Paid'
rank: 5
release_date: '2021-10-11'
param_count: '530B'
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [llm, research, legacy]
extra_model_types: ['Reasoning']
---

Megatron-Turing NLG is a 530 billion parameter dense transformer language model that NVIDIA and Microsoft trained jointly and announced in October 2021. At the time it was the largest monolithic (non-mixture-of-experts) language model ever trained, built by combining NVIDIA's Megatron-LM tensor-parallelism with Microsoft's DeepSpeed pipeline-parallelism and ZeRO optimizer across hundreds of A100 GPUs. The model has 105 transformer layers and was trained on a 270 billion token corpus drawn from web text, books, and other curated sources.

It served mainly as a research and engineering demonstration of how far dense-model scaling and distributed training software could go before mixture-of-experts architectures became the more practical path to larger models. NVIDIA and Microsoft published results on completion, reading comprehension, and reasoning benchmarks where it outperformed smaller predecessors like GPT-3 and Turing-NLG, but the model itself was never opened up as a public product or API.
