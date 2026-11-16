---
title: 'Megatron-Turing NLG'
name: 'Megatron-Turing NLG'
slug: 'megatron-turing-nlg'
subtitle: 'Das Forschungsmodell mit 530B Parametern von NVIDIA und Microsoft, eines der größten dichten LLMs seiner Zeit'
description: 'Das Forschungsmodell mit 530B Parametern von NVIDIA und Microsoft, eines der größten dichten LLMs seiner Zeit'
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
i18n_source: '06b0502910e0'
---
Megatron-Turing NLG ist ein dichtes Transformer-Sprachmodell mit 530 Milliarden Parametern, das NVIDIA und Microsoft gemeinsam trainierten und im Oktober 2021 ankündigten. Damals war es das größte trainierte monolithische Sprachmodell ohne Mixture-of-Experts. Es verband NVIDIAs Tensor-Parallelisierung aus Megatron-LM mit Microsofts Pipeline-Parallelisierung und dem ZeRO-Optimizer von DeepSpeed und lief auf Hunderten A100-GPUs. Das Modell hat 105 Transformer-Schichten und wurde mit einem Korpus von 270 Milliarden Tokens aus Webtexten, Büchern und anderen kuratierten Quellen trainiert.

Es diente vor allem als Forschungs- und Technikdemonstration dafür, wie weit sich dichte Modelle skalieren und verteilte Trainingssoftware einsetzen ließen, bevor Mixture-of-Experts-Architekturen zum praktischeren Weg für noch größere Modelle wurden. NVIDIA und Microsoft veröffentlichten Ergebnisse zu Textvervollständigung, Leseverständnis und Schlussfolgerungs-Benchmarks. Dabei übertraf das Modell kleinere Vorgänger wie GPT-3 und Turing-NLG. Das Modell selbst wurde jedoch nie als öffentliches Produkt oder API angeboten.
