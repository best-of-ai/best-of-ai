---
title: 'Aquila2'
name: 'Aquila2'
slug: 'aquila2'
subtitle: 'BAAIの第2世代バイリンガル基盤モデルファミリー'
description: 'BAAIの第2世代バイリンガル基盤モデルファミリー'
company: 'baai'
model_type: 'Language'
logo_url: ''
product_url: 'https://github.com/FlagAI-Open/Aquila2'
price: 'Free'
rank: 4
release_date: '2023-10-16'
param_count: '34B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'BAAI License'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, multilingual]
i18n_source: '41c2600cced5'
---

Aquila2は、北京智源人工知能研究院（BAAI）の第2世代のバイリンガルモデルファミリーで、2023年10月に最初のAquilaの後継としてリリースされました。7Bと34Bのベースモデル、チャット向けにチューニングしたAquilaChat2、位置エンコーディングの補間で1万6,000トークンまで広げた長いコンテキスト長の版、さらに試験的な70Bのチェックポイントがあります。BAAIは、公開時点の中国語ベンチマークで、Aquila2-34Bが同規模のほかの中国語・英語のオープンモデルを上回ったと報告しています。

コードベースはApache 2.0ライセンスで公開されています。モデルの重みはBAAI独自のAquilaライセンス契約の下にあり、一定の条件で商用利用ができます。Aquila2は、LLaMAなど欧米のベースモデルに頼らずに高いバイリンガル性能を求める開発者を対象にしていました。その後BAAIがFlagEmbeddingなどの専用モデルに力を移すまで、BAAIの主要なオープンリリースの1つであり続けました。
