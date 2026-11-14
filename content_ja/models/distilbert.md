---
title: 'DistilBERT'
name: 'DistilBERT'
slug: 'distilbert'
subtitle: 'Hugging Faceが作った、BERTを蒸留してサイズを40%小さくしつつ性能の大半を保ったバージョン'
description: 'Hugging Faceが作った、BERTを蒸留してサイズを40%小さくしつつ性能の大半を保ったバージョン'
company: 'hugging-face'
model_type: 'Language'
logo_url: ''
product_url: 'https://arxiv.org/abs/1910.01108'
price: 'Free'
rank: 7
release_date: '2019-10-02'
param_count: '66M'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, legacy, small-model]
i18n_source: '4bb37eb28b4c'
---

DistilBERTはGoogleのBERTを圧縮したバージョンで、Hugging Faceが2019年10月に公開しました。知識蒸留という手法を使い、事前学習の間に、小さな生徒モデルが大きな教師であるBERTの出力をまねるよう学習させています。パラメータ数は6600万で、元のBERT-baseより40%小さく、約60%速く動きます。それでいてGLUEベンチマークでは、BERTの性能の約97%を保ちます。SQuADの質問応答やIMDbの感情分類のようなタスクでは、サイズを削ったのに、本物のBERTとの差は数ポイントに収まります。

論文「DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter」はNLPで最も引用された論文の一つになりました。モデル自体も、モバイル端末を含む限られたハードウェアでBERT級の言語理解がほしいチームにとって、標準的な選択肢になりました。Apache 2.0ライセンスで公開されており、公開から何年たっても、Hugging Faceで最もダウンロードされているモデルの一つです。
