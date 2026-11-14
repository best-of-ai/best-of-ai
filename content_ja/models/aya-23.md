---
title: 'Aya 23'
name: 'Aya 23'
slug: 'aya-23'
subtitle: '23言語に対応する、Cohere For AIのオープンウェイトの多言語モデル'
description: '23言語に対応する、Cohere For AIのオープンウェイトの多言語モデル'
company: 'cohere'
model_type: 'Language'
logo_url: ''
product_url: 'https://cohere.com/research/aya'
price: 'Free'
rank: 5
release_date: '2024-05-27'
param_count: '35B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'CC-BY-NC 4.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, multilingual]
i18n_source: '7472f170a470'
---

Aya 23は、Cohereの研究組織Cohere For AIが2024年5月に公開した多言語の言語モデルファミリーです。英語に加え、アラビア語、中国語、ヒンディー語、日本語、ロシア語、スペイン語など23言語に対応します。8Bと35Bの2サイズがあり、どちらもCohereのCommandアーキテクチャをベースに、事前学習済みのチェックポイントから初期化して、さらに多言語で学習しています。ここで取り上げているのは35B版で、コンテキスト長は8192トークンです。英語中心のオープンモデルでは手薄になりがちな言語で、検索や指示への追従のタスクを想定しています。Cohereは、許容される使い方の追加条項付きのCC-BY-NC 4.0ライセンスで重みを公開しました。研究と非商用なら無料で使えますが、本番の運用には別途商用契約が必要です。101言語のデータと評価に取り組んだ最初のAyaプロジェクトに続くもので、対象言語を絞る代わりに、言語ごとの品質を高めました。
