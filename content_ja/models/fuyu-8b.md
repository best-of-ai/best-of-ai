---
title: 'Fuyu-8B'
name: 'Fuyu-8B'
slug: 'fuyu-8b'
company: 'adept-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.adept.ai/blog/fuyu-8b'
price: 'Free'
rank: 3
release_date: '2023-10-17'
param_count: '8B'
context_window_tokens: 16000
modality: [text, image]
open_weight: true
license: 'CC-BY-NC 4.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, multimodal, open-weight, agentic]
subtitle: 'Adeptのオープンウェイトのマルチモーダルモデル。デジタルエージェントの知覚向けに作られた'
description: 'Adeptのオープンウェイトのマルチモーダルモデル。デジタルエージェントの知覚向けに作られた'
---

Fuyu-8Bは、Adept AIが2023年10月に公開したマルチモーダルモデルです。汎用のチャットボットとしてではなく、画面を見て操作するデジタルエージェントを支えるために作られました。Adeptは構造を単純にしています。別個の画像エンコーダーを使わず、画像パッチを標準的なデコーダー専用transformerに直接入力します。そのため、すべてを固定サイズに縮小せず、入ってきた解像度のまま画像を受け付けられます。これはAdeptの用途にとって重要です。UIの要素、ボタン、文字を元の解像度のまま読み取って、スクリーンショット、グラフ、図についての質問に答え、画面上の特定の要素の位置を特定する必要があるからです。Adeptは80億パラメータのモデルをCC-BY-NCライセンスでHugging Faceに公開しました。無料で使えて改変もできますが、商用目的では使えません。これは、完全に別の製品というより、Adept自身の製品を動かすモデルの小さな公開プレビューという位置づけです。コンテキスト長は16Kトークンです。Adeptはその後買収され、2024年にチームの多くがAmazonに移りました。Fuyu-8Bは、同社のエージェント重視の研究の方向性を残した記録になっています。
