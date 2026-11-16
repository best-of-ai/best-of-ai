---
title: 'Granite Guardian'
name: 'Granite Guardian'
slug: 'granite-guardian'
subtitle: '有害なLLM入力・出力を検出するIBMの安全性・リスク検知モデル'
description: '有害なLLM入力・出力を検出するIBMの安全性・リスク検知モデル'
company: 'ibm'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.ibm.com/granite'
price: 'Free'
rank: 5
release_date: '2024-10-21'
param_count: '8B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['IBM watsonx', 'Hugging Face']
date: '2026-07-16'
tags: [safety, open-weight, enterprise]
i18n_source: '6ce71d1a9d0a'
---
Granite Guardianは、主要なLLMの隣で動作し、ユーザーやアプリケーションに届く前に危険なプロンプトや応答を検出するIBMの安全性モデル群です。2024年10月、Granite 3.0とともに2B・8B版が公開されました。どちらも一から学習したのではなく、基盤となるGranite指示モデルをファインチューニングしています。IBMのAI Risk Atlasに記載された危害、たとえばジェイルブレイクの試み、暴言、社会的偏見、暴力、エージェント型ワークフローでのツール呼び出しや検索結果の幻覚を確認します。遅延やコストを抑えたいチーム向けに、38Mパラメータの小型HAP（hate、abuse、profanity）版も提供しています。Apache 2.0のオープンウェイトモデルで、Hugging Face、Ollama、NVIDIA、watsonxから利用できます。ユーザー定義の判定基準に対応した4.1版など、後の更新でこの方式を新しいGranite基盤モデルにも広げました。
