---
title: 'ByT5'
name: 'ByT5'
slug: 'byt5'
subtitle: '生のバイトを直接扱う、GoogleのトークンフリーなT5の派生モデル'
description: '生のバイトを直接扱う、GoogleのトークンフリーなT5の派生モデル'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://arxiv.org/abs/2105.13626'
price: 'Free'
rank: 4
release_date: '2021-05-28'
param_count: '13B'
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, legacy, research]
i18n_source: 'e8007dd611dd'
---

ByT5は、GoogleのテキストtoテキストモデルT5の派生モデルで、Google Researchが2021年半ばに発表しました。トークン化を完全にやめ、生のUTF-8のバイトを直接扱う点が特徴です。標準的な言語モデルは、トークナイザーが作る固定の語彙で、テキストをサブワードのトークンに分けます。この語彙が想定した言語や文字体系ではうまく動きますが、まれな単語、誤字、あまり使われない言語は苦手になりがちです。ByT5はあらゆる入力をバイト列として扱うことでこれを避け、数万のサブワードトークンの代わりに、数百種類の値だけからなる語彙を持ちます。

引き換えに、同じテキストでもバイト列はトークン列よりずっと長くなります。そのため、標準的なベンチマークでトークンベースのモデルに並ぶには、より深いエンコーダと、入力あたりのより多くの計算が必要です。Googleは約130億パラメータのByT5-XXLまでのサイズのByT5ファミリーを公開し、すべてのチェックポイントをHugging FaceでApache 2.0のもと公開しています。ノイズの多いテキスト、翻字、リソースの少ない文字体系を含む多言語タスクで特に良い成績でした。本番の言語モデルの大半は効率の面でトークンベースの手法にとどまっていますが、トークンを使わない、文字単位のモデリングの研究では参照点になっています。
