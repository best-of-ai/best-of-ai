---
title: 'CLIP (LAION variant)'
name: 'CLIP (LAION variant)'
slug: 'clip-laion-variant'
subtitle: 'LAIONが再学習した、オープンウェイトのCLIP視覚言語エンベディングモデル'
description: 'LAIONが再学習した、オープンウェイトのCLIP視覚言語エンベディングモデル'
company: 'laion'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://laion.ai/'
price: 'Free'
rank: 4
release_date: '2022-09-15'
param_count: '428M'
modality: [text, image]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [embedding, open-weight, vision, self-hosted]
i18n_source: '40efbd85bd2a'
---

このCLIPバリアントは、OpenAIの元のCLIPアーキテクチャをオープンウェイトで再学習したものです。LAIONが作り、OpenAI自身ではなくopen_clipプロジェクトを通じて配布されています。ViT-L/14の視覚Transformerをバックボーンに使い、パラメータ数は約4億2800万です。学習には、より大きなLAION-5Bデータセットのうち英語の20億の画像とテキストのペアから成るLAION-2Bを使い、JUWELSスーパーコンピュータの384基のA100 GPUを使いました。元のCLIPと同様に、画像とテキストを共通のエンベディング空間に写します。そのため、タスク固有のファインチューニングなしで、ゼロショットの画像分類、画像とテキストの検索、類似検索ができ、ImageNet-1kのゼロショット精度は約75.3パーセントです。重みはオープンなライセンスで公開され、Hugging Faceに置かれているため、OpenAIのクローズドなCLIPチェックポイントの代わりとして、オープンソースの画像検索、キャプション生成、生成アートのパイプラインで広く使われています。いくつかのStable Diffusionのバリアントでは、テキストエンコーダとしても使われています。
