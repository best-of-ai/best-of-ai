---
title: 'GPT-1'
name: 'GPT-1'
slug: 'gpt-1'
subtitle: '2018年の論文で示された、GPTアーキテクチャを生んだOpenAI最初のモデル'
description: '2018年の論文で示された、GPTアーキテクチャを生んだOpenAI最初のモデル'
company: 'openai'
model_type: 'Language'
logo_url: ''
product_url: 'https://openai.com/index/language-unsupervised/'
price: 'Free'
rank: 5
release_date: '2018-06-11'
param_count: '117M'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Research']
date: '2026-07-16'
tags: [llm, legacy, foundation-model]
---

GPT-1は、OpenAI初のGenerative Pre-trained Transformerで、2018年6月の論文「Improving Language Understanding by Generative Pre-Training」で発表されました。パラメータ数は1億1700万、学習には未出版の小説を集めたBookCorpusを使い、コンテキスト長は512トークンでした。中心にある考え方は単純です。ラベルのない生のテキストでTransformerを事前学習し、その同じモデルを質問応答やテキスト含意などの個別のタスクでファインチューンします。

この方法は、OpenAIが比較した12のベンチマークのうち9つで、タスクごとに専用に作られたアーキテクチャを上回りました。論文の本当の要点はそこです。GPT-1自体は製品になっていません。生成的な事前学習のあとにファインチューンする方法が、タスクごとに別々に作って学習したモデルに勝てることの証明でした。この結果が、GPT-2、GPT-3、そのあとに続くすべてのモデルへとOpenAIがスケールアップしていく型になりました。
