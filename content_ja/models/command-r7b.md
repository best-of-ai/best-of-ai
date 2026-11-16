---
title: 'Command R7B'
name: 'Command R7B'
slug: 'command-r7b'
subtitle: 'Cohereの現行世代で最小のCommandモデル'
description: 'Cohereの現行世代で最小のCommandモデル'
company: 'cohere'
model_type: 'Language'
logo_url: ''
product_url: 'https://cohere.com/command'
price: 'Free'
rank: 3
release_date: '2024-12-13'
param_count: '7B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'CC-BY-NC 4.0'
input_price_usd_per_m: 0.0375
output_price_usd_per_m: 0.15
api_available: true
mmlu_score: 70.4
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Cohere Platform', 'Hugging Face']
date: '2026-07-16'
tags: [llm, small-model, open-weight, low-latency]
i18n_source: 'a4ee277c137e'
---

Command R7BはCohereのRシリーズで最小のモデルで、同社がこのラインナップの最終作と呼ぶ形で2024年12月に公開されました。パラメータ数は70億で、CPUや単体のGPUといった安価なハードウェアで動かせるように作られています。それでいて、Cohereの大型モデルが想定していた検索拡張生成、ツール利用、推論のタスクもこなします。公開時にはHugging FaceのOpen LLM Leaderboardで同規模のオープンウェイトモデルの首位に立ち、MMLU、IFEval、GPQAなどのベンチマークの平均でGemma 2 9B、Ministral 8B、Llama 3.1 8Bを上回りました。コンテキスト長は上位モデルと同じ128,000トークンで、価格はそれらよりずっと低く抑えられています。最先端レベルのタスクよりも、大量処理や低レイテンシが求められるアプリケーション向けです。
