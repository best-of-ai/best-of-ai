---
title: 'DeepSeek LLM 67B'
name: 'DeepSeek LLM 67B'
slug: 'deepseek-llm-67b'
subtitle: 'DeepSeekが最初に出した、密結合のオープンウェイト基盤モデル'
description: 'DeepSeekが最初に出した、密結合のオープンウェイト基盤モデル'
company: 'deepseek'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 4
release_date: '2023-11-29'
param_count: '67B'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'DeepSeek License'
api_available: false
mmlu_score: 71.9
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted, legacy]
i18n_source: 'b8bff96ba077'
---

DeepSeek LLM 67BはDeepSeekが最初に出した密結合の基盤モデルで、2023年11月に公開されました。この後、同社はのちのV2やV3で使うMixture-of-Expertsアーキテクチャへ移っていきます。670億パラメータの密結合transformerで、英語と中国語のテキスト2兆トークンで学習しました。MMLUのスコアは約71.9で、一般知識のベンチマークではLlama 2 70Bとほぼ同等、いくつかの中国語タスクではそれを上回りました。コンテキスト長は4,096トークンと、のちの基準では短めです。これは2023年後半の学習の水準を反映しています。ベースとチャットの両バージョンが、商用利用を認める寛容なDeepSeekライセンスで公開されました。その後DeepSeekがより広く使われるモデルを作るうえでの土台にもなっています。
