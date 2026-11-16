---
title: 'ELECTRA'
name: 'ELECTRA'
slug: 'electra'
subtitle: '置換トークン検出の目的関数を使う、Googleのよりサンプル効率の高い事前学習の手法'
description: '置換トークン検出の目的関数を使う、Googleのよりサンプル効率の高い事前学習の手法'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://arxiv.org/abs/2003.10555'
price: 'Free'
rank: 6
release_date: '2020-03-23'
param_count: '335M'
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
i18n_source: 'f5cba0d29eb6'
---

ELECTRAはテキストエンコーダの事前学習の手法で、GoogleとStanfordの研究者がICLR 2020向けの論文で発表し、この手法で作った事前学習済みモデルのファミリーも出しました。BERTのマスク言語モデリングの目的関数では、ランダムに隠した単語をモデルが予測します。ELECTRAはそうではなく、小さな生成器にいくつかのトークンをもっともらしい別のものに置き換えさせ、識別器がどのトークンが入れ替えられたかを見抜くように学習します。この「置換トークン検出」の目的関数では、マスクされたトークンだけでなく系列内のすべてのトークンから学習の信号が得られます。そのため、事前学習のサンプル効率がずっと高くなります。

公開された最大のバージョンであるELECTRA-Largeは3億3500万パラメータで、RoBERTaやXLNetの4分の1の事前学習計算量で、それらに匹敵するGLUEスコアに達しました。計算量の予算を同じにすると、それらを明確に上回りました。Googleはコードと重みをApache 2.0ライセンスで公開しており、より小さなELECTRA-SmallとELECTRA-Baseは、BERT並みの精度がほしいが、BERT並みの学習コストは避けたいチームに選ばれてきました。
