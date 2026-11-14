---
title: 'BGE-large-en'
name: 'BGE-large-en'
slug: 'bge-large-en'
subtitle: 'BAAIの、英語検索向けに広く使われている汎用の埋め込みモデル'
description: 'BAAIの、英語検索向けに広く使われている汎用の埋め込みモデル'
company: 'baai'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://huggingface.co/BAAI/bge-large-en-v1.5'
price: 'Free'
rank: 6
release_date: '2023-09-15'
param_count: '335M'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'MIT'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [embedding, open-weight, api]
i18n_source: 'f70b29aa405b'
---

BGE-large-en-v1.5は、北京智源人工知能研究院（BAAI）のテキスト埋め込みモデルで、2023年9月に公開されました。数週間前に出た初代のBGE-large-enの更新版にあたります。パラメータ数は3億3,500万、埋め込みは1024次元で、扱える系列は512トークンまでです。後に出てきた大きなデコーダベースの埋め込みモデルではなく、ほかのBERT規模のエンコーダモデルと同じ大きさのクラスに入ります。v1.5の更新では、初版の類似度スコアの分布の問題を主に直し、タスク別の指示のプレフィックスなしで使ったときの検索品質も改善しました。v1では、ここが粗い部分でした。BAAIはMITライセンスで公開し、無料で、動きが速く、サイズの割にMTEBベンチマークで良いスコアを出したことから、英語の検索やRAGパイプライン向けのオープンな埋め込みモデルとして最も広く使われるものの1つになりました。その後、BGE-M3のようにより大きく高性能なBAAIのモデルも加わりましたが、軽量なセルフホストの検索では、今も定番のデフォルトです。
