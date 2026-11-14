---
title: 'DeepSeek-MoE-16B'
name: 'DeepSeek-MoE-16B'
slug: 'deepseek-moe-16b'
subtitle: 'DeepSeekが早い時期に出した細粒度のMixture-of-Expertsモデルで、のちのMoEアーキテクチャの下地になった'
description: 'DeepSeekが早い時期に出した細粒度のMixture-of-Expertsモデルで、のちのMoEアーキテクチャの下地になった'
company: 'deepseek'
model_type: 'Language'
logo_url: ''
product_url: 'https://github.com/deepseek-ai/DeepSeek-MoE'
price: 'Free'
rank: 5
release_date: '2024-01-11'
param_count: '16.4B'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'DeepSeek License'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, mixture-of-experts, legacy]
i18n_source: '61ec60299e14'
---

DeepSeek-MoE-16Bは2024年1月に公開された、DeepSeekによる細粒度Mixture-of-Expertsアーキテクチャの初期の試みで、その設計上の選択はのちのV2やV3にも引き継がれました。総パラメータ数は164億ですが、1トークンあたりの有効パラメータ数は約28億だけです。これは論文で説明された2つの手法によるものです。エキスパートをより小さく専門的な単位に分けることと、共通の知識を捉えるために常に動く共有エキスパートを分離することです。英語と中国語の2兆トークンでゼロから学習し、密結合のDeepSeek 7BやLlama 2 7Bと同程度の性能に達しながら、推論時の計算量はそれらの約40%で済みます。コンテキスト長は4,096トークンで、DeepSeekのオープンライセンスで公開され、自前でのホストが可能です。本番利用を重視した公開というより、エキスパートの専門化を示す研究上のデモという性格が強いモデルです。
