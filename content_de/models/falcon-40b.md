---
title: 'Falcon 40B'
name: 'Falcon 40B'
slug: 'falcon-40b'
subtitle: 'Das frühere offene Modell von TII, das vor Falcon 180B Bestenlisten anführte'
description: 'Das frühere offene Modell von TII, das vor Falcon 180B Bestenlisten anführte'
company: 'technology-innovation-institute'
model_type: 'Language'
logo_url: ''
product_url: 'https://falconllm.tii.ae/'
price: 'Free'
rank: 4
release_date: '2023-05-25'
param_count: '40B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
mmlu_score: 82.7
humaneval_score: 76.3
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted, legacy]
extra_model_types: ['Code']
i18n_source: '109766ee6da4'
---
Falcon 40B ist ein kausales Sprachmodell mit ausschließlich Decoder und 40 Milliarden Parametern. Es wurde im Mai 2023 vom Technology Innovation Institute veröffentlicht. Trainiert wurde es mit etwa einer Billion Tokens aus RefinedWeb, einem umfangreichen Webdatensatz, den TII selbst zusammenstellte und filterte, sowie ausgewählten zusätzlichen Korpora. Bei der Veröffentlichung führte es die Open-LLM-Bestenliste von Hugging Face unter den offenen Modellen an. Mit 82,7 Punkten bei MMLU und 76,3 bei HumanEval lag es vor damaligen Konkurrenten wie MPT und RedPajama und konkurrierte bei mehreren Benchmarks mit dem größeren Llama 2 70B von Meta. Multiquery-Attention und FlashAttention senken die Inferenzkosten im Verhältnis zur Größe. TII veröffentlichte es gebührenfrei unter Apache 2.0 – für ein Modell dieser Größenordnung damals ungewöhnlich freizügig. Das trug zur frühen Nutzung in Unternehmen bei, unter anderem über AWS SageMaker JumpStart. Falcon 40B wurde inzwischen durch Falcon 180B und die Falcon-3-Familie abgelöst. Sein Kontextfenster von 2048 Tokens ist gegenüber heutigen Modellen klein.
