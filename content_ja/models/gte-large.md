---
title: 'GTE-large'
name: 'GTE-large'
slug: 'gte-large'
subtitle: '検索と意味類似度判定向けのAlibaba汎用テキスト埋め込みモデル'
description: '検索と意味類似度判定向けのAlibaba汎用テキスト埋め込みモデル'
company: 'alibaba'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://huggingface.co/thenlper/gte-large'
price: 'Free'
rank: 5
release_date: '2023-08-07'
param_count: '335M'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Alibaba Cloud']
date: '2026-07-16'
tags: [embedding, open-weight, api]
i18n_source: '25ba91e27698'
---
GTE-largeはAlibaba DAMO Academyのテキスト埋め込みモデルです。2023年半ば、GTE-baseやGTE-smallとともにGeneral Text Embeddings（GTE）シリーズの一部としてHugging Faceで公開されました。335百万パラメータのBERT系エンコーダーで、ウェブと専門分野の幅広いテキストを使った複数段階の対照学習で訓練されています。最大512トークンの入力から1024次元のベクトルを生成します。検索、意味検索、クラスタリング、再ランキングを想定しており、公開時のMTEBベンチマークでは同規模のオープン埋め込みモデルの中で高いスコアを記録し、中国の他研究所のBGEやE5系と競いました。Apache 2.0のオープンウェイトで、推論は単一GPUまたはCPUで実行できます。Hugging FaceとAlibaba Cloudから利用でき、APIに依存しないコンパクトな埋め込みモデルを求めるチームによく使われています。
