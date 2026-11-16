---
title: 'MiniMax-01'
name: 'MiniMax-01'
slug: 'minimax-01'
subtitle: '400万トークンのコンテキスト長を備えたMiniMaxの2025年オープンウェイトモデル'
description: '400万トークンのコンテキスト長を備えたMiniMaxの2025年オープンウェイトモデル'
company: 'minimax-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.minimaxi.com/'
price: 'Free'
rank: 6
release_date: '2025-01-15'
param_count: '456B (45.9B active)'
context_window_tokens: 4000000
modality: [text]
open_weight: true
license: 'Apache 2.0'
input_price_usd_per_m: 0.2
output_price_usd_per_m: 1.1
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, long-context, mixture-of-experts]
extra_model_types: ['Multimodal']
i18n_source: '7af458104dd5'
---
MiniMax-01は中国企業MiniMaxが2025年1月に公開したオープンウェイト群です。同じハイブリッド構成のテキスト版MiniMax-Text-01と視覚言語版MiniMax-VL-01から成ります。混合エキスパート方式で総パラメータ数4,560億、トークンごとの有効数約459億。Lightning Attentionと通常のsoftmax attentionを組み合わせ、長い系列の処理を現実的にします。最大400万トークンを扱え、当時の多くの競合を上回りますが、API版は通常100万トークンです。

重みはApache 2.0でHugging Faceから提供され、独自API料金は入力100万トークンあたり0.20ドル、出力1.10ドルと、欧米の最先端モデルより低価格です。長文書分析、長時間エージェント作業、コードベース推論など、パラメータ数よりコンテキスト長が制約となる用途向けです。
