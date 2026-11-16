---
title: 'Jina Embeddings v2'
name: 'Jina Embeddings v2'
slug: 'jina-embeddings-v2'
subtitle: '公開時に8Kトークンのコンテキスト長が注目されたJina AIの埋め込みモデル'
description: '公開時に8Kトークンのコンテキスト長が注目されたJina AIの埋め込みモデル'
company: 'jina-ai'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://jina.ai/news/jina-embeddings-2-the-best-solution-for-embedding-long-documents/'
price: 'Free'
rank: 5
release_date: '2023-10-30'
param_count: '137M'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Jina API']
date: '2026-07-16'
tags: [embedding, open-weight, api, legacy]
i18n_source: '9b381be032d7'
---
Jina Embeddings v2はJina AIが2023年10月に公開したテキスト埋め込みモデルです。主に2つのサイズがあり、小型版は3,300万、ベース版は1億3,700万のパラメータを備えます。どちらも標準的な位置埋め込みの代わりにALiBi位置エンコーディングを使うよう変更したBERTアーキテクチャを基にしています。この方式により、当時のオープンな埋め込みモデルでは珍しい最大8,192トークンの系列を処理でき、モデルサイズを大幅に抑えながら長文書の検索でOpenAIの非公開モデルtext-embedding-ada-002に対抗しました。Apache 2.0ライセンスで公開され、ローカル実行とJina APIの両方に対応します。多言語対応と用途別アダプターを加えたjina-embeddings-v3に後継しましたが、小型である利点を生かし、英語の検索用途では今も使われています。
