---
title: 'BLOOMZ'
name: 'BLOOMZ'
slug: 'bloomz'
subtitle: '言語をまたぐ指示に従うよう学習した、BLOOMの指示チューニング版'
description: '言語をまたぐ指示に従うよう学習した、BLOOMの指示チューニング版'
company: 'hugging-face'
model_type: 'Language'
logo_url: ''
product_url: 'https://huggingface.co/bigscience/bloomz'
price: 'Free'
rank: 5
release_date: '2022-11-03'
param_count: '176B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'RAIL License'
api_available: false
access_methods: [Self-hosted]
runs_at_home: false
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, multilingual, legacy]
i18n_source: '9dff7db95770'
---

BLOOMZは、BigScienceによるBLOOMの指示チューニング版で、2022年末に公開されました。1,760億パラメータのベースモデルを、自然言語の指示として書かれた多言語タスクの大規模なコレクションxP3でファインチューンしています。このプロジェクトの狙いは言語をまたぐ汎化でした。BLOOMZは主に英語の指示でチューニングされましたが、BLOOMの元の事前学習で出会った言語であれば、ファインチューンで指示と組み合わせて見ていない言語でも、指示に従えることを示しました。指示に従う能力が、言語ごとに別々のチューニングを要さず、言語間で転移することを示した、初期の公開デモの1つです。

BLOOMと同じく、BLOOMZはベースモデルの2,048トークンのコンテキスト長と、密なTransformerのアーキテクチャを引き継いでいます。ライセンスも同じRAILで、広い用途を認めつつ、禁止する用途のリストがあります。今は、本番のチャットモデルというより、多言語の指示チューニングを研究する人の関心が中心です。新しい指示チューニング済みのオープンモデルのほうが、同程度かそれ以下の計算コストで、品質が高くコンテキスト長もはるかに長いためです。
