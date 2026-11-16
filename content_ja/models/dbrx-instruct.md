---
title: 'DBRX Instruct'
name: 'DBRX Instruct'
slug: 'dbrx-instruct'
subtitle: 'DatabricksのオープンウェイトモデルDBRXを指示チューニングしたバージョン'
description: 'DatabricksのオープンウェイトモデルDBRXを指示チューニングしたバージョン'
company: 'databricks'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm'
price: 'Free'
rank: 4
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
tags: [llm, open-weight, instruction-tuned, self-hosted]
extra_model_types: ['Code']
i18n_source: '2f1996df20fb'
---

DBRX InstructはDatabricksのDBRXモデルをファインチューンしてチャットですぐ使えるようにしたバージョンで、2024年3月にDBRXのベースモデルと同時に公開されました。細粒度のMixture-of-Expertsアーキテクチャで、総パラメータ数は1320億ですが、1トークンごとに動くのは360億だけです。テキストとコード12兆トークンで学習しています。Databricksは指示への追従と複数ターンの会話に特化して調整しており、公開時にはMMLU(73.7%対70.0%)とHumanEval(70.1%対48.1%)でGPT-3.5を上回ったと報告しています。コンテキスト長は32,000トークンで、Databricks Open Model Licenseで配布されます。このライセンスは商用利用を認めており、ごく大規模な運用には一部制限があります。利用はDatabricksのプラットフォーム経由か、Hugging Faceの重みを自前でホストする形です。
