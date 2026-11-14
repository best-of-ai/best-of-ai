---
title: 'Qwen4-Max'
name: 'Qwen4-Max'
slug: 'qwen4-max'
subtitle: 'Qwen APIとクラウドプラットフォーム向けAlibabaの主力非公開モデル'
description: 'Qwen APIとクラウドプラットフォーム向けAlibabaの主力非公開モデル'
company: 'alibaba'
model_type: 'Language'
logo_url: ''
product_url: 'https://qwen.ai/'
price: 'Paid'
rank: 8
release_date: '2026-07-11'
param_count: 'Undisclosed'
context_window_tokens: 1000000
modality: [text, image]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 1.20
output_price_usd_per_m: 4.80
api_available: true
mmlu_score: 88.0
lmarena_score: 1352
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['Alibaba Cloud', 'Qwen Chat', 'API']
date: '2026-07-19'
tags: [llm, proprietary, api, multimodal]
i18n_source: 'd9ca0c4f1096'
---
Qwen4-MaxはAlibabaの最上位非公開モデルで、同社がHugging Faceで公開し続けているオープンウェイトのQwen3シリーズより上位に位置します。Qwen3と異なり非公開で、Alibaba CloudのAPI、Qwen Chat、提携プラットフォームからのみ利用できます。料金は入力100万トークンあたり1.20ドル、出力100万トークンあたり4.80ドルです。テキストと画像を入力でき、コンテキスト長は100万トークンです。Alibabaは自社のベンチマーク比較でGPT-5.6やGemini 3.5 Proと直接競うモデルとして位置付けています。

オープンなQwen3と非公開のQwen4-Maxに分ける戦略は、他の研究機関にも見られます。開発者の支持を集めるため中規模モデルの重みを公開する一方、学習コストが最も高い最大モデルは有料APIにします。この方法でAlibabaは中国国外にもQwenを広めてきました。特にHugging Face上で公開モデルをファインチューニングし、本番環境でより強い推論性能が必要なときはMaxを選ぶ開発者に浸透しています。
