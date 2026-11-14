---
title: 'Falcon Mamba 7B'
name: 'Falcon Mamba 7B'
slug: 'falcon-mamba-7b'
subtitle: 'TIIのオープンウェイトモデル。状態空間モデルのMambaアーキテクチャを採用'
description: 'TIIのオープンウェイトモデル。状態空間モデルのMambaアーキテクチャを採用'
company: 'technology-innovation-institute'
model_type: 'Language'
logo_url: ''
product_url: 'https://falconllm.tii.ae/'
price: 'Free'
rank: 3
release_date: '2024-08-12'
param_count: '7B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'TII Falcon Mamba 7B License 1.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, hybrid-architecture, self-hosted]
---

Falcon Mamba 7Bは、Technology Innovation Instituteが2024年8月に公開したモデルで、transformerのアテンションではなく、状態空間アーキテクチャのMambaだけで作られた、初の高性能な7Bオープン言語モデルです。アテンション機構がないため、生成する系列が長くなってもメモリ使用量と推論速度は一定です。系列長に応じて計算量が増えるtransformerとは違います。TIIは段階的に学習し、扱えるコンテキストを2,048トークンから8,192トークンまで広げました。ベンチマークの比較では、Mistral 7BやMetaのLlama 3.1 8Bなど、同じ規模のtransformerモデルに並ぶか上回りました。RecurrentGemma 9BやRWKV-v6といったtransformer以外のモデルも上回っています。重みはHugging FaceでTII独自のFalcon Mambaライセンスのもと配布されています。長い系列を扱う処理で、アテンション型とは別の選択肢がほしい研究者や開発者が対象です。
