---
title: 'Cohere Embed v3'
name: 'Cohere Embed v3'
slug: 'cohere-embed-v3'
subtitle: 'RAGと検索向けの、Cohereの多言語テキストエンベディングモデル'
description: 'RAGと検索向けの、Cohereの多言語テキストエンベディングモデル'
company: 'cohere'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://cohere.com/embed'
price: 'Paid'
rank: 5
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
platforms: ['Cohere Platform']
date: '2026-07-16'
tags: [embedding, retrieval, rag, api]
i18n_source: '7f7e30fb76b2'
---

Cohere Embed v3は、Cohereが2023年11月に公開したテキストエンベディングモデルで、検索、検索拡張生成、セマンティック検索のアプリケーション向けです。英語版と多言語版があり、多言語版は100を超える言語で学習されています。MIRACLベンチマークでは、前の世代より検索精度が約35%向上しました。呼び出す側は、テキストが検索クエリか文書かを指定でき、それに応じてエンベディング空間が調整されて、検索精度が上がります。Cohereが提供するAPIからのみ使え、料金は入力が100万トークンあたり0.10ドルで、入力は最大512トークンまで受け付けます。Embed v3は、OpenAIのtext-embedding-3やVoyage AIのエンベディングモデルと並んで、RAGパイプラインの標準的な選択肢になりました。2025年にCohereがマルチモーダルのEmbed v4を出すまでのことです。
