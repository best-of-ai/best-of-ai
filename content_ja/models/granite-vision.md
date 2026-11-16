---
title: 'Granite Vision'
name: 'Granite Vision'
slug: 'granite-vision'
subtitle: '文書や図表の理解に向けたIBMの小型視覚言語モデル'
description: '文書や図表の理解に向けたIBMの小型視覚言語モデル'
company: 'ibm'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.ibm.com/granite'
price: 'Free'
rank: 5
release_date: '2025-02-26'
param_count: '2B'
context_window_tokens: 16384
modality: [text, image]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['IBM watsonx', 'Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, vision, enterprise]
i18n_source: 'a32ea768a093'
---
Granite VisionはIBMの小型視覚言語モデルです。2025年2月のGranite 3.2更新の一部として公開され、一般的な画像チャットではなく、文書の視覚的な理解を目的に作られました。20億パラメータで、表、グラフ、インフォグラフィック、プロット、スキャン文書を読み取り、構造化テキストに変換します。DocVQAやChartQAなどのベンチマークを対象とし、IBMは数倍の規模を持つオープンモデルに匹敵するとしています。大規模なマルチモーダルモデルを動かすのが現実的でない、請求書の解析やレポートからのデータ抽出など日常的な企業業務向けに、小さなモデルサイズを意図的に選びました。コンテキスト長は16Kで、Apache 2.0のオープンウェイトとしてHugging FaceとIBM watsonxから提供されます。3.3版やGranite 4.0の視覚モデルも、同じ文書理解中心の設計を引き継いでいます。
