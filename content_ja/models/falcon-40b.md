---
title: 'Falcon 40B'
name: 'Falcon 40B'
slug: 'falcon-40b'
subtitle: 'TIIの初期のオープンウェイトモデル。Falcon 180Bの前にランキング首位だった'
description: 'TIIの初期のオープンウェイトモデル。Falcon 180Bの前にランキング首位だった'
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
---

Falcon 40Bは、Technology Innovation Instituteが2023年5月に公開した、400億パラメータのデコーダー専用の因果言語モデルです。TIIが自前で集めて選別した大規模ウェブデータセットのRefinedWebから約1兆トークンを使い、一部の追加コーパスと組み合わせて学習しました。公開時点で、オープンソースモデルの中ではHugging FaceのOpen LLM Leaderboardの首位でした。MMLUは82.7、HumanEvalは76.3で、MPTやRedPajamaといった同時期のモデルを上回り、より大きいMetaのLlama 2 70Bともいくつかのベンチマークで競っています。アーキテクチャにはmultiquery attentionとFlashAttentionを使い、サイズのわりに推論コストを抑えています。TIIはロイヤリティなしのApache 2.0ライセンスで公開しました。この規模のモデルとしては当時めずらしい寛容な選択で、AWS SageMaker JumpStartでの提供を含め、企業での早い時期の採用につながりました。その後、Falcon 40BはFalcon 180BとFalcon 3ファミリーに世代交代し、2,048トークンのコンテキスト長は現在のモデルと比べると小さく見えます。
