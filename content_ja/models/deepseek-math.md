---
title: 'DeepSeek-Math'
name: 'DeepSeek-Math'
slug: 'deepseek-math'
subtitle: 'DeepSeekのオープンウェイトの、数学的推論に特化したモデル'
description: 'DeepSeekのオープンウェイトの、数学的推論に特化したモデル'
company: 'deepseek'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 4
release_date: '2024-02-05'
param_count: '7B'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'DeepSeek License'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, math, reasoning]
i18n_source: 'f4c27d033105'
---

DeepSeekMathはDeepSeekが数学的推論のために作った70億パラメータのモデルで、2024年2月に公開されました。DeepSeek-Coder-Baseを初期値にしています。ウェブデータから集めた数学関連の1200億トークンに、自然言語とコードを加えて学習しました。競技レベルのMATHベンチマークでは、外部の電卓やツールを使わずに51.7%を記録しています。これは当時、Gemini-UltraやGPT-4のようなはるかに大きなクローズドモデルに近い水準でした。ベース、指示チューニング、強化学習チューニングの3つのバージョンが公開され、強化学習版はGroup Relative Policy Optimizationで学習されています。これはDeepSeekがこの論文で導入し、のちにDeepSeek-R1でも使ったアルゴリズムです。コンテキスト長は4,096トークンです。汎用のチャットよりも、数学の指導、定理証明、定量的な推論に取り組む研究者や開発者を想定しています。
