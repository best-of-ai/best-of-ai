---
title: 'Granite Code'
name: 'Granite Code'
slug: 'granite-code'
subtitle: 'IBMのオープンウェイトコード生成モデルファミリー'
description: 'IBMのオープンウェイトコード生成モデルファミリー'
company: 'ibm'
model_type: 'Code'
logo_url: ''
product_url: 'https://www.ibm.com/granite'
price: 'Free'
rank: 4
release_date: '2024-05-06'
param_count: '3B, 8B, 20B, 34B'
context_window_tokens: 8192
modality: [text, code]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'IBM watsonx']
date: '2026-07-16'
tags: [llm, open-weight, code, self-hosted]
i18n_source: '10f0aa565ad0'
---
Granite CodeはIBMのオープンコードモデル群です。2024年5月に、30億、80億、200億、340億パラメータの4サイズで公開されました。それぞれ基盤版と指示チューニング版があります。IBM Researchは116のプログラミング言語からなる約3兆〜4兆トークンで学習しました。生のコードとコードに関する自然言語を組み合わせ、コード生成、バグ修正、コードの説明を1つのモデル群で扱います。Apache 2.0で公開され、企業はライセンス上の制約を気にせずファインチューニングして再展開できます。IBMはクローズドなコードアシスタントを避けたい企業を主な対象にしました。公開時のベンチマークでは、HumanEvalなどで同規模のオープンコードモデルと同等以上の結果を示しました。Hugging Face、Ollama、AWS Bedrock、SageMakerから利用でき、後の規模拡張で一部モデルのコンテキスト長は128Kになりました。
