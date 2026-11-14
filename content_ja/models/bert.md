---
title: 'BERT'
name: 'BERT'
slug: 'bert'
subtitle: 'NLP研究のあり方を変えた、Googleの2018年の双方向エンコーダ'
description: 'NLP研究のあり方を変えた、Googleの2018年の双方向エンコーダ'
company: 'google'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://github.com/google-research/bert'
price: 'Free'
rank: 6
release_date: '2018-10-11'
param_count: '340M'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [embedding, open-weight, nlp, legacy]
i18n_source: '9489893b9c63'
---

BERT（Bidirectional Encoder Representations from Transformers）は、Google Researchが2018年10月に発表した言語モデルで、NLPタスクの事前学習に対する分野の考え方を変えました。テキストを左から右へ読む従来のモデルとは違い、BERTはマスクした単語の予測と次の文の予測で学習します。そのため、両方向の文脈を同時に使った表現を作れます。Googleは主に2つのサイズを公開しました。1億1,000万パラメータのBERT-baseと、3億4,000万パラメータのBERT-largeで、どちらも入力は512トークンまでです。重みはApache 2.0でGitHub、後にHugging Faceで自由に入手できます。ファインチューンしたBERTは、公開時に質問応答や自然言語推論を含む11のNLPベンチマークで新記録を出しました。分類、固有表現抽出、検索ランキングなどのタスクで、ファインチューンする標準的なベースモデルになりました。現在ではRoBERTaやDeBERTaといった新しいエンコーダモデルや、その後の埋め込みモデルにほとんど置き換えられていますが、NLPで最も引用された論文の1つであり、そのアーキテクチャは後のエンコーダベースのシステムの多くの土台になっています。
