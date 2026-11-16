---
title: 'Falcon 7B'
name: 'Falcon 7B'
slug: 'falcon-7b'
subtitle: 'TIIの小型Falcon。最初のFalcon公開を広める助けになった'
description: 'TIIの小型Falcon。最初のFalcon公開を広める助けになった'
company: 'technology-innovation-institute'
model_type: 'Language'
logo_url: ''
product_url: 'https://falconllm.tii.ae/'
price: 'Free'
rank: 5
release_date: '2023-05-25'
param_count: '7B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, small-model, legacy]
---

Falcon 7Bは、TIIが最初に公開したFalconのうち小さいほうのモデルです。Falcon 40Bと同じRefinedWebデータセットで学習しており、GPU1枚で安く動かせるサイズにしています。TIIは2023年の初めに約2週間かけて学習し、寛容なApache 2.0ライセンスで公開しました。そのため開発者は、ロイヤリティなしで商用に使い、改変し、展開できます。当時は、同程度のオープンモデルの多くが研究用途に限られていたため、このライセンスは目を引きました。Falcon 7Bは、40Bモデルと同じ、multiquery attention付きのデコーダー専用transformerを使います。コンテキスト長は2,048トークンで、必要な計算量が少ないため、2023年から2024年初めにかけて、ファインチューニングの実験やオンデバイス用途でよく選ばれました。その後TIIはFalcon 3とFalcon Mambaファミリーに移り、Falcon 7Bは旧世代のモデルとして、今もHugging Face上で広くミラーされています。
