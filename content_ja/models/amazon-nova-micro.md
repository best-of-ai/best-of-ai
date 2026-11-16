---
title: 'Amazon Nova Micro'
name: 'Amazon Nova Micro'
slug: 'amazon-nova-micro'
subtitle: '単純なテキストタスク向けの、Novaで最速かつ最安のティア'
description: '単純なテキストタスク向けの、Novaで最速かつ最安のティア'
company: 'amazon'
model_type: 'Language'
logo_url: ''
product_url: 'https://aws.amazon.com/ai/generative-ai/nova/'
price: 'Paid'
rank: 5
release_date: '2024-12-03'
param_count: 'Undisclosed'
context_window_tokens: 128000
modality: [text]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.035
output_price_usd_per_m: 0.14
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['AWS Bedrock']
date: '2026-07-16'
tags: [llm, low-cost, api]
i18n_source: '8a91538f6295'
---

Amazon Nova Microは、AmazonのNovaラインナップで最小かつ最安のモデルです。2024年12月にファミリーのほかのモデルと同時に発表され、Amazon Bedrockから使えます。入力も出力もテキストのみで、コンテキスト長は12万8,000トークン、料金は入力が100万トークンあたり0.035ドル、出力が0.14ドルです。GPT-4o miniやGemini Flash-Liteのような軽量モデルに対するAmazonの答えです。テキスト分類、単純な抽出、大きなエージェントのパイプライン内のルーティング処理など、大量でレイテンシに敏感なワークロード向けに作られました。

画像や動画の理解を省いているので、マルチモーダルなNovaのLiteやProより速く安く動きます。その代わり、視覚入力は処理できません。BedrockでファインチューンとモデルのディスティレーションにMicro対応しています。大きなモデルの出力で学習させれば、限られたタスクで、そのモデルに近い品質をわずかなコストで得られます。
