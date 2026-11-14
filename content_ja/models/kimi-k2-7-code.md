---
title: 'Kimi K2.7 Code'
name: 'Kimi K2.7 Code'
slug: 'kimi-k2-7-code'
subtitle: 'ツール利用と長時間タスク向けに調整されたMoonshotのオープンウェイト・エージェント型コーディングモデル'
description: 'ツール利用と長時間タスク向けに調整されたMoonshotのオープンウェイト・エージェント型コーディングモデル'
company: 'moonshot-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://www.moonshot.ai/'
price: 'Free'
rank: 8
release_date: '2026-06-12'
param_count: '1T (32B active)'
context_window_tokens: 256000
modality: [text, code]
open_weight: true
license: 'Modified MIT'
input_price_usd_per_m: 0.95
output_price_usd_per_m: 4.0
api_available: true
humaneval_score: 90.0
lmarena_score: 1360
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, code, agentic, mixture-of-experts]
extra_model_types: ['Reasoning']
i18n_source: '7d2adc3dc4a7'
---
Kimi K2.7 CodeはMoonshot AIが2026年6月に公開した、Kimi K2.6を基にしたコーディング特化モデルです。総パラメータ数1兆、約320億の有効パラメータを持つ同じMixture of Expertsアーキテクチャと、256,000トークンのコンテキスト長を維持しながら、長期的なコーディングとエージェント型のタスク分解に合わせて調整されています。Moonshotによると、K2.6と比べてKimi Code Bench v2で約22％、Program Benchで11％、MLS Bench Liteで31.5％向上し、タスクあたりの推論トークンを約30％削減しました。これにより、エージェントループで実行する際の実質的なコストも下がります。常に思考モードで動作し、思考しない方式には切り替えられません。コードに加えてテキスト、画像、動画を入力できます。重みはHugging Faceで公開され、Moonshot APIの料金は入力・出力ともClaude OpusやGPT-5.5などの非公開モデルを大きく下回ります。
