---
title: 'DBRX'
name: 'DBRX'
slug: 'dbrx'
subtitle: 'DatabricksのオープンウェイトのMixture-of-Expertsモデル'
description: 'DatabricksのオープンウェイトのMixture-of-Expertsモデル'
company: 'databricks'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm'
price: 'Free'
rank: 5
release_date: '2024-03-27'
param_count: '132B (36B active)'
context_window_tokens: 32000
modality: [text]
open_weight: true
license: 'Databricks Open Model License'
api_available: true
mmlu_score: 73.7
humaneval_score: 70.1
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Databricks']
date: '2026-07-16'
tags: [llm, open-weight, mixture-of-experts, self-hosted]
extra_model_types: ['Code']
i18n_source: 'c49f11ecc44d'
---

DBRXはDatabricksのオープンウェイトの大規模言語モデルで、指示チューニング版のDBRX Instructのベースモデルとして2024年3月に公開されました。細粒度のMixture-of-Expertsモデルで、総パラメータ数は1320億、1トークンあたりの有効パラメータ数は360億です。テキストとコード12兆トークンを使い、DatabricksのMosaic AI学習スタックでゼロから学習しています。公開時にDatabricksは、MMLUやHumanEvalなどのベンチマークで、Llama 2 70BやMixtralを含む当時の他のオープンモデルを上回ったと報告しました。企業向けのビジネスを手がける会社でも、大手ラボ並みの研究予算に頼らず競争力のある基盤モデルを学習できる、という実例として打ち出されました。コンテキスト長は32,000トークンで、Databricks Open Model Licenseで公開されています。重みはHugging Faceにあり、自前でホストするか、Databricksの配信基盤から使えます。
