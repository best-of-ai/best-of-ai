---
title: 'BTLM-3B'
name: 'BTLM-3B'
slug: 'btlm-3b'
subtitle: 'パラメータ数以上の性能が出るよう調整された、Cerebrasの小型オープンウェイトモデル'
description: 'パラメータ数以上の性能が出るよう調整された、Cerebrasの小型オープンウェイトモデル'
company: 'cerebras'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.cerebras.ai/blog/btlm-3b-8b-7b-parameter-performance-in-a-3-billion-parameter-model'
price: 'Free'
rank: 4
release_date: '2023-07-24'
param_count: '3B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, small-model]
i18n_source: '2c4fad8daa2c'
---

BTLM-3B-8Kは、CerebrasがOpentensor Foundationと作った30億パラメータの言語モデルで、Cerebrasのウェハースケールシステム、CS-2で学習しました。2023年の夏に発表され、70億パラメータのモデルに並ぶ品質を保ちつつ、スマートフォンやメモリの少ない機器で動くほど小さくする、という具体的な目標で設計されています。Cerebrasによると、BTLM-3Bは量子化すると約3GBのメモリに収まり、iPhone、Google Pixel、Raspberry Piといったハードウェアでも動きます。一般的なベンチマークでは、RedPajama-INCITE-7Bなど当時の7Bモデルと同程度の性能です。

モデルはSlimPajamaデータセットの6,270億トークンで学習されました。当時の競合する3Bモデルのいくつかより少ない量です。ALiBi位置埋め込みを使い、8,192トークンのコンテキスト長をネイティブにサポートし、それを超えてもそれなりに外挿できます。CerebrasはBTLM-3BをApache 2.0で公開したので、商用利用も無料です。MicrosoftやGoogleなどの新しい小型モデルに抜かれるまで、短い間、性能が最も高いオープンな3Bモデルの座にありました。
