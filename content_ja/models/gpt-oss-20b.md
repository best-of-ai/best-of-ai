---
title: 'GPT-OSS-20B'
name: 'GPT-OSS-20B'
slug: 'gpt-oss-20b'
subtitle: 'OpenAIのオープンウェイトモデル群のうち、小型で単体GPUに適したモデル'
description: 'OpenAIのオープンウェイトモデル群のうち、小型で単体GPUに適したモデル'
company: 'openai'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://openai.com/index/introducing-gpt-oss/'
price: 'Free'
rank: 7
release_date: '2025-08-05'
param_count: '21B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
mmlu_score: 85.3
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Together AI']
date: '2026-07-16'
tags: [llm, reasoning, open-weight, small-model, api]
i18n_source: '7a4a62f3cc31'
---
GPT-OSS-20Bは、OpenAIが2025年8月5日にGPT-OSS-120Bとともに公開した2つのオープンウェイトモデルのうち、小型のものです。GPT-2以来初のオープンモデルリリースでした。混合エキスパート方式を採用し、総パラメータ数は約210億、トークンごとに有効になるのは約36億です。16GB以上のメモリを持つ一般向けGPU 1基で動かせる軽さを目指し、サーバー級のハードウェアなしで推論モデルを使いたい開発者や愛好家向けに作られました。公開時のMMLUスコアは85.3で、同クラスとして高い結果でした。大きさを抑えながら、コーディング、数学、一般的な推論で上位モデルに近い性能を発揮します。Apache 2.0ライセンスで公開され、自由にファインチューニングや再配布ができます。Hugging Face、Together AI、OpenAI APIで利用でき、APIは自社運用に代わるマネージド環境を必要とするチーム向けです。
