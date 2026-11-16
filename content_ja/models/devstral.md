---
title: 'Devstral'
name: 'Devstral'
slug: 'devstral'
subtitle: 'エージェント型のコーディングとコードベースの探索向けにチューニングされた、Mistralのオープンウェイトモデル'
description: 'エージェント型のコーディングとコードベースの探索向けにチューニングされた、Mistralのオープンウェイトモデル'
company: 'mistral-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://mistral.ai/news/devstral/'
price: 'Free'
rank: 6
release_date: '2025-05-21'
param_count: '24B'
context_window_tokens: 128000
modality: [text, code]
open_weight: true
license: 'Apache 2.0'
input_price_usd_per_m: 0.1
output_price_usd_per_m: 0.3
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Mistral API']
date: '2026-07-16'
tags: [code, open-weight, agentic, api]
i18n_source: '10cd7f3fca31'
---

Devstralは、Mistral AIが2025年5月21日に公開した240億パラメータのコードモデルです。OpenHandsエージェントフレームワークを手がけるAll Hands AIと共同で作りました。コードモデルの多くは主にオートコンプリートや1回のやり取りでのコード生成向けに調整されていますが、Devstralはエージェント型のコーディングに特化して学習しています。複数のファイルにまたがってコードベースを探索し、ツールを使い、複数ステップのソフトウェアエンジニアリングのタスクをやり遂げる使い方です。SWE-bench Verifiedでは46.8%で、公開時に入手できたあらゆるオープンモデルを上回り、一部のより大きな独自モデルにも勝りました。

Mistralは重みをApache 2.0ライセンスで公開しました。単体のハイエンドなコンシューマー向けGPUで動かせるほど小さいので、ローカルのコーディングエージェントのベースとして人気になりました。Mistralはその後、Devstral Small 1.1とより大きなDevstral 2を出し、どちらもSWE-benchのスコアを引き上げました。それでも初代Devstralは、汎用のコード補完ではなくエージェント型のソフトウェアエンジニアリングを軸に作られた、最初期のオープンウェイトモデルの一つとして知られています。
