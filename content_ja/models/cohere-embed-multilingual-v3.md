---
title: 'Cohere Embed Multilingual v3'
name: 'Cohere Embed Multilingual v3'
slug: 'cohere-embed-multilingual-v3'
subtitle: '100以上の言語での検索に合わせて調整された、Cohereのエンベディングモデル'
description: '100以上の言語での検索に合わせて調整された、Cohereのエンベディングモデル'
company: 'cohere'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://cohere.com/blog/introducing-embed-v3'
price: 'Paid'
rank: 6
release_date: '2023-11-02'
param_count: 'Undisclosed'
context_window_tokens: 512
modality: [text]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.1
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['Cohere API']
date: '2026-07-16'
tags: [embedding, api, multilingual]
i18n_source: '5c2674ca56c9'
---

Cohere Embed Multilingual v3は、Cohereが2023年11月に公開したテキストエンベディングモデルで、100を超える言語での検索、検索拡張生成、意味的な類似性のタスクに使います。入力は最大512トークンのテキストで、既定では1024次元のベクトルを出力します。より高速な検索や低い保存コストが必要な場合は、384次元や768次元の短いエンベディングにも対応します。Cohereは英語専用の姉妹モデルであるEmbed English v3と並べて学習しました。どちらもv2からのアップグレードとして位置づけています。パッセージを、似ているかどうかだけでなく、関連性が高そうかどうかで重みづけるため、RAGパイプラインでのノイズの多い検索結果が減るためです。Cohere APIでの料金は100万トークンあたり0.10ドルで、AWS、Azure、Oracle Cloudのマーケットプレイスからも配布されています。Cohereはその後、新しいEmbed v4モデルを出しており、Oracleのような一部のクラウドプロバイダーは、v3を旧世代または非推奨の選択肢として掲載しています。ただしCohere自身のAPIとHugging Faceでは、引き続き使えます。
