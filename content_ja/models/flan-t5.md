---
title: 'Flan-T5'
name: 'Flan-T5'
slug: 'flan-t5'
subtitle: 'Googleの指示チューニング済みオープンウェイトモデル。T5の後継'
description: 'Googleの指示チューニング済みオープンウェイトモデル。T5の後継'
company: 'google'
model_type: 'Language'
logo_url: ''
product_url: 'https://huggingface.co/google/flan-t5-xxl'
price: 'Free'
rank: 4
release_date: '2022-10-20'
param_count: '11B'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, instruction-tuned, legacy]
---

Flan-T5は、Googleが2022年10月に公開した、テキストからテキストへ変換するtransformer、T5の指示チューニング版です。基本のアーキテクチャは変えず、指示の形で書かれた1,000を超えるタスクでT5をファインチューニングしています。タスクは翻訳、要約、推論、分類にわたり、言語も多岐にわたります。このファインチューニングで、そのままでも、素のT5よりずっと使いやすくなりました。素のT5は、よい性能を出すにはタスクごとのチューニングが必要でした。Googleはこのファミリーを複数のサイズで公開しました。小さいものは8000万パラメータ、大きいものはFlan-T5-XXLの110億パラメータで、すべてApache 2.0ライセンスのもと、Hugging Faceから自由にダウンロードできます。512トークンのコンテキスト長は今の基準では短く、扱えるのは短い文書やプロンプトに限られます。指示チューニングの研究では今もよくベースラインとして使われます。また、大きなデコーダー専用のLLMを動かす計算コストをかけずに、単純なNLPタスクのためにオープンでセルフホストできるモデルがほしいチームにとって、軽い選択肢でもあります。
