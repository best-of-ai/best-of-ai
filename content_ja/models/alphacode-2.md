---
title: 'AlphaCode 2'
name: 'AlphaCode 2'
slug: 'alphacode-2'
subtitle: 'Geminiをベースにした競技プログラミング用のDeepMindのモデル。人間のトップ競技者に並ぶ順位'
description: 'Geminiをベースにした競技プログラミング用のDeepMindのモデル。人間のトップ競技者に並ぶ順位'
company: 'google-deepmind'
model_type: 'Code'
logo_url: ''
product_url: 'https://deepmind.google/discover/blog/alphacode-2-technical-report/'
price: 'Paid'
rank: 6
release_date: '2023-12-06'
param_count: 'Undisclosed'
modality: [text, code]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [code, research]
i18n_source: 'd985a201f8f1'
---

AlphaCode 2はGoogle DeepMindの競技プログラミング用システムで、2023年12月に技術レポートとして発表されました。最初のAlphaCodeの後継です。単一のモデルではなく、ファインチューンしたGeminiモデルを使ったパイプラインです。1問につき最大100万件のC++の解答候補を生成し、テストによる検証、挙動のクラスタリング、学習済みのスコアリングモデルで絞り込んで、最終的に約10件を提出します。直近のCodeforcesのコンテスト群では、10回の提出以内に問題の43パーセントを解き、元のAlphaCodeの25パーセントのほぼ2倍でした。

DeepMindの推定では、AlphaCode 2はCodeforcesの人間の参加者の上位85パーセンタイルに入り、同プラットフォームの「Expert」と「Candidate Master」の間にあたります。このプロジェクトは研究のみで、製品やAPIとしては出ていません。性能の高いベースモデルに大量のサンプリングと絞り込みを組み合わせると、検証可能な難しいコーディング問題の成績がどこまで上がるかを示す役割を果たしました。後にDeepMindのGeminiやAlphaProofの取り組みに取り込まれた推論とコード生成の技術の、直接の祖先です。
