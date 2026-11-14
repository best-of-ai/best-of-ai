---
title: 'Hermes 3'
name: 'Hermes 3'
slug: 'hermes-3'
subtitle: '操作性と推論に重点を置くNous Researchのオープンウェイト調整モデル'
description: '操作性と推論に重点を置くNous Researchのオープンウェイト調整モデル'
company: 'nous-research'
model_type: 'Language'
logo_url: ''
product_url: 'https://nousresearch.com/hermes3/'
price: 'Free'
rank: 4
release_date: '2024-08-27'
param_count: '405B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Llama 3.1 Community License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: false
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, fine-tune, self-hosted]
i18n_source: 'b20d0dae77b1'
---
Hermes 3は、Nous ResearchがMetaのLlama 3.1 405Bをベースに開発したオープンウェイト言語モデルです。2024年8月、軽量アダプターではなく全パラメータを調整したモデルとして公開されました。システムプロンプトによる制御、エージェント型のツール利用、長い推論を通じて、利用者がモデルをより細かく操作できるようにすることを目指しています。8B、70B、405Bの3サイズがあり、主にNousが選別した合成データで訓練されました。構造化出力や関数呼び出しにも対応し、エージェントのバックエンドとして使えます。公開ベンチマークではARC、HellaSwag、IFEvalなどでMetaのLlama 3.1 Instructと同等以上の結果を出し、コミュニティ製の調整モデルが開発元の公式モデルと競う形になりました。Llama 3.1ライセンスのもとで重みが公開され、405Bモデルを自社環境で動かすほか、独自APIではなく外部の推論サービスを利用することもできます。
