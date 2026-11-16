---
title: 'DeepSeek V3.2'
name: 'DeepSeek V3.2'
slug: 'deepseek-v3-2'
subtitle: '新しいスパースアテンションの仕組みを軸にした、DeepSeekのV3.1の更新版'
description: '新しいスパースアテンションの仕組みを軸にした、DeepSeekのV3.1の更新版'
company: 'deepseek'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 8
release_date: '2025-12-01'
param_count: '685B (MoE)'
context_window_tokens: 163840
modality: [text, code]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 0.21
output_price_usd_per_m: 0.32
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-25'
tags: [llm, open-weight, reasoning, coding, mixture-of-experts]
extra_model_types: ['Code']
i18n_source: 'd6a4a3b7b4f4'
---

DeepSeek V3.2はDeepSeekによるV3.1の更新版で、9月の実験的なプレビューを経て、2025年12月1日に詳細が公開されました。DeepSeek Sparse Attentionという細粒度のスパースアテンションの仕組みを導入しています。これは長いコンテキストのタスクで品質を保ちつつ、学習と推論のコストを下げるものです。フラッグシップのSpeciale版はMixture-of-Expertsの構成で、約6850億パラメータを持ちます。コンテキスト長は163,840トークン、出力は最大64,000トークンです。DeepSeekは、2025年の国際数学オリンピックと国際情報オリンピックの問題セットで金メダル級の結果を報告しています。API料金は入力が100万トークンあたり約0.21ドル、出力が約0.32ドルで、特に長いコンテキストのデコードでは、V3.1-Terminusのおよそ半額です。DeepSeekのほかのモデルと同じくMITライセンスで、重みはHugging Faceにあります。翌春にDeepSeekがV4-Proを作る際のベースにもなりました。
