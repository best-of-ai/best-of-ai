---
title: 'Grok-1'
name: 'Grok-1'
slug: 'grok-1'
subtitle: '後にApache 2.0でオープンウェイト公開されたxAI初のモデル'
description: '後にApache 2.0でオープンウェイト公開されたxAI初のモデル'
company: 'xai'
model_type: 'Language'
logo_url: ''
product_url: 'https://x.ai/blog/grok-os'
price: 'Free'
rank: 5
release_date: '2023-11-04'
param_count: '314B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: false
platforms: ['Hugging Face', 'GitHub']
date: '2026-07-16'
tags: [llm, open-weight, legacy]
i18n_source: '1027c6ce5f38'
---
Grok-1はイーロン・マスクのAI企業xAIが開発した初の大規模言語モデルで、2023年11月からX Premium+の利用者に提供されました。3,140億パラメータの混合エキスパートモデルで、8個のエキスパートと上位2つを選ぶルーティングを備えています。各トークンで有効になる重みは全体の約4分の1で、コンテキスト長は8,192トークンです。xAIは2024年3月17日、基盤モデルの重みとアーキテクチャをApache 2.0ライセンスで公開しました。当時、一般公開された最大のオープンウェイトMoEモデルでした。ただし公開されたのは事前学習済みの重みのみで、指示調整版やチャット対応版は含まれなかったため、主に研究者やインフラチームが利用しました。xAIはPyTorchではなく、独自のJAX・Rust環境で学習し、事前学習はGrok-2に置き換えられる前の2023年10月に完了していました。
