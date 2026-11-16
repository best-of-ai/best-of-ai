---
title: 'jina-embeddings-v3'
name: 'jina-embeddings-v3'
slug: 'jina-embeddings-v3'
subtitle: 'Jina AIのオープンウェイト多言語埋め込みモデル'
description: 'Jina AIのオープンウェイト多言語埋め込みモデル'
company: 'jina-ai'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://jina.ai/embeddings/'
price: 'Free'
rank: 4
release_date: '2024-09-18'
param_count: '570M'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'CC-BY-NC 4.0'
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [embedding, open-weight, retrieval, multilingual]
i18n_source: '881f6947c894'
---
jina-embeddings-v3はJina AIが2024年9月に公開した多言語テキスト埋め込みモデルです。5億7,000万のパラメータを持ち、89言語と、ロータリー位置埋め込みを使う8,192トークンのコンテキスト長に対応します。クエリと文書の検索、クラスタリング、分類、テキスト照合など、用途別のLoRAアダプターを使います。モデル全体を再学習しなくても、同じ重みを複数の作業向けに調整できます。Matryoshka表現学習にも対応し、検索品質の大部分を維持したまま、標準の1,024次元から最低32次元まで出力埋め込みを短縮できます。Jina AIの報告では、MTEBで英語タスクにおいてOpenAIやCohereの非公開埋め込みを上回り、多言語タスクではmultilingual-e5-large-instructを上回りました。CC BY-NC 4.0ライセンスで公開され、研究・評価には無料で使えますが、大規模な商用利用には商用ライセンスが必要です。
