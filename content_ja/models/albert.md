---
title: 'ALBERT'
name: 'ALBERT'
slug: 'albert'
subtitle: 'GoogleによるBERTのパラメータ共有版。大規模でも効率よく動くよう設計'
description: 'GoogleによるBERTのパラメータ共有版。大規模でも効率よく動くよう設計'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://arxiv.org/abs/1909.11942'
price: 'Free'
rank: 6
release_date: '2019-09-26'
param_count: '223M'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, legacy, foundation-model]
i18n_source: '4c3c3afa8529'
---

ALBERT（A Lite BERT）は、Google ResearchとToyota Technological Instituteが2019年9月に発表した言語表現モデルで、BERTの後継にあたります。埋め込みの因数分解とレイヤー間のパラメータ共有という2つの削減手法で、パラメータ数を大きく減らしながら、はるかに大きなモデルに並ぶ精度を保ちます。最大構成のALBERT-xxlargeは約2億2,300万パラメータで、BERT-largeの約18分の1です。それでも学習は速く、公開時点でGLUE、SQuAD 2.0、RACEの最高スコアを更新しました。

ALBERTはBERTと同じくエンコーダのみのモデルです。分類、質問応答、読解といった理解タスク向けで、自由な文章生成には向きません。入力は1シーケンスあたり512トークンまでです。Googleはコードと学習済みの重みを公開しており、2020年代初めには、デコーダのみの生成モデルが注目を集める前のNLP研究や実運用で、よく使われるベースラインになりました。
